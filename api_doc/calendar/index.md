# Calendar API

Team calendar endpoints for viewing approved leaves, interview schedules, and department filtering. Separate endpoints for employees (general access) and admins (whitelist-gated).

**Note:** Public holidays are managed via frontend configuration, not the database.

---

## 56. Calendar (Employee)

Employee-accessible calendar endpoints. Requires the authenticated user to exist in the employees table.

**Access control:** Employee authentication required (user must exist in employees table).

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/calendar/team` | Get team calendar with approved leaves for a given month. Defaults to the curren | [get_calendar_team.md](./get_calendar_team.md) |
| `GET` | `/calendar/team/range` | Get team calendar for a custom date range. | [get_calendar_team_range.md](./get_calendar_team_range.md) |
| `GET` | `/calendar/departments` | Get list of departments that have employees, for use as filter options. | [get_calendar_departments.md](./get_calendar_departments.md) |
| `GET` | `/calendar/interviews` | Get confirmed interviews for calendar display within a date range. | [get_calendar_interviews.md](./get_calendar_interviews.md) |
| `GET` | `/admin/calendar/team` | Get team calendar with approved leaves for a given month (admin view). Defaults  | [get_admin_calendar_team.md](./get_admin_calendar_team.md) |
