# POST /onboarding/{workflow_id}/send-to-talent


Send an invitation email to the talent (new hire) with a link to fill and sign documents. Requires workflow to be in `input` status. Sends both in-app notification and email (if email setting enabled).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "message": "Email sent to jane.doe@example.com",
  "status": "input"
}
```

**Errors:**
- `400` — Workflow not in `input` status
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
