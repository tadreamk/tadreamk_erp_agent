# DELETE /api/v1/payslip-workflow/{workflow_id}


Soft delete a payslip workflow. Only allowed during `pending_payment` status. Also soft-deletes the linked expense record.

**Access control:** Whitelist `payslip` or `payslip-ceo` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Payslip workflow ID |

**Response:**
```json
{
  "message": "Payslip deleted"
}
```

**Errors:**
- `400` -- Can only delete payslip during `pending_payment` status
- `401` -- Not authenticated
- `403` -- No access to payslip section
- `404` -- Payslip workflow not found

---

## 37. Payslip Workflow (Employee)
