# Customer Management API

Base prefix: `/customers`

All endpoints require `customer-management` whitelist access.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /customers | List customers | [get_customers.md](get_customers.md) |
| GET | /customers/count | Get customer count | [get_customers_count.md](get_customers_count.md) |
| GET | /customers/{customer_id} | Get a customer by ID | [get_customers_{customer_id}.md](get_customers_{customer_id}.md) |
| POST | /customers | Create a customer | [post_customers.md](post_customers.md) |
| PUT | /customers/{customer_id} | Update a customer | [put_customers_{customer_id}.md](put_customers_{customer_id}.md) |
| DELETE | /customers/{customer_id} | Delete a customer | [delete_customers_{customer_id}.md](delete_customers_{customer_id}.md) |
