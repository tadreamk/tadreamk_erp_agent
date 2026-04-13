# GET /equipment/my

Get equipment assigned to the currently authenticated user. Requires authentication.

**Response:**
```json
[
  {
    "id": "uuid",
    "name": "MacBook Pro 14\"",
    "category": "Laptops",
    "serial_number": "SN12345",
    "assigned_date": "2024-01-01",
    "status": "assigned",
    "location": "HQ",
    "license_key": null,
    "renewal_date": null
  }
]
```

**Errors:**
- `401` — Not authenticated
