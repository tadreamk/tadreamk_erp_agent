# POST /onboarding/{workflow_id}/cancel


Cancel an onboarding workflow. Can be cancelled from any status except `complete`. Transitions to `cancelled`. Sends cancellation notification and email (if email setting enabled).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| reason | string | No | Cancellation reason |

**Response:**
```json
{
  "message": "Workflow cancelled",
  "status": "cancelled"
}
```

**Errors:**
- `400` — Cannot cancel a completed workflow
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
