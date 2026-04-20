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

Use an HTML `<img>` tag so the image is **downscaled** to a readable width in markdown preview:

```markdown
<img src="<GCS_URL>" alt="<filename without extension>" width="600" />
```

- `width="600"` gives a comfortable preview size — adjust to `400` for smaller inline visuals or `800` for wide diagrams.
- If the image is decorative / a screenshot, use `width="600"`.

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

Then for each file:

**screenshot.png** — paste this into your content:
```markdown
<img src="https://storage.googleapis.com/..." alt="screenshot" width="600" />
```

**report.pdf** — paste this into your content:
```markdown
[📄 report.pdf](https://storage.googleapis.com/...)
```

## Notes

- **Image display width**: `width="600"` is the default. The user can ask to change it (e.g., "make it smaller" → `width="400"`, "full width" → `width="800"`).
- **PDF inline preview**: Most markdown renderers do not embed PDF viewers — a labelled link is the correct format.
- **Supported image types for GCS image endpoint**: `.png` `.jpg` `.jpeg` `.gif` `.webp` only. Other file types (including `.pdf`) must use the technical-reports upload endpoint.
- **Auth scope**: Both endpoints require a valid employee auth token (`WEBAPP_ACCESS_TOKEN`).
