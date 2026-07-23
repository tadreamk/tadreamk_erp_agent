# GET /personal-particulars/{username}

Get Personal Particular. Requires `)
    entry = get_personal_particular_or_404_by_username(db, username)
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
