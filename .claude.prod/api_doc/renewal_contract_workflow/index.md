# Renewal Contract Workflow API

Base prefixes:
- `/renewal-contract-workflow`
- `/renewal-contract-workflow/{workflow_id}`
- `/talent`
- `/talent/renewal-contract-workflow`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /renewal-contract-workflow | Public | List Workflows | [get_renewal-contract-workflow.md](get_renewal-contract-workflow.md) |
| POST | /renewal-contract-workflow | Public | Create Workflow | [post_renewal-contract-workflow.md](post_renewal-contract-workflow.md) |
| DELETE | /renewal-contract-workflow/{workflow_id} | Public | Delete Workflow | [delete_renewal-contract-workflow_{workflow_id}.md](delete_renewal-contract-workflow_{workflow_id}.md) |
| GET | /renewal-contract-workflow/{workflow_id} | Public | Get Workflow | [get_renewal-contract-workflow_{workflow_id}.md](get_renewal-contract-workflow_{workflow_id}.md) |
| PUT | /renewal-contract-workflow/{workflow_id} | Public | Update Workflow | [put_renewal-contract-workflow_{workflow_id}.md](put_renewal-contract-workflow_{workflow_id}.md) |
| POST | /renewal-contract-workflow/{workflow_id}/cancel | Public | Cancel Workflow | [post_renewal-contract-workflow_{workflow_id}_cancel.md](post_renewal-contract-workflow_{workflow_id}_cancel.md) |
| POST | /renewal-contract-workflow/{workflow_id}/ceo-confirm | Public | Ceo Confirm | [post_renewal-contract-workflow_{workflow_id}_ceo-confirm.md](post_renewal-contract-workflow_{workflow_id}_ceo-confirm.md) |
| POST | /renewal-contract-workflow/{workflow_id}/ceo-reject | Public | Ceo Reject | [post_renewal-contract-workflow_{workflow_id}_ceo-reject.md](post_renewal-contract-workflow_{workflow_id}_ceo-reject.md) |
| POST | /renewal-contract-workflow/{workflow_id}/ceo-reject-signature | Public | Ceo Reject Signature | [post_renewal-contract-workflow_{workflow_id}_ceo-reject-signature.md](post_renewal-contract-workflow_{workflow_id}_ceo-reject-signature.md) |
| POST | /renewal-contract-workflow/{workflow_id}/ceo-sign | Public | Ceo Sign | [post_renewal-contract-workflow_{workflow_id}_ceo-sign.md](post_renewal-contract-workflow_{workflow_id}_ceo-sign.md) |
| POST | /renewal-contract-workflow/{workflow_id}/finalize | Public | Finalize Workflow | [post_renewal-contract-workflow_{workflow_id}_finalize.md](post_renewal-contract-workflow_{workflow_id}_finalize.md) |
| POST | /renewal-contract-workflow/{workflow_id}/hr-request-revision | Public | Hr Request Revision | [post_renewal-contract-workflow_{workflow_id}_hr-request-revision.md](post_renewal-contract-workflow_{workflow_id}_hr-request-revision.md) |
| POST | /renewal-contract-workflow/{workflow_id}/hr-send-to-ceo | Public | Hr Send To Ceo | [post_renewal-contract-workflow_{workflow_id}_hr-send-to-ceo.md](post_renewal-contract-workflow_{workflow_id}_hr-send-to-ceo.md) |
| GET | /renewal-contract-workflow/{workflow_id}/notes | Public | List Workflow Notes | [get_renewal-contract-workflow_{workflow_id}_notes.md](get_renewal-contract-workflow_{workflow_id}_notes.md) |
| POST | /renewal-contract-workflow/{workflow_id}/reopen | Public | Reopen Workflow | [post_renewal-contract-workflow_{workflow_id}_reopen.md](post_renewal-contract-workflow_{workflow_id}_reopen.md) |
| POST | /renewal-contract-workflow/{workflow_id}/send-for-ceo-confirmation | Public | Send For Ceo Confirmation | [post_renewal-contract-workflow_{workflow_id}_send-for-ceo-confirmation.md](post_renewal-contract-workflow_{workflow_id}_send-for-ceo-confirmation.md) |
| GET | /talent/renewal-contract-workflow | Public | Get My Workflow | [get_talent_renewal-contract-workflow.md](get_talent_renewal-contract-workflow.md) |
| PUT | /talent/renewal-contract-workflow | Public | Update My Workflow | [put_talent_renewal-contract-workflow.md](put_talent_renewal-contract-workflow.md) |
| POST | /talent/renewal-contract-workflow/decline | Public | Decline My Workflow | [post_talent_renewal-contract-workflow_decline.md](post_talent_renewal-contract-workflow_decline.md) |
| POST | /talent/renewal-contract-workflow/sign | Public | Sign My Workflow | [post_talent_renewal-contract-workflow_sign.md](post_talent_renewal-contract-workflow_sign.md) |
| POST | /talent/renewal-contract-workflow/submit | Public | Submit My Workflow | [post_talent_renewal-contract-workflow_submit.md](post_talent_renewal-contract-workflow_submit.md) |
