# Grammar API

Base prefixes:
- `/grammar`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| POST | /grammar/fix | Public | Fix Grammar | [post_grammar_fix.md](post_grammar_fix.md) |
