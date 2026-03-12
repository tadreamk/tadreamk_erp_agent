# GET /admin/personal-particular


Get all personal particular records with search filtering and pagination. Returns abbreviated list view.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search across username, family name, first name, preferred name, mobile phone |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "personal_particulars": [
    {
      "id": "uuid",
      "username": "john.doe",
      "family_name_english": "Doe",
      "first_name_english": "John",
      "preferred_name": "Johnny",
      "nationality": "Hong Kong",
      "mobile_phone": "+852-1234-5678"
    }
  ],
  "total": 42,
  "page": 1,
  "limit": 50
}
```
