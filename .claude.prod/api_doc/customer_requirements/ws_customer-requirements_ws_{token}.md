# WS /customer-requirements/ws/{token}

Public WebSocket relay for one collaborative document. **No authentication** — anyone with the token can connect.

**Path parameter:** `token` — the 12-character share token.

**Frame protocol:** every frame is a raw Yjs binary update (output of `Y.encodeStateAsUpdate` / input to `Y.applyUpdate`). The server broadcasts each inbound update to the other peers and applies it to a server-side `y_py.YDoc` mirror. On connect the server sends one initial state frame so the new peer converges with the current document.

**Close codes:**
- `1008` — link disabled or token unknown
- `1009` — inbound frame exceeded 256 KB
- `1011` — document markdown exceeded 1 MB cap
- `1013` — room is full (20 concurrent peers max)

**Caps:**
- Max 20 peers per room.
- Max 256 KB per binary frame.
- Max 1 MB of rendered markdown per snapshot (enforced on snapshot, closes all peers if breached).

**Persistence:** the server persists a snapshot of the room's y-doc every 10 s while dirty, and once more on last-peer-leave.
