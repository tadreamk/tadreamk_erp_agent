# GET /equipment/{equipment_id}

Get a specific equipment record by ID. Requires `equipment-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | The equipment's unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "name": "MacBook Pro 14\"",
  "category": "Laptops",
  "serial_number": "SN12345",
  "description": "string",
  "purchase_date": "2023-01-01",
  "purchase_price": 15000.0,
  "warranty_until": "2026-01-01",
  "expense_management_id": null,
  "employee_username": "alice",
  "employee_full_name": "Alice Wong",
  "assigned_date": "2024-01-01",
  "location": "HQ",
  "status": "assigned",
  "note": "string",
  "file_urls": [],
  "license_key": null,
  "total_seats": null,
  "renewal_date": null,
  "calendar_event_id": null,
  "updated_by": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "is_active": true
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `404` — Equipment not found
