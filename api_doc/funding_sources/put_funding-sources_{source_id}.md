# PUT /funding-sources/{source_id}

Update an existing funding source. Requires `funding-sources` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |

**Request Body:** (all fields optional, same as POST)

**Response:** Updated funding source object

**Errors:**
- `400` — Duplicate source name or end_date < start_date
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
- `404` — Funding source not found
