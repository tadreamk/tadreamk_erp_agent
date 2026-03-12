# Employees API

Manages employee records. Split into self-service endpoints (authenticated employees managing their own profile) and admin/HR endpoints (whitelist-protected, for managing all employees).

---

## 18. Employees (Self-Service)

Base path: `/employee`

**Authentication:** All endpoints require user authentication via request headers.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/employee/me` | Get the current authenticated employee's profile. | [get_employee_me.md](./get_employee_me.md) |
| `GET` | `/employee/my-company-roles` | Get the current authenticated user's active company roles. | [get_employee_my_company_roles.md](./get_employee_my_company_roles.md) |
| `GET` | `/employees` | Get all employees with filtering and pagination. Returns employee list enriched  | [get_employees.md](./get_employees.md) |
| `GET` | `/employees/departments` | Get unique department names from all employee contracts, for use in filter dropd | [get_employees_departments.md](./get_employees_departments.md) |
| `GET` | `/employees/active` | Get active employees for picker/dropdown selection. Returns minimal fields plus  | [get_employees_active.md](./get_employees_active.md) |
| `GET` | `/employees/stats` | Get employee count statistics. | [get_employees_stats.md](./get_employees_stats.md) |
| `POST` | `/employees` | Create a new employee record. | [post_employees.md](./post_employees.md) |
| `GET` | `/employees/company-roles` | Get all active company roles with employee name details. Enriches each role reco | [get_employees_company_roles.md](./get_employees_company_roles.md) |
| `PUT` | `/employees/company-roles/{role_title}` | Update username assignment for a company role. Revokes all existing active assig | [put_employees_company_roles_by_id.md](./put_employees_company_roles_by_id.md) |
| `GET` | `/employees/{employee_id}` | Get a specific employee by ID. | [get_employees_by_id.md](./get_employees_by_id.md) |
| `GET` | `/employees/{employee_id}/full` | Get full employee details including nested contract and personal particular data | [get_employees_by_id_full.md](./get_employees_by_id_full.md) |
| `PUT` | `/employees/{employee_id}` | Update an employee record. Only fields included in the request body are updated. | [put_employees_by_id.md](./put_employees_by_id.md) |
| `POST` | `/employees/{employee_id}/deactivate` | Deactivate an active employee. | [post_employees_by_id_deactivate.md](./post_employees_by_id_deactivate.md) |
| `POST` | `/employees/{employee_id}/reactivate` | Reactivate a deactivated employee. | [post_employees_by_id_reactivate.md](./post_employees_by_id_reactivate.md) |
| `DELETE` | `/employees/{employee_id}` | Soft-delete an employee record. | [delete_employees_by_id.md](./delete_employees_by_id.md) |
