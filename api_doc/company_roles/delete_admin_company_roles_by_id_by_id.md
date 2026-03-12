# DELETE /admin/company-roles/{username}/{role_title}


Revoke a role from a user (soft revoke -- sets the assignment to inactive).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| username | string | Yes | Username to revoke the role from |
| role_title | string | Yes | Role title to revoke |

**Response:** `204 No Content` (empty body)

**Errors:**
- `400` -- Role assignment is already revoked
- `404` -- User '{username}' does not have role '{role_title}'
