# POST /personal-particulars/

Create Personal Particular. Requires `)
    try:
        entry = personal_particular_write_ops.create_personal_particular(
            db,
            username=username,
            created_by=user.username,
            fields=payload.model_dump(exclude_unset=True),
        )
    except PersonalParticularCreateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    return APIResponse(
        success=True,
        message=` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes |  |

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
