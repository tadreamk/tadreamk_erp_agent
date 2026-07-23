# Exercise Tags API

Base prefixes:
- `/exercise-tags`
- `/exercise-tags/{tag_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /exercise-tags | Authenticated | List Exercise Tags | [get_exercise-tags.md](get_exercise-tags.md) |
| POST | /exercise-tags | Authenticated | Create Exercise Tag | [post_exercise-tags.md](post_exercise-tags.md) |
| PUT | /exercise-tags/{tag_id} | Authenticated | Update Exercise Tag | [put_exercise-tags_{tag_id}.md](put_exercise-tags_{tag_id}.md) |
| POST | /exercise-tags/{tag_id}/restore | Authenticated | Restore Exercise Tag | [post_exercise-tags_{tag_id}_restore.md](post_exercise-tags_{tag_id}_restore.md) |
| POST | /exercise-tags/{tag_id}/retire | Authenticated | Retire Exercise Tag | [post_exercise-tags_{tag_id}_retire.md](post_exercise-tags_{tag_id}_retire.md) |
