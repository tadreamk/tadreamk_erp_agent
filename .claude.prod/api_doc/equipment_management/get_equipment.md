# GET /equipment

List all equipment with optional filters. Requires `equipment-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status (available, assigned, in_repair, reserved, retired, lost) |
| category | string | No | Filter by category (Laptops, Phones, Keys, Parking, Monitors, Furniture, Software, Other) |
| employee_username | string | No | Filter by assigned employee |
| search | string | No | Search by name or serial number |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "MacBook Pro 14\"",
    "category": "Laptops",
    "serial_number": "SN12345",
    "employee_username": "alice",
    "employee_full_name": "Alice Wong",
    "assigned_date": "2024-01-01",
    "status": "assigned",
    "location": "HQ",
    "renewal_date": null,
    "created_at": "datetime"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
