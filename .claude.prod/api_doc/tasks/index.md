# Tasks API

Base prefixes:
- `/tasks`
- `/tasks/employees`
- `/tasks/timeline`
- `/tasks/{slug}`
- `/tasks/{slug}/members`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /tasks | Public | Get Tasks | [get_tasks.md](get_tasks.md) |
| POST | /tasks | Public | Create New Task | [post_tasks.md](post_tasks.md) |
| GET | /tasks/ | Public | Get Tasks | [get_tasks_.md](get_tasks_.md) |
| POST | /tasks/ | Public | Create New Task | [post_tasks_.md](post_tasks_.md) |
| GET | /tasks/employees/picker | Public | Get Employees For Picker | [get_tasks_employees_picker.md](get_tasks_employees_picker.md) |
| GET | /tasks/team-overview | Public | Get Team Overview | [get_tasks_team-overview.md](get_tasks_team-overview.md) |
| GET | /tasks/timeline/range | Public | Get Tasks Timeline | [get_tasks_timeline_range.md](get_tasks_timeline_range.md) |
| DELETE | /tasks/{slug} | Public | Delete Task By Slug | [delete_tasks_{slug}.md](delete_tasks_{slug}.md) |
| GET | /tasks/{slug} | Public | Get Task | [get_tasks_{slug}.md](get_tasks_{slug}.md) |
| PUT | /tasks/{slug} | Public | Update Existing Task | [put_tasks_{slug}.md](put_tasks_{slug}.md) |
| POST | /tasks/{slug}/members | Public | Add Member To Task | [post_tasks_{slug}_members.md](post_tasks_{slug}_members.md) |
| DELETE | /tasks/{slug}/members/{username} | Public | Remove Member From Task | [delete_tasks_{slug}_members_{username}.md](delete_tasks_{slug}_members_{username}.md) |
| WEBSOCKET | /tasks/{slug}/ws | Authenticated | WebSocket /tasks/{slug}/ws | [websocket_tasks_{slug}_ws.md](websocket_tasks_{slug}_ws.md) |
