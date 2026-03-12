# GET /guide-quiz/{slug}/questions


Get all quiz questions for a specific guide slug, along with the current user's prior answers (if any).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| slug | string | Yes | Guide identifier slug |

**Response:**
```json
{
  "questions": [
    {
      "id": "uuid",
      "question_text": "What is the company's core value?",
      "option_1": "Innovation",
      "option_2": "Profit",
      "option_3": "Speed",
      "option_4": "Competition"
    }
  ],
  "user_answers": {
    "uuid": {
      "selected_option": 1,
      "is_correct": true,
      "response_text": "Correct! Innovation is our core value.",
      "correct_option": 1,
      "response_1": "Correct! Innovation is our core value.",
      "response_2": "Incorrect. While important, profit is not our core value.",
      "response_3": "Incorrect. Speed is valued but not our core value.",
      "response_4": "Incorrect. We focus on collaboration, not competition."
    }
  }
}
```

**`questions` array fields:**
| Field | Type | Description |
|-------|------|-------------|
| id | string (UUID) | Question unique identifier |
| question_text | string | The question text |
| option_1 | string | First answer option |
| option_2 | string | Second answer option |
| option_3 | string | Third answer option |
| option_4 | string | Fourth answer option |

**`user_answers` object** (keyed by question ID, only present for previously answered questions):
| Field | Type | Description |
|-------|------|-------------|
| selected_option | int | Option number the user selected (1-4) |
| is_correct | boolean | Whether the answer was correct |
| response_text | string | Feedback text for the selected option |
| correct_option | int | The correct option number |
| response_1 | string | Feedback text for option 1 |
| response_2 | string | Feedback text for option 2 |
| response_3 | string | Feedback text for option 3 |
| response_4 | string | Feedback text for option 4 |

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access quizzes
