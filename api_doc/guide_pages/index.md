# Guide Pages API

Internal knowledge base pages organized by section with ordering support. Employee endpoints return active pages only (content excluded in list view for performance). Admin endpoints support full CRUD with active/inactive management.

**Access control:** Employee endpoints require authentication and an active employee record. Admin endpoints require whitelist `guide-pages`.

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/guide-pages` | List all active guide pages (content excluded for performance). Employee only. | [get_guide_pages.md](./get_guide_pages.md) |
| `GET` | `/guide-pages/{slug}` | Get a single guide page by slug (with content). Employee only. | [get_guide_pages_by_slug.md](./get_guide_pages_by_slug.md) |
| `GET` | `/guide-pages/admin` | List all guide pages including inactive. Admin only. | [get_guide_pages_admin.md](./get_guide_pages_admin.md) |
| `POST` | `/guide-pages/admin` | Create a new guide page. Admin only. | [post_guide_pages_admin.md](./post_guide_pages_admin.md) |
| `PUT` | `/guide-pages/admin/{page_id}` | Update an existing guide page. Admin only. | [put_guide_pages_admin_by_id.md](./put_guide_pages_admin_by_id.md) |
| `DELETE` | `/guide-pages/admin/{page_id}` | Delete a guide page. Admin only. | [delete_guide_pages_admin_by_id.md](./delete_guide_pages_admin_by_id.md) |
