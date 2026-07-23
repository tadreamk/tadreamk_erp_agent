# Market Research API

Base prefixes:
- `/market-research`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /market-research | Authenticated | List Companies | [get_market-research.md](get_market-research.md) |
| POST | /market-research | Authenticated | Create Company | [post_market-research.md](post_market-research.md) |
| GET | /market-research/stats | Authenticated | Get Stats | [get_market-research_stats.md](get_market-research_stats.md) |
| DELETE | /market-research/{company_id} | Authenticated | Soft Delete Company | [delete_market-research_{company_id}.md](delete_market-research_{company_id}.md) |
| GET | /market-research/{company_id} | Authenticated | Get Company | [get_market-research_{company_id}.md](get_market-research_{company_id}.md) |
| PUT | /market-research/{company_id} | Authenticated | Update Company | [put_market-research_{company_id}.md](put_market-research_{company_id}.md) |
