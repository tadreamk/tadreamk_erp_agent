# POST /leave/my-requests/{request_id}/documents

Upload supporting documents (e.g., sick leave certificate) for a leave request. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | The leave request's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| document_urls | list[string] | Yes | URLs of uploaded documents |

**Response:**
```json
{
  "message": "Documents uploaded successfully",
  "leave_request": { "...updated leave request..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to modify this request
- `404` — Leave request not found
