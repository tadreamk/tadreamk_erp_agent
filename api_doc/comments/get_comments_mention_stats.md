# GET /comments/mention-stats


Get global mention frequency counts for ranking @mention suggestions in the UI. Results are cached for 5 minutes.

**Response:**
```json
{
  "mention_stats": {
    "john.doe": 42,
    "jane.smith": 18,
    "admin": 7
  }
}
```

**Errors:**
- `401` — Not authenticated
