# GET /admin/personal-particular

List all personal particulars with optional search filter. Requires `personal-particulars` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by username, name, or mobile phone |
| page | integer | No | Page number (default: 1) |
| limit | integer | No | Items per page (default: 50) |

**Response:**
```json
{
  "personal_particulars": [
    {
      "id": "uuid",
      "username": "string",
      "family_name_english": "string",
      "first_name_english": "string",
      "preferred_name": "string",
      "nationality": "string",
      "mobile_phone": "string"
    }
  ],
  "total": 100,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on personal-particulars whitelist
