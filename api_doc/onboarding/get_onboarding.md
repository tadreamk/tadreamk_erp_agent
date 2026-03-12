# GET /onboarding


List onboarding workflows. HR sees all workflows; CEO sees only workflows assigned to them.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| status | string | No | — | Filter by workflow status |
| hr_username | string | No | — | Filter by assigned HR username |
| is_active | bool | No | `true` | Filter by active/inactive |
| limit | int | No | `100` | Results per page (1-500) |
| offset | int | No | `0` | Pagination offset (>=0) |

**Response:**
```json
[
  {
    "id": "uuid",
    "talent_email": "talent@example.com",
    "talent_username": "jane.doe",
    "hr_username": "hr.admin",
    "ceo_username": "ceo.user",
    "status": "input",
    "talent_submitted_at": "2026-03-10T08:00:00+00:00",
    "sent_to_ceo_at": null,
    "created_at": "2026-03-01T10:00:00+00:00",
    "updated_at": "2026-03-10T08:00:00+00:00",
    "is_active": true,
    "document_count": 3
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to contract section (non-HR user with no assigned workflows)
