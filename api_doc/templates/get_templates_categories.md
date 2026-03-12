# GET /templates/categories


Get list of all unique template categories from active templates.

**Response:**
```json
{
  "categories": ["onboarding", "payslip", "contract"],
  "total": 3
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No templates whitelist access
