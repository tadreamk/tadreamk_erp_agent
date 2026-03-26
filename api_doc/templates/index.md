# Templates API

Base prefix: `/templates`

Authentication: Required. Most endpoints require `templates` whitelist access. Exceptions: `/{template_id}/onboarding/{document_id}` and `/{template_id}/payslip-workflow/{workflow_id}` require authentication with appropriate workflow access.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/templates` | List all templates |
| GET | `/templates/categories` | Get all template categories |
| POST | `/templates` | Create or update a template (admin) |
| POST | `/templates/rename` | Rename a template (admin) |
| GET | `/templates/{template_id}` | Get template by ID |
| GET | `/templates/{template_id}/onboarding/{document_id}` | Get template with onboarding field values |
| GET | `/templates/{template_id}/payslip-workflow/{workflow_id}` | Get template with payslip field values |
| POST | `/templates/{template_id}/preview` | Preview template with field values |
| POST | `/templates/{template_id}/generate-pdf` | Generate PDF from template |
| GET | `/templates/{template_id}/download-pdf` | Download PDF for a template |

## Endpoint Documentation

- [GET /templates](get_templates.md)
- [GET /templates/categories](get_templates_categories.md)
- [POST /templates](post_templates.md)
- [POST /templates/rename](post_templates_rename.md)
- [GET /templates/{template_id}](get_templates_{template_id}.md)
- [GET /templates/{template_id}/onboarding/{document_id}](get_templates_{template_id}_onboarding_{document_id}.md)
- [GET /templates/{template_id}/payslip-workflow/{workflow_id}](get_templates_{template_id}_payslip-workflow_{workflow_id}.md)
- [POST /templates/{template_id}/preview](post_templates_{template_id}_preview.md)
- [POST /templates/{template_id}/generate-pdf](post_templates_{template_id}_generate-pdf.md)
- [GET /templates/{template_id}/download-pdf](get_templates_{template_id}_download-pdf.md)
