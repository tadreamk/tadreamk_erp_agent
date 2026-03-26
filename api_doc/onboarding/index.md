# Onboarding API

Base prefix: `/onboarding`

Authentication: Required. HR staff require `onboarding` whitelist access. CEO users can access their own workflows.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/onboarding` | List onboarding workflows |
| GET | `/onboarding/count` | Count onboarding workflows (HR only) |
| GET | `/onboarding/{workflow_id}` | Get onboarding workflow with documents |
| POST | `/onboarding` | Create a new onboarding workflow (HR only) |
| PUT | `/onboarding/{workflow_id}` | Update an onboarding workflow (HR only) |
| DELETE | `/onboarding/{workflow_id}` | Soft delete an onboarding workflow (HR only) |
| POST | `/onboarding/{workflow_id}/ceo-sign` | CEO signs workflow to complete it |

## Endpoint Documentation

- [GET /onboarding](get_onboarding.md)
- [GET /onboarding/count](get_onboarding_count.md)
- [GET /onboarding/{workflow_id}](get_onboarding_{workflow_id}.md)
- [POST /onboarding](post_onboarding.md)
- [PUT /onboarding/{workflow_id}](put_onboarding_{workflow_id}.md)
- [DELETE /onboarding/{workflow_id}](delete_onboarding_{workflow_id}.md)
- [POST /onboarding/{workflow_id}/ceo-sign](post_onboarding_{workflow_id}_ceo-sign.md)
