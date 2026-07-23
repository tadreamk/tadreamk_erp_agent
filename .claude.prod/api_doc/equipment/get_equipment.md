# GET /equipment

List Equipment. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | EquipmentStatusEnum | No |  |
| category | EquipmentCategoryEnum | No |  |
| assigned_username | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
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
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
