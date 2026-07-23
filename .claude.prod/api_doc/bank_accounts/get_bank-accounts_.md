# GET /bank-accounts/

List Bank Accounts. Requires `)
    rows, total = bank_account_queries.list_bank_accounts_left_join_employee(
        db, search=search, page=page, limit=limit
    )
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "username": "string",
      "preferred_name": "string",
      "bank_name": "string",
      "bank_account_number_last4": "string",
      "bank_record_status": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
