---
name: article-draft
description: Generate a full article with diagram and translations, saving
  everything locally as a draft. Use when user says "write an article",
  "article draft", "draft article", "create article", or "generate article
  with diagram".
disable-model-invocation: true
---

# Article Draft

Generate a full article with diagram and translations, saving everything locally as a draft for review before uploading.

The user's request is: $ARGUMENTS

If the request is empty or unclear, ask the user to describe what article they want written. Example:
```
/article-draft Write a technical article about how our ERP system handles job application workflows
```

## References

- [slide-template.md](references/slide-template.md) — React slide App.jsx template, project structure, design guidelines, export options
- [color-themes.md](references/color-themes.md) — 7 color themes (Midnight, Ocean, Forest, Sunset, Violet, Slate, Warm) with Tailwind classes
- [lucide-icons.md](references/lucide-icons.md) — Curated list of verified Lucide icon names by category
- [python-diagrams.md](references/python-diagrams.md) — Python diagrams library script template, common node imports, render and branding commands
- [linkedin-post.md](references/linkedin-post.md) — LinkedIn post format rules, content rules, category-to-URL mapping

## Prerequisites

This skill requires certain tools. If they are not set up, install them first:

1. **Python virtual environment** — If `venv/` does not exist at the project root, create one:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install playwright Pillow diagrams
   playwright install chromium
   ```
2. **Node dependencies for slides** — If `slides/node_modules` does not exist:
   ```bash
   cd slides && npm install
   ```
3. **Scripts** — The `scripts/` directory must contain `export_slides_images.py` and `add_branding.py`.

## Step 1: Write the Article (English)

Based on the user's request, generate a professional article in **Markdown** format with:
- A clear, engaging **title** (max 500 chars)
- A concise **summary** (2-3 sentences)
- Full **content** in Markdown with headings, paragraphs, code blocks, lists as appropriate
- Estimate a **read_time** in minutes (word count / 200)
- Ask the user to select a **category** using the AskUserQuestion tool with these options: `TadReamk AI`, `TadReamk Design`, `IP Law`, `News`, `TadReamk-AIGC`, `TadReamk-ERP`
- Set **author** by reading the `ARTICLE_AUTHOR_NAME` variable from `.env`
- If the user provides **source URLs** (e.g., `## source: https://...`), extract them into a `"sources"` array in the metadata. Each entry should have `url` and `name` (derive the name from the domain, e.g., `"RTHK"` from `news.rthk.hk`, `"SCMP"` from `scmp.com`).

The article should be well-structured with an introduction, body sections with H2/H3 headings, and a conclusion. Do NOT use "Introduction" or "Conclusion" as section headings — just write the opening and closing paragraphs directly without titles.

**No title in content:** The title and summary are stored in `article_meta.json` only. The content body (saved to `article_en.md` and translation files) must NOT include the article title as H1. Start the content with the opening paragraph(s) directly — no `# Title` line at the top.

**Markdown formatting rules:**
- **Bullet lists**: Do NOT put blank lines between consecutive list items. Write them as tight lists.
- **Numbered lists**: Same rule — no blank lines between items.
- **Image placement**: Place the diagram image at the **upper part of the article** — right after the opening paragraph(s), before the first H2 heading. This gives readers an immediate visual overview before diving into the details.
- **Image with caption**: Use this pattern for the diagram image:
  ```markdown
  ![Diagram description|center](diagram.png)

  *Brief description of what the diagram shows*
  ```
  The `|center` modifier centers the image. Use `diagram.png` (relative path). The `/article-upload` command will replace it with the GCS URL.

## Step 2: Generate a Diagram Image

Generate a visual that captures the key idea of the article, then save it as `diagram.png`.

1. Derive a **slug** from the article title:
   1. Lowercase the title
   2. Replace any sequence of non-`[a-z0-9]` characters with a single hyphen
   3. Strip leading and trailing hyphens
   For example, `"Hello World! 123"` → `"hello-world-123"`. The folder name is `{YYMMDD}_<slug>` using the current date, e.g. `260312_understanding-erp-systems`
2. Create the output directory: `data/articles/<YYMMDD_slug>/`
3. **Randomly pick one of two diagram methods** — flip a coin each time, do NOT always pick the same one:

