# GET /admin/leave/requests/{request_id}


Get a specific leave request by ID (admin view, no ownership restriction).

**Access control:** Whitelist `leave-management` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | Leave request ID |

**Response:**
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "employee_username": "john.doe",
  "manager_username": "jane.smith",
  "leave_type": "annual",
  "leave_periods": [
    {
      "start_date": "2026-04-01",
      "start_apm": "AM",
      "end_date": "2026-04-03",
      "end_apm": "PM"
    }
  ],
  "swap_work_periods": null,
  "total_days": 3.0,
  "leave_reason": "Family vacation",
  "supporting_document_urls": [],
  "status": "pending",
  "reviewed_by_username": null,
  "reviewed_at": null,
  "created_at": "2026-03-10T08:00:00+00:00",
  "updated_at": null
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`
- `404` — Leave request not found
