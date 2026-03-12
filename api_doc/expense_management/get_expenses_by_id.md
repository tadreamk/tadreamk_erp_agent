# GET /expenses/{expense_id}


Get full details of a specific expense, including related payroll/reimbursement data and employee payment information.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | Expense ID |

**Response:**
```json
{
  "id": "uuid",
  "payroll_id": "uuid-or-null",
  "reimbursement_workflow_id": "uuid-or-null",
  "expense_category_id": "uuid",
  "total_value": 5000.00,
  "funding_allocation": [
    {
      "funding_sources_id": "uuid",
      "value": 3000.00
    },
    {
      "funding_sources_id": "uuid",
      "value": 2000.00
    }
  ],
  "file_urls": ["https://storage.example.com/receipt1.pdf"],
  "note": "March payroll",
  "status": "pending",
  "source_type": "payslip",
  "total_allocated": 5000.00,
  "is_fully_allocated": true,
  "updated_by": "admin_user",
  "created_at": "2026-03-01T10:00:00",
  "updated_at": "2026-03-05T15:30:00",
  "is_active": true,
  "expense_category_name": "Salaries & Wages",
  "payroll_employee": "john.doe",
  "payroll_period": "2026-03",
  "reimbursement_employee": null,
  "payment_info": {
    "bank_name": "DBS Bank",
    "bank_code": "7171",
    "branch_code": "001",
    "bank_account_number": "123-456-789",
    "bank_beneficiary_name": "John Doe"
  }
}
```

**Errors:**
- `404` -- Expense not found
