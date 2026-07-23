# GET /hr-requests/all/{request_id}

Get Request For Oversight. Requires `)
    row = get_hr_request_or_404(db, request_id)
    return APIResponse(
        success=True,
        message=` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | string |  |

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
