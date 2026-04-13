# GET /guide-quiz/my-scores

Get the current user's quiz scores for all guide slugs. Requires employee authentication.

**Response:**
```json
{
  "scores": [
    {
      "slug": "getting-started",
      "correct": 4,
      "total": 5,
      "score_pct": 80.0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access quizzes
