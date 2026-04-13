# DELETE /funding-sources/{source_id}

Soft delete a funding source. Requires `funding-sources` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |

**Response:**
```json
{
  "message": "Funding source deleted"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
- `404` — Funding source not found
