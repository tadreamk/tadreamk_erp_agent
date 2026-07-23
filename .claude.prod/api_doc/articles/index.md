# Articles API

Base prefixes:
- `/articles`
- `/articles/public`
- `/articles/{article_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /articles | Authenticated | List Articles | [get_articles.md](get_articles.md) |
| POST | /articles | Authenticated | Create Article | [post_articles.md](post_articles.md) |
| GET | /articles/public | Public | List Public Articles | [get_articles_public.md](get_articles_public.md) |
| GET | /articles/public/{slug} | Public | Get Public Article | [get_articles_public_{slug}.md](get_articles_public_{slug}.md) |
| GET | /articles/{article_id} | Authenticated | Get Article | [get_articles_{article_id}.md](get_articles_{article_id}.md) |
| PUT | /articles/{article_id} | Authenticated | Update Article | [put_articles_{article_id}.md](put_articles_{article_id}.md) |
| POST | /articles/{article_id}/archive | Public | Archive Article | [post_articles_{article_id}_archive.md](post_articles_{article_id}_archive.md) |
| POST | /articles/{article_id}/publish | Public | Publish Article | [post_articles_{article_id}_publish.md](post_articles_{article_id}_publish.md) |
| POST | /articles/{article_id}/republish | Public | Republish Article | [post_articles_{article_id}_republish.md](post_articles_{article_id}_republish.md) |
