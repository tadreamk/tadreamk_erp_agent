# POST /funding-sources

Create a new funding source. Requires `funding-sources` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| source_name | string | Yes | Source name (must be unique) |
| funding_type | string | Yes | Funding type (required, enum) |
| provider | string | No | Provider/grantor name |
| reference_no | string | No | Reference number |
| description | string | No | Description |
| total_approved | decimal | Yes | Total approved amount (must be > 0) |
| start_date | date | No | Start date |
| end_date | date | No | End date (must be >= start_date) |
| status | string | No | Status |
| funding_opportunity_id | UUID | No | Linked funding opportunity |

**Response:** Created funding source object

**Errors:**
- `400` — Funding source with this name already exists
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
