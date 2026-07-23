# GET /audit-log/

List Audit Log. Requires `)
    rows, total = audit_log_queries.list_audit_log_paginated(
        db,
        caller_username=caller_username,
        target_username=target_username,
        endpoint=endpoint,
        occurred_after=occurred_after,
        occurred_before=occurred_before,
        page=page,
        limit=limit,
    )
    usernames: set[str] = set()
    for row in rows:
        if row.caller_username:
            usernames.add(row.caller_username)
        if row.target_username:
            usernames.add(row.target_username)
    employees_by_username = (
        employee_queries.find_employees_by_usernames(db, list(usernames)) if usernames else {}
    )
    return {
        ` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| caller_username | string | No |  |
| target_username | string | No |  |
| endpoint | string | No |  |
| occurred_after | string | No |  |
| occurred_before | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "occurred_at": "datetime",
      "caller_username": "string",
      "caller_preferred_name": "string",
      "endpoint": "string",
      "method": "string",
      "target_username": "string",
      "target_preferred_name": "string",
      "row_count": 0,
      "fields_touched": "string"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
