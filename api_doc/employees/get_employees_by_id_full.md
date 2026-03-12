# GET /employees/{employee_id}/full


Get full employee details including nested contract and personal particular data. Sensitive fields (HKID, bank account number) are masked.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| employee_id | UUID | Yes | Employee unique identifier |

**Response:**
```json
{
  "id": "uuid",
  "username": "john.doe",
  "work_email": "john.doe@company.com",
  "manager_username": "jane.smith",
  "is_active": true,
  "contract_id": "uuid",
  "personal_particular_id": "uuid",
  "onboarding_id": "uuid",
  "created_at": "2025-06-01T00:00:00",
  "updated_at": "2025-07-01T00:00:00",
  "updated_by": "admin.user",
  "contract": {
    "id": "uuid",
    "username": "john.doe",
    "candidate_title": "Mr",
    "candidate_first_name": "John",
    "candidate_last_name": "Doe",
    "full_name": "DOE John",
    "position": "Software Engineer",
    "department": "Engineering",
    "work_location": "Hong Kong",
    "employment_type": "Full-time",
    "start_date": "2025-06-01",
    "employment_end_date": null,
    "probation_end_date": "2025-09-01",
    "monthly_salary": 35000.00,
    "living_allowance": 2000.00,
    "annual_leave_days": 14,
    "remote_work_days": 2,
    "hkid": "****5678",
    "address": "123 Main St, Hong Kong",
    "mobile_no": "+852-1234-5678",
    "employee_signed_at": "2025-05-20T10:00:00",
    "ceo_signed_at": "2025-05-22T14:00:00",
    "created_at": "2025-05-15T00:00:00",
    "updated_at": "2025-05-22T14:00:00"
  },
  "personal_particular": {
    "id": "uuid",
    "username": "john.doe",
    "family_name_english": "Doe",
    "first_name_english": "John",
    "full_name_chinese": null,
    "preferred_name": "Johnny",
    "hkid": "****5678",
    "nationality": "Hong Kong",
    "date_of_birth": "1990-01-15",
    "gender": "Male",
    "marital_status": "Single",
    "mobile_phone": "+852-1234-5678",
    "personal_email": "john@personal.com",
    "residential_address": "123 Main St, Hong Kong",
    "emergency_contact_name": "Jane Doe",
    "emergency_contact_phone": "+852-9876-5432",
    "emergency_contact_relationship": "Spouse",
    "bank_name": "HSBC",
    "bank_code": "004",
    "branch_code": "001",
    "bank_account_number": "****7890",
    "bank_beneficiary_name": "John Doe",
    "created_at": "2025-05-15T00:00:00",
    "updated_at": "2025-06-01T00:00:00",
    "updated_by": "admin.user"
  }
}
```

**Errors:**
- `404` -- Employee not found
