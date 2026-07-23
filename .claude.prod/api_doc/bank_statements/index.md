# Bank Statements API

Base prefixes:
- `/bank-statements`
- `/bank-statements/{statement_id}`
- `/bank-statements/{statement_id}/attachments`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /bank-statements | Authenticated | List Bank Statements | [get_bank-statements.md](get_bank-statements.md) |
| POST | /bank-statements | Authenticated | Create Bank Statement | [post_bank-statements.md](post_bank-statements.md) |
| GET | /bank-statements/bank-accounts | Authenticated | List Distinct Bank Accounts | [get_bank-statements_bank-accounts.md](get_bank-statements_bank-accounts.md) |
| DELETE | /bank-statements/{statement_id} | Authenticated | Delete Bank Statement | [delete_bank-statements_{statement_id}.md](delete_bank-statements_{statement_id}.md) |
| GET | /bank-statements/{statement_id} | Authenticated | Get Bank Statement | [get_bank-statements_{statement_id}.md](get_bank-statements_{statement_id}.md) |
| PUT | /bank-statements/{statement_id} | Authenticated | Save Bank Statement | [put_bank-statements_{statement_id}.md](put_bank-statements_{statement_id}.md) |
| POST | /bank-statements/{statement_id}/attachments | Authenticated | Upload Bank Statement Attachment | [post_bank-statements_{statement_id}_attachments.md](post_bank-statements_{statement_id}_attachments.md) |
| DELETE | /bank-statements/{statement_id}/attachments/{file_id} | Authenticated | Detach Bank Statement Attachment | [delete_bank-statements_{statement_id}_attachments_{file_id}.md](delete_bank-statements_{statement_id}_attachments_{file_id}.md) |
