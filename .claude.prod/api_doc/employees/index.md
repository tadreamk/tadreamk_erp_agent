# Employees API

Admin prefix: `/employees` (requires `employees` whitelist)
Self-service prefix: `/employee` (requires authentication)

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /employees | `employees` whitelist | List all employees | [get_employees.md](get_employees.md) |
| GET | /employees/departments | `employees` whitelist | List departments | [get_employees_departments.md](get_employees_departments.md) |
| GET | /employees/active | `employees` whitelist | Get active employees picker | [get_employees_active.md](get_employees_active.md) |
| GET | /employees/stats | `employees` whitelist | Get employee statistics | [get_employees_stats.md](get_employees_stats.md) |
| POST | /employees | `employees` whitelist | Create an employee | [post_employees.md](post_employees.md) |
| GET | /employees/company-roles | `employees` whitelist | List all company roles | [get_employees_company-roles.md](get_employees_company-roles.md) |
| PUT | /employees/company-roles/{role_title} | `employees` whitelist | Update role assignment | [put_employees_company-roles_{role_title}.md](put_employees_company-roles_{role_title}.md) |
| GET | /employees/{employee_id} | `employees` whitelist | Get employee by ID | [get_employees_{employee_id}.md](get_employees_{employee_id}.md) |
| GET | /employees/{employee_id}/full | `employees` whitelist | Get full employee details | [get_employees_{employee_id}_full.md](get_employees_{employee_id}_full.md) |
| PUT | /employees/{employee_id} | `employees` whitelist | Update an employee | [put_employees_{employee_id}.md](put_employees_{employee_id}.md) |
| POST | /employees/{employee_id}/deactivate | `employees` whitelist | Deactivate an employee | [post_employees_{employee_id}_deactivate.md](post_employees_{employee_id}_deactivate.md) |
| POST | /employees/{employee_id}/reactivate | `employees` whitelist | Reactivate an employee | [post_employees_{employee_id}_reactivate.md](post_employees_{employee_id}_reactivate.md) |
| DELETE | /employees/{employee_id} | `employees` whitelist | Delete an employee | [delete_employees_{employee_id}.md](delete_employees_{employee_id}.md) |
| GET | /employee/me | Authenticated | Get own employee record | [get_employee_me.md](get_employee_me.md) |
| GET | /employee/my-company-roles | Authenticated | Get own company roles | [get_employee_my-company-roles.md](get_employee_my-company-roles.md) |
