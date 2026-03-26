# Market Research API

Base prefix: `/market-research`

All endpoints require `market-research` whitelist access.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /market-research/companies | List companies | [get_market-research_companies.md](get_market-research_companies.md) |
| GET | /market-research/companies/count | Get company count | [get_market-research_companies_count.md](get_market-research_companies_count.md) |
| GET | /market-research/companies/stats | Get dashboard stats | [get_market-research_companies_stats.md](get_market-research_companies_stats.md) |
| GET | /market-research/companies/{slug} | Get company by slug | [get_market-research_companies_{slug}.md](get_market-research_companies_{slug}.md) |
| PUT | /market-research/companies/{slug} | Update a company | [put_market-research_companies_{slug}.md](put_market-research_companies_{slug}.md) |
| DELETE | /market-research/companies/{slug} | Delete a company | [delete_market-research_companies_{slug}.md](delete_market-research_companies_{slug}.md) |
| PATCH | /market-research/companies/{slug}/note | Update company note | [patch_market-research_companies_{slug}_note.md](patch_market-research_companies_{slug}_note.md) |
| POST | /market-research/companies/import | Bulk import companies | [post_market-research_companies_import.md](post_market-research_companies_import.md) |
