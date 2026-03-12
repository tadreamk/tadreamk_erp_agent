# GET /equipment


List all equipment with optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status: `available`, `assigned`, `in_repair`, `reserved`, `retired`, `lost` |
| category | string | No | Filter by category: `Laptops`, `Phones`, `Keys`, `Parking`, `Monitors`, `Furniture`, `Software`, `Other` |
| employee_username | string | No | Filter by assigned employee username |
| search | string | No | Search across equipment fields |
| skip | int | No | Offset for pagination (default: 0, min: 0) |
| limit | int | No | Max items to return (default: 50, min: 1, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "MacBook Pro 16\"",
    "category": "Laptops",
    "serial_number": "C02X1234ABCD",
    "employee_username": "john.doe",
    "employee_full_name": null,
    "assigned_date": "2025-06-15",
    "status": "assigned",
    "location": "Office A",
    "renewal_date": null,
    "created_at": "2025-06-01T10:00:00Z"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to equipment management
