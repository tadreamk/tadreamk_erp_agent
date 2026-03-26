# PUT /notifications/read-all

Mark all notifications as read for the authenticated user. Requires authentication.

**Response:**
```json
{
  "marked_count": 12
}
```

**Errors:**
- `401` — Not authenticated
