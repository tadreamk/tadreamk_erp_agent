# GET /personal-particular/me

Get the authenticated user's personal particular data. Requires authentication.

**Response:**
```json
{
  "id": "uuid",
  "username": "string",
  "family_name_english": "string",
  "first_name_english": "string",
  "full_name_chinese": "string",
  "preferred_name": "string",
  "hkid": "string",
  "nationality": "string",
  "date_of_birth": "2000-01-01",
  "gender": "string",
  "marital_status": "string",
  "mobile_phone": "string",
  "personal_email": "string",
  "residential_address": "string",
  "emergency_contact_name": "string",
  "emergency_contact_phone": "string",
  "emergency_contact_relationship": "string",
  "bank_name": "string",
  "bank_code": "string",
  "branch_code": "string",
  "bank_account_number": "string",
  "bank_beneficiary_name": "string",
  "created_at": "2024-01-01T00:00:00",
  "updated_at": "2024-01-01T00:00:00"
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Personal particular record not found
