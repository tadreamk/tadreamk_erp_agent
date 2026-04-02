# POST /funding-opportunities

Create a new funding opportunity. Requires `funding-opportunities` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| opportunity_name | string | Yes | Opportunity name (must be unique) |
| funding_type | string | No | Funding type |
| status | string | No | Status |
| estimated_amount | decimal | No | Funding amount |
| application_deadline | date | No | Application deadline |
| description | string | No | Description |

**Response:** Created funding opportunity object

**Errors:**
- `400` — A funding opportunity with this name already exists
- `401` — Not authenticated
- `403` — No funding-opportunities whitelist access
