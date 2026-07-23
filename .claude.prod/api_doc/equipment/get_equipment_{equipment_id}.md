# GET /equipment/{equipment_id}

Get Equipment. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "category": "string",
  "description": "string",
  "serial_number": "string",
  "purchase_date": "date",
  "warranty_expiry": "date",
  "purchase_price": "string",
  "status": "string",
  "assigned_username": "string",
  "assigned_username_preferred_name": "string",
  "assigned_date": "date",
  "license_key": "string",
  "total_seats": 0,
  "renewal_date": "date",
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string"
}
```

**Errors:**
- `422` — Validation Error
