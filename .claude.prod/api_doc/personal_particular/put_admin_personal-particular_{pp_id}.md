# PUT /admin/personal-particular/{pp_id}

Update a personal particular record (HR only). Requires `personal-particulars` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| pp_id | UUID | The personal particular record's unique identifier |

**Request Body:** Key-value map of personal particular fields to update

**Response:**
```json
{
  "message": "Personal particular updated",
  "personal_particular": { "...full personal particular object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on personal-particulars whitelist
- `404` — Personal particular not found
