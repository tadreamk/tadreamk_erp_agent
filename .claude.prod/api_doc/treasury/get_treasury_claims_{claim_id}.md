# GET /treasury/claims/{claim_id}

Get a single funder claim by ID. Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | The funder claim's unique identifier |

**Response:** Funder claim object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Claim not found
