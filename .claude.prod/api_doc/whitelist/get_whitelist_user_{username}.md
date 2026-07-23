# GET /whitelist/user/{username}

Get User Endpoints. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string |  |

**Response:**
```json
{
  "username": "string",
  "endpoints": [
    "string"
  ]
}
```

**Errors:**
- `422` — Validation Error
