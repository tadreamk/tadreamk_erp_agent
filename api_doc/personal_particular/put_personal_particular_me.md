# PUT /personal-particular/me


Update personal particular data for the authenticated user. Only fields included in the request body are updated.

**Request Body:** Same fields as POST (all optional). Only provided fields are updated.

**Request Example:**
```json
{
  "mobile_phone": "+852-9999-8888",
  "residential_address": "456 New St, Hong Kong"
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
    "bank_name": "HSBC",
    "bank_code": "004",
    "branch_code": "001",
    "bank_account_number": "123456789",
    "bank_beneficiary_name": "John Doe",
    "created_at": "2025-06-01T00:00:00",
    "updated_at": "2025-08-01T00:00:00"
  }
}
```

**Errors:**
- `401` -- Not authenticated
- `404` -- Personal particular record not found. Use POST to create.

---

## 21. Personal Particular (Admin / HR)

Base path: `/admin/personal-particular`

**Access control:** Whitelist `personal-particulars` required for all endpoints.
