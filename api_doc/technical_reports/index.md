# 60. Technical Reports API

Employee-facing system for submitting and tracking technical/IT support reports. Employees submit reports with optional file attachments; technical administrators (users with `technical-reports` whitelist) can view all reports and mark them as resolved. Notifications are sent to the Head of IT on submission and to the reporter on resolution.

**Base path:** `/technical-reports`

**Access control:** All endpoints require authentication. Employee endpoints require the user to exist in the employees table. Admin-level endpoints require `technical-reports` whitelist access.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/technical-reports/my-reports` | Get technical reports submitted by the authenticated employee. | [get_technical_reports_my_reports.md](./get_technical_reports_my_reports.md) |
| `GET` | `/technical-reports/my-reports/count` | Get count of technical reports submitted by the authenticated employee. | [get_technical_reports_my_reports_count.md](./get_technical_reports_my_reports_count.md) |
| `GET` | `/technical-reports` | List all technical reports across all employees. Requires `technical-reports` wh | [get_technical_reports.md](./get_technical_reports.md) |
| `GET` | `/technical-reports/count` | Get count of all technical reports. Requires `technical-reports` whitelist. | [get_technical_reports_count.md](./get_technical_reports_count.md) |
| `POST` | `/technical-reports` | Create a new technical report. The authenticated employee is recorded as the rep | [post_technical_reports.md](./post_technical_reports.md) |
| `POST` | `/technical-reports/upload` | Upload a supporting file to Google Cloud Storage. Returns the file URL for use i | [post_technical_reports_upload.md](./post_technical_reports_upload.md) |
| `GET` | `/technical-reports/{report_id}` | Get detailed view of a technical report. The report owner sees it with `employee | [get_technical_reports_by_id.md](./get_technical_reports_by_id.md) |
| `POST` | `/technical-reports/{report_id}/resolve` | Mark a technical report as resolved. Requires `technical-reports` whitelist. Onl | [post_technical_reports_by_id_resolve.md](./post_technical_reports_by_id_resolve.md) |
