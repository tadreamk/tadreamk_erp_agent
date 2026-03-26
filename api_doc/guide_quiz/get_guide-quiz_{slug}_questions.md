# GET /guide-quiz/{slug}/questions

Get all quiz questions for a guide slug, along with the user's prior answers. Requires employee authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The guide page slug |

**Response:**
```json
{
  "questions": [
    {
      "id": "uuid",
      "question_text": "What is X?",
      "option_1": "Answer A",
      "option_2": "Answer B",
      "option_3": "Answer C",
      "option_4": "Answer D"
    }
  ],
  "user_answers": {
    "question-uuid": {
      "selected_option": 2,
      "is_correct": true,
      "response_text": "Answer B",
      "correct_option": 2,
      "response_1": "...",
      "response_2": "...",
      "response_3": "...",
      "response_4": "..."
    }
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access quizzes
