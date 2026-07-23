# GET /leave/all

List All Requests. Requires `)
    rows, total = leave_crud.find_all(
        db,
        status_filter=status_filter,
        leave_type=leave_type,
        employee_username=employee_username,
        manager_username=manager_username,
        from_date=_parse_date(from_date),
        to_date=_parse_date(to_date),
        page=page,
        limit=limit,
    )
    return {
        ` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| leave_type | string | No |  |
| employee_username | string | No |  |
| manager_username | string | No |  |
| from_date | string | No |  |
| to_date | string | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "employee_username": "string",
      "employee_preferred_name": "string",
      "manager_username": "string",
      "manager_preferred_name": "string",
      "leave_type": "string",
      "leave_periods": [
        {}
      ],
      "swap_work_periods": [
        {}
      ],
      "swap_pair_id": "uuid",
      "supporting_document_urls": [
        "string"
      ],
      "remarks": "string",
      "status": "pending",
      "reviewed_by_username": "string",
      "reviewed_by_preferred_name": "string",
      "reviewed_at": "datetime",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
