# 64. Guide Quiz API

Quiz system tied to employee guides. Each guide (identified by a slug) has a set of multiple-choice questions. Employees can submit answers (one attempt per question) and view their scores across all guides.

**Base path:** `/guide-quiz`

**Access control:** Authentication required. User must exist in the employees table (matched by work email). No whitelist required.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/guide-quiz/my-scores` | Get the current user's quiz scores for all guide slugs. | [get_guide_quiz_my_scores.md](./get_guide_quiz_my_scores.md) |
| `GET` | `/guide-quiz/{slug}/questions` | Get all quiz questions for a specific guide slug, along with the current user's  | [get_guide_quiz_by_id_questions.md](./get_guide_quiz_by_id_questions.md) |
| `POST` | `/guide-quiz/{slug}/answer` | Submit an answer to a quiz question. Each question allows only one attempt per u | [post_guide_quiz_by_id_answer.md](./post_guide_quiz_by_id_answer.md) |
