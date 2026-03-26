# POST /treasury/claims

Create a new funder claim in `draft` status. Requires `expense-management` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_source_id | UUID | Yes | The funding source to claim from |
| expense_ids | list[UUID] | Yes | List of finished expense IDs to include |
| claim_date | date | No | Claim submission date |
| notes | string | No | Additional notes |

**Response:** `201 Created` — Funder claim object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
