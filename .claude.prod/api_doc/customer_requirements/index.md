# Customer Requirements API

Base prefixes:
- `/customer-requirements`
- `/customer-requirements/public`
- `/customer-requirements/public/{token}`
- `/customer-requirements/public/{token}/attachments`
- `/customer-requirements/ws`
- `/customer-requirements/{requirement_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /customer-requirements | Public | List Requirements | [get_customer-requirements.md](get_customer-requirements.md) |
| POST | /customer-requirements | Public | Create New Requirement | [post_customer-requirements.md](post_customer-requirements.md) |
| GET | /customer-requirements/count | Public | Get Requirements Count | [get_customer-requirements_count.md](get_customer-requirements_count.md) |
| GET | /customer-requirements/public/{token} | Public | Get Public Requirement | [get_customer-requirements_public_{token}.md](get_customer-requirements_public_{token}.md) |
| GET | /customer-requirements/public/{token}/attachments | Public | List Public Attachments | [get_customer-requirements_public_{token}_attachments.md](get_customer-requirements_public_{token}_attachments.md) |
| POST | /customer-requirements/public/{token}/attachments | Public | Upload Public Attachment | [post_customer-requirements_public_{token}_attachments.md](post_customer-requirements_public_{token}_attachments.md) |
| DELETE | /customer-requirements/public/{token}/attachments/{attachment_id} | Public | Delete Public Attachment | [delete_customer-requirements_public_{token}_attachments_{attachment_id}.md](delete_customer-requirements_public_{token}_attachments_{attachment_id}.md) |
| POST | /customer-requirements/public/{token}/format | Public | Format Public Requirement | [post_customer-requirements_public_{token}_format.md](post_customer-requirements_public_{token}_format.md) |
| WEBSOCKET | /customer-requirements/ws/{token} | Authenticated | WebSocket /customer-requirements/ws/{token} | [websocket_customer-requirements_ws_{token}.md](websocket_customer-requirements_ws_{token}.md) |
| DELETE | /customer-requirements/{requirement_id} | Public | Delete Requirement Endpoint | [delete_customer-requirements_{requirement_id}.md](delete_customer-requirements_{requirement_id}.md) |
| GET | /customer-requirements/{requirement_id} | Public | Get Requirement | [get_customer-requirements_{requirement_id}.md](get_customer-requirements_{requirement_id}.md) |
| PUT | /customer-requirements/{requirement_id} | Public | Update Existing Requirement | [put_customer-requirements_{requirement_id}.md](put_customer-requirements_{requirement_id}.md) |
| POST | /customer-requirements/{requirement_id}/rotate-token | Public | Rotate Token | [post_customer-requirements_{requirement_id}_rotate-token.md](post_customer-requirements_{requirement_id}_rotate-token.md) |
