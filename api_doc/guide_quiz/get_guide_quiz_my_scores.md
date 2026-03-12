# GET /guide-quiz/my-scores


Get the current user's quiz scores for all guide slugs.

**Response:**
```json
{
  "scores": [
    {
      "slug": "company-handbook",
      "total_questions": 10,
      "correct_answers": 8,
      "score_percentage": 80.0
    },
    {
      "slug": "safety-guidelines",
      "total_questions": 5,
      "correct_answers": 5,
      "score_percentage": 100.0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access quizzes
