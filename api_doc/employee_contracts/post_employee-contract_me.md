# POST /employee-contract/me

Create employee contract data for the authenticated user. Requires authentication. Only creates if no record exists.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| candidate_title | string | No | Title (max 10 chars) |
| candidate_last_name | string | No | Last name |
| candidate_first_name | string | No | First name |
| position | string | No | Job position |
| work_location | string | No | Work location |
| department | string | No | Department |
| employment_type | string | No | Employment type |
| start_date | date | No | Start date |
| employment_end_date | date | No | Employment end date |
| probation_end_date | date | No | Probation end date |
| contract_pay_type | string | No | Pay type (default: monthly) |
| monthly_salary | decimal | No | Monthly salary |
| hourly_rate | decimal | No | Hourly rate |
| living_allowance | decimal | No | Living allowance |
| annual_leave_days | int | No | Annual leave days |
| remote_work_days | int | No | Remote work days per week |
| hkid | string | No | HKID number |
| address | string | No | Address |
| mobile_no | string | No | Mobile number |
| employee_signature | string | No | Signature data |
| ceo_signature | string | No | CEO signature data |

**Response:**
```json
{
  "message": "Employee contract created",
  "employee_contract": { "...contract object..." }
}
```

**Errors:**
- `400` — Contract already exists. Use PUT to update.
- `401` — Not authenticated
