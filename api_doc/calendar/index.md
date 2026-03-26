# Calendar API

Team calendar showing approved leaves and confirmed interviews.

**Access control:**
- Employee endpoints (`/calendar`): Requires authentication with a valid employee record.
- Admin endpoints (`/admin/calendar`): Requires admin/moderator role + `calendar` whitelist.

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/calendar/team` | Get team calendar for a month (employee) | [get_calendar_team.md](./get_calendar_team.md) |
| `GET` | `/calendar/team/range` | Get team calendar for a custom date range | [get_calendar_team_range.md](./get_calendar_team_range.md) |
| `GET` | `/calendar/departments` | Get departments list for filtering | [get_calendar_departments.md](./get_calendar_departments.md) |
| `GET` | `/calendar/interviews` | Get confirmed interviews for calendar | [get_calendar_interviews.md](./get_calendar_interviews.md) |
| `GET` | `/admin/calendar/team` | Get team calendar (admin view) | [get_admin_calendar_team.md](./get_admin_calendar_team.md) |
