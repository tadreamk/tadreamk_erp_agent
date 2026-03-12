# Whitelist API (Admin)

Direct access control system — admins explicitly grant section-level access per employee. No role-based hierarchy; each user's permissions are individually managed.

**Access control:** Whitelist `whitelist` required for all endpoints except `GET /whitelist/my-endpoints`.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/whitelist/my-endpoints` | Get current authenticated user's accessible endpoints. No admin whitelist needed | [get_whitelist_my_endpoints.md](./get_whitelist_my_endpoints.md) |
| `GET` | `/whitelist/endpoints` | Get list of all valid ERP endpoints from the database. | [get_whitelist_endpoints.md](./get_whitelist_endpoints.md) |
| `GET` | `/whitelist/stats` | Get whitelist statistics — total active entries plus count per endpoint. | [get_whitelist_stats.md](./get_whitelist_stats.md) |
| `GET` | `/whitelist/` | List whitelist entries with filtering and pagination. | [get_whitelist.md](./get_whitelist.md) |
| `GET` | `/whitelist/entry/{whitelist_id}` | Get a single whitelist entry by ID. | [get_whitelist_entry_by_id.md](./get_whitelist_entry_by_id.md) |
| `GET` | `/whitelist/user/{username}` | Get a specific user's accessible endpoints. | [get_whitelist_user_by_id.md](./get_whitelist_user_by_id.md) |
| `POST` | `/whitelist/` | Create a new whitelist entry. | [post_whitelist.md](./post_whitelist.md) |
| `POST` | `/whitelist/bulk` | Bulk-create whitelist entries for a single user across multiple endpoints. | [post_whitelist_bulk.md](./post_whitelist_bulk.md) |
| `PUT` | `/whitelist/{whitelist_id}` | Update a whitelist entry (change username or endpoint). | [put_whitelist_by_id.md](./put_whitelist_by_id.md) |
| `DELETE` | `/whitelist/{whitelist_id}` | Deactivate (soft delete) a whitelist entry with audit trail. | [delete_whitelist_by_id.md](./delete_whitelist_by_id.md) |
