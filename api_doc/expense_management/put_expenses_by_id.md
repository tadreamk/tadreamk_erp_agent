# PUT /expenses/{expense_id}


Update an existing expense. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | Expense ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category_id | UUID | No | FK to expense category |
| total_value | decimal | No | Total expense amount (>= 0) |
| note | string | No | Additional notes |
| file_urls | string[] | No | List of supporting document URLs |

**Response:** Updated expense object.

**Errors:**
- `404` -- Expense not found
