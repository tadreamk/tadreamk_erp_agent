# PUT /contracts/{contract_id}

Update Contract. Requires `)
    contract = get_contract_or_404_by_id(db, contract_id)
    contract = contract_write_ops.update_contract(
        db,
        contract=contract,
        updated_by=user.username,
        fields=payload.model_dump(exclude_unset=True),
    )
    return APIResponse(
        success=True,
        message=` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| contract_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
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
