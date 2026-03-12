# GET /expenses/count


Get count of expenses matching optional filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status: `pending`, `finished` |
| expense_category_id | UUID | No | Filter by expense category ID |
| source_type | string | No | Filter by source: `payslip`, `reimbursement`, `manual` |

**Response:**
```json
{
  "count": 42
}
```
