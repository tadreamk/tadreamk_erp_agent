# Onboarding API

Base prefixes:
- `/onboarding`
- `/onboarding/documents`
- `/onboarding/documents/{document_id}`
- `/onboarding/{workflow_id}`
- `/onboarding/{workflow_id}/documents`
- `/onboarding/{workflow_id}/documents/{document_id}`
- `/onboarding/{workflow_id}/notes`
- `/talent`
- `/talent/onboarding`
- `/talent/onboarding/documents`
- `/talent/onboarding/documents/{document_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /onboarding | Public | List Workflows | [get_onboarding.md](get_onboarding.md) |
| POST | /onboarding | Public | Create Workflow | [post_onboarding.md](post_onboarding.md) |
| GET | /onboarding/count | Public | Count Workflows | [get_onboarding_count.md](get_onboarding_count.md) |
| GET | /onboarding/documents/{document_id} | Public | Get Document By Id | [get_onboarding_documents_{document_id}.md](get_onboarding_documents_{document_id}.md) |
| GET | /onboarding/documents/{document_id}/preview | Public | Preview Document Html | [get_onboarding_documents_{document_id}_preview.md](get_onboarding_documents_{document_id}_preview.md) |
| DELETE | /onboarding/{workflow_id} | Public | Soft Delete Workflow | [delete_onboarding_{workflow_id}.md](delete_onboarding_{workflow_id}.md) |
| GET | /onboarding/{workflow_id} | Public | Get Workflow | [get_onboarding_{workflow_id}.md](get_onboarding_{workflow_id}.md) |
| PUT | /onboarding/{workflow_id} | Public | Update Workflow | [put_onboarding_{workflow_id}.md](put_onboarding_{workflow_id}.md) |
| POST | /onboarding/{workflow_id}/cancel | Public | Cancel Workflow | [post_onboarding_{workflow_id}_cancel.md](post_onboarding_{workflow_id}_cancel.md) |
| POST | /onboarding/{workflow_id}/ceo-confirm | Public | Ceo Confirm | [post_onboarding_{workflow_id}_ceo-confirm.md](post_onboarding_{workflow_id}_ceo-confirm.md) |
| POST | /onboarding/{workflow_id}/ceo-reject | Public | Ceo Reject | [post_onboarding_{workflow_id}_ceo-reject.md](post_onboarding_{workflow_id}_ceo-reject.md) |
| POST | /onboarding/{workflow_id}/ceo-sign | Public | Ceo Sign | [post_onboarding_{workflow_id}_ceo-sign.md](post_onboarding_{workflow_id}_ceo-sign.md) |
| GET | /onboarding/{workflow_id}/documents | Public | List Documents | [get_onboarding_{workflow_id}_documents.md](get_onboarding_{workflow_id}_documents.md) |
| POST | /onboarding/{workflow_id}/documents | Public | Add Documents | [post_onboarding_{workflow_id}_documents.md](post_onboarding_{workflow_id}_documents.md) |
| DELETE | /onboarding/{workflow_id}/documents/{document_id} | Public | Remove Document | [delete_onboarding_{workflow_id}_documents_{document_id}.md](delete_onboarding_{workflow_id}_documents_{document_id}.md) |
| PUT | /onboarding/{workflow_id}/documents/{document_id} | Public | Update Document Fields | [put_onboarding_{workflow_id}_documents_{document_id}.md](put_onboarding_{workflow_id}_documents_{document_id}.md) |
| POST | /onboarding/{workflow_id}/documents/{document_id}/upload-pdf | Public | Upload Document Pdf | [post_onboarding_{workflow_id}_documents_{document_id}_upload-pdf.md](post_onboarding_{workflow_id}_documents_{document_id}_upload-pdf.md) |
| POST | /onboarding/{workflow_id}/finalize | Public | Finalize Workflow | [post_onboarding_{workflow_id}_finalize.md](post_onboarding_{workflow_id}_finalize.md) |
| POST | /onboarding/{workflow_id}/generate-documents | Public | Generate Documents | [post_onboarding_{workflow_id}_generate-documents.md](post_onboarding_{workflow_id}_generate-documents.md) |
| GET | /onboarding/{workflow_id}/notes | Public | List Notes | [get_onboarding_{workflow_id}_notes.md](get_onboarding_{workflow_id}_notes.md) |
| POST | /onboarding/{workflow_id}/notes | Public | Create Note | [post_onboarding_{workflow_id}_notes.md](post_onboarding_{workflow_id}_notes.md) |
| DELETE | /onboarding/{workflow_id}/notes/{note_id} | Public | Delete Note | [delete_onboarding_{workflow_id}_notes_{note_id}.md](delete_onboarding_{workflow_id}_notes_{note_id}.md) |
| PUT | /onboarding/{workflow_id}/notes/{note_id} | Public | Update Note | [put_onboarding_{workflow_id}_notes_{note_id}.md](put_onboarding_{workflow_id}_notes_{note_id}.md) |
| POST | /onboarding/{workflow_id}/reopen | Public | Reopen Workflow | [post_onboarding_{workflow_id}_reopen.md](post_onboarding_{workflow_id}_reopen.md) |
| POST | /onboarding/{workflow_id}/return-to-talent | Public | Return To Talent | [post_onboarding_{workflow_id}_return-to-talent.md](post_onboarding_{workflow_id}_return-to-talent.md) |
| POST | /onboarding/{workflow_id}/send-to-ceo | Public | Send To Ceo | [post_onboarding_{workflow_id}_send-to-ceo.md](post_onboarding_{workflow_id}_send-to-ceo.md) |
| POST | /onboarding/{workflow_id}/send-to-ceo-confirmation | Public | Send To Ceo Confirmation | [post_onboarding_{workflow_id}_send-to-ceo-confirmation.md](post_onboarding_{workflow_id}_send-to-ceo-confirmation.md) |
| POST | /onboarding/{workflow_id}/send-to-talent | Public | Send To Talent | [post_onboarding_{workflow_id}_send-to-talent.md](post_onboarding_{workflow_id}_send-to-talent.md) |
| GET | /talent/onboarding | Authenticated | Get My Onboarding | [get_talent_onboarding.md](get_talent_onboarding.md) |
| PUT | /talent/onboarding/documents/{document_id} | Authenticated | Update My Document Fields | [put_talent_onboarding_documents_{document_id}.md](put_talent_onboarding_documents_{document_id}.md) |
| GET | /talent/onboarding/documents/{document_id}/preview-data | Authenticated | Get My Document Preview Data | [get_talent_onboarding_documents_{document_id}_preview-data.md](get_talent_onboarding_documents_{document_id}_preview-data.md) |
| POST | /talent/onboarding/documents/{document_id}/sign | Authenticated | Sign My Document | [post_talent_onboarding_documents_{document_id}_sign.md](post_talent_onboarding_documents_{document_id}_sign.md) |
| POST | /talent/onboarding/documents/{document_id}/upload-pdf | Authenticated | Upload My Document Pdf | [post_talent_onboarding_documents_{document_id}_upload-pdf.md](post_talent_onboarding_documents_{document_id}_upload-pdf.md) |
| POST | /talent/onboarding/submit | Authenticated | Submit My Onboarding | [post_talent_onboarding_submit.md](post_talent_onboarding_submit.md) |
