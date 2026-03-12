# 47. Customer Management

Manage customer records with contact details, company info, industry classification, and lead source tracking.

**Base path:** `/customers`

**Access control:** Whitelist `customer-management` required for all endpoints.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/customers` | List all customers with optional filters. | [get_customers.md](./get_customers.md) |
| `GET` | `/customers/count` | Get total count of customers matching the given filters. | [get_customers_count.md](./get_customers_count.md) |
| `GET` | `/customers/{customer_id}` | Get a specific customer by ID. | [get_customers_by_id.md](./get_customers_by_id.md) |
| `POST` | `/customers` | Create a new customer record. | [post_customers.md](./post_customers.md) |
| `PUT` | `/customers/{customer_id}` | Update an existing customer record. | [put_customers_by_id.md](./put_customers_by_id.md) |
| `DELETE` | `/customers/{customer_id}` | Soft delete a customer record. | [delete_customers_by_id.md](./delete_customers_by_id.md) |
