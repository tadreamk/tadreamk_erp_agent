# DELETE /personal-particulars/{username}

Delete Personal Particular. Requires `)
    removed = personal_particular_write_ops.delete_personal_particular(db, username)
    if not removed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist.

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
