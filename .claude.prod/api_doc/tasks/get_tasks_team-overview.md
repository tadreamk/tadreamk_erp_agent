# GET /tasks/team-overview

Get Team Overview. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by task status |
| priority | string | No | Filter by priority |
| project_id | string | No | Filter by project |
| page | integer | No | Page number |
| limit | integer | No | Items per page |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
