# GET /personal-particulars/

List Personal Particulars. Requires `)
    rows, total = personal_particular_queries.list_personal_particulars_left_join_employee(
        db,
        search=search,
        include_inactive=include_inactive,
        page=page,
        limit=limit,
    )
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No |  |
| include_inactive | boolean | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "username": "string",
      "preferred_name": "string",
      "family_name_english": "string",
      "first_name_english": "string",
      "full_name_chinese": "string",
      "mobile_phone": "string",
      "is_active": false
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
