# GET /contracts/

List Contracts. Requires `)
    rows, total = contract_queries.list_contracts_paginated(
        db,
        search=search,
        include_inactive_employees=include_inactive_employees,
        include_inactive_contracts=include_inactive_contracts,
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
| include_inactive_employees | boolean | No |  |
| include_inactive_contracts | boolean | No |  |
| page | integer | No |  |
| limit | integer | No |  |

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "username": "string",
      "preferred_name": "string",
      "position": "string",
      "start_date": "date",
      "employment_type": "string",
      "contract_pay_type": "string",
      "is_active": false,
      "is_currently_effective": false
    }
  ],
  "total": 0,
  "page": 0,
  "limit": 0
}
```

**Errors:**
- `422` — Validation Error
