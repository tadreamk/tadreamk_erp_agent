# PUT /customers/{customer_id}

Update an existing customer record. Requires `customer-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | UUID | The customer's unique identifier |

**Request Body:** (all fields optional)
| Field | Type | Description |
|-------|------|-------------|
| first_name | string | First name |
| last_name | string | Last name |
| title | string | Title |
| company_name | string | Company name |
| email | string | Email address |
| phone | string | Phone number |
| address | string | Full address |
| country | string | Country |
| website | string | Website URL |
| linkedin | string | LinkedIn URL |
| industry | string | Industry |
| source | string | Customer source |
| note | string | Additional notes |

**Response:** Customer object (same as GET by ID)

**Errors:**
- `401` — Not authenticated
- `403` — No customer-management whitelist access
- `404` — Customer not found
