# POST /onboarding/{workflow_id}/ceo-sign


CEO signs the workflow, applying the CEO signature to all documents that have a `ceo_signature` field. Transitions workflow from `input` to `complete`. Triggers sync to employee contract table and sends completion notification.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| ceo_signature | string | Yes | CEO signature data (base64 encoded image) |

**Request Example:**
```json
{
  "ceo_signature": "data:image/png;base64,iVBORw0KGgo..."
}
```

**Response:**
```json
{
  "message": "Workflow signed and completed",
  "status": "complete"
}
```

**Errors:**
- `400` — Workflow not in `input` status; CEO signature missing
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found

---

## 26. Onboarding HR Actions

Workflow lifecycle actions performed by HR. All endpoints require `onboarding` whitelist access.
