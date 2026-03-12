# POST /personal-particular/me


Create personal particular data for the authenticated user. Each user can only have one record.

**Request Body (all fields optional):**
| Field | Type | Required | Max Length | Description |
|-------|------|----------|------------|-------------|
| family_name_english | string | No | 100 | Family name in English |
| first_name_english | string | No | 100 | First name in English |
| full_name_chinese | string | No | 200 | Full name in Chinese characters |
| preferred_name | string | No | 100 | Preferred / nickname |
| hkid | string | No | 50 | Hong Kong identity card number |
| nationality | string | No | 100 | Nationality |
| date_of_birth | date | No | -- | Date of birth (YYYY-MM-DD) |
| gender | string | No | 20 | Gender |
| marital_status | string | No | 50 | Marital status |
| mobile_phone | string | No | 50 | Mobile phone number |
| personal_email | string (email) | No | -- | Personal email address |
| residential_address | string | No | -- | Residential address |
| emergency_contact_name | string | No | 200 | Emergency contact name |
| emergency_contact_phone | string | No | 50 | Emergency contact phone |
| emergency_contact_relationship | string | No | 50 | Emergency contact relationship |
| bank_name | string | No | 100 | Bank name |
| bank_code | string | No | 10 | Bank code |
| branch_code | string | No | 10 | Branch code |
| bank_account_number | string | No | 50 | Bank account number |
| bank_beneficiary_name | string | No | 200 | Bank beneficiary name |

**Request Example:**
```json
{
  "family_name_english": "Doe",
  "first_name_english": "John",
  "nationality": "Hong Kong",
  "date_of_birth": "1990-01-15",
  "gender": "Male",
  "mobile_phone": "+852-1234-5678",
  "personal_email": "john@personal.com"
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
    "personal_email": "john@personal.com",
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
    "updated_at": null
  }
}
```

**Errors:**
- `400` -- Personal particular record already exists. Use PUT to update.
- `401` -- Not authenticated
