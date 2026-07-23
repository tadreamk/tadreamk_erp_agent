# Task AI Instructions API

Base prefixes:
- `/task-ai-instructions`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /task-ai-instructions | Authenticated employee | List Instructions | [get_task-ai-instructions.md](get_task-ai-instructions.md) |
| POST | /task-ai-instructions | Authenticated employee | Create Instruction | [post_task-ai-instructions.md](post_task-ai-instructions.md) |
| DELETE | /task-ai-instructions/{instruction_id} | Authenticated employee | Delete Instruction | [delete_task-ai-instructions_{instruction_id}.md](delete_task-ai-instructions_{instruction_id}.md) |
| GET | /task-ai-instructions/{instruction_id} | Authenticated employee | Get Instruction | [get_task-ai-instructions_{instruction_id}.md](get_task-ai-instructions_{instruction_id}.md) |
| PUT | /task-ai-instructions/{instruction_id} | Authenticated employee | Update Instruction | [put_task-ai-instructions_{instruction_id}.md](put_task-ai-instructions_{instruction_id}.md) |
