# GET /contracts/{contract_id}

Get Contract. Requires `)
    entry = get_contract_or_404_by_id(db, contract_id)
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=f` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| contract_id | string |  |

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
