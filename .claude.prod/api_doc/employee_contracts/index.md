# Employee Contracts API

Employee self-service prefix: `/employee-contract`
Admin prefix: `/admin/employee-contract`

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /employee-contract/me | Authenticated | Get own contract | [get_employee-contract_me.md](get_employee-contract_me.md) |
| POST | /employee-contract/me | Authenticated | Create own contract | [post_employee-contract_me.md](post_employee-contract_me.md) |
| PUT | /employee-contract/me | Authenticated | Update own contract | [put_employee-contract_me.md](put_employee-contract_me.md) |
| GET | /admin/employee-contract | `employee-contracts` whitelist | List all contracts | [get_admin_employee-contract.md](get_admin_employee-contract.md) |
| GET | /admin/employee-contract/{contract_id} | `employee-contracts` whitelist | Get contract by ID | [get_admin_employee-contract_{contract_id}.md](get_admin_employee-contract_{contract_id}.md) |
| POST | /admin/employee-contract | `employee-contracts` whitelist | Create contract for user | [post_admin_employee-contract.md](post_admin_employee-contract.md) |
| PUT | /admin/employee-contract/{contract_id} | `employee-contracts` whitelist | Update contract by ID | [put_admin_employee-contract_{contract_id}.md](put_admin_employee-contract_{contract_id}.md) |
| GET | /admin/employee-contract/{username}/history | `employee-contracts` whitelist | Get contract history | [get_admin_employee-contract_{username}_history.md](get_admin_employee-contract_{username}_history.md) |
