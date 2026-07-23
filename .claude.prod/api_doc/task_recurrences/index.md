# Task Recurrences API

Base prefixes:
- `/tasks`
- `/tasks/recurrences`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /tasks/recurrences | Public | List Recurrences | [get_tasks_recurrences.md](get_tasks_recurrences.md) |
| POST | /tasks/recurrences | Public | Create New Recurrence | [post_tasks_recurrences.md](post_tasks_recurrences.md) |
| GET | /tasks/recurrences/ | Public | List Recurrences | [get_tasks_recurrences_.md](get_tasks_recurrences_.md) |
| POST | /tasks/recurrences/ | Public | Create New Recurrence | [post_tasks_recurrences_.md](post_tasks_recurrences_.md) |
| DELETE | /tasks/recurrences/{recurrence_id} | Public | Delete Existing Recurrence | [delete_tasks_recurrences_{recurrence_id}.md](delete_tasks_recurrences_{recurrence_id}.md) |
| PUT | /tasks/recurrences/{recurrence_id} | Public | Update Existing Recurrence | [put_tasks_recurrences_{recurrence_id}.md](put_tasks_recurrences_{recurrence_id}.md) |
