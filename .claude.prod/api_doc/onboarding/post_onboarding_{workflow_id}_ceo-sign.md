# POST /onboarding/{workflow_id}/ceo-sign

CEO signs the onboarding workflow. Transitions status to `completed` and applies the CEO signature to all documents with a `ceo_signature` field. Requires `onboarding` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ceo_signature | string | Yes | CEO's signature data (base64 or URL) |

**Response:**
```json
{
  "message": "Workflow signed and completed",
  "status": "completed"
}
```

**Errors:**
- `400` — CEO signature not provided in request body
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
