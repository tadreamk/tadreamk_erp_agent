# POST /admin/personal-particular


Create a new personal particular record for a specified user. If the user has an employee record without a linked personal particular, it is automatically linked.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Username to create the record for |

**Request Body:** JSON object with any of the personal particular fields (see POST /personal-particular/me for full field list). The `updated_by` field is set automatically from the authenticated admin.

**Request Example:**
```json
{
  "family_name_english": "Doe",
  "first_name_english": "John",
  "nationality": "Hong Kong",
  "date_of_birth": "1990-01-15",
  "gender": "Male",
  "mobile_phone": "+852-1234-5678"
}
```

**Response (201):**
```json
{
  "message": "Personal particular created",
  "personal_particular": {
    "id": "uuid",
    "username": "john.doe",
    "family_name_english": "Doe",
    "first_name_english": "John",
    "full_name_chinese": null,
    "preferred_name": null,
    "hkid": null,
    "nationality": "Hong Kong",
    "date_of_birth": "1990-01-15",
    "gender": "Male",
    "marital_status": null,
    "mobile_phone": "+852-1234-5678",
    "personal_email": null,
    "residential_address": null,
    "emergency_contact_name": null,
    "emergency_contact_phone": null,
    "emergency_contact_relationship": null,
    "bank_name": null,
    "bank_code": null,
    "branch_code": null,
    "bank_account_number": null,
    "bank_beneficiary_name": null,
    "created_at": "2025-06-01T00:00:00",
    "updated_at": null,
    "updated_by": "admin.user"
  }
}
```

**Errors:**
- `400` -- `username` query parameter is required
- `400` -- Personal particular already exists for this username
