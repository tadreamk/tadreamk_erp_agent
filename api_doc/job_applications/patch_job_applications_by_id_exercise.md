# PATCH /job-applications/{application_id}/exercise


Assign or unassign an exercise to an application. Sends an email notification to the candidate when an exercise is assigned (if the recruitment email setting is enabled).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Request Body (JSON):**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| exercise_id | string (UUID) or null | No | Exercise UUID to assign. Pass `null` to unassign. |

**Example Request:**
```json
{
  "exercise_id": "b2c3d4e5-..."
}
```

**Response (200):** Updated `JobApplicationResponse` object.

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format or invalid exercise ID format |
| 401 | Not authenticated |
| 403 | Admin or moderator access required |
| 404 | Application not found or exercise not found |
| 500 | Failed to update application exercise |

---

## 9. Job Application Actions (Admin)
