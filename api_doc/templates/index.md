# 59. Templates API

Read-only API for accessing document templates. Templates are managed by developers via SQL migrations. Supports both static PDF templates and dynamic templates with fillable fields. Integrates with onboarding and payslip workflows to populate field values.

**Base path:** `/templates`

**Access control:** Authentication required. Most endpoints require `templates` whitelist access. Onboarding/payslip endpoints use workflow-specific access checks.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/templates` | List all templates with optional filtering. Returns active templates by default. | [get_templates.md](./get_templates.md) |
| `GET` | `/templates/categories` | Get list of all unique template categories from active templates. | [get_templates_categories.md](./get_templates_categories.md) |
| `GET` | `/templates/{template_id}` | Get a single template by ID. | [get_templates_by_id.md](./get_templates_by_id.md) |
| `GET` | `/templates/{template_id}/onboarding/{document_id}` | Get template with field values populated from an onboarding document. Access is  | [get_templates_by_id_onboarding_by_id.md](./get_templates_by_id_onboarding_by_id.md) |
| `GET` | `/templates/{template_id}/payslip-workflow/{workflow_id}` | Get template with field values populated from a payslip workflow. Access is gran | [get_templates_by_id_payslip_workflow_by_id.md](./get_templates_by_id_payslip_workflow_by_id.md) |
| `POST` | `/templates/{template_id}/preview` | Preview a template with field values. Returns rendered HTML for dynamic template | [post_templates_by_id_preview.md](./post_templates_by_id_preview.md) |
| `POST` | `/templates/{template_id}/generate-pdf` | Generate a PDF from a template with field values. For PDF templates, returns the | [post_templates_by_id_generate_pdf.md](./post_templates_by_id_generate_pdf.md) |
| `GET` | `/templates/{template_id}/download-pdf` | Download PDF for a template. For PDF templates, returns the direct PDF URL. For  | [get_templates_by_id_download_pdf.md](./get_templates_by_id_download_pdf.md) |
