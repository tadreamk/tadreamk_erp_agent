# GET /onboarding

List Workflows. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| hr_username | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
