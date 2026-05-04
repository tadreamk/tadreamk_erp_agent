---
name: local-erp-marketing-article
description: End-to-end ERP marketing article workflow — fetch today's marketing
  task, write the article with diagram and translations, upload to production, and
  mark the task as completed. Use when user says "marketing article", "erp marketing",
  "write today's marketing article", or "local-erp-marketing-article".
model: claude-sonnet-4-6
effort: high
---

# ERP Marketing Article — Full Workflow

Automates the complete lifecycle of an ERP Marketing article: from finding today's task, to writing, uploading, and closing the task.

This skill orchestrates several plugin skills in sequence. Each step below specifies which plugin skill to invoke.

## Step 1: Fetch Today's Marketing Task

**Use skill:** `tadreamk-erp:task-overview`

1. Invoke `/tadreamk-erp:task-overview` to pull all active tasks
2. From the results, filter for **marketing-related** tasks:
   - Task belongs to project titled "ERP Marketing", OR has "marketing" in the title/slug/description
   - Task status is one of: `in_progress`, `in_queue`, `not_started`
3. Identify the task with `start_date` matching **today's date**
   - If no task matches today, show all active marketing tasks with their start dates and ask the user which one to work on
   - If multiple tasks match today, list them and ask the user to pick one

## Step 2: Get Task Details

**Use skill:** `tadreamk-erp:task-detail`

1. Invoke `/tadreamk-erp:task-detail <task_slug>` on the selected task
2. From the task `description`, extract:
   - The pain points to highlight in the article
   - The feature reference doc path (e.g., `/Users/alan/Documents/projects/fullstack_erp/docs/abstract/human_resources/employee.md`)
3. Read the referenced feature doc to understand the feature in detail

## Step 3: Write Article, Generate Diagram, Translate

**Use skill:** `tadreamk-erp:article-draft`

1. Invoke `/tadreamk-erp:article-draft` with the task description and feature doc context as the argument
   - The article-draft skill handles: writing the English article, generating a diagram (slide or Python diagrams), translating to zh and zh-TW, saving all local draft files, and generating a LinkedIn post
2. When the article-draft skill asks for a **category**, select `TadReamk-ERP` (or whichever category fits the article topic)

The article-draft skill will save all files to `data/articles/<YYMMDD_slug>/`:
- `article_en.md`, `article_zh.md`, `article_zh-TW.md`
- `article_meta.json`
- `diagram.png`
- `article_linkedin.md`

## Step 4: Upload Article to Production

**Use skill:** `tadreamk-erp:article-upload`

1. Invoke `/tadreamk-erp:article-upload <slug>` to publish the drafted article
   - The article-upload skill handles: uploading diagram to GCS, replacing local image paths with GCS URLs, creating the article via API, adding translations via API, and cleaning up temp files
2. Note the returned article ID, slug, and public URL

## Step 5: Mark Task as Completed on ERP

**No plugin skill — direct API call.**

Load `WEBAPP_ACCESS_TOKEN` from `.env`, then:

```bash
curl -s -X PATCH "https://api-erp.tadreamk.com/api/v1/tasks/<task_slug>" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"status": "completed"}'
```

## Step 6: Display Summary

Show:
- Article title (EN, zh, zh-TW)
- Article ID, slug, category, author, read time
- Public URL (built from category + slug, e.g., `https://tadreamk.com/magazine/erp/<slug>`)
- Cover image (GCS URL)
- Translation status
- Task slug and completion status
- The diagram image
- The LinkedIn post text for copy-paste
