# POST /tasks/{slug}/members

Add Member To Task. Public endpoint (no auth).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| task_member_username | string | Yes |  |
| task_role | string | No | Role: member or manager |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
