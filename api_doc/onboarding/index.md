# Onboarding API

Multi-stage onboarding workflow system for managing new-hire document preparation, review, and signing between HR, CEO, and Talent (the new hire). The workflow progresses through statuses: `template_selection` -> `pending_ceo_confirmation` -> `input` -> `complete` (with `cancelled` as a utility status).

**Base URL:** `/api/v1`

**Workflow Status Values:**
| Status | Description |
|--------|-------------|
| `template_selection` | HR selecting and configuring document templates |
| `pending_ceo_confirmation` | Awaiting CEO review and approval of selected documents |
| `input` | All parties (HR, Talent, CEO) filling fields and signing |
| `complete` | All documents signed, workflow finished |
| `cancelled` | Workflow cancelled |

**Valid Status Transitions:**
| From | Allowed To |
|------|-----------|
| `template_selection` | `pending_ceo_confirmation`, `cancelled` |
| `pending_ceo_confirmation` | `input`, `template_selection`, `cancelled` |
| `input` | `complete`, `cancelled` |
| `cancelled` | `template_selection` |

**Access Roles:**
- **HR** — Users on the `onboarding` whitelist. Full management access.
- **CEO** — The CEO assigned to a workflow (`ceo_username`). Confirmation and signing access.
- **Talent** — The new hire assigned to a workflow (`talent_email`). Document filling and signing access.

---

## 25. Onboarding (HR)

