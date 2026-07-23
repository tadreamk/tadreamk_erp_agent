# POST /contracts/{contract_id}/deactivate

Deactivate Contract. Requires `)
    contract = get_contract_or_404_by_id(db, contract_id)
    contract = contract_write_ops.deactivate_contract(db, contract=contract, caller=user.username)
    return APIResponse(
        success=True,
        message=` whitelist.

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
