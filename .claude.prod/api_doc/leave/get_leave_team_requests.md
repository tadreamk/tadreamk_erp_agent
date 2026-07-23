# GET /leave/team/requests

List Team Requests. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No |  |
| leave_type | string | No |  |
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
