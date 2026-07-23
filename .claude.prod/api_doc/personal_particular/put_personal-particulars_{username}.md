# PUT /personal-particulars/{username}

Update Personal Particular. Requires `)
    entry = personal_particular_write_ops.update_personal_particular(
        db,
        username,
        updated_by=user.username,
        fields=payload.model_dump(exclude_unset=True),
    )
    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| family_name_english | string | No |  |
| first_name_english | string | No |  |
| full_name_chinese | string | No |  |
| hkid | string | No |  |
| date_of_birth | string | No |  |
| gender | string | No |  |
| mobile_phone | string | No |  |
| personal_email | string | No |  |
| residential_address | string | No |  |

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
