# GET /job-applications-workflow/{workflow_id}/exercise-content


Get the exercise content assigned to a workflow. Accessible by the workflow owner (candidate) or staff.

**Access:** Authenticated (workflow owner or whitelist staff)

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | UUID | Yes | Workflow ID |

**Response:**
```json
{
  "id": "uuid-string",
  "title": "Backend API Design Challenge",
  "tags": ["python", "api", "design"],
  "content": "## Instructions\n\nDesign and implement a REST API..."
}
```

**Errors:**
- `400` — Invalid UUID format
- `401` — Not authenticated
- `403` — Access denied (not staff and not workflow owner)
- `404` — Workflow not found / no exercise assigned / exercise record not found

---

## 15. Job Application Workflow (Interview)

Interview scheduling, confirmation, scoring, and management (Steps 5-6 of the workflow).
