# PUT /admin/personal-particular/{pp_id}


Update an existing personal particular record. The `updated_by` field is set automatically from the authenticated admin.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pp_id | UUID | Yes | Personal particular unique identifier |

**Request Body:** JSON object with any of the personal particular fields to update.

**Request Example:**
```json
{
  "mobile_phone": "+852-9999-8888",
  "residential_address": "456 New St, Hong Kong",
  "bank_name": "Standard Chartered",
  "bank_account_number": "987654321"
}
```

**Response:**
```json
{
  "message": "Personal particular updated",
  "personal_particular": {
    "id": "uuid",
    "username": "john.doe",
    "family_name_english": "Doe",
    "first_name_english": "John",
    "full_name_chinese": null,
    "preferred_name": "Johnny",
    "hkid": "A1234567",
    "nationality": "Hong Kong",
    "date_of_birth": "1990-01-15",
    "gender": "Male",
    "marital_status": "Single",
    "mobile_phone": "+852-9999-8888",
    "personal_email": "john@personal.com",
    "residential_address": "456 New St, Hong Kong",
    "emergency_contact_name": "Jane Doe",
    "emergency_contact_phone": "+852-9876-5432",
    "emergency_contact_relationship": "Spouse",
    "bank_name": "Standard Chartered",
    "bank_code": "004",
    "branch_code": "001",
    "bank_account_number": "987654321",
    "bank_beneficiary_name": "John Doe",
    "created_at": "2025-06-01T00:00:00",
    "updated_at": "2025-08-15T00:00:00",
    "updated_by": "admin.user"
  }
}
```

**Errors:**
- `404` -- Personal particular not found
