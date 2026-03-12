# POST /job-applications/admin/{application_id}/reject


Reject a candidate with a mandatory reason. Changes status to `rejected` and sends a rejection email.

**Precondition:** Application must not already be `rejected` or `accepted`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Request Body (JSON):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | Yes | Reason for rejection (1-2000 characters) |

**Example Request:**
```json
{
  "reason": "Candidate does not meet the minimum experience requirements for this role."
}
```

**Response (200):**
```json
{
  "message": "Candidate rejected",
  "application": {
    "id": "a1b2c3d4-...",
    "status": "rejected",
    "...": "..."
  }
}
```

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format, application is already rejected, or cannot reject an already accepted application |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found |

---

## 10. Job Application Interview (Admin)
