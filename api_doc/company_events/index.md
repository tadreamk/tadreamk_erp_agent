# Company Events API

CRUD endpoints for company-wide events (meetings, gatherings, celebrations). All employees can view events; creating, updating, and deleting requires `company-events` whitelist access. Supports participant management, reminders, and notification/email dispatch.

---

## 58. Company Events

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/company-events/calendar` | Get company events for calendar display within a date range. All employees can v | [get_company_events_calendar.md](./get_company_events_calendar.md) |
| `GET` | `/company-events/employees` | Get employees for the participant picker dropdown. Requires `company-events` whi | [get_company_events_employees.md](./get_company_events_employees.md) |
| `GET` | `/company-events` | List all company events with optional search and date filters. All employees can | [get_company_events.md](./get_company_events.md) |
| `GET` | `/company-events/{event_id}` | Get full company event details. All employees can view. Response includes `can_e | [get_company_events_by_id.md](./get_company_events_by_id.md) |
| `POST` | `/company-events` | Create a new company event. Requires `company-events` whitelist access. Sends in | [post_company_events.md](./post_company_events.md) |
| `PUT` | `/company-events/{event_id}` | Update a company event. Requires `company-events` whitelist access. All fields a | [put_company_events_by_id.md](./put_company_events_by_id.md) |
| `DELETE` | `/company-events/{event_id}` | Delete a company event (soft delete). Requires `company-events` whitelist access | [delete_company_events_by_id.md](./delete_company_events_by_id.md) |
