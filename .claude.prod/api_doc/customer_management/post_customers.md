# POST /customers

Create a new customer record. Requires `customer-management` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| first_name | string | Yes | First name |
| last_name | string | Yes | Last name |
| title | string | No | Title (Mr., Mrs., Ms., Dr., Prof.) |
| company_name | string | No | Company name |
| email | string | No | Email address |
| phone | string | No | Phone number |
| address | string | No | Full address |
| country | string | No | Country |
| website | string | No | Website URL |
| linkedin | string | No | LinkedIn URL |
| industry | string | No | Industry |
| source | string | No | Customer source |
| note | string | No | Additional notes |

**Response:**
```json
{
  "id": "uuid",
  "first_name": "John",
  "last_name": "Doe",
  "...": "..."
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No customer-management whitelist access
