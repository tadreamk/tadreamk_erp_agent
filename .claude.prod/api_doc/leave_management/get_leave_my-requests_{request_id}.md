# GET /leave/my-requests/{request_id}

Get a specific leave request for the current user. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | The leave request's unique identifier |

**Response:** Leave request object

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to view this request
- `404` — Leave request not found
