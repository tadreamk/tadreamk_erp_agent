# GET /equipment/{equipment_id}


Get a specific equipment record by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | Equipment record ID |

**Response:**
```json
{
  "id": "uuid",
  "name": "MacBook Pro 16\"",
  "category": "Laptops",
  "serial_number": "C02X1234ABCD",
  "description": "16-inch, M2 Pro, 32GB RAM",
  "purchase_date": "2025-05-20",
  "purchase_price": 2499.00,
  "warranty_until": "2028-05-20",
  "expense_management_id": null,
  "employee_username": "john.doe",
  "assigned_date": "2025-06-15",
  "location": "Office A",
  "status": "assigned",
  "note": null,
  "file_urls": [],
  "license_key": null,
  "total_seats": null,
  "renewal_date": null,
  "calendar_event_id": null,
  "updated_by": "admin",
  "created_at": "2025-06-01T10:00:00Z",
  "updated_at": "2025-06-15T14:30:00Z",
  "is_active": true,
  "employee_full_name": null
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to equipment management
- `404` — Equipment not found
