# Payslips API

Base prefixes:
- `/payslips`
- `/payslips/by-expense`
- `/payslips/mine`
- `/payslips/{payslip_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /payslips | Authenticated employee | List Payslips | [get_payslips.md](get_payslips.md) |
| POST | /payslips/batch-create | Authenticated employee | Batch Create Payslips | [post_payslips_batch-create.md](post_payslips_batch-create.md) |
| GET | /payslips/by-expense/{expense_id} | Authenticated employee | Get Payslip By Expense | [get_payslips_by-expense_{expense_id}.md](get_payslips_by-expense_{expense_id}.md) |
| GET | /payslips/mine | Authenticated employee | List My Payslips | [get_payslips_mine.md](get_payslips_mine.md) |
| GET | /payslips/mine/{payslip_id} | Authenticated employee | Get My Payslip | [get_payslips_mine_{payslip_id}.md](get_payslips_mine_{payslip_id}.md) |
| GET | /payslips/{payslip_id} | Authenticated employee | Get Payslip | [get_payslips_{payslip_id}.md](get_payslips_{payslip_id}.md) |
| PUT | /payslips/{payslip_id} | Authenticated employee | Update Payslip | [put_payslips_{payslip_id}.md](put_payslips_{payslip_id}.md) |
| POST | /payslips/{payslip_id}/cancel | Authenticated employee | Cancel Payslip | [post_payslips_{payslip_id}_cancel.md](post_payslips_{payslip_id}_cancel.md) |
| POST | /payslips/{payslip_id}/decline | Authenticated employee | Decline Payslip | [post_payslips_{payslip_id}_decline.md](post_payslips_{payslip_id}_decline.md) |
| POST | /payslips/{payslip_id}/sign | Authenticated employee | Sign Payslip | [post_payslips_{payslip_id}_sign.md](post_payslips_{payslip_id}_sign.md) |
| POST | /payslips/{payslip_id}/submit | Authenticated employee | Submit Payslip | [post_payslips_{payslip_id}_submit.md](post_payslips_{payslip_id}_submit.md) |
