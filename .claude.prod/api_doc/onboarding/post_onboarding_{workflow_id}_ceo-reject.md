# POST /onboarding/{workflow_id}/ceo-reject

CEO rejects onboarding documents, transitioning status from `ceo_confirmation` back to `template_selection`. Creates an internal note with the rejection reason.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reason | string | No | Rejection reason (saved as a note) |

**Auth:** Requires `onboarding` whitelist or CEO owner access.

**Response:** `200 OK`
```json
{
  "message": "CEO rejected onboarding documents",
  "status": "template_selection"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only CEO can reject documents
- `404` — Workflow not found
