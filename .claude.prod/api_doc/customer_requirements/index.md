# Customer Requirements API

Base prefix: `/customer-requirements`

Dashboard endpoints require `customer-requirements` whitelist access.
Public endpoints do NOT require authentication.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /customer-requirements | Whitelist | List requirements | [get_customer-requirements.md](get_customer-requirements.md) |
| GET | /customer-requirements/count | Whitelist | Filtered count | [get_customer-requirements_count.md](get_customer-requirements_count.md) |
| GET | /customer-requirements/{id} | Whitelist | Get requirement by id | [get_customer-requirements_{id}.md](get_customer-requirements_{id}.md) |
| POST | /customer-requirements | Whitelist | Create requirement | [post_customer-requirements.md](post_customer-requirements.md) |
| PUT | /customer-requirements/{id} | Whitelist | Update requirement | [put_customer-requirements_{id}.md](put_customer-requirements_{id}.md) |
| POST | /customer-requirements/{id}/rotate-token | Whitelist | Regenerate share_token | [post_customer-requirements_{id}_rotate-token.md](post_customer-requirements_{id}_rotate-token.md) |
| DELETE | /customer-requirements/{id} | Whitelist | Soft-delete requirement | [delete_customer-requirements_{id}.md](delete_customer-requirements_{id}.md) |
| GET | /customer-requirements/public/{token} | Public (rate-limited) | Bootstrap the share-link editor | [get_customer-requirements_public_{token}.md](get_customer-requirements_public_{token}.md) |
| WS | /customer-requirements/ws/{token} | Public (room cap) | Yjs binary relay | [ws_customer-requirements_ws_{token}.md](ws_customer-requirements_ws_{token}.md) |
| GET | /customer-requirements/public/{token}/attachments | Public (rate-limited) | List attachments for a requirement | [get_customer-requirements_public_{token}_attachments.md](get_customer-requirements_public_{token}_attachments.md) |
| POST | /customer-requirements/public/{token}/attachments | Public (rate-limited) | Upload an attachment | [post_customer-requirements_public_{token}_attachments.md](post_customer-requirements_public_{token}_attachments.md) |
| DELETE | /customer-requirements/public/{token}/attachments/{attachment_id} | Public (rate-limited) | Delete an attachment | [delete_customer-requirements_public_{token}_attachments_{attachment_id}.md](delete_customer-requirements_public_{token}_attachments_{attachment_id}.md) |
| POST | /customer-requirements/public/{token}/format | Public (rate-limited) | AI-format the editor text as Markdown (Gemini) | [post_customer-requirements_public_{token}_format.md](post_customer-requirements_public_{token}_format.md) |
