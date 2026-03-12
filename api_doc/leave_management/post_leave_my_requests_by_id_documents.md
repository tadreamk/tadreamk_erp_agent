# POST /leave/my-requests/{request_id}/documents


Upload supporting document URLs for a leave request.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| request_id | UUID | Leave request ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| document_urls | array of strings | Yes | List of document URLs to attach |

**Request example:**
```json
{
  "document_urls": [
    "https://storage.example.com/docs/medical-cert-001.pdf"
  ]
}
```

**Response:**
```json
{
  "message": "Documents uploaded successfully",
  "leave_request": {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "supporting_document_urls": [
      "https://storage.example.com/docs/medical-cert-001.pdf"
    ],
    "...": "..."
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized to modify this request
- `404` — Leave request not found
