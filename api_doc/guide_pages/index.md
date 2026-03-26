# Guide Pages API

Employee prefix: `/guide-pages` (requires employee authentication)
Admin prefix: `/guide-pages/admin` (requires `guide-pages` whitelist)

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /guide-pages | Employee | List all active guide pages | [get_guide-pages.md](get_guide-pages.md) |
| GET | /guide-pages/{slug} | Employee | Get guide page by slug | [get_guide-pages_{slug}.md](get_guide-pages_{slug}.md) |
| GET | /guide-pages/admin | `guide-pages` whitelist | List all pages (including inactive) | [get_guide-pages_admin.md](get_guide-pages_admin.md) |
| POST | /guide-pages/admin | `guide-pages` whitelist | Create a guide page | [post_guide-pages_admin.md](post_guide-pages_admin.md) |
| PUT | /guide-pages/admin/{page_id} | `guide-pages` whitelist | Update a guide page | [put_guide-pages_admin_{page_id}.md](put_guide-pages_admin_{page_id}.md) |
| DELETE | /guide-pages/admin/{page_id} | `guide-pages` whitelist | Delete a guide page | [delete_guide-pages_admin_{page_id}.md](delete_guide-pages_admin_{page_id}.md) |
