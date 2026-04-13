# POST /treasury/claims/{claim_id}/receive

Mark a submitted funder claim as received. Creates a treasury inflow transaction. Sends a notification. Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | The funder claim's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| actual_amount | number | Yes | Actual amount received from funder |
| received_date | date | Yes | Date payment was received |

**Response:** Updated funder claim object

**Errors:**
- `400` — Only submitted claims can be received
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Claim not found
