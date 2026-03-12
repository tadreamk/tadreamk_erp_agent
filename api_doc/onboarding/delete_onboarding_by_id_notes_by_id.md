# DELETE /onboarding/{workflow_id}/notes/{note_id}


Delete a note. Only the original author can delete.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | string (UUID) | Onboarding workflow ID |
| note_id | string (UUID) | Note ID |

**Access:** HR or CEO only. Author-only deletion.

**Response:** `204 No Content` (empty body)

**Errors:**
- `400` — Invalid workflow_id or note_id format
- `401` — Not authenticated
- `403` — Notes are not accessible to talent; you can only modify your own notes; no access to workflow
- `404` — Note not found

---

## 30. Onboarding (Talent)

Talent-facing portal for the new hire to view their onboarding, fill in document fields, sign, upload PDFs, and submit. All endpoints require authentication and verify the requesting user's email matches the workflow's `talent_email`.

**Base prefix:** `/talent/onboarding`
