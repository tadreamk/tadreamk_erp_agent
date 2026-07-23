# Customer API

Base prefixes:
- `/customer`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /customer | Authenticated | List Customers | [get_customer.md](get_customer.md) |
| POST | /customer | Authenticated | Create Customer | [post_customer.md](post_customer.md) |
| DELETE | /customer/{customer_id} | Authenticated | Soft Delete Customer | [delete_customer_{customer_id}.md](delete_customer_{customer_id}.md) |
| GET | /customer/{customer_id} | Authenticated | Get Customer | [get_customer_{customer_id}.md](get_customer_{customer_id}.md) |
| PUT | /customer/{customer_id} | Authenticated | Update Customer | [put_customer_{customer_id}.md](put_customer_{customer_id}.md) |
