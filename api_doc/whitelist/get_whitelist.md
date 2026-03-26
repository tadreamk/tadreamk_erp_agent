# GET /whitelist/

List whitelist entries with filtering and pagination. Requires `whitelist` admin access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| erp_endpoint | string | No | Filter by ERP endpoint name |
| username | string | No | Search by username |
| page | integer | No | Page number (default: 1) |
| limit | integer | No | Items per page (default: 50, max: 100) |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "erp_endpoint": "leave-management",
      "username": "alice",
      "is_active": true,
      "created_by": "admin",
      "created_at": "2024-01-01T00:00:00"
    }
  ],
  "total": 50,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `400` — Invalid endpoint name
- `401` — Not authenticated
- `403` — Not on whitelist admin access
