# GET /api/v1/reimbursement-workflow/{workflow_id}


Get reimbursement workflow details. Accessible by the employee (owner), the assigned approver, or any user with `reimbursement-workflow` whitelist.

**Access control:** Employee (owner), approver, or whitelist `reimbursement-workflow`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Reimbursement workflow ID |

**Response:**
```json
{
  "id": "uuid",
  "employee_username": "john.doe",
  "approval_username": "finance.head",
  "expense_category": "category-uuid",
  "status": "submitted",
  "total_value": 1500.00,
  "file_urls": ["https://onedrive.example.com/receipt1.pdf"],
  "employee_note": "Client dinner",
  "created_at": "2026-03-01T10:00:00",
  "updated_at": null,
  "is_active": true,
  "employee_name": "John Doe",
  "approval_name": "Finance Head",
  "expense_category_title": "Entertainment",
  "can_edit": true,
  "can_delete": true,
  "can_approve": false,
  "can_reject": false,
  "can_confirm": false
}
```

**Role-based action flags:**
| Flag | Employee | Approver |
|------|----------|----------|
| can_edit | `submitted` | -- |
| can_delete | `submitted` | -- |
| can_approve | -- | `submitted` |
| can_reject | -- | `submitted` |
| can_confirm | `paid` | -- |

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to this reimbursement
- `404` -- Reimbursement workflow not found
