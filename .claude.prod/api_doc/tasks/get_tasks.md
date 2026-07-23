# GET /tasks

Get Tasks. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filter_by_role | string | No | Filter by role (manager, member, or none for both) |
| status | string | No | Filter by status |
| modified_after | string | No | ISO date/datetime — tasks modified on or after |
| modified_before | string | No | ISO date/datetime — tasks modified on or before |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
