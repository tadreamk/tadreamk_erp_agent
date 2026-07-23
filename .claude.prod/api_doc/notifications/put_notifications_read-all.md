# PUT /notifications/read-all

Mark All As Read. Requires authentication.

**Response:**
```json
{
  "success": false,
  "message": "string",
  "data": {}
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
