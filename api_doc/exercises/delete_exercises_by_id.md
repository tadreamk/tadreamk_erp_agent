# DELETE /exercises/{exercise_id}


Soft-delete an exercise (sets `post_active` to `false`).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| exercise_id | UUID | Exercise ID |

**Response:**
```json
{
  "success": true,
  "message": "Exercise deleted successfully",
  "data": {
    "id": "uuid"
  }
}
```

**Errors:**
- `400` -- Invalid exercise ID format
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
- `404` -- Exercise not found

---

# 17. Exercise Score Instructions (Admin)

Manage reusable scoring instruction templates that can be attached to exercises. Each instruction contains markdown content describing how to evaluate exercise submissions.

**Access control:** Whitelist `exercise` required for all endpoints.

**Base URL:** `/api/v1`
