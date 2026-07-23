# GET /hr-ops/workflows

List Workflows. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_status | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