### Method A: React Slide

Best for: component overviews, feature breakdowns, module grids, hub-and-spoke layouts.

1. Analyze the article and design a single-slide visual. Choose the best layout: grid, stats, hub-and-spoke, comparison, timeline, or hierarchy.
2. Pick a color theme from [color-themes.md](references/color-themes.md). Match the theme to the article topic.
3. Edit `slides/src/App.jsx` following the template in [slide-template.md](references/slide-template.md). Use only icons from [lucide-icons.md](references/lucide-icons.md).
4. Start the Vite dev server if not already running:
   ```bash
   cd slides && node node_modules/vite/bin/vite.js --port 3009 &
   ```
   (Use this direct path instead of `npx vite` to avoid ERR_MODULE_NOT_FOUND with some Node/npm setups.)
5. Export:
   ```bash
   source venv/bin/activate && python scripts/export_slides_images.py --url http://localhost:3009 --output data/articles/<YYMMDD_slug>/diagram.png
   ```
6. Set `diagram_method` to `"slides"` in metadata

### Method B: Python Diagrams

Best for: system architecture, infrastructure, service flows, data pipelines, deployment diagrams.

Follow the instructions in [python-diagrams.md](references/python-diagrams.md) to write a script, render, and add branding. Set `diagram_method` to `"diagrams"` in metadata.

---

After generating with either method, read the image to display it to the user.

## Step 3: Translate to Traditional Chinese (zh-TW) and Simplified Chinese (zh)

**Do the translations directly yourself (Claude CLI) — do NOT call any translation API.**

Use the Task tool with a background agent to translate the article's **title**, **summary**, and **content** into both languages. The **content** being translated is the body only (no title H1) — same as what goes in `article_en.md`.

### Translation rules:
- Translate ALL text fully, including headings, sub-headings, and technical terms
- Do NOT leave English words untranslated unless they are proper nouns (brand names, person names), URLs, or code snippets
- Preserve all Markdown formatting (headings, bold, italic, links, images, code blocks, lists, etc.)
- Preserve all image URLs exactly as-is (do NOT translate URLs)
- Maintain the same tone and style as the original
- For zh-TW, use Traditional Chinese characters and Taiwan-localized terminology

## Step 4: Save All Files Locally

Save everything to `data/articles/<YYMMDD_slug>/`:

1. **`article_en.md`** — The English content body only (no title H1, no summary)
2. **`article_zh.md`** — The Simplified Chinese content body only (no title H1, no summary)
3. **`article_zh-TW.md`** — The Traditional Chinese content body only (no title H1, no summary)
4. **`article_meta.json`** — Metadata file with this structure:
   ```json
   {
     "title_en": "English Title",
     "title_zh": "简体中文标题",
     "title_zh-TW": "繁體中文標題",
     "summary_en": "English summary...",
     "summary_zh": "简体中文摘要...",
     "summary_zh-TW": "繁體中文摘要...",
     "category": "TadReamk AI",
     "author": "<ARTICLE_AUTHOR_NAME from .env>",
     "read_time": 8,
     "diagram_method": "slides or diagrams",
     "slug": "the-article-slug",
     "sources": [
       {"url": "https://example.com/article", "name": "Source Name"}
     ]
   }
   ```
5. **`diagram.png`** — The rendered diagram image (already created in Step 2)

## Step 5: Summary

Display a summary to the user:
- Article title (EN, zh, zh-TW)
- Slug and local path (`data/articles/<YYMMDD_slug>/`)
- Category, author, read_time
- List of all saved files
- The generated slide image (read and display it)
- Remind the user they can review/edit the files, then run `/article-upload <slug>` to publish

## Step 6: Generate LinkedIn Post

After displaying the summary, generate a LinkedIn post for the article following the guidelines in [linkedin-post.md](references/linkedin-post.md).

1. Read `article_meta.json` and `article_en.md` from the draft
2. Write the LinkedIn post following the format, content, and closing rules
3. Save to `data/articles/<slug>/article_linkedin.md` — **do NOT add a heading** (e.g. `# LinkedIn Post`) at the top; the file must contain only the post text so the user can copy-paste directly into LinkedIn
4. Display the full post text so the user can review and copy-paste it directly into LinkedIn
