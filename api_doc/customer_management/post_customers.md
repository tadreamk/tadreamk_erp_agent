# POST /customers


Create a new customer record.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Title: `Mr.`, `Mrs.`, `Ms.`, `Dr.`, `Prof.`, or empty (max 20 chars) |
| first_name | string | Yes | First name (1-100 chars) |
| last_name | string | Yes | Last name (1-100 chars) |
| company_name | string | No | Company name (max 255 chars) |
| email | string | No | Email address (max 255 chars) |
| phone | string | No | Phone number (max 50 chars) |
| address | string | No | Full address |
| country | string | No | Country (max 100 chars) |
| website | string | No | Website URL (max 255 chars) |
| linkedin | string | No | LinkedIn URL (max 255 chars) |
| industry | string | No | Industry (max 100 chars) |
| source | string | No | Customer source (max 100 chars) |
| note | string | No | Additional notes |

**Response:** Same as `GET /customers/{customer_id}`.

**Errors:**
- `401` — Not authenticated
- `403` — No access to customer management
