# 63. Contact Directory API

Employee directory providing non-sensitive contact information for all active employees. No whitelist required -- any authenticated employee can browse the directory.

**Base path:** `/contacts`

**Access control:** Authentication required. User must exist in the employees table (matched by work email).

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/contacts` | List all active employee contacts with optional search and department filtering. | [get_contacts.md](./get_contacts.md) |
| `GET` | `/contacts/departments` | Get list of unique department names for the directory filter dropdown. | [get_contacts_departments.md](./get_contacts_departments.md) |
