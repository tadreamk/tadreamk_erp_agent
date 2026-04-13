# GET /funding-sources/{source_id}

Get detailed information for a specific funding source. Requires `funding-sources` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |

**Response:** Full funding source object

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
- `404` — Funding source not found
