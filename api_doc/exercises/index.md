# 16. Exercises (Admin)

Manage coding/technical exercises assigned to job applicants. Exercises support tagging, markdown content, and optional scoring instructions.

**Access control:** Authentication required for all endpoints. Most endpoints require whitelist `exercise`. The list endpoint (`GET /exercises/`) returns an empty result set instead of `403` when the user lacks whitelist access. The detail endpoint (`GET /exercises/{slug}`) allows non-whitelisted users to view an exercise only if it is active **and** the user has been assigned that exercise through a job application.

**Base URL:** `/api/v1`

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/exercises/tags` | Get the predefined list of valid tags. | [get_exercises_tags.md](./get_exercises_tags.md) |
| `GET` | `/exercises/active-list` | Get a lightweight list of active exercises for dropdown/select inputs. | [get_exercises_active_list.md](./get_exercises_active_list.md) |
| `GET` | `/exercises/` | List exercises with filtering and pagination. Returns an empty list (not `403`)  | [get_exercises.md](./get_exercises.md) |
| `GET` | `/exercises/{slug}` | Get a single exercise by its URL slug. | [get_exercises_by_id.md](./get_exercises_by_id.md) |
| `POST` | `/exercises/` | Create a new exercise. | [post_exercises.md](./post_exercises.md) |
| `PUT` | `/exercises/{exercise_id}` | Update an existing exercise. Only provided fields are updated; omitted fields re | [put_exercises_by_id.md](./put_exercises_by_id.md) |
| `PATCH` | `/exercises/{exercise_id}/status` | Toggle the active/inactive status of an exercise. | [patch_exercises_by_id_status.md](./patch_exercises_by_id_status.md) |
| `DELETE` | `/exercises/{exercise_id}` | Soft-delete an exercise (sets `post_active` to `false`). | [delete_exercises_by_id.md](./delete_exercises_by_id.md) |
| `GET` | `/exercise-score-instructions/active-list` | Get a lightweight list of active score instructions for dropdown/select inputs. | [get_exercise_score_instructions_active_list.md](./get_exercise_score_instructions_active_list.md) |
| `GET` | `/exercise-score-instructions/` | List score instructions with filtering and pagination. | [get_exercise_score_instructions.md](./get_exercise_score_instructions.md) |
| `GET` | `/exercise-score-instructions/{instruction_id}` | Get a single score instruction by ID. | [get_exercise_score_instructions_by_id.md](./get_exercise_score_instructions_by_id.md) |
| `POST` | `/exercise-score-instructions/` | Create a new score instruction. | [post_exercise_score_instructions.md](./post_exercise_score_instructions.md) |
| `PUT` | `/exercise-score-instructions/{instruction_id}` | Update an existing score instruction. Only provided fields are updated; omitted  | [put_exercise_score_instructions_by_id.md](./put_exercise_score_instructions_by_id.md) |
| `DELETE` | `/exercise-score-instructions/{instruction_id}` | Soft-delete a score instruction (sets `post_active` to `false`). | [delete_exercise_score_instructions_by_id.md](./delete_exercise_score_instructions_by_id.md) |
