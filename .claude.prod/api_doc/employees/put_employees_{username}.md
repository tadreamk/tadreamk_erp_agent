# PUT /employees/{username}

Update Employee. Requires `)
    try:
        entry = employee_crud.update_employee(
            db,
            username,
            updated_by=user.username,
            new_work_email=payload.work_email,
            new_preferred_name=payload.preferred_name,
            new_manager_username=payload.manager_username,
            new_is_active=payload.is_active,
        )
    except EmployeeUpdateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    if not entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| work_email | string | No |  |
| preferred_name | string | No |  |
| manager_username | string | No |  |
| is_active | boolean | No |  |

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
