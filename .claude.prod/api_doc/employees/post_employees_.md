# POST /employees/

Create Employee. Requires `)
    if payload.manager_username and payload.manager_username == payload.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| username | string | Yes |  |
| work_email | string | Yes |  |
| preferred_name | string | Yes |  |
| manager_username | string | No |  |

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
