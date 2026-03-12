# PUT /api/v1/reimbursement-workflow/{workflow_id}


Update a reimbursement request. Only allowed when status is `submitted` and only by the employee who created it.

**Access control:** Must be the reimbursement's employee (owner).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Reimbursement workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| total_value | decimal | No | Updated total amount in HKD |
| employee_note | string | No | Updated notes or description |
| file_urls | string[] | No | Updated list of supporting document URLs |

**Request example:**
```json
{
  "total_value": 1800.00,
  "employee_note": "Updated: includes taxi fare"
}
```

**Response:** Same structure as `GET /api/v1/reimbursement-workflow/{workflow_id}`.

**Errors:**
- `400` -- Cannot edit reimbursement. Current status: {status}
- `400` -- Failed to update reimbursement
- `401` -- Not authenticated
- `403` -- Only the employee can edit their reimbursement
- `404` -- Reimbursement workflow not found
