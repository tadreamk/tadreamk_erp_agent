# GET /funding-opportunities/{opportunity_id}

Get a specific funding opportunity by ID. Requires `funding-opportunities` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | UUID | The opportunity's unique identifier |

**Response:** Full funding opportunity object

**Errors:**
- `401` — Not authenticated
- `403` — No funding-opportunities whitelist access
- `404` — Funding opportunity not found
