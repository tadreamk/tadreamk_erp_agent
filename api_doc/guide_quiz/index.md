# Guide Quiz API

Base prefix: `/guide-quiz`

All endpoints require employee authentication.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /guide-quiz/my-scores | Get current user's quiz scores | [get_guide-quiz_my-scores.md](get_guide-quiz_my-scores.md) |
| GET | /guide-quiz/{slug}/questions | Get questions for a guide | [get_guide-quiz_{slug}_questions.md](get_guide-quiz_{slug}_questions.md) |
| POST | /guide-quiz/{slug}/answer | Submit an answer | [post_guide-quiz_{slug}_answer.md](post_guide-quiz_{slug}_answer.md) |
