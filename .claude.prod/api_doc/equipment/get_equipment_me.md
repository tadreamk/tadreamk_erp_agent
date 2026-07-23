# GET /equipment/me

List My Equipment. Requires authentication.

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
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
