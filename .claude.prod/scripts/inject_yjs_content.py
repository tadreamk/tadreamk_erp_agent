"""
Inject markdown content into a Yjs-backed collaborative document via WebSocket.

Used by the customer-requirement-draft skill to populate the editor body after
the document is created via the REST API.

Usage:
    python .claude.prod/scripts/inject_yjs_content.py <share_token> <markdown_file>

Arguments:
    share_token    12-character share token returned by POST /customer-requirements
    markdown_file  Path to a file containing the markdown content to inject

Requires: y-py, websockets
"""

import asyncio
import sys
import y_py as Y
import websockets

API_BASE = "wss://api-erp.tadreamk.com/api/v1"


async def inject(share_token: str, content: str) -> None:
    ws_url = f"{API_BASE}/customer-requirements/ws/{share_token}"
    async with websockets.connect(ws_url) as ws:
        # Receive initial server state and apply it to a local doc
        frame = await asyncio.wait_for(ws.recv(), timeout=10.0)
        doc = Y.YDoc()
        Y.apply_update(doc, frame)

        # Insert content into the 'content' Y.Text, clearing any existing text
        text = doc.get_text("content")
        current_len = len(str(text))
        with doc.begin_transaction() as txn:
            if current_len > 0:
                text.delete(txn, 0, current_len)
            text.insert(txn, 0, content)

        # Send the full Yjs state update; server persists within ~10 s
        await ws.send(Y.encode_state_as_update(doc))
        await asyncio.sleep(1.5)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: inject_yjs_content.py <share_token> <markdown_file>")
        sys.exit(1)

    share_token = sys.argv[1]
    markdown_file = sys.argv[2]

    with open(markdown_file, "r", encoding="utf-8") as f:
        content = f.read()

    asyncio.run(inject(share_token, content))
    print(f"Content injected into document {share_token} ({len(content)} chars)")


if __name__ == "__main__":
    main()
