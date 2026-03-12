# PUT /customers/{customer_id}


Update an existing customer record.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | UUID | Customer record ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | No | Title (max 20 chars) |
| first_name | string | No | First name (1-100 chars) |
| last_name | string | No | Last name (1-100 chars) |
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
- `404` — Customer not found
