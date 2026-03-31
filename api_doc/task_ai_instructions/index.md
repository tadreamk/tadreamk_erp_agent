# Task AI Instructions API

Base prefix: `/task-ai-instructions`

All endpoints require `task` whitelist access. AI instructions are scoped per user (you only see your own).

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /task-ai-instructions/active-list | `task` whitelist | Get active instructions list | [get_task-ai-instructions_active-list.md](get_task-ai-instructions_active-list.md) |
| GET | /task-ai-instructions | `task` whitelist | List instructions with filters | [get_task-ai-instructions.md](get_task-ai-instructions.md) |
| GET | /task-ai-instructions/{instruction_id} | `task` whitelist | Get instruction by ID | [get_task-ai-instructions_{instruction_id}.md](get_task-ai-instructions_{instruction_id}.md) |
| POST | /task-ai-instructions | `task` whitelist | Create instruction | [post_task-ai-instructions.md](post_task-ai-instructions.md) |
| PUT | /task-ai-instructions/{instruction_id} | `task` whitelist | Update instruction | [put_task-ai-instructions_{instruction_id}.md](put_task-ai-instructions_{instruction_id}.md) |
| DELETE | /task-ai-instructions/{instruction_id} | `task` whitelist | Delete instruction | [delete_task-ai-instructions_{instruction_id}.md](delete_task-ai-instructions_{instruction_id}.md) |
