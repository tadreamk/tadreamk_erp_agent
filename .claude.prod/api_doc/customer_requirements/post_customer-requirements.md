# POST /customer-requirements

Create a new customer requirement. Backend generates the 12-char `share_token`.

**Request body:**
```json
{
  "title": "Example Requirement",
  "summary": "short dashboard description",
  "status": "Draft",
  "share_mode": "edit"
}
```

`status` ∈ `Draft`, `Active`, `Delivered`, `Archived`. `share_mode` ∈ `edit`, `disabled`.

**Response:** `CustomerRequirementResponse` (see `get_customer-requirements_{id}.md`).

**Errors:**
- `401`, `403` — auth / whitelist
- `422` — validation (empty title, invalid enum value)
