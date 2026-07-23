# POST /leave/me/requests

Submit My Request. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| leave_type | LeaveTypeEnum | Yes |  |
| leave_periods | array[LeavePeriod] | Yes |  |
| swap_work_periods | array[LeavePeriod] | No |  |
| swap_pair_id | string | No |  |
| supporting_document_urls | array[string] | No |  |
| remarks | string | No |  |

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
