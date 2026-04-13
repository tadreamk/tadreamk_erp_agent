# GET /notifications/unread-count

Get the count of unread notifications for the authenticated user. Requires authentication.

**Response:**
```json
{
  "unread_count": 5
}
```

**Errors:**
- `401` — Not authenticated
