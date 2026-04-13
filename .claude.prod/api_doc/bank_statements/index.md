# Bank Statements API

Base prefix: `/bank-statements`

All endpoints require `bank-statements` whitelist.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /bank-statements | List statements (filter: bank_account_id, year, month) | [get_bank-statements.md](get_bank-statements.md) |
| GET | /bank-statements/count | Count statements | [get_bank-statements_count.md](get_bank-statements_count.md) |
| POST | /bank-statements | Create statement header | [post_bank-statements.md](post_bank-statements.md) |
| GET | /bank-statements/{statement_id} | Get statement with lines | [get_bank-statements_{statement_id}.md](get_bank-statements_{statement_id}.md) |
| PUT | /bank-statements/{statement_id} | Update statement header | [put_bank-statements_{statement_id}.md](put_bank-statements_{statement_id}.md) |
| DELETE | /bank-statements/{statement_id} | Delete statement (cascades to lines) | [delete_bank-statements_{statement_id}.md](delete_bank-statements_{statement_id}.md) |
| POST | /bank-statements/{statement_id}/lines | Add a transaction line | [post_bank-statements_{statement_id}_lines.md](post_bank-statements_{statement_id}_lines.md) |
| PUT | /bank-statements/{statement_id}/lines/{line_id} | Edit a transaction line | [put_bank-statements_{statement_id}_lines_{line_id}.md](put_bank-statements_{statement_id}_lines_{line_id}.md) |
| DELETE | /bank-statements/{statement_id}/lines/{line_id} | Delete a transaction line | [delete_bank-statements_{statement_id}_lines_{line_id}.md](delete_bank-statements_{statement_id}_lines_{line_id}.md) |
