# DELETE /funding-opportunities/{opportunity_id}

Soft delete a funding opportunity. Requires `funding-opportunities` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | UUID | The opportunity's unique identifier |

**Response:**
```json
{
  "message": "Funding opportunity deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-opportunities whitelist access
- `404` — Funding opportunity not found
