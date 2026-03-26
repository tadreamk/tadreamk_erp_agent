# PUT /onboarding/{workflow_id}

Update an onboarding workflow. Validates status transitions. Requires `onboarding` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| talent_email | string | No | Updated talent email |
| talent_username | string | No | Updated talent username |
| hr_username | string | No | Updated HR username |
| ceo_username | string | No | Updated CEO username |
| status | string | No | New status (must be valid transition) |

**Response:**
```json
{
  "message": "Onboarding workflow updated",
  "workflow": { "...workflow object..." }
}
```

**Errors:**
- `400` — Invalid status value or invalid status transition
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
- `404` — Workflow not found
