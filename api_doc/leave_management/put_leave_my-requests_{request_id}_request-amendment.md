# PUT /leave/my-requests/{request_id}/request-amendment

Submit an amendment request for an approved leave. Requires authentication. Leave must be in `approved` status and have no pending amendments.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| request_id | uuid | Yes | Leave request ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| amendment_type | string | Yes | `cancel` or `change` |
| reason | string | Yes | Reason for amendment |
| new_leave_periods | list | No | Required for `change` type — new leave periods |
| new_swap_work_periods | list | No | New swap work periods for `change` type |

**Response:**
```json
{
  "id": "uuid",
  "leave_request_id": "uuid",
  "amendment_type": "cancel",
  "reason": "Plans changed",
  "status": "pending",
  "requested_by": "john_doe",
  "created_at": "datetime"
}
```

**Errors:**
- `400` — Can only amend approved leave / Pending amendment already exists / new_leave_periods required for change type
- `401` — Not authenticated
- `403` — Not authorized to amend this request
- `404` — Leave request not found
