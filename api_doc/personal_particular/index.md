# Personal Particular API

Manages employee personal details (names, identity documents, contact information, emergency contacts, bank details). Split into self-service endpoints (employees managing their own records) and admin/HR endpoints (whitelist-protected, for managing any employee's records).

---

## 20. Personal Particular (Self-Service)

Base path: `/personal-particular`

**Authentication:** All endpoints require user authentication via request headers.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/personal-particular/me` | Get the authenticated user's personal particular data. | [get_personal_particular_me.md](./get_personal_particular_me.md) |
| `POST` | `/personal-particular/me` | Create personal particular data for the authenticated user. Each user can only h | [post_personal_particular_me.md](./post_personal_particular_me.md) |
| `PUT` | `/personal-particular/me` | Update personal particular data for the authenticated user. Only fields included | [put_personal_particular_me.md](./put_personal_particular_me.md) |
| `GET` | `/admin/personal-particular` | Get all personal particular records with search filtering and pagination. Return | [get_admin_personal_particular.md](./get_admin_personal_particular.md) |
| `GET` | `/admin/personal-particular/{pp_id}` | Get a single personal particular record with full unmasked data. | [get_admin_personal_particular_by_id.md](./get_admin_personal_particular_by_id.md) |
| `POST` | `/admin/personal-particular` | Create a new personal particular record for a specified user. If the user has an | [post_admin_personal_particular.md](./post_admin_personal_particular.md) |
| `PUT` | `/admin/personal-particular/{pp_id}` | Update an existing personal particular record. The `updated_by` field is set aut | [put_admin_personal_particular_by_id.md](./put_admin_personal_particular_by_id.md) |
