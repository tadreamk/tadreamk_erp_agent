# GET /bank-accounts/{username}

Get Bank Account. Requires `)
    entry = get_bank_account_or_404_by_username(db, username)
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=f` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string |  |

**Response:**
```json
{
  "success": false,
  "message": "string",
  "data": {}
}
```

**Errors:**
- `422` — Validation Error
