# GET /talent/renewal-contract-workflow

Get My Workflow. Public endpoint (no auth).

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "string",
  "employee_preferred_name": "string",
  "hr_username": "string",
  "hr_preferred_name": "string",
  "ceo_username": "string",
  "ceo_preferred_name": "string",
  "template_id": "uuid",
  "template": {
    "id": "uuid",
    "title": "string",
    "description": "string",
    "category": "string",
    "fields": [
      {
        "field_key": {},
        "title": {},
        "data_type": {},
        "description": {},
        "options": {},
        "input_by_role": {},
        "input_by_username": {},
        "section": {},
        "group": {},
        "default_value": {}
      }
    ],
    "pdf_url": "string",
    "is_active": false,
    "created_at": "datetime",
    "updated_at": "datetime"
  },
  "previous_contract_id": "uuid",
  "previous_contract": {
    "id": "uuid",
    "position": "string",
    "start_date": "string",
    "employment_end_date": "string",
    "contract_pay_type": "string",
    "is_active": false
  },
  "new_contract_id": "uuid",
  "new_contract": {
    "id": "uuid",
    "position": "string",
    "start_date": "string",
    "employment_end_date": "string",
    "contract_pay_type": "string",
    "is_active": false
  },
  "status": "string",
  "field_values": {},
  "pdf_url": "string",
  "employee_pdf_url": "string",
  "sent_for_ceo_confirmation_at": "datetime",
  "ceo_confirmed_at": "datetime",
  "talent_submitted_at": "datetime",
  "sent_to_ceo_at": "datetime",
  "is_active": false,
  "created_at": "datetime",
  "updated_at": "datetime"
}
```
