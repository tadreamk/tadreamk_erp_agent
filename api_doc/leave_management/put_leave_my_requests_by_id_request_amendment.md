# PUT /leave/my-requests/{request_id}/request-amendment


Submit an amendment request for an approved leave. Only approved leave requests can be amended. Only one pending amendment is allowed per leave request at a time.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | Leave request ID (must have `approved` status) |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| amendment_type | string | Yes | `cancel` or `change` |
| reason | string | Yes | Reason for the amendment (non-empty) |
| new_leave_periods | array | Conditional | Required when `amendment_type` is `change`; new leave period objects |
| new_swap_work_periods | array | No | New swap work period objects (for swap-type leave changes) |

**Request example (cancel):**
```json
{
  "amendment_type": "cancel",
  "reason": "Plans changed, no longer need time off"
}
```

**Request example (change):**
```json
{
  "amendment_type": "change",
  "reason": "Need to shift dates by one week",
  "new_leave_periods": [
    {
      "start_date": "2026-04-08",
      "start_apm": "AM",
      "end_date": "2026-04-10",
      "end_apm": "PM"
    }
  ]
}
```

**Response:**
```json
{
  "id": "c3d4e5f6-a7b8-9012-cdef-123456789012",
  "leave_request_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "amendment_type": "cancel",
  "new_leave_periods": null,
  "new_swap_work_periods": null,
  "reason": "Plans changed, no longer need time off",
  "status": "pending",
  "requested_by": "john.doe",
  "reviewed_by": null,
  "reviewed_at": null,
  "created_at": "2026-03-11T10:00:00+00:00"
}
```

**Errors:**
- `400` — Can only request amendments for approved leave
- `400` — There is already a pending amendment for this request
- `400` — `new_leave_periods` is required for change amendments
- `401` — Not authenticated
- `403` — Not authorized to amend this request
- `404` — Leave request not found
