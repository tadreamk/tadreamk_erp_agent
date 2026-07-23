# Document Templates API

Base prefixes:
- `/document-templates`
- `/document-templates/{template_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /document-templates | Authenticated | List Document Templates | [get_document-templates.md](get_document-templates.md) |
| GET | /document-templates/{template_id} | Authenticated | Get Document Template | [get_document-templates_{template_id}.md](get_document-templates_{template_id}.md) |
| POST | /document-templates/{template_id}/preview-pdf | Authenticated | Generate Document Template Preview Pdf | [post_document-templates_{template_id}_preview-pdf.md](post_document-templates_{template_id}_preview-pdf.md) |
