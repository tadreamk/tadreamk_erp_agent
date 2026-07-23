# GET /bank-statements/bank-accounts

List Distinct Bank Accounts. Requires authentication.

**Response:**
```json
{
  "items": [
    {
      "bank_name": "string",
      "account_number": "string"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
