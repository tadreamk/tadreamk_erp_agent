# DELETE /admin/company-roles/{username}/{role_title}

Revoke a role from a user. Requires `company-roles` whitelist. Returns 204 No Content on success.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string | Username of the employee |
| role_title | string | Role title to revoke |

**Response:** `204 No Content`

**Errors:**
- `400` — Role assignment is already revoked
- `401` — Not authenticated
- `403` — No company-roles whitelist access
- `404` — User does not have this role
