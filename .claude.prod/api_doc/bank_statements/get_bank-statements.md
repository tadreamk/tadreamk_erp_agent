# GET /bank-statements

List Bank Statements. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| year | integer | No |  |
| bank_name | string | No |  |
| account_number | string | No |  |
| skip | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "items": [
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
          "file_id": {},
          "filename": {},
          "file_url": {},
          "file_size": {},
          "content_type": {},
          "is_active": {}
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
          "id": {},
          "bank_statement_id": {},
          "transaction_date": {},
          "description": {},
          "deposit_amount": {},
          "withdrawal_amount": {},
          "running_balance": {},
          "record_order": {},
          "created_at": {},
          "updated_at": {}
        }
      ]
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
