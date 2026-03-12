# DELETE /job-applications-workflow/{workflow_id}/notes/{note_id}


Delete a note. Only the original author can delete.

**Access:** Whitelist (`job-applications`) + note author only

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |
| note_id | UUID | Yes | Note ID |

**Response:** `204 No Content` (empty body)

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Staff access required / not the note author
- `404` — Note not found

---

## 12. Job Application Workflow (Dashboard)

Dashboard endpoints for listing, filtering, and viewing workflow records. Includes both staff (admin) and talent (candidate) views.
