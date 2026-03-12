# POST /onboarding/{workflow_id}/return-to-talent


HR returns documents to talent for revision. Clears the `talent_submitted_at` and `sent_to_ceo_at` timestamps. Requires workflow to be in `input` status. Sends revision-request notification and email (if email setting enabled).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "message": "Documents returned to talent",
  "status": "input",
  "talent_submitted_at": null
}
```

**Errors:**
- `400` — Workflow not in `input` status
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Workflow not found

---

## 27. Onboarding HR Documents

Document management within onboarding workflows. Manage the list of template-based documents attached to a workflow, update field values, and upload PDFs.
