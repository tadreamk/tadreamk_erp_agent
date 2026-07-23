# Task Projects API

Base prefixes:
- `/task-projects`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /task-projects | Authenticated employee | List Task Projects | [get_task-projects.md](get_task-projects.md) |
| POST | /task-projects | Authenticated employee | Create Task Project | [post_task-projects.md](post_task-projects.md) |
| GET | /task-projects/active | Authenticated employee | List Active Task Projects | [get_task-projects_active.md](get_task-projects_active.md) |
| DELETE | /task-projects/{project_id} | Authenticated employee | Delete Task Project | [delete_task-projects_{project_id}.md](delete_task-projects_{project_id}.md) |
| GET | /task-projects/{project_id} | Authenticated employee | Get Task Project | [get_task-projects_{project_id}.md](get_task-projects_{project_id}.md) |
| PUT | /task-projects/{project_id} | Authenticated employee | Update Task Project Route | [put_task-projects_{project_id}.md](put_task-projects_{project_id}.md) |
