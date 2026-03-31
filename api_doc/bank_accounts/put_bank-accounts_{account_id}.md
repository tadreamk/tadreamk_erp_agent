# PUT /bank-accounts/{account_id}

Update a bank account. Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| account_id | UUID | Bank account ID |

**Request Body (all optional):**
```json
{
  "bank_name": "Updated Bank Name",
  "account_number": "new-account-number",
  "currency": "USD",
  "note": "Updated note",
  "is_active": true
}
```

**Response:** `200` — Updated account object

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Bank account not found
