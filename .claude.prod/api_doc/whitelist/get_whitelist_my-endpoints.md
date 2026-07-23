# GET /whitelist/my-endpoints

Get My Endpoints. Requires authentication.

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
- `401` — Not authenticated
- `404` — Not found
