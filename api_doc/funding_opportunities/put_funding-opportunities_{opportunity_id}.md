# PUT /funding-opportunities/{opportunity_id}

Update an existing funding opportunity. Requires `funding-opportunities` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | UUID | The opportunity's unique identifier |

**Request Body:** (all fields optional, same as POST)

**Response:** Updated funding opportunity object

**Errors:**
- `400` — Duplicate opportunity name
- `401` — Not authenticated
- `403` — No funding-opportunities whitelist access
- `404` — Funding opportunity not found
