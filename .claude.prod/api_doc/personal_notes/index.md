# Personal Notes API

Base prefix: `/personal-notes`

Authentication: Requires authentication. Only employees can access personal notes. No whitelist required.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/personal-notes` | List notes owned by or shared with the current user |
| GET | `/personal-notes/{note_id}` | Get a single note by ID |
| POST | `/personal-notes` | Create a new personal note |
| PUT | `/personal-notes/{note_id}` | Update a personal note (owner only) |
| DELETE | `/personal-notes/{note_id}` | Soft delete a personal note (owner only) |
| POST | `/personal-notes/{note_id}/shares` | Share a note with employees (owner only) |
| DELETE | `/personal-notes/{note_id}/shares/{username}` | Remove sharing access for a user (owner only) |

## Endpoint Documentation

- [GET /personal-notes](get_personal-notes.md)
- [GET /personal-notes/{note_id}](get_personal-notes_{note_id}.md)
- [POST /personal-notes](post_personal-notes.md)
- [PUT /personal-notes/{note_id}](put_personal-notes_{note_id}.md)
- [DELETE /personal-notes/{note_id}](delete_personal-notes_{note_id}.md)
- [POST /personal-notes/{note_id}/shares](post_personal-notes_{note_id}_shares.md)
- [DELETE /personal-notes/{note_id}/shares/{username}](delete_personal-notes_{note_id}_shares_{username}.md)
