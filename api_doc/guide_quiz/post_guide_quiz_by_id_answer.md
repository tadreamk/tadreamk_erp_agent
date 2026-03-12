# POST /guide-quiz/{slug}/answer


Submit an answer to a quiz question. Each question allows only one attempt per user.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| slug | string | Yes | Guide identifier slug |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| question_id | string | Yes | UUID of the question being answered (min 1 character) |
| selected_option | int | Yes | Selected option number (1-4) |

```json
{
  "question_id": "uuid",
  "selected_option": 1
}
```

**Response:**
```json
{
  "is_correct": true,
  "correct_option": 1,
  "response_text": "Correct! Innovation is our core value."
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access quizzes
- `422` — Validation error (missing question_id, selected_option out of range 1-4)
