---
name: guide-page-upload
description: Upload a locally drafted guide page to the database. Use when user
  says "upload guide page", "publish guide page", "guide-page-upload", or "push
  guide page to production".
disable-model-invocation: true
---

# Guide Page Upload

Upload a locally drafted guide page to the database.

This command takes no arguments. It auto-detects drafts from `data/guide_pages/`.

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token and Select Draft

Load the auth token by reading `.env` in the current working directory and extracting the `WEBAPP_ACCESS_TOKEN` value. If the variable is missing or empty, try `~/.claude/.env` as a fallback. If still missing in both locations, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

Scan `data/guide_pages/` for files that have a matching `*_meta.json` file (e.g., `how-to-submit-leave.md` + `how-to-submit-leave_meta.json`).
- If **no drafts found**, tell the user to run `/guide-page-draft` first and stop.
- If **one draft found**, use it automatically.
- If **multiple drafts found**, list each draft's slug, title, and section, then ask the user which one to upload.

## Step 1: Read Local Draft Files

Read the selected draft files:
- `data/guide_pages/{filename}.md` — Markdown content
- `data/guide_pages/{filename}_meta.json` — Metadata (slug, title, section, sort_order, is_active)

Verify both files exist. If either is missing, report the error and stop.

## Step 2: Check for Existing Guide Page

Check if a guide page with the same slug already exists by listing all guide pages:

```bash
curl -s -X GET "https://api-erp.tadreamk.com/api/v1/guide-pages/admin" \
  -H "Authorization: Bearer <token>"
```

Search the response array for a page with a matching `slug`.

- If **found** → this is an **update**. Note the existing page `id` and proceed to Step 3b.
- If **not found** → this is a **new page**. Proceed to Step 3a.

## Step 3a: Create New Guide Page

Create the guide page via the API:

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/guide-pages/admin" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "slug": "<slug from meta>",
    "title": "<title from meta>",
    "section": "<section from meta>",
    "content": "<markdown content>",
    "sort_order": <sort_order from meta>,
    "is_active": <is_active from meta>
  }'
```

**Important:** The content field contains Markdown with special characters. Use a temporary JSON file and `curl -d @file.json` to avoid shell escaping issues:
1. Write the request body to a temporary file (e.g., `data/guide_pages/tmp_create.json`)
2. Run: `curl -s -X POST "https://api-erp.tadreamk.com/api/v1/guide-pages/admin" -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d @data/guide_pages/tmp_create.json`
3. Delete the temporary file after use

Parse the response to get the page `id`. If creation fails, display the error and stop.

Skip to Step 4.

## Step 3b: Update Existing Guide Page

Update the existing guide page via the API:

```bash
curl -s -X PUT "https://api-erp.tadreamk.com/api/v1/guide-pages/admin/<page_id>" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "<title from meta>",
    "section": "<section from meta>",
    "content": "<markdown content>",
    "sort_order": <sort_order from meta>,
    "is_active": <is_active from meta>
  }'
```

Use a temporary JSON file as in Step 3a to avoid escaping issues.

Parse the response. If update fails, display the error and stop.

## Step 4: Clean Up and Summary

1. **Clean up** any temporary files created during upload (tmp_create.json)

2. **Display summary**:
   - Action taken: Created or Updated
   - Page ID and slug
   - Title
   - Section and sort order
   - Active status
   - Confirm the guide page is live in the system
