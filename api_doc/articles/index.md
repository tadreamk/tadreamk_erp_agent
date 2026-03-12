# Articles API

Markdown article editor for company operations content. Supports categories, status workflow (draft/published/archived), AI-powered translation, and image uploads to GCP.

**Access control:** Whitelist `article` required for admin endpoints. Public endpoints require no authentication.

---

## Admin Endpoints (Whitelist: article)

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/articles` | List articles with filters, pagination, and stats. | [get_articles.md](./get_articles.md) |
| `GET` | `/articles/{article_id}` | Get a single article by ID. | [get_articles_by_id.md](./get_articles_by_id.md) |
| `POST` | `/articles` | Create a new article. | [post_articles.md](./post_articles.md) |
| `PUT` | `/articles/{article_id}` | Update an existing article. Only provided fields are updated. | [put_articles_by_id.md](./put_articles_by_id.md) |
| `PATCH` | `/articles/{article_id}/status` | Change article status only. | [patch_articles_by_id_status.md](./patch_articles_by_id_status.md) |
| `DELETE` | `/articles/{article_id}` | Delete an article. | [delete_articles_by_id.md](./delete_articles_by_id.md) |
| `POST` | `/articles/image-storage` | Upload an image to GCP storage. Returns the public URL. | [post_articles_image_storage.md](./post_articles_image_storage.md) |
| `POST` | `/articles/translate` | Translate article content via Gemini AI. Returns translations without saving. | [post_articles_translate.md](./post_articles_translate.md) |
| `GET` | `/articles-public` | List published articles. No authentication required. | [get_articles_public.md](./get_articles_public.md) |
| `GET` | `/articles-public/{slug}` | Get a single published article by slug. No authentication required. | [get_articles_public_by_id.md](./get_articles_public_by_id.md) |
