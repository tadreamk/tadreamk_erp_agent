# LinkedIn Post Guidelines

## Format rules
- **Length**: 150-250 words (LinkedIn truncates after ~210 words with "...see more")
- **Opening hook**: The first 1-2 lines are CRITICAL — they must stop the scroll. Use marketing-style hooks that create curiosity or tension before the "see more" fold. Techniques:
  - **Contrarian statement**: Challenge a common belief ("90% of people use AI wrong.")
  - **Surprising stat or number**: Lead with a concrete, unexpected figure
  - **Bold claim**: Make a strong assertion that demands proof ("Your prompts are broken. Here's why.")
  - **Question that stings**: Ask something the reader can't ignore ("Why does AI give you garbage answers?")
  - **Pattern interrupt**: Short, punchy fragments that break reading rhythm
  - Do NOT start with generic setups like "Most people..." or "Here's the thing..." — these are weak openers that blend into the feed
- **Body**: 3-5 short paragraphs summarizing the key insight, not a full article recap
- **Tone**: Professional but conversational — write as a practitioner sharing what they built/learned, not a press release
- **Use line breaks** between paragraphs for readability (LinkedIn renders single newlines)
- **Hashtags**: Add 3-5 relevant hashtags at the end, always including `#HKSTP` (e.g., #AI #ERP #SoftwareEngineering #TechStartup #HKSTP)
- **No emojis** unless the user explicitly asks for them

## Content rules
- Focus on the **one key insight** or takeaway, not every section of the article
- Use concrete numbers or specifics when possible ("30+ tables", "5 iterations per query")
- Write in first person or first person plural ("We built...", "I learned...")
- Do NOT copy-paste from the article — rewrite for the LinkedIn audience

## Closing — Links

Check `article_meta.json` for a `"sources"` array.

### If sources exist (article based on external references)

Use the **original source URLs** instead of the TadReamk URL. This lets LinkedIn profile/preview the original articles.

Format:
```
Sources:
<URL 1>
<URL 2>
```

**Example** (2 sources):
```
Sources:
https://news.rthk.hk/rthk/en/component/k2/1845788-20260303.htm
https://www.scmp.com/news/hong-kong/society/article/3345158/mainland-chinese-firm-build-northern-metropolis-data-cluster-facility
```

### If no sources (original article)

Build the TadReamk URL from the **category** and **slug** in `article_meta.json`:

| Category | URL prefix |
|---|---|
| `TadReamk AI` | `https://tadreamk.com/magazine/ai/` |
| `TadReamk Design` | `https://tadreamk.com/magazine/design/` |
| `IP Law` | `https://tadreamk.com/magazine/law/` |
| `News` | `https://tadreamk.com/news/` |
| `TadReamk-AIGC` | `https://tadreamk.com/magazine/aigc/` |
| `TadReamk-ERP` | `https://tadreamk.com/magazine/erp/` |

The slug used in the URL is the **API slug** (returned when the article was created), NOT the local folder slug. The API slug does NOT include the trailing random integer suffix (e.g., `-5821`). Read the slug from `article_meta.json` field `"slug"`.

**Examples:**
- Category `TadReamk AI`, slug `rachel-ai-intelligent-database-assistant` → `https://tadreamk.com/magazine/ai/rachel-ai-intelligent-database-assistant`
- Category `TadReamk Design`, slug `evolution-of-famous-logos` → `https://tadreamk.com/magazine/design/evolution-of-famous-logos`
- Category `News`, slug `new-partnership-ip-protection` → `https://tadreamk.com/news/new-partnership-ip-protection`

Format:
```
Read the full article: <URL>
```