Core CRUD operations for onboarding workflows. Most endpoints require `onboarding` whitelist access (HR).

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/onboarding` | List onboarding workflows. HR sees all workflows; CEO sees only workflows assign | [get_onboarding.md](./get_onboarding.md) |
| `GET` | `/onboarding/count` | Get count of onboarding workflows matching filters (HR only). | [get_onboarding_count.md](./get_onboarding_count.md) |
| `GET` | `/onboarding/{workflow_id}` | Get a single onboarding workflow with all documents and template details. Access | [get_onboarding_by_id.md](./get_onboarding_by_id.md) |
| `POST` | `/onboarding` | Create a new onboarding workflow (HR only). | [post_onboarding.md](./post_onboarding.md) |
| `PUT` | `/onboarding/{workflow_id}` | Update an onboarding workflow (HR only). Status transitions are validated. | [put_onboarding_by_id.md](./put_onboarding_by_id.md) |
| `DELETE` | `/onboarding/{workflow_id}` | Soft-delete an onboarding workflow (HR only). Sets `is_active` to `false`. | [delete_onboarding_by_id.md](./delete_onboarding_by_id.md) |
| `POST` | `/onboarding/{workflow_id}/ceo-sign` | CEO signs the workflow, applying the CEO signature to all documents that have a  | [post_onboarding_by_id_ceo_sign.md](./post_onboarding_by_id_ceo_sign.md) |
| `POST` | `/onboarding/{workflow_id}/generate-documents` | Generate documents from selected templates. Validates that documents have been a | [post_onboarding_by_id_generate_documents.md](./post_onboarding_by_id_generate_documents.md) |
| `POST` | `/onboarding/{workflow_id}/send-to-ceo-confirmation` | Send documents to CEO for review and confirmation. Transitions workflow from `te | [post_onboarding_by_id_send_to_ceo_confirmation.md](./post_onboarding_by_id_send_to_ceo_confirmation.md) |
| `POST` | `/onboarding/{workflow_id}/send-to-talent` | Send an invitation email to the talent (new hire) with a link to fill and sign d | [post_onboarding_by_id_send_to_talent.md](./post_onboarding_by_id_send_to_talent.md) |
| `POST` | `/onboarding/{workflow_id}/cancel` | Cancel an onboarding workflow. Can be cancelled from any status except `complete | [post_onboarding_by_id_cancel.md](./post_onboarding_by_id_cancel.md) |
| `POST` | `/onboarding/{workflow_id}/reopen` | Reopen a cancelled workflow. Transitions from `cancelled` back to `template_sele | [post_onboarding_by_id_reopen.md](./post_onboarding_by_id_reopen.md) |
| `POST` | `/onboarding/{workflow_id}/return-to-talent` | HR returns documents to talent for revision. Clears the `talent_submitted_at` an | [post_onboarding_by_id_return_to_talent.md](./post_onboarding_by_id_return_to_talent.md) |
| `GET` | `/onboarding/{workflow_id}/documents` | List all documents for a workflow with template details (HR only). | [get_onboarding_by_id_documents.md](./get_onboarding_by_id_documents.md) |
| `POST` | `/onboarding/{workflow_id}/documents` | Add documents (by template) to a workflow. Replaces existing documents but prese | [post_onboarding_by_id_documents.md](./post_onboarding_by_id_documents.md) |
| `PUT` | `/onboarding/{workflow_id}/documents/{document_id}` | Update field values for a specific document. Accessible by HR, CEO, and Talent.  | [put_onboarding_by_id_documents_by_id.md](./put_onboarding_by_id_documents_by_id.md) |
| `DELETE` | `/onboarding/{workflow_id}/documents/{document_id}` | Remove a document from a workflow (HR only). Only allowed in `template_selection | [delete_onboarding_by_id_documents_by_id.md](./delete_onboarding_by_id_documents_by_id.md) |
| `POST` | `/onboarding/{workflow_id}/documents/{document_id}/upload-pdf` | Upload a PDF file for a document to OneDrive (HR). Used for documents that requi | [post_onboarding_by_id_documents_by_id_upload_pdf.md](./post_onboarding_by_id_documents_by_id_upload_pdf.md) |
| `POST` | `/onboarding/{workflow_id}/ceo-confirm` | CEO confirms the prepared documents. Transitions workflow from `pending_ceo_conf | [post_onboarding_by_id_ceo_confirm.md](./post_onboarding_by_id_ceo_confirm.md) |
| `POST` | `/onboarding/{workflow_id}/ceo-reject` | CEO rejects the prepared documents. Transitions workflow from `pending_ceo_confi | [post_onboarding_by_id_ceo_reject.md](./post_onboarding_by_id_ceo_reject.md) |
| `POST` | `/onboarding/{workflow_id}/send-to-ceo` | HR sends the workflow to CEO for final signature. Requires the talent to have su | [post_onboarding_by_id_send_to_ceo.md](./post_onboarding_by_id_send_to_ceo.md) |
| `POST` | `/onboarding/{workflow_id}/finalize` | CEO finalizes the onboarding and completes the workflow. Validates all CEO signa | [post_onboarding_by_id_finalize.md](./post_onboarding_by_id_finalize.md) |
| `GET` | `/onboarding/{workflow_id}/notes` | List all notes for a workflow. Ordered by creation time. | [get_onboarding_by_id_notes.md](./get_onboarding_by_id_notes.md) |
| `POST` | `/onboarding/{workflow_id}/notes` | Create a new note on a workflow. Optionally mention other users to trigger notif | [post_onboarding_by_id_notes.md](./post_onboarding_by_id_notes.md) |
| `PUT` | `/onboarding/{workflow_id}/notes/{note_id}` | Update a note. Only the original author can update. | [put_onboarding_by_id_notes_by_id.md](./put_onboarding_by_id_notes_by_id.md) |
| `DELETE` | `/onboarding/{workflow_id}/notes/{note_id}` | Delete a note. Only the original author can delete. | [delete_onboarding_by_id_notes_by_id.md](./delete_onboarding_by_id_notes_by_id.md) |
| `GET` | `/talent/onboarding` | Get the authenticated talent's onboarding workflows. Returns all active (non-can | [get_talent_onboarding.md](./get_talent_onboarding.md) |
| `PUT` | `/talent/onboarding/documents/{document_id}` | Talent updates their field values on a document. Document must not be locked (si | [put_talent_onboarding_documents_by_id.md](./put_talent_onboarding_documents_by_id.md) |
| `POST` | `/talent/onboarding/documents/{document_id}/sign` | Talent signs a document. This locks the document, preventing further field edits | [post_talent_onboarding_documents_by_id_sign.md](./post_talent_onboarding_documents_by_id_sign.md) |
| `POST` | `/talent/onboarding/documents/{document_id}/upload-pdf` | Talent uploads a PDF file for a document to OneDrive. Workflow must be in `input | [post_talent_onboarding_documents_by_id_upload_pdf.md](./post_talent_onboarding_documents_by_id_upload_pdf.md) |
| `POST` | `/talent/onboarding/submit` | Talent submits all documents, confirming everything is signed. All documents mus | [post_talent_onboarding_submit.md](./post_talent_onboarding_submit.md) |
