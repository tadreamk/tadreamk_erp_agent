# GET /whitelist/stats

Get whitelist statistics showing user count per endpoint. Requires `whitelist` admin access.

**Response:**
```json
{
  "stats": [
    {
      "erp_endpoint": "leave-management",
      "user_count": 15
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on whitelist admin access
