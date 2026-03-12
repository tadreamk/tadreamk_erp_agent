# GET /customers/{customer_id}


Get a specific customer by ID.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | UUID | Customer record ID |

**Response:**
```json
{
  "id": "uuid",
  "title": "Mr.",
  "first_name": "John",
  "last_name": "Doe",
  "company_name": "Acme Corp",
  "email": "john@acme.com",
  "phone": "+1-555-0100",
  "address": "123 Main St, Springfield, IL 62701",
  "country": "United States",
  "website": "https://acme.com",
  "linkedin": "https://linkedin.com/in/johndoe",
  "industry": "Technology",
  "source": "Referral",
  "note": "Key decision maker for enterprise deals",
  "updated_by": "admin",
  "created_at": "2025-08-01T10:00:00Z",
  "updated_at": "2025-09-15T14:30:00Z",
  "is_active": true
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to customer management
- `404` — Customer not found
