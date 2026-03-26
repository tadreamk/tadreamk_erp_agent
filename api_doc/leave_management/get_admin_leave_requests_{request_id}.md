# GET /admin/leave/requests/{request_id}

Get a specific leave request (admin view). Requires `leave-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | The leave request's unique identifier |

**Response:** Full leave request object

**Errors:**
- `401` — Not authenticated
- `403` — No leave-management whitelist access
- `404` — Leave request not found
