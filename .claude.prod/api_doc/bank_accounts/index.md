# Bank Accounts API

Base prefix: `/bank-accounts`

All endpoints require `bank-statements` whitelist.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /bank-accounts | List active bank accounts | [get_bank-accounts.md](get_bank-accounts.md) |
| POST | /bank-accounts | Create a bank account | [post_bank-accounts.md](post_bank-accounts.md) |
| PUT | /bank-accounts/{account_id} | Update a bank account | [put_bank-accounts_{account_id}.md](put_bank-accounts_{account_id}.md) |
| DELETE | /bank-accounts/{account_id} | Soft-delete a bank account | [delete_bank-accounts_{account_id}.md](delete_bank-accounts_{account_id}.md) |
