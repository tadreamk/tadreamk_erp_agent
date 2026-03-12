# Employee Contract API

Manages employee contract records including employment terms, compensation, and signatures. Split into self-service endpoints (employees managing their own contract) and admin/HR endpoints (whitelist-protected, for managing all contracts).

---

## 22. Employee Contract (Self-Service)

Base path: `/employee-contract`

**Authentication:** All endpoints require user authentication via request headers.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/employee-contract/me` | Get the authenticated user's employee contract data. | [get_employee_contract_me.md](./get_employee_contract_me.md) |
| `POST` | `/employee-contract/me` | Create employee contract data for the authenticated user. Each user can only hav | [post_employee_contract_me.md](./post_employee_contract_me.md) |
| `PUT` | `/employee-contract/me` | Update employee contract data for the authenticated user. Only fields included i | [put_employee_contract_me.md](./put_employee_contract_me.md) |
| `GET` | `/admin/employee-contract` | List all employee contracts with optional search and department filters. | [get_admin_employee_contract.md](./get_admin_employee_contract.md) |
| `GET` | `/admin/employee-contract/{contract_id}` | Get a single employee contract by ID. | [get_admin_employee_contract_by_id.md](./get_admin_employee_contract_by_id.md) |
| `POST` | `/admin/employee-contract` | Create a new employee contract. Requires the target username as a query paramete | [post_admin_employee_contract.md](./post_admin_employee_contract.md) |
| `PUT` | `/admin/employee-contract/{contract_id}` | Update an existing employee contract. Only fields included in the request body a | [put_admin_employee_contract_by_id.md](./put_admin_employee_contract_by_id.md) |
