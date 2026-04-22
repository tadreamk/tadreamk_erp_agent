---
name: file-attachment
description: Upload image or PDF files to GCS and return markdown-ready URLs for
  embedding in content. Use when user says "attach file", "upload image", "upload
  pdf", "file attachment", "attach image", "attach pdf", or "upload file".
---

# File Attachment

Upload one or more image or PDF files to Google Cloud Storage and produce markdown-ready snippets ready to paste into task descriptions, article content, or any other ERP text field.

The user's request is: $ARGUMENTS

If no file paths are provided, ask the user to specify the file(s) to upload.

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.

## Step 0: Load Token

Read `.env` in the current working directory and extract `WEBAPP_ACCESS_TOKEN`. If missing or empty, try `~/.claude/.env`. If still missing, tell the user to set it in either file and stop.

## Step 1: Upload File(s) to GCS

For each file provided by the user, detect its type by extension and call the appropriate endpoint.

### Images (`.png` `.jpg` `.jpeg` `.gif` `.webp`)

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/articles/image-storage" \
  -H "Authorization: Bearer <token>" \
  -F "file=@<file_path>"
```

Max file size: **2 MB**. If the file exceeds this limit, warn the user and skip it.

### PDFs and other documents (`.pdf` `.docx` `.xlsx` `.pptx` `.txt` `.csv` `.md` `.zip`)

```bash
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/technical-reports/upload" \
  -H "Authorization: Bearer <token>" \
  -F "file=@<file_path>"
```

Max file size: **2 MB**. If the file exceeds this limit, warn the user and skip it.

Parse each response and extract the `url` field. If any upload fails, display the error detail and continue with the remaining files.

## Step 2: Generate Markdown Snippets

For each successfully uploaded file, produce a markdown snippet based on its type.

### Images

Always use pure markdown image syntax:

```markdown
![<filename without extension>](<GCS_URL>)
```

Concrete example:
```markdown
![diagram](https://storage.googleapis.com/public-tadreamk-media/image-storage/alan_20260422_120931_diagram_600.png)
```

- Standard CommonMark syntax — renders on every ERP surface (articles, tasks, comments, personal notes, technical reports).
- **No authoring-time width control.** The rendered size is determined entirely by the target renderer's CSS. If a surface stretches images too wide, that is a renderer/CSS fix, not something the skill should work around.
- **Do not emit HTML `<img>` tags** — strict CommonMark renderers (e.g., personal notes) show them as literal text, and the ERP surfaces we've validated render markdown correctly without needing HTML.
- **Do not emit non-standard width extensions** — `![alt](url =600x)`, `![alt](url){width=600}`, `![alt|width=600](url)` are all ignored by the ERP renderers we've tested.

### PDFs

Use a markdown link with a document emoji so it stands out in rendered content:

```markdown
[📄 <original filename>](<GCS_URL>)
```

### Multiple files

Present each snippet separately, clearly labelled by filename, so the user can pick and paste the ones they need.

## Step 3: Display Results

Show a summary table then each ready-to-paste snippet in its own fenced code block:

```
Uploaded 2 file(s):

| File | Type | Size | GCS URL |
|------|------|------|---------|
| screenshot.png | image | 245 KB | https://storage.googleapis.com/... |
| report.pdf     | pdf   | 1.1 MB | https://storage.googleapis.com/... |
```

Then for each file, show the single ready-to-paste snippet:

**screenshot.png** — paste this into your content:
```markdown
![screenshot](https://storage.googleapis.com/...)
```

**report.pdf** — paste this into your content:
```markdown
[📄 report.pdf](https://storage.googleapis.com/...)
```

## Notes

- **Only emit pure markdown image syntax** (`![alt](url)`). Do not emit HTML `<img>` tags or non-standard width extensions — they either render as literal text on strict renderers or are silently ignored.
- **No width control at authoring time.** Image size is controlled by the target renderer's CSS. If an image looks too wide on a given surface, file a frontend change request; do not pre-resize or swap to HTML.
- **PDF inline preview**: Most markdown renderers do not embed PDF viewers — a labelled link is the correct format.
- **Supported image types for GCS image endpoint**: `.png` `.jpg` `.jpeg` `.gif` `.webp` only. Other file types (including `.pdf`) must use the technical-reports upload endpoint.
- **Auth scope**: Both endpoints require a valid employee auth token (`WEBAPP_ACCESS_TOKEN`).
