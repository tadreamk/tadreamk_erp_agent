# GET /technical-reports


List all technical reports across all employees. Requires `technical-reports` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by report status |
| search | string | No | Search in report titles/descriptions |
| skip | int | No | Number of records to skip (default: 0, min: 0) |
| limit | int | No | Maximum records to return (default: 50, min: 1, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "employee_username": "john.doe",
    "employee_name": "DOE John",
    "title": "VPN connection issue",
    "status": "submitted",
    "created_at": "2026-03-10T09:00:00",
    "resolved_at": null
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to technical reports
