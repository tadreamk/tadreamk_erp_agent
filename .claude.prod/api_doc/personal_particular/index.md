# Personal Particular API

Base prefixes:
- `/personal-particular` — Employee self-service
- `/admin/personal-particular` — HR admin access (requires `personal-particulars` whitelist)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/personal-particular/me` | Get own personal particular data |
| POST | `/personal-particular/me` | Create own personal particular record |
| PUT | `/personal-particular/me` | Update own personal particular record |
| GET | `/admin/personal-particular` | List all personal particulars (HR) |
| GET | `/admin/personal-particular/{pp_id}` | Get a single personal particular (HR) |
| POST | `/admin/personal-particular` | Create a personal particular record (HR) |
| PUT | `/admin/personal-particular/{pp_id}` | Update a personal particular record (HR) |

## Endpoint Documentation

- [GET /personal-particular/me](get_personal-particular_me.md)
- [POST /personal-particular/me](post_personal-particular_me.md)
- [PUT /personal-particular/me](put_personal-particular_me.md)
- [GET /admin/personal-particular](get_admin_personal-particular.md)
- [GET /admin/personal-particular/{pp_id}](get_admin_personal-particular_{pp_id}.md)
- [POST /admin/personal-particular](post_admin_personal-particular.md)
- [PUT /admin/personal-particular/{pp_id}](put_admin_personal-particular_{pp_id}.md)
