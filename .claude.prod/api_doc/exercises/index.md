# Exercises API

Base prefixes:
- `/exercises`
- `/exercises/{exercise_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /exercises | Authenticated | List Exercises | [get_exercises.md](get_exercises.md) |
| POST | /exercises | Authenticated | Create Exercise | [post_exercises.md](post_exercises.md) |
| GET | /exercises/{exercise_id} | Authenticated | Get Exercise | [get_exercises_{exercise_id}.md](get_exercises_{exercise_id}.md) |
| PUT | /exercises/{exercise_id} | Authenticated | Update Exercise | [put_exercises_{exercise_id}.md](put_exercises_{exercise_id}.md) |
| POST | /exercises/{exercise_id}/restore | Authenticated | Restore Exercise | [post_exercises_{exercise_id}_restore.md](post_exercises_{exercise_id}_restore.md) |
| POST | /exercises/{exercise_id}/retire | Authenticated | Retire Exercise | [post_exercises_{exercise_id}_retire.md](post_exercises_{exercise_id}_retire.md) |
