# GET /onboarding

List onboarding workflows. HR staff see all workflows; CEO users see only workflows assigned to them. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| hr_username | string | No | Filter by HR username (HR only) |
| is_active | boolean | No | Filter by active status (default: true) |
| limit | integer | No | Max results (default: 100, max: 500) |
| offset | integer | No | Pagination offset (default: 0) |

**Response:** Array of workflow list objects
```json
[
  {
    "id": "uuid",
    "talent_email": "talent@example.com",
    "talent_username": "string",
    "hr_username": "string",
    "ceo_username": "string",
    "status": "pending",
    "document_count": 3,
    "is_active": true,
    "created_at": "2024-01-01T00:00:00"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an HR user and no CEO workflows found
