# GET /exercise-score-instructions/active-list

Get list of active score instructions for dropdown selection. Requires `exercise` whitelist.

**Response:**
```json
{
  "instructions": [
    {
      "id": "uuid",
      "title": "Standard Scoring"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
