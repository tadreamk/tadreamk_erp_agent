# GET /company-roles/role-titles

List Role Titles. Requires `)
    rows = company_role_queries.list_company_roles_with_holders(db)
    return {
        ` whitelist.

**Response:**
```json
{
  "entries": [
    {
      "role_title": "string",
      "role_description": "string",
      "holder": {
        "username": {},
        "preferred_name": {}
      }
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No `)
    rows = company_role_queries.list_company_roles_with_holders(db)
    return {
        ` whitelist access
- `404` — Not found
