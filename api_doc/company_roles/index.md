# Company Roles API (Admin)

Manages company role assignments -- mapping users to role titles (e.g., `head_of_hr`, `head_of_it`, `ceo`). Roles are used for access control and notification routing throughout the ERP system.

**Access control:** Whitelist `company-roles` required for all endpoints.

---

## 24. Company Roles (Admin)

Base path: `/admin/company-roles`

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/admin/company-roles/roles` | List all available roles (distinct role titles) in the system. | [get_admin_company_roles_roles.md](./get_admin_company_roles_roles.md) |
| `GET` | `/admin/company-roles/roles/{role_title}/users` | List all active usernames assigned to a specific role. | [get_admin_company_roles_roles_by_id_users.md](./get_admin_company_roles_roles_by_id_users.md) |
| `GET` | `/admin/company-roles` | List all company role assignments with pagination. | [get_admin_company_roles.md](./get_admin_company_roles.md) |
| `POST` | `/admin/company-roles` | Assign a role to a user. If the role title does not already exist, it will be cr | [post_admin_company_roles.md](./post_admin_company_roles.md) |
| `DELETE` | `/admin/company-roles/{username}/{role_title}` | Revoke a role from a user (soft revoke -- sets the assignment to inactive). | [delete_admin_company_roles_by_id_by_id.md](./delete_admin_company_roles_by_id_by_id.md) |
