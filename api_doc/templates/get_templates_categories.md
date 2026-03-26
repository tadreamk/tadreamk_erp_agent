# GET /templates/categories

Get a list of all unique template categories. Returns categories from active templates only. Requires `templates` whitelist access.

**Response:**
```json
{
  "categories": ["onboarding", "payslip", "contract"],
  "total": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on templates whitelist
