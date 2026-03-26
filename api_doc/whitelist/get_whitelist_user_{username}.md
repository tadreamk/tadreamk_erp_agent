# GET /whitelist/user/{username}

Get all accessible endpoints for a specified user. Requires `whitelist` admin access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string | The username to look up |

**Response:**
```json
{
  "username": "alice",
  "endpoints": ["leave-management", "tasks"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on whitelist admin access
