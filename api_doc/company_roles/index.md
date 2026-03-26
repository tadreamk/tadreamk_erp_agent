# Company Roles API

Base prefix: `/admin/company-roles`

All endpoints require `company-roles` whitelist access.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /admin/company-roles/roles | List all role titles | [get_admin_company-roles_roles.md](get_admin_company-roles_roles.md) |
| GET | /admin/company-roles/roles/{role_title}/users | List users with a role | [get_admin_company-roles_roles_{role_title}_users.md](get_admin_company-roles_roles_{role_title}_users.md) |
| GET | /admin/company-roles | List all role assignments | [get_admin_company-roles.md](get_admin_company-roles.md) |
| POST | /admin/company-roles | Assign a role to a user | [post_admin_company-roles.md](post_admin_company-roles.md) |
| DELETE | /admin/company-roles/{username}/{role_title} | Revoke a role from a user | [delete_admin_company-roles_{username}_{role_title}.md](delete_admin_company-roles_{username}_{role_title}.md) |
