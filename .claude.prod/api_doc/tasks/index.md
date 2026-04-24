# Tasks API

Base prefixes:
- `/tasks` — Task CRUD and team member management
- `/task-projects` — Task project management
- `/tasks/recurrences` — Recurring task templates

Authentication: Requires authentication. Most task endpoints also require `task` whitelist access. Task project admin endpoints require `task` whitelist.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/tasks` | List tasks where user is a member |
| GET | `/tasks/employees/picker` | Get employee list for task member picker |
| GET | `/tasks/timeline/range` | Get tasks within a date range for timeline view |
| GET | `/tasks/team-overview` | Get tasks of subordinates via manager hierarchy |
| GET | `/tasks/{slug}` | Get task by slug |
| POST | `/tasks/` | Create a new task |
| PUT | `/tasks/{slug}` | Update a task |
| POST | `/tasks/{slug}/members` | Add a member to a task |
| DELETE | `/tasks/{slug}/members/{username}` | Remove a member from a task (manager only) |
| DELETE | `/tasks/{slug}` | Delete a task (manager only) |
| WebSocket | `/tasks/{slug}/ws` | Real-time task comments stream |
| GET | `/task-projects/active-list` | Get active task projects for dropdown |
| GET | `/task-projects/` | List task projects (paginated) |
| GET | `/task-projects/{project_id}` | Get task project by ID |
| POST | `/task-projects/` | Create a task project |
| PUT | `/task-projects/{project_id}` | Update a task project |
| DELETE | `/task-projects/{project_id}` | Soft delete a task project |
| POST | `/tasks/recurrences` | Create a recurrence template |
| GET | `/tasks/recurrences` | List recurrences managed by user |
| PUT | `/tasks/recurrences/{recurrence_id}` | Update a recurrence (manager only) |
| DELETE | `/tasks/recurrences/{recurrence_id}` | Delete a recurrence (manager only) |

## Endpoint Documentation

- [GET /tasks](get_tasks.md)
- [GET /tasks/employees/picker](get_tasks_employees_picker.md)
- [GET /tasks/timeline/range](get_tasks_timeline_range.md)
- [GET /tasks/team-overview](get_tasks_team-overview.md)
- [GET /tasks/{slug}](get_tasks_{slug}.md)
- [POST /tasks/](post_tasks.md)
- [PUT /tasks/{slug}](put_tasks_{slug}.md)
- [POST /tasks/{slug}/members](post_tasks_{slug}_members.md)
- [DELETE /tasks/{slug}/members/{username}](delete_tasks_{slug}_members_{username}.md)
- [DELETE /tasks/{slug}](delete_tasks_{slug}.md)
- [WebSocket /tasks/{slug}/ws](websocket_tasks_{slug}_ws.md)
- [GET /task-projects/active-list](get_task-projects_active-list.md)
- [GET /task-projects/](get_task-projects.md)
- [GET /task-projects/{project_id}](get_task-projects_{project_id}.md)
- [POST /task-projects/](post_task-projects.md)
- [PUT /task-projects/{project_id}](put_task-projects_{project_id}.md)
- [DELETE /task-projects/{project_id}](delete_task-projects_{project_id}.md)
- [POST /tasks/recurrences](post_tasks_recurrences.md)
- [GET /tasks/recurrences](get_tasks_recurrences.md)
- [PUT /tasks/recurrences/{recurrence_id}](put_tasks_recurrences_{recurrence_id}.md)
- [DELETE /tasks/recurrences/{recurrence_id}](delete_tasks_recurrences_{recurrence_id}.md)
