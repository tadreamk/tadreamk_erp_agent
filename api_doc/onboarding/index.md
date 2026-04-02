# Onboarding API

Base prefix: `/onboarding`, `/talent/onboarding`

Authentication: Required. HR staff require `onboarding` whitelist access. CEO users can access their own workflows. Talent accesses via `/talent/onboarding` endpoints.

## Core Workflow

| Method | Path | Description |
|--------|------|-------------|
| GET | `/onboarding` | List onboarding workflows |
| GET | `/onboarding/count` | Count onboarding workflows (HR only) |
| GET | `/onboarding/{workflow_id}` | Get onboarding workflow with documents |
| POST | `/onboarding` | Create a new onboarding workflow (HR only) |
| PUT | `/onboarding/{workflow_id}` | Update an onboarding workflow (HR only) |
| DELETE | `/onboarding/{workflow_id}` | Soft delete an onboarding workflow (HR only) |
| POST | `/onboarding/{workflow_id}/ceo-sign` | CEO signs workflow to complete it |

## CEO Actions

| Method | Path | Description |
|--------|------|-------------|
| POST | `/onboarding/{workflow_id}/ceo-confirm` | CEO confirms documents (ceo_confirmation -> talent_input) |
| POST | `/onboarding/{workflow_id}/ceo-reject` | CEO rejects documents (ceo_confirmation -> template_selection) |
| POST | `/onboarding/{workflow_id}/send-to-ceo` | HR sends to CEO for final signature (hr_review -> ceo_signature) |
| POST | `/onboarding/{workflow_id}/finalize` | CEO finalizes onboarding (ceo_signature -> completed) |

## HR Actions

| Method | Path | Description |
|--------|------|-------------|
| POST | `/onboarding/{workflow_id}/generate-documents` | Validate documents ready for HR input |
| POST | `/onboarding/{workflow_id}/send-to-ceo-confirmation` | Send to CEO for confirmation (template_selection -> ceo_confirmation) |
| POST | `/onboarding/{workflow_id}/send-to-talent` | Send notification email to talent |
| POST | `/onboarding/{workflow_id}/cancel` | Cancel workflow |
| POST | `/onboarding/{workflow_id}/reopen` | Reopen a cancelled workflow |
| POST | `/onboarding/{workflow_id}/return-to-talent` | Return documents to talent for changes |

## HR Document Management

| Method | Path | Description |
|--------|------|-------------|
| GET | `/onboarding/{workflow_id}/documents` | List all documents for a workflow |
| POST | `/onboarding/{workflow_id}/documents` | Add documents to a workflow |
| PUT | `/onboarding/{workflow_id}/documents/{document_id}` | Update document field values |
| DELETE | `/onboarding/{workflow_id}/documents/{document_id}` | Remove a document from workflow |
| POST | `/onboarding/{workflow_id}/documents/{document_id}/upload-pdf` | Upload PDF/image (HR) |

## Notes (Staff Only)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/onboarding/{workflow_id}/notes` | List notes for a workflow |
| POST | `/onboarding/{workflow_id}/notes` | Create a note |
| PUT | `/onboarding/{workflow_id}/notes/{note_id}` | Update a note (author only) |
| DELETE | `/onboarding/{workflow_id}/notes/{note_id}` | Delete a note (author only) |

## Talent Portal

| Method | Path | Description |
|--------|------|-------------|
| GET | `/talent/onboarding` | Get talent's onboarding workflows |
| PUT | `/talent/onboarding/documents/{document_id}` | Update document fields |
| POST | `/talent/onboarding/documents/{document_id}/sign` | Sign a document (locks it) |
| POST | `/talent/onboarding/documents/{document_id}/upload-pdf` | Upload PDF/image |
| POST | `/talent/onboarding/submit` | Submit all documents for HR review |

## Endpoint Documentation

**Core**
- [GET /onboarding](get_onboarding.md)
- [GET /onboarding/count](get_onboarding_count.md)
- [GET /onboarding/{workflow_id}](get_onboarding_{workflow_id}.md)
- [POST /onboarding](post_onboarding.md)
- [PUT /onboarding/{workflow_id}](put_onboarding_{workflow_id}.md)
- [DELETE /onboarding/{workflow_id}](delete_onboarding_{workflow_id}.md)
- [POST /onboarding/{workflow_id}/ceo-sign](post_onboarding_{workflow_id}_ceo-sign.md)

**CEO Actions**
- [POST /onboarding/{workflow_id}/ceo-confirm](post_onboarding_{workflow_id}_ceo-confirm.md)
- [POST /onboarding/{workflow_id}/ceo-reject](post_onboarding_{workflow_id}_ceo-reject.md)
- [POST /onboarding/{workflow_id}/send-to-ceo](post_onboarding_{workflow_id}_send-to-ceo.md)
- [POST /onboarding/{workflow_id}/finalize](post_onboarding_{workflow_id}_finalize.md)

**HR Actions**
- [POST /onboarding/{workflow_id}/generate-documents](post_onboarding_{workflow_id}_generate-documents.md)
- [POST /onboarding/{workflow_id}/send-to-ceo-confirmation](post_onboarding_{workflow_id}_send-to-ceo-confirmation.md)
- [POST /onboarding/{workflow_id}/send-to-talent](post_onboarding_{workflow_id}_send-to-talent.md)
- [POST /onboarding/{workflow_id}/cancel](post_onboarding_{workflow_id}_cancel.md)
- [POST /onboarding/{workflow_id}/reopen](post_onboarding_{workflow_id}_reopen.md)
- [POST /onboarding/{workflow_id}/return-to-talent](post_onboarding_{workflow_id}_return-to-talent.md)

**HR Documents**
- [GET /onboarding/{workflow_id}/documents](get_onboarding_{workflow_id}_documents.md)
- [POST /onboarding/{workflow_id}/documents](post_onboarding_{workflow_id}_documents.md)
- [PUT /onboarding/{workflow_id}/documents/{document_id}](put_onboarding_{workflow_id}_documents_{document_id}.md)
- [DELETE /onboarding/{workflow_id}/documents/{document_id}](delete_onboarding_{workflow_id}_documents_{document_id}.md)
- [POST /onboarding/{workflow_id}/documents/{document_id}/upload-pdf](post_onboarding_{workflow_id}_documents_{document_id}_upload-pdf.md)

**Notes**
- [GET /onboarding/{workflow_id}/notes](get_onboarding_{workflow_id}_notes.md)
- [POST /onboarding/{workflow_id}/notes](post_onboarding_{workflow_id}_notes.md)
- [PUT /onboarding/{workflow_id}/notes/{note_id}](put_onboarding_{workflow_id}_notes_{note_id}.md)
- [DELETE /onboarding/{workflow_id}/notes/{note_id}](delete_onboarding_{workflow_id}_notes_{note_id}.md)

**Talent Portal**
- [GET /talent/onboarding](get_talent_onboarding.md)
- [PUT /talent/onboarding/documents/{document_id}](put_talent_onboarding_documents_{document_id}.md)
- [POST /talent/onboarding/documents/{document_id}/sign](post_talent_onboarding_documents_{document_id}_sign.md)
- [POST /talent/onboarding/documents/{document_id}/upload-pdf](post_talent_onboarding_documents_{document_id}_upload-pdf.md)
- [POST /talent/onboarding/submit](post_talent_onboarding_submit.md)
