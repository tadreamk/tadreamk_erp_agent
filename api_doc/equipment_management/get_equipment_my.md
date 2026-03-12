# GET /equipment/my


Get equipment assigned to the currently authenticated user. No whitelist required — any authenticated user can call this.

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "MacBook Pro 16\"",
    "category": "Laptops",
    "serial_number": "C02X1234ABCD",
    "assigned_date": "2025-06-15",
    "status": "assigned",
    "location": "Office A",
    "license_key": null,
    "renewal_date": null
  }
]
```

**Errors:**
- `401` — Not authenticated
