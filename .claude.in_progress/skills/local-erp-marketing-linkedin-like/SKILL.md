---
name: local-erp-marketing-linkedin-like
description: Bulk-like posts on the TadReamk LinkedIn company page feed. Navigates
  to the admin feed, injects a JS script that likes posts with random delays, scrolls
  to load more, and monitors until the target count is reached. Use when user says
  "linkedin like", "like linkedin posts", "bulk like", or "local-erp-marketing-linkedin-like".
model: claude-sonnet-4-6
---

# LinkedIn Bulk Like — TadReamk Company Page

Automates liking posts on the TadReamk LinkedIn company page admin feed to boost engagement with followed companies.

## Prerequisites

- Chrome browser open with the Claude-in-Chrome extension active
- User logged into LinkedIn with admin access to the TadReamk company page (ID: `103008400`)

## Step 1: Open the LinkedIn Admin Feed

1. Load Chrome tools: `tabs_context_mcp`, `tabs_create_mcp`, `navigate`
2. Get current tab context with `tabs_context_mcp` (create if empty)
3. Create a new tab or use an existing one
4. Navigate to: `https://www.linkedin.com/company/103008400/admin/feed/following/`
5. Verify the page loads by reading the page — confirm heading "Feed" and TadReamk branding are present

## Step 2: Inject the Auto-Like Script

Load Chrome tools: `javascript_tool`, `computer`

Inject the following JavaScript into the page. Adjust `target` and delay range based on user input:

```javascript
window.__likeJob = {
  liked: 0,
  target: 100,  // adjust per user request
  running: true,
  log: [],

  randomDelay() {
    return Math.floor(Math.random() * 10000) + 5000; // 5000-15000ms (5-15s)
  },

  async run() {
    while (this.liked < this.target && this.running) {
      const allButtons = Array.from(document.querySelectorAll('button'));
      const likeButtons = allButtons.filter(btn => {
        const text = btn.getAttribute('aria-label') || btn.innerText || '';
        return text.includes('React Like') && !text.includes('Unlike');
      });

      if (likeButtons.length === 0) {
        // Try "Show more results" button
        const showMore = allButtons.find(
          btn => (btn.innerText || '').includes('Show more results')
        );
        if (showMore) {
          showMore.click();
          this.log.push(`[${this.liked}] Clicked "Show more results", waiting...`);
          await new Promise(r => setTimeout(r, 3000));
          continue;
        }

        // Scroll down to trigger lazy loading
        window.scrollBy(0, 800);
        this.log.push(`[${this.liked}] Scrolling to load more posts...`);
        await new Promise(r => setTimeout(r, 3000));

        // Re-check for like buttons
        const retryButtons = Array.from(document.querySelectorAll('button')).filter(btn => {
          const text = btn.getAttribute('aria-label') || btn.innerText || '';
          return text.includes('React Like') && !text.includes('Unlike');
        });
        if (retryButtons.length === 0) {
          this.log.push(`[${this.liked}] No more like buttons found. Stopping.`);
          this.running = false;
          break;
        }
        continue;
      }

      // Click the first available like button
      const btn = likeButtons[0];
      const article = btn.closest('article');
      let postInfo = 'unknown';
      if (article) {
        const heading = article.querySelector('a[href*="/company/"]');
        if (heading) postInfo = heading.innerText || heading.getAttribute('aria-label') || 'unknown';
      }

      btn.click();
      this.liked++;
      const delay = this.randomDelay();
      this.log.push(`[${this.liked}/${this.target}] Liked: ${postInfo.substring(0, 50)} — next in ${(delay/1000).toFixed(1)}s`);

      // Scroll every 2 likes to bring new posts into view
      if (this.liked % 2 === 0) {
        window.scrollBy(0, 400);
      }

      await new Promise(r => setTimeout(r, delay));
    }

    this.log.push(`Done! Total liked: ${this.liked}`);
    return `Completed: ${this.liked} posts liked`;
  }
};

window.__likeJob.run();
```

## Step 3: Monitor Progress

Poll the job status periodically (every ~60 seconds) using:

```javascript
JSON.stringify({
  liked: window.__likeJob.liked,
  running: window.__likeJob.running,
  recentLog: window.__likeJob.log.slice(-8)
}, null, 2)
```

Between checks, use `computer` tool with `wait` action (10s intervals) to let the script run.

Report progress to the user at milestones (25%, 50%, 75%, 90%, done).

## Step 4: Report Completion

Once `window.__likeJob.liked` reaches the target or `running` becomes `false`, report:
- Total posts liked
- Whether it completed fully or stopped early (e.g., ran out of posts)
- Any notable log entries (errors, multiple "Show more" clicks, etc.)

## Notes

- To **stop the job early**, run: `window.__likeJob.running = false;`
- The script filters out already-liked posts (`Unlike` in aria-label) to avoid double-liking
- If LinkedIn shows a rate-limit warning or CAPTCHA, the script will naturally stall — monitor and inform the user
