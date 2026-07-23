# PUT /notification-settings/{category_key}

Update Setting. Requires `)
    try:
        setting = email_settings_crud.update_setting(
            db,
            category_key,
            is_enabled=payload.is_enabled,
            updated_by=user.username,
        )
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    if setting is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_key | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| is_enabled | boolean | Yes |  |

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
