# POST /onboarding/{workflow_id}/ceo-reject


CEO rejects the prepared documents. Transitions workflow from `pending_ceo_confirmation` back to `template_selection`. Optionally saves the rejection reason as an internal note. Sends rejection notification to HR.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reason | string | No | Rejection reason (saved as internal note) |

**Access:** CEO only.

**Response:**
```json
{
  "message": "CEO rejected onboarding documents",
  "status": "template_selection"
}
```

**Errors:**
- `400` — Workflow not in `pending_ceo_confirmation` status
- `401` — Not authenticated
- `403` — Only CEO can reject documents; no access to workflow
- `404` — Onboarding workflow not found
