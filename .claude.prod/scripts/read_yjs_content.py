"""
Read markdown content from a Yjs-backed collaborative document via WebSocket.

Used by the customer-requirement-update skill to fetch the current editor body
before merging update points into it.

Usage:
    python .claude.prod/scripts/read_yjs_content.py <share_token>

Arguments:
    share_token    12-character share token returned by POST /customer-requirements

Requires: y-py, websockets
"""

import asyncio
import sys
import y_py as Y
import websockets

API_BASE = "wss://api-erp.tadreamk.com/api/v1"


async def read(share_token: str) -> str:
    ws_url = f"{API_BASE}/customer-requirements/ws/{share_token}"
    async with websockets.connect(ws_url) as ws:
        frame = await asyncio.wait_for(ws.recv(), timeout=10.0)
        doc = Y.YDoc()
        Y.apply_update(doc, frame)
        text = doc.get_text("content")
        return str(text)


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: read_yjs_content.py <share_token>")
        sys.exit(1)

    share_token = sys.argv[1]
    content = asyncio.run(read(share_token))
    print(content)


if __name__ == "__main__":
    main()
