# GET /whitelist/


List whitelist entries with filtering and pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| erp_endpoint | string | No | Filter by ERP endpoint |
| username | string | No | Search by username |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50, max: 100) |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "erp_endpoint": "task",
      "username": "john.doe",
      "created_at": "2026-01-10T08:00:00Z",
      "created_by": "admin",
      "is_active": true,
      "updated_by": null,
      "updated_at": null,
      "deactivated_by": null,
      "deactivated_at": null
    }
  ],
  "total": 45,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `400` — Invalid endpoint filter value
