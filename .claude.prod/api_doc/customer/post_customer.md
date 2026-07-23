# POST /customer

Create Customer. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | CustomerTitleEnum | No |  |
| first_name | string | Yes |  |
| last_name | string | Yes |  |
| position | string | No |  |
| company_name | string | No |  |
| email | string | No |  |
| phone | string | No |  |
| address | string | No |  |
| country | string | No |  |
| website | string | No |  |
| linkedin | string | No |  |
| industry | CustomerIndustryEnum | No |  |
| source | CustomerSourceEnum | No |  |
| note | string | No |  |

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
