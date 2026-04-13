# POST /onboarding

Create a new onboarding workflow. Requires `onboarding` whitelist access.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| talent_email | string | Yes | Talent's email address |
| talent_username | string | Yes | Talent's username |
| hr_username | string | Yes | HR staff username |
| ceo_username | string | Yes | CEO username |
| status | string | Yes | Initial status (must be valid OnboardingWorkflowStatus) |

**Response:** `201 Created`
```json
{
  "message": "Onboarding workflow created",
  "workflow": { "...workflow object..." }
}
```

**Errors:**
- `400` — Invalid status value
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
