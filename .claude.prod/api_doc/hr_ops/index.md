# HR Ops API

Base prefixes:
- `/hr-ops`
- `/hr-ops/workflows`
- `/talent/hr-ops`
- `/talent/hr-ops/workflows`
- `/talent/hr-ops/workflows/{workflow_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /hr-ops/templates | Public | List Active Templates | [get_hr-ops_templates.md](get_hr-ops_templates.md) |
| GET | /hr-ops/workflows | Public | List Workflows | [get_hr-ops_workflows.md](get_hr-ops_workflows.md) |
| POST | /hr-ops/workflows | Public | Create Workflow | [post_hr-ops_workflows.md](post_hr-ops_workflows.md) |
| GET | /hr-ops/workflows/{workflow_id} | Public | Get Workflow | [get_hr-ops_workflows_{workflow_id}.md](get_hr-ops_workflows_{workflow_id}.md) |
| GET | /talent/hr-ops/workflows | Authenticated | List My Workflows | [get_talent_hr-ops_workflows.md](get_talent_hr-ops_workflows.md) |
| GET | /talent/hr-ops/workflows/{workflow_id} | Authenticated | Get My Workflow | [get_talent_hr-ops_workflows_{workflow_id}.md](get_talent_hr-ops_workflows_{workflow_id}.md) |
| POST | /talent/hr-ops/workflows/{workflow_id}/submit | Authenticated | Submit My Workflow | [post_talent_hr-ops_workflows_{workflow_id}_submit.md](post_talent_hr-ops_workflows_{workflow_id}_submit.md) |
