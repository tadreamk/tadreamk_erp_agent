# POST /personal-particular/me

Create personal particular data for the authenticated user. Only one record per user is allowed. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| family_name_english | string | No | Family name in English |
| first_name_english | string | No | First name in English |
| full_name_chinese | string | No | Full name in Chinese |
| preferred_name | string | No | Preferred name |
| hkid | string | No | HKID number |
| nationality | string | No | Nationality |
| date_of_birth | date | No | Date of birth |
| gender | string | No | Gender |
| marital_status | string | No | Marital status |
| mobile_phone | string | No | Mobile phone number |
| personal_email | string | No | Personal email address |
| residential_address | string | No | Residential address |
| emergency_contact_name | string | No | Emergency contact name |
| emergency_contact_phone | string | No | Emergency contact phone |
| emergency_contact_relationship | string | No | Emergency contact relationship |
| bank_name | string | No | Bank name |
| bank_code | string | No | Bank code |
| branch_code | string | No | Branch code |
| bank_account_number | string | No | Bank account number |
| bank_beneficiary_name | string | No | Bank beneficiary name |

**Response:** `201 Created`
```json
{
  "message": "Personal particular created",
  "personal_particular": { "...personal particular object..." }
}
```

**Errors:**
- `400` — Record already exists. Use PUT to update.
- `401` — Not authenticated
