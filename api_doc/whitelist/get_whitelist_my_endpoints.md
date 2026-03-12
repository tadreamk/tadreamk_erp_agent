# GET /whitelist/my-endpoints


Get current authenticated user's accessible endpoints. No admin whitelist needed.

**Response:**
```json
{
  "username": "john.doe",
  "endpoints": ["task", "job-posts", "exercise"]
}
```

**Errors:**
- `401` — Not authenticated
