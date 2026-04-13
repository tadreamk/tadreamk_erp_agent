# DELETE /market-research/companies/{slug}

Soft delete a market research company. Requires `market-research` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL-friendly company identifier |

**Response:**
```json
{
  "message": "Company deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
- `404` — Company not found
