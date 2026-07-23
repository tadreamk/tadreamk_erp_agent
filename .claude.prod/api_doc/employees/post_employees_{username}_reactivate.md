# POST /employees/{username}/reactivate

Reactivate Employee. Requires `)
    entry = employee_crud.reactivate_employee(db, username, reactivated_by=user.username)
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=` whitelist.

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
