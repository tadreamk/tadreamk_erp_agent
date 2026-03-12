# PUT /api/v1/payslip-workflow/{workflow_id}


Update payslip field values. Only allowed during `pending_payment` or `finance_confirmed` status. Also updates the linked expense's total value.

**Access control:** Whitelist `payslip` or `payslip-ceo` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Updated field values dictionary |

**Request example:**
```json
{
  "field_values": {
    "monthly_salary": 32000,
    "living_allowance": 5000,
    "overtime_pay": 2000
  }
}
```

**Response:** Same as `GET /api/v1/payslip-workflow/{workflow_id}` with role `hr`.

**Errors:**
- `400` -- Can only edit payslip during `pending_payment` or `finance_confirmed` status
- `401` -- Not authenticated
- `403` -- No access to payslip section
- `404` -- Payslip workflow not found
