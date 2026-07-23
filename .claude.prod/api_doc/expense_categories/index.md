# Expense Categories API

Base prefixes:
- `/expense-categories`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /expense-categories | Authenticated employee | List Expense Categories | [get_expense-categories.md](get_expense-categories.md) |
| POST | /expense-categories | Authenticated employee | Create Expense Category Route | [post_expense-categories.md](post_expense-categories.md) |
| DELETE | /expense-categories/{category_id} | Authenticated employee | Delete Expense Category | [delete_expense-categories_{category_id}.md](delete_expense-categories_{category_id}.md) |
| GET | /expense-categories/{category_id} | Authenticated employee | Get Expense Category | [get_expense-categories_{category_id}.md](get_expense-categories_{category_id}.md) |
| PUT | /expense-categories/{category_id} | Authenticated employee | Update Expense Category Route | [put_expense-categories_{category_id}.md](put_expense-categories_{category_id}.md) |
