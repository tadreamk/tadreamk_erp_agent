# GET /job-applications/{application_id}


Get a specific application by ID. Accessible by the application owner or any user with whitelist access to `job-applications`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| application_id | string (UUID) | Application ID |

**Response (200):**
```json
{
  "id": "a1b2c3d4-...",
  "job_post_id": "e5f6a7b8-...",
  "username": "johndoe",
  "family_name": "Doe",
  "given_name": "John",
  "email": "john@example.com",
  "phone": "+1234567890",
  "linkedin_url": "https://linkedin.com/in/johndoe",
  "portfolio_url": "https://johndoe.dev",
  "resume_url": "https://storage.googleapis.com/.../resume.pdf",
  "cover_letter": "I am excited to apply...",
  "additional_info": null,
  "job_title": "Senior Software Engineer",
  "status": "exercise_assigned",
  "created_at": "2026-01-15T10:30:00"
}
```

**Error Codes:**
| Code | Detail |
|------|--------|
| 400 | Invalid application ID format |
| 401 | Not authenticated |
| 403 | Access denied (not owner and no whitelist access) |
| 404 | Application not found |

---

## 8. Job Applications (Admin)
