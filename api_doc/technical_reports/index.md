# Technical Reports API

Base prefix: `/technical-reports`

Authentication: Required. Employee endpoints require employee authentication. Admin/list endpoints require `technical-reports` whitelist access.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/technical-reports/my-reports` | Get technical reports for the authenticated employee |
| GET | `/technical-reports/my-reports/count` | Count technical reports for the authenticated employee |
| GET | `/technical-reports` | List all technical reports (whitelist required) |
| GET | `/technical-reports/count` | Count all technical reports (whitelist required) |
| POST | `/technical-reports` | Submit a new technical report (employee) |
| POST | `/technical-reports/upload` | Upload a supporting file to GCS |
| GET | `/technical-reports/{report_id}` | Get technical report details |
| PUT | `/technical-reports/{report_id}` | Update a submitted report (owner only) |
| POST | `/technical-reports/{report_id}/resolve` | Mark a report as resolved (whitelist required) |

## Endpoint Documentation

- [GET /technical-reports/my-reports](get_technical-reports_my-reports.md)
- [GET /technical-reports/my-reports/count](get_technical-reports_my-reports_count.md)
- [GET /technical-reports](get_technical-reports.md)
- [GET /technical-reports/count](get_technical-reports_count.md)
- [POST /technical-reports](post_technical-reports.md)
- [POST /technical-reports/upload](post_technical-reports_upload.md)
- [GET /technical-reports/{report_id}](get_technical-reports_{report_id}.md)
- [PUT /technical-reports/{report_id}](put_technical-reports_{report_id}.md)
- [POST /technical-reports/{report_id}/resolve](post_technical-reports_{report_id}_resolve.md)
