# POST /guide-quiz/{slug}/answer

Submit an answer to a guide quiz question. One attempt only per question. Requires employee authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | The guide page slug |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| question_id | UUID | Yes | The question's unique identifier |
| selected_option | int | Yes | Selected option number (1-4) |

**Response:**
```json
{
  "is_correct": true,
  "correct_option": 2,
  "response_text": "Answer B"
}
```

**Errors:**
- `409` — Already answered this question
- `401` — Not authenticated
- `403` — Only employees can access quizzes
- `404` — Question not found
