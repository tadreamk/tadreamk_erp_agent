# GET /equipment/my

Get equipment assigned to the currently authenticated user. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results per page (default: 50, max: 200) |

**Response:**
```json
{
  "equipment": [
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
  ],
  "total": 1,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
