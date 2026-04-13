# POST /onboarding/{workflow_id}/documents

Add documents to a workflow. Replaces existing documents but preserves field values for matching template IDs. Workflow must be in `template_selection` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Auth:** Requires `onboarding` whitelist access (HR only).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| documents | array | Yes | Array of document objects |
| documents[].template_id | UUID | Yes | Template to use |
| documents[].document_type | string | No | `"onboarding"` (default) or `"contract"` |
| documents[].field_values | object | No | Initial field values (default `{}`) |

**Response:** `201 Created`
```json
{
  "message": "Added 3 documents to workflow",
  "count": 3
}
```

**Errors:**
- `400` — Can only modify documents in template_selection status
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
