# Articles API

Manage internal articles and publish them publicly. Includes AI-powered translation via Gemini and GCP image storage.

**Access control:** Authenticated users with `articles` whitelist access. Public endpoints (`/articles-public`) require no authentication.

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/articles` | List articles with filters and pagination | [get_articles.md](./get_articles.md) |
| `GET` | `/articles/{article_id}` | Get a single article by ID | [get_articles_{article_id}.md](./get_articles_{article_id}.md) |
| `POST` | `/articles` | Create a new article | [post_articles.md](./post_articles.md) |
| `PUT` | `/articles/{article_id}` | Update an existing article | [put_articles_{article_id}.md](./put_articles_{article_id}.md) |
| `PATCH` | `/articles/{article_id}/status` | Update article status only | [patch_articles_{article_id}_status.md](./patch_articles_{article_id}_status.md) |
| `DELETE` | `/articles/{article_id}` | Delete an article | [delete_articles_{article_id}.md](./delete_articles_{article_id}.md) |
| `POST` | `/articles/image-storage` | Upload an image to GCP | [post_articles_image-storage.md](./post_articles_image-storage.md) |
| `POST` | `/articles/translate` | Translate article content via Gemini AI | [post_articles_translate.md](./post_articles_translate.md) |
| `GET` | `/articles-public` | List published articles (no auth) | [get_articles-public.md](./get_articles-public.md) |
| `GET` | `/articles-public/{slug}` | Get a published article by slug (no auth) | [get_articles-public_{slug}.md](./get_articles-public_{slug}.md) |
