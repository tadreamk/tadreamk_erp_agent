# Funding Utilization API

Base prefix: `/funding-utilization`

All endpoints require `funding-sources` whitelist.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /funding-utilization/summary | Overall utilization summary | [get_funding-utilization_summary.md](get_funding-utilization_summary.md) |
| GET | /funding-utilization/by-category | Utilization grouped by category | [get_funding-utilization_by-category.md](get_funding-utilization_by-category.md) |
| GET | /funding-utilization/by-source | Utilization per funding source | [get_funding-utilization_by-source.md](get_funding-utilization_by-source.md) |
| GET | /funding-utilization/source/{funding_source_id} | Detailed utilization for a source | [get_funding-utilization_source_{funding_source_id}.md](get_funding-utilization_source_{funding_source_id}.md) |
| GET | /funding-utilization/source/{funding_source_id}/expenses | Expenses for a source | [get_funding-utilization_source_{funding_source_id}_expenses.md](get_funding-utilization_source_{funding_source_id}_expenses.md) |
