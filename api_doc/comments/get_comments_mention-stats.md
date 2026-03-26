# GET /comments/mention-stats

Get global mention frequency counts for ranking mention suggestions in the comment editor. Results are cached for 5 minutes.

**Response:**
```json
{
  "mention_stats": {
    "alice": 42,
    "bob": 17
  }
}
```

**Errors:**
- `401` — Not authenticated
