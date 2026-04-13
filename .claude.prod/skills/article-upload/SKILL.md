---
name: article-upload
description: Upload a locally drafted article to GCS and the database. Use
  when user says "upload article", "publish article", "article-upload", or
  "push article to production".
disable-model-invocation: true
---

# Article Upload

Upload a locally drafted article to GCS and the database.

This command takes no arguments. It auto-detects drafts from `data/articles/`.

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token and Select Draft

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

Scan `data/articles/` for directories that contain an `article_meta.json` file.
- If **no drafts found**, tell the user to run `/article-draft` first and stop.
- If **one draft found**, use it automatically.
- If **multiple drafts found**, list each draft's slug, title, and category, then ask the user which one to upload.

## Step 1: Read Local Draft Files

Read all files from `data/articles/<slug>/`:
- `article_meta.json` — metadata (title, summary, category, author, read_time, translations)
- `article_en.md` — English content
- `article_zh.md` — Simplified Chinese content
- `article_zh-TW.md` — Traditional Chinese content
- `diagram.png` — diagram image (**only if `diagram_method` is NOT `"none"` in meta**)

Verify all required files exist. If any are missing, report the error and stop.

Check `diagram_method` in `article_meta.json`:
- If `"none"` → this is a **video article** (no diagram). Skip Steps 2-3 entirely.
- Otherwise → this is a **diagram article**. Proceed with Steps 2-3.

## Step 2: Upload Diagram to GCS (diagram articles only)

Skip this step if `diagram_method` is `"none"`.

Upload the diagram image using the API:

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/articles/image-storage" \
  -H "Authorization: Bearer <token>" \
  -F "file=@data/articles/<slug>/diagram.png"
```

Parse the response to get the GCS URL from the `url` field. If the upload fails, display the error and stop.

## Step 3: Prepare Content (diagram articles only)

Skip this step if `diagram_method` is `"none"`.

Replace the local image path `diagram.png` with the actual GCS URL in:
- The English content (`article_en.md`)
- The Simplified Chinese content (`article_zh.md`)
- The Traditional Chinese content (`article_zh-TW.md`)

## Step 4: Create Article via API

Create the article as a draft.

**For diagram articles** (has GCS URL from Step 2):
```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/articles" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "<title_en from meta>",
    "category": "<category from meta>",
    "author": "<author from meta>",
    "summary": "<summary_en from meta>",
    "content": "<English content with GCS URL>",
    "cover_image_url": "<GCS URL>",
    "read_time": <read_time from meta>,
    "status": "published"
  }'
```

**For video articles** (no diagram, `diagram_method` is `"none"`):
- Use the article content as-is (no URL replacements needed)
- For `cover_image_url`, extract the video thumbnail:
  - YouTube: `https://img.youtube.com/vi/<VIDEO_ID>/maxresdefault.jpg`
  - Bilibili: leave `cover_image_url` as empty string `""`
  - Douyin: leave `cover_image_url` as empty string `""`

Parse the response to get the article **id** and **slug**. If creation fails, display the error and stop.

**Important:** The content field contains Markdown with special characters. Use a temporary JSON file and `curl -d @file.json` to avoid shell escaping issues:
1. Write the request body to a temporary file (e.g., `data/articles/<slug>/tmp_create.json`)
2. Run: `curl -s -X POST "https://api-erp.tadreamk.com/api/v1/articles" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d @data/articles/<slug>/tmp_create.json`
3. Delete the temporary file after use

## Step 5: Update Article with Translations

Update the article to add Chinese translations:

```bash
curl -s -X PUT "https://api-erp.tadreamk.com/api/v1/articles/<article_id>" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "translations": {
      "zh": {
        "title": "<title_zh from meta>",
        "summary": "<summary_zh from meta>",
        "content": "<zh content with GCS URL>"
      },
      "zh-TW": {
        "title": "<title_zh-TW from meta>",
        "summary": "<summary_zh-TW from meta>",
        "content": "<zh-TW content with GCS URL>"
      }
    }
  }'
```

Again, use a temporary JSON file for the request body to avoid escaping issues:
1. Write to `data/articles/<slug>/tmp_update.json`
2. Run the curl command with `-d @data/articles/<slug>/tmp_update.json`
3. Delete the temporary file after use

## Step 6: Clean Up and Summary

1. **Clean up** any temporary files created during upload (tmp_create.json, tmp_update.json)

2. **Display summary**:
   - Article ID and slug
   - Article title (EN, zh, zh-TW)
   - Category and status (published)
   - Cover image URL (GCS)
   - Translation status
   - **Public URL** on TadReamk website, built from the category and slug:

     | Category | URL prefix |
     |---|---|
     | `TadReamk AI` | `https://tadreamk.com/magazine/ai/` |
     | `TadReamk Design` | `https://tadreamk.com/magazine/design/` |
     | `IP Law` | `https://tadreamk.com/magazine/law/` |
     | `News` | `https://tadreamk.com/news/` |
     | `TadReamk-AIGC` | `https://tadreamk.com/magazine/aigc/` |
     | `TadReamk-ERP` | `https://tadreamk.com/magazine/erp/` |

     Example: category `TadReamk-ERP`, slug `setting-up-mpf` → `https://tadreamk.com/magazine/erp/setting-up-mpf`
