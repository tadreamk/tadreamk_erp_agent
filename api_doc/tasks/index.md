# 48. Tasks

Collaborative task management with membership-based access control. Users can only see tasks where they are a member (manager or member role). Tasks support timeline views, AI-generated comments, project grouping, and real-time collaboration via WebSocket.

**Base path:** `/tasks`

**Access control:** All authenticated users can access tasks filtered by their membership. No whitelist required — access is governed by task membership.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/tasks` | Get list of tasks where the current user is a member. | [get_tasks.md](./get_tasks.md) |
| `GET` | `/tasks/employees/picker` | Get employee usernames for the task member picker dropdown. Available to all aut | [get_tasks_employees_picker.md](./get_tasks_employees_picker.md) |
| `GET` | `/tasks/timeline/range` | Get tasks within a date range for timeline view. | [get_tasks_timeline_range.md](./get_tasks_timeline_range.md) |
| `GET` | `/tasks/{slug}` | Get a single task by its slug. Requires task membership. | [get_tasks_by_id.md](./get_tasks_by_id.md) |
| `POST` | `/tasks/` | Create a new task. The creator is automatically added as a manager. Notification | [post_tasks.md](./post_tasks.md) |
| `PATCH` | `/tasks/{slug}` | Update a task. Requires task membership. Only provided fields are updated. | [patch_tasks_by_id.md](./patch_tasks_by_id.md) |
| `POST` | `/tasks/{slug}/members` | Add a member to a task. Any existing team member can add new members. | [post_tasks_by_id_members.md](./post_tasks_by_id_members.md) |
| `DELETE` | `/tasks/{slug}/members/{username}` | Remove a member from a task. Managers only. Cannot remove the last manager. | [delete_tasks_by_id_members_by_id.md](./delete_tasks_by_id_members_by_id.md) |
| `DELETE` | `/tasks/{slug}` | Delete a task and cascade-delete all comments and members. Managers only. | [delete_tasks_by_id.md](./delete_tasks_by_id.md) |
| `GET` | `/task-projects/active-list` | Get list of active task projects for dropdown selection. Only requires authentic | [get_task_projects_active_list.md](./get_task_projects_active_list.md) |
| `GET` | `/task-projects/` | Get list of task projects with filtering and pagination. | [get_task_projects.md](./get_task_projects.md) |
| `GET` | `/task-projects/{project_id}` | Get a task project by ID. | [get_task_projects_by_id.md](./get_task_projects_by_id.md) |
| `POST` | `/task-projects/` | Create a new task project. | [post_task_projects.md](./post_task_projects.md) |
| `PUT` | `/task-projects/{project_id}` | Update an existing task project. Only provided fields are updated. | [put_task_projects_by_id.md](./put_task_projects_by_id.md) |
| `DELETE` | `/task-projects/{project_id}` | Soft delete a task project by setting `post_active` to `false`. | [delete_task_projects_by_id.md](./delete_task_projects_by_id.md) |
| `GET` | `/task-ai-instructions/active-list` | Get list of active AI instructions belonging to the current user, for dropdown s | [get_task_ai_instructions_active_list.md](./get_task_ai_instructions_active_list.md) |
| `GET` | `/task-ai-instructions` | Get list of the current user's task AI instructions with filtering and paginatio | [get_task_ai_instructions.md](./get_task_ai_instructions.md) |
| `GET` | `/task-ai-instructions/{instruction_id}` | Get a task AI instruction by ID. | [get_task_ai_instructions_by_id.md](./get_task_ai_instructions_by_id.md) |
| `POST` | `/task-ai-instructions` | Create a new task AI instruction. The instruction is owned by the authenticated  | [post_task_ai_instructions.md](./post_task_ai_instructions.md) |
| `PUT` | `/task-ai-instructions/{instruction_id}` | Update an existing task AI instruction. Only provided fields are updated. | [put_task_ai_instructions_by_id.md](./put_task_ai_instructions_by_id.md) |
| `DELETE` | `/task-ai-instructions/{instruction_id}` | Soft delete a task AI instruction by setting `post_active` to `false`. | [delete_task_ai_instructions_by_id.md](./delete_task_ai_instructions_by_id.md) |
