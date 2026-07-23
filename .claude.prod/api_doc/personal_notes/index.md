# Personal Notes API

Base prefixes:
- `/personal-note`
- `/personal-note/{note_id}`
- `/personal-note/{note_id}/share`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /personal-note | Authenticated employee | List Notes | [get_personal-note.md](get_personal-note.md) |
| POST | /personal-note | Authenticated employee | Create Note | [post_personal-note.md](post_personal-note.md) |
| DELETE | /personal-note/{note_id} | Authenticated employee | Delete Note | [delete_personal-note_{note_id}.md](delete_personal-note_{note_id}.md) |
| GET | /personal-note/{note_id} | Authenticated employee | Get Note | [get_personal-note_{note_id}.md](get_personal-note_{note_id}.md) |
| PATCH | /personal-note/{note_id} | Authenticated employee | Update Note | [patch_personal-note_{note_id}.md](patch_personal-note_{note_id}.md) |
| POST | /personal-note/{note_id}/read | Authenticated employee | Mark Read | [post_personal-note_{note_id}_read.md](post_personal-note_{note_id}_read.md) |
| GET | /personal-note/{note_id}/share | Authenticated employee | List Shares | [get_personal-note_{note_id}_share.md](get_personal-note_{note_id}_share.md) |
| POST | /personal-note/{note_id}/share | Authenticated employee | Share Note | [post_personal-note_{note_id}_share.md](post_personal-note_{note_id}_share.md) |
| DELETE | /personal-note/{note_id}/share/{recipient_username} | Authenticated employee | Revoke Share | [delete_personal-note_{note_id}_share_{recipient_username}.md](delete_personal-note_{note_id}_share_{recipient_username}.md) |
