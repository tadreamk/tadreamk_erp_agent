# GET /customer/{customer_id}

Get Customer. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "title": "string",
  "first_name": "string",
  "last_name": "string",
  "position": "string",
  "company_name": "string",
  "email": "string",
  "phone": "string",
  "address": "string",
  "country": "string",
  "website": "string",
  "linkedin": "string",
  "industry": "string",
  "source": "string",
  "note": "string",
  "is_active": false,
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
