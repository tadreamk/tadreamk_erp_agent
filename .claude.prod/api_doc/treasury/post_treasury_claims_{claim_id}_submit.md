# POST /treasury/claims/{claim_id}/submit

Submit a draft funder claim. Transitions status from `draft` to `submitted`. Sends a notification. Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | The funder claim's unique identifier |

**Response:** Updated funder claim object

**Errors:**
- `400` — Only draft claims can be submitted
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Claim not found
