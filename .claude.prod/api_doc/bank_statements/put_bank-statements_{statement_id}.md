# PUT /bank-statements/{statement_id}

Save Bank Statement. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| header | BankStatementHeaderPayload | Yes |  |
| records | array[BankStatementRecordPayload] | No |  |

**Response:**
```json
{
  "id": "uuid",
  "bank_name": "string",
  "account_number": "string",
  "statement_year": 0,
  "statement_month": 0,
  "statement_date": "date",
  "opening_balance": "string",
  "closing_balance": "string",
  "note": "string",
  "attachments": [
    {
      "file_id": "string",
      "filename": "string",
      "file_url": "string",
      "file_size": 0,
      "content_type": "string",
      "is_active": true
    }
  ],
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string",
  "records": [
    {
      "id": "uuid",
      "bank_statement_id": "uuid",
      "transaction_date": "date",
      "description": "string",
      "deposit_amount": "string",
      "withdrawal_amount": "string",
      "running_balance": "string",
      "record_order": 0,
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
}
```

**Errors:**
- `422` — Validation Error
