# POST /onboarding/{workflow_id}/documents


Add documents (by template) to a workflow. Replaces existing documents but preserves previously saved field values for templates that remain. Only allowed in `template_selection` status.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| documents | array | Yes | List of document objects |
| documents[].template_id | UUID | Yes | Template to use |
| documents[].document_type | string | No | `"onboarding"` (default) or `"contract"` |
| documents[].field_values | object | No | Pre-filled field values (default: `{}`) |

**Request Example:**
```json
{
  "documents": [
    { "template_id": "uuid-1", "document_type": "contract" },
    { "template_id": "uuid-2", "document_type": "onboarding", "field_values": { "department": "Engineering" } }
  ]
}
```

**Response (201):**
```json
{
  "message": "Added 2 documents to workflow",
  "count": 2
}
```

**Errors:**
- `400` — Workflow not in `template_selection` status
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
