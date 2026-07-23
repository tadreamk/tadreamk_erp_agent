# POST /contracts/

Create Contract. Requires `)
    fields = payload.model_dump(exclude={` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes |  |
| candidate_title | string | No |  |
| candidate_first_name | string | No |  |
| candidate_last_name | string | No |  |
| address | string | No |  |
| position | string | No |  |
| work_location | string | No |  |
| employment_type | EmploymentTypeEnum | No |  |
| start_date | string | No |  |
| employment_end_date | string | No |  |
| probation_end_date | string | No |  |
| contract_pay_type | ContractPayTypeEnum | No |  |
| monthly_salary | number|string | No |  |
| hourly_rate | number|string | No |  |
| living_allowance | number|string | No |  |
| annual_leave_days | integer | No |  |
| remote_work_days | integer | No |  |

**Response:**
```json
{
  "success": false,
  "message": "string",
  "data": {}
}
```

**Errors:**
- `422` — Validation Error
