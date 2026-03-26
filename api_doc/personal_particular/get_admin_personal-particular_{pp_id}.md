# GET /admin/personal-particular/{pp_id}

Get a single personal particular record with full (unmasked) data. Requires `personal-particulars` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| pp_id | UUID | The personal particular record's unique identifier |

**Response:** Full personal particular object including HKID, bank details, and `updated_by` field

**Errors:**
- `401` — Not authenticated
- `403` — Not on personal-particulars whitelist
- `404` — Personal particular not found
