# Exercise Score Instructions API

Base prefix: `/exercise-score-instructions`

All endpoints require `exercise` whitelist access.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /exercise-score-instructions/active-list | `exercise` whitelist | Get active instructions list | [get_exercise-score-instructions_active-list.md](get_exercise-score-instructions_active-list.md) |
| GET | /exercise-score-instructions/ | `exercise` whitelist | List instructions with filters | [get_exercise-score-instructions.md](get_exercise-score-instructions.md) |
| GET | /exercise-score-instructions/{instruction_id} | `exercise` whitelist | Get instruction by ID | [get_exercise-score-instructions_{instruction_id}.md](get_exercise-score-instructions_{instruction_id}.md) |
| POST | /exercise-score-instructions/ | `exercise` whitelist | Create instruction | [post_exercise-score-instructions.md](post_exercise-score-instructions.md) |
| PUT | /exercise-score-instructions/{instruction_id} | `exercise` whitelist | Update instruction | [put_exercise-score-instructions_{instruction_id}.md](put_exercise-score-instructions_{instruction_id}.md) |
| DELETE | /exercise-score-instructions/{instruction_id} | `exercise` whitelist | Delete instruction | [delete_exercise-score-instructions_{instruction_id}.md](delete_exercise-score-instructions_{instruction_id}.md) |
