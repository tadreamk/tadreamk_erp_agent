# POST /contracts/{contract_id}/reactivate

Reactivate Contract. Requires `)
    contract = get_contract_or_404_by_id(db, contract_id)
    try:
        contract = contract_write_ops.reactivate_contract(
            db, contract=contract, caller=user.username
        )
    except ContractReactivateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
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
