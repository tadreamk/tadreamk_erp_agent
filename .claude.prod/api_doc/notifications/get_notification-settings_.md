# GET /notification-settings/

List Settings. Requires `)
    settings = email_settings_crud.get_all_settings(db)
    return {
        ` whitelist.

**Response:**
```json
{
  "entries": [
    {
      "id": "string",
      "category_key": "string",
      "description": "string",
      "is_enabled": false,
      "is_locked": false,
      "updated_by": "string",
      "updated_at": "datetime",
      "created_at": "datetime"
    }
  ],
  "total": 0
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No `)
    settings = email_settings_crud.get_all_settings(db)
    return {
        ` whitelist access
- `404` — Not found
