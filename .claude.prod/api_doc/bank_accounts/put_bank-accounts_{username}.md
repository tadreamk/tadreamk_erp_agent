# PUT /bank-accounts/{username}

Upsert Bank Account. Requires `)
    try:
        entry = bank_account_write_ops.upsert_bank_account(
            db,
            username=username,
            actor_username=user.username,
            fields=payload.model_dump(exclude_unset=True),
        )
    except BankAccountWriteError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    audit_names = resolve_audit_pair_names(
        db,
        created_by=entry.created_by,
        updated_by=entry.updated_by,
    )
    return APIResponse(
        success=True,
        message=` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| bank_name | string | No |  |
| bank_code | string | No |  |
| branch_code | string | No |  |
| bank_account_number | string | No |  |
| bank_beneficiary_name | string | No |  |

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
