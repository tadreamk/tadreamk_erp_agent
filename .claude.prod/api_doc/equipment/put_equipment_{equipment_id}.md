# PUT /equipment/{equipment_id}

Update Equipment. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| category | EquipmentCategoryEnum | No |  |
| description | string | No |  |
| serial_number | string | No |  |
| purchase_date | string | No |  |
| warranty_expiry | string | No |  |
| purchase_price | number|string | No |  |
| status | EquipmentStatusEnum | No |  |
| assigned_username | string | No |  |
| assigned_date | string | No |  |
| license_key | string | No |  |
| total_seats | integer | No |  |
| renewal_date | string | No |  |

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
