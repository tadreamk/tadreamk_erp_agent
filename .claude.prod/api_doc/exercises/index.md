# Exercises API

Base prefix: `/exercises`

Employee access requires authentication (with exercise assigned or admin/moderator role).
Admin access requires `exercise` whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /exercises/{slug} | Authenticated (with access) | Get exercise by slug | [get_exercises_{slug}.md](get_exercises_{slug}.md) |
| GET | /exercises/tags | `exercise` whitelist | Get predefined tags | [get_exercises_tags.md](get_exercises_tags.md) |
| GET | /exercises/active-list | `exercise` whitelist | Get active exercises list | [get_exercises_active-list.md](get_exercises_active-list.md) |
| GET | /exercises/ | `exercise` whitelist | List exercises with filters | [get_exercises_list.md](get_exercises_list.md) |
| POST | /exercises/ | `exercise` whitelist | Create an exercise | [post_exercises.md](post_exercises.md) |
| PUT | /exercises/{exercise_id} | `exercise` whitelist | Update an exercise | [put_exercises_{exercise_id}.md](put_exercises_{exercise_id}.md) |
| PUT | /exercises/{exercise_id}/status | `exercise` whitelist | Update exercise status | [put_exercises_{exercise_id}_status.md](put_exercises_{exercise_id}_status.md) |
| DELETE | /exercises/{exercise_id} | `exercise` whitelist | Delete an exercise | [delete_exercises_{exercise_id}.md](delete_exercises_{exercise_id}.md) |
