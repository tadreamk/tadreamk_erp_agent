# GET /customers/{customer_id}

Get a specific customer by ID. Requires `customer-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | UUID | The customer's unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "title": "Mr.",
  "first_name": "John",
  "last_name": "Doe",
  "company_name": "Acme Corp",
  "email": "john@acme.com",
  "phone": "+1 555 1234",
  "address": "123 Main St",
  "country": "Hong Kong",
  "website": "https://acme.com",
  "linkedin": "https://linkedin.com/in/johndoe",
  "industry": "Technology",
  "source": "Referral",
  "note": "string",
  "updated_by": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "is_active": true
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No customer-management whitelist access
- `404` — Customer not found
