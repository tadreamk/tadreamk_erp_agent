---
name: local-generate-narrative-user-story
description: Generate a narrative user-story documentation set from a customer-requirement
  share URL. Fetches the document, saves it under data/customer_requirements/ as
  requirements.md (or requirements_cn.md + requirements_en.md if Chinese), then
  turns each feature into a human-centred, diagram-driven chapter under
  narrative_user_story/. Use when user says "generate narrative user story",
  "write narrative user story", "narrative story from requirements",
  "narrative docs", or "local-generate-narrative-user-story".
model: claude-opus-4-7
effort: high
---

# Generate Narrative User Story from a Customer-Requirement URL

Turns a live customer-requirement document (hosted on the ERP share-link editor) into:

1. A local `requirements.md` snapshot (bilingual variants if the source is Chinese).
2. A narrative user-story documentation set (characters, scenes, ASCII diagrams) matching the shape established in `data/customer_requirements/260420_amazing_grace/narrative_user_story/`.

## Input

The skill argument is **one of**:

- A public share URL, e.g. `https://erp.tadreamk.com/shared/customer-requirements/4JJs6gikrdfx`
- A bare 12-character share token, e.g. `4JJs6gikrdfx`
- An existing local folder path, e.g. `data/customer_requirements/260420_amazing_grace/` (skips to Step 5; used when the requirements file is already on disk)

If the argument is missing, ask the user for the URL, token, or folder path before proceeding.

## Output

A project folder under `data/customer_requirements/<YYMMDD>_<project_slug>/`:

```
<folder>/
  requirements.md                 # English source (or bilingual pair below)
  requirements_cn.md              # Original Chinese (only when source is Chinese)
  requirements_en.md              # English translation (only when source is Chinese)
  narrative_user_story/
    index.md
    ch1_<feature_slug>/
      01_<section_slug>.md
      02_<section_slug>.md
      ...
    ch2_<feature_slug>/
      ...
```

Naming rules for the project folder:

- `YYMMDD` — today's date from `date +%y%m%d`.
- `project_slug` — short snake_case slug derived from the fetched document title (strip punctuation, lowercase, max ~3 words). Confirm with the user before creating the folder.

## What "Narrative" Means Here

In a user story, the **narrative** is the short, structured sentence that defines **who** the user is, **what** they want, and **why** they want it — the human-readable description that sits at the heart of the story. Every chapter section this skill produces must be built on top of one such narrative sentence.

### The Narrative Template

> **As a [user role], I want [goal/action], so that [benefit/reason].**

- **"As a [role]"** — a specific persona from the cast (Step 6). Never a generic "user".
- **"I want [goal]"** — one concrete behaviour the requirements describe as solving the pain.
- **"So that [benefit]"** — the pain relieved, as described in the requirements.

The prose in every section dramatises all three parts through a concrete scene; the ASCII diagram shows how the system fulfils the "I want". Acceptance criteria and field lists belong in the diagram, not the paragraphs.

## Timing

Record a wall-clock start time at the very beginning of Step 0 using `python3 -c "import time; print(int(time.time()*1000))"`. Record a per-step start time at each step and compute its duration. Report accumulated timings at the end.

## Step 0: Classify the Input

Record step start time. Decide which branch to take:

- If the argument looks like a URL → extract the share token (last path segment).
- If the argument is a 12-character alphanumeric token → use it directly.
- If the argument is an existing directory path that contains `requirements.md` (or `requirements_en.md`) → **skip Steps 1–4** and jump to Step 5 with that folder.
- Otherwise → ask the user for a valid URL, token, or folder.

Set:
- `share_token` — when the source is remote.
- `folder` — resolved only after Step 4 when remote, or taken directly when local.

## Step 1: Fetch Metadata and Body

Record step start time. Skip if the source is a local folder.

Run these two operations in parallel:

**1a — Metadata** (public endpoint, no auth):
```bash
curl -s "https://api-erp.tadreamk.com/api/v1/customer-requirements/public/<share_token>"
```
Extract `title` from the response. Errors `404`/`429` should stop the skill with a clear message.

**1b — Body** (Yjs over WebSocket):
```bash
python3 .claude.prod/scripts/read_yjs_content.py <share_token>
```
Capture stdout as `raw_content`. If `raw_content` is empty, stop and tell the user the document has no body to turn into a narrative.

## Step 2: Detect Language and Derive Slug

Record step start time.

**Language detection** — scan `raw_content`:
- If it contains any CJK Unified Ideograph (Unicode `一-鿿`) covering more than ~10% of non-whitespace characters, treat the source as **Chinese**.
- Otherwise treat it as **English**.

**Project slug** — derive from `title`:
- Lowercase, strip punctuation, replace whitespace with `_`, keep the first 2–3 meaningful words.
- Show the user the proposed folder name `<YYMMDD>_<project_slug>` and ask them to confirm or override the slug before creating anything on disk.

## Step 3: Create the Project Folder

Record step start time. After the user confirms the slug:

```bash
mkdir -p data/customer_requirements/<YYMMDD>_<project_slug>
```

Set `folder = data/customer_requirements/<YYMMDD>_<project_slug>`.

If the folder already exists and is non-empty, ask the user whether to overwrite, choose a different slug, or abort.

## Step 4: Write the Requirements File(s)

Record step start time.

**English source** — write `raw_content` directly to `<folder>/requirements.md`. Done.

**Chinese source** — write two files:

1. `<folder>/requirements_cn.md` — the exact `raw_content` as fetched.
2. `<folder>/requirements_en.md` — a faithful English translation of `raw_content`.

Translation rules:
- Preserve headings, lists, tables, code blocks, and link URLs exactly.
- Keep product names, company names, and domain terms untranslated when no established English equivalent exists (retain the Chinese in parentheses after the first mention).
- Do not summarise, reorder, or drop content. The English file is a translation, not an abstract.
- Retain the same markdown structure so downstream readers can diff the two files section-by-section.

Do **not** also write `requirements.md` when the source is Chinese — the bilingual pair replaces it.

Record which file downstream steps should read:
- English source → `<folder>/requirements.md`
- Chinese source → `<folder>/requirements_en.md`

Call that file `requirements_file` for the remainder of the skill.

## Step 5: Read the Requirements and Identify Feature Areas

Record step start time.

1. Read `requirements_file` in full.
2. Walk its section headings and group related content into a list of **feature areas** — each one a coherent slice of functionality that could become its own chapter. Top-level `##` headings and major `###` subsections are the usual candidates. Merge adjacent sections that describe the same feature under different angles.
3. For each identified feature area, extract an internal outline with:
   - **Problem** — the pain or status-quo frustration the requirements describe (explicit or implied).
   - **Solution** — the concrete behaviour the ERP / system introduces.
   - **User Flow** — the sequence of steps the requirements describe (if present).
   - **Scope** — bullets worth dramatising; anything explicitly in or out of scope.
   - **Acceptance Criteria** — measurable rules, field lists, or record shapes mentioned (these feed diagrams, not prose).

If the requirements file is too thin to yield at least one feature area with a discernible Problem and Solution, stop and tell the user the document needs more detail before a narrative can be generated.

## Step 6: Design the Cast

Record step start time. Before writing any chapter, define the cast of characters. The cast is shared across all chapters. Keep it small (6–10 characters) and grounded in the real business.

Derive characters from the requirements:
- **Owner / operator** — the person who runs the business today (maps to the `one person with one backup` role if present).
- **Admin / backup** — the second person handling paperwork, payroll, reconciliation.
- **1–2 frontline workers** — whoever actually delivers the service. Give each a distinct background so the story can show team coverage and differing tenure.
- **1 end-customer + 1 family member** — the recipient of the service and the person paying / reading reports.
- **AI / automation personas** — name the AI communication agent (if any) and any external AI marketing / partner service. Treat each as a character with a clear voice and scope.
- **Any domain-specific persona** introduced in the requirements (inspector, regulator, referral partner, etc.).

For each character write one short paragraph: name, role, and what they represent in the story (what pain they embody or what capability they personify). Save this cast internally — it will be reused across chapters.

### Character naming convention — parenthesised title before the name

Every character's **display name** is `(<Title>) <Given Name or Full Name>`, with the title wrapped in parentheses. That full display name is used consistently throughout the story — in the `## The People in This Story` cast block, in every narrative user-story sentence (`As (<Title>) <Name>, I want …`), and in every prose reference where the full name appears.

The title is a short descriptor of role chosen so that a reader who lands on any chapter can identify the person's role at a glance without flipping back to the cast. Examples from the Butterfly Plan story:

- `(Program Director) Mei Lau`
- `(Admin) Tung Ho`
- `(Communications Lead) Noah Kwok`
- `(AI Agent) Rachel`
- `(Principal) Wong`
- `(Teacher) Lam`
- `(CSR Lead) Mr Chan`
- `(Mother) Madam Chow`
- `(Nurse) Auntie Lee`
- `(Student) Jia Wong`

Rules:

- **Every** named character in the cast — including ones whose existing honorific suggests their role (Principal, Teacher, Mr/Madam) — carries the parenthesised title. Write `(Principal) Wong`, not `Principal Wong`.
- Spell titles out in full — prefer `(Communications Lead)` over `(Comms Lead)`, since not every reader knows the shorthand.
- The bold header in the cast block uses the full `(<Title>) <Name>`. Do not repeat the same title or role phrase in the body paragraph that follows (avoid `**(AI Agent) Rachel** — An AI coordinating assistant…`; rephrase the body as `**(AI Agent) Rachel** — Named after an early volunteer…` or similar).
- **Attach the title to every prose reference to a character, including bare first names and bare surnames.** Write `(Program Director) Mei called (Admin) Tung` and `(Student) Jia said yes`, not `Mei called Tung` or `Jia said yes`. This keeps a reader who lands on any chapter oriented without flipping back to the cast.
- One exception: within a character's own cast-block body paragraph, do not re-title self-references (write `**(Admin) Tung Ho** — … Tung is the backup for everything`, not `… (Admin) Tung is the backup`). Cross-references to other characters in that same paragraph still carry their title.
- Keep ASCII diagrams untouched — inside fenced code blocks, use the bare name (`Owner: Mei`, RACI column `Tung  Mei  vendor`) so column alignment is preserved. The `(Title)` convention applies to narrative prose, not tables or diagrams.
- Edge cases that look like a character's name but are not: preserve them verbatim (e.g., `Lee Mei-fong` is Auntie Lee's Chinese given name, not a reference to `(Program Director) Mei`; `Chan & Partners` is a firm, not `(CSR Lead) Mr Chan`).
- Use the same title consistently across every chapter — pick once in Step 6, do not drift later.

## Step 7: Plan Chapters and Sections

Record step start time. For each feature area identified in Step 5:

1. Pick a chapter title. Use a display name drawn from the feature area's heading in the requirements.
2. Decide how many sections the chapter needs. One section per distinct ASCII diagram or concept block. Suggested defaults:
   - Simple reused module → 1 section.
   - Feature with clear record + flow + management UI → 3–5 sections.
   - Cross-cutting feature (communication, notifications) → 2–4 sections.
3. For each section, name the single diagram it will hold. Section filename uses a two-digit prefix and a short snake_case slug.

Write the planned chapter/section outline and confirm it with the user **before** writing any content. Show:

```
Planned story structure:

  Ch1 — <Feature 1 title>
    01_<section>.md — <one-line purpose>
    02_<section>.md — <one-line purpose>
    ...
  Ch2 — <Feature 2 title>
    ...

Proceed?
```

Wait for confirmation.

## Step 8: Write `narrative_user_story/index.md`

Record step start time. Create `<folder>/narrative_user_story/index.md` with:

- A title (`# <Project Display Name> — A Digital <Domain> Narrative User Story`).
- A short, evocative subtitle in a blockquote.
- A one-paragraph framing: the story follows the business through an ordinary stretch of time that becomes extraordinary because of the ERP threads connecting every interaction.
- A note that each chapter is split into short sections, one per diagram, openable independently.
- A `## The People in This Story` cast block — the full cast from Step 6, one bolded `**(<Title>) <Name>**` per character followed by the short paragraph written in Step 6. The cast lives in the index (not inside any chapter) so that any reader landing on the story has the cast one click away from every chapter via the `[↑ Index](../index.md)` nav link.
- A `## Chapters` list, each chapter with bullet links to its sections (matches the confirmed outline).
- A closing line: `*All characters in this story are fictional. All concepts are real.*`

## Step 9: Write Each Chapter Section

Record step start time. For every section file, use this template:

```markdown
# Chapter <N>: <Chapter Title> — <Section Title>

<nav-line>

---

<Opening — see rules below>

## <Inline Heading — a noun phrase about the diagram>

<Narrative paragraphs — 1 to 3. Explain the concept through one character's
perspective. Ground in the pain point identified from the requirements and
show how the solution concretely changes the moment.>

```
<ASCII DIAGRAM — one block, monospaced, boxed where helpful. Draw from the
user flow or record shape described in the requirements. Anchor to a concrete
named order / customer / worker from the cast.>
```

<Optional closing paragraph — a quiet, human beat. Not a summary of the feature.
A moment.>

---

<nav-line>
```

### Navigation line format

```
[← Prev: <Prev Section Title>](<prev-path>) | [↑ Index](../index.md) | [Next: <Next Section Title> →](<next-path>)
```

Special cases:
- First section of chapter 1: use `[↑ Index](../index.md) | [Next: <next> →](./02_...md)` (no prev).
- Last section of the last chapter: use `[← Prev: <prev>](./...md) | [↑ Index](../index.md)` (no next).
- When crossing chapters, use relative paths like `../ch<N+1>_<slug>/01_<slug>.md`.

### Opening rules

- The **cast block (`## The People in This Story`) lives in `narrative_user_story/index.md`, not in any chapter section.** It sits between the framing paragraph and the `## Chapters` list, so that every reader sees the cast once at the top of the story and every chapter's `[↑ Index]` nav link gives one-click access back to it. Do not duplicate the cast block into Chapter 1 or any other section.
- The **very first section of Chapter 1** opens directly with the evocative scene-setting paragraph ("It started with a phone call on a Tuesday morning…") that seeds the first customer's situation — no cast preamble, since that now lives in the index.
- Every chapter's **first section** opens with 2–4 narrative paragraphs grounding the reader: what was the status quo before the ERP for this feature, seen through the character who felt the pain most?
- Subsequent sections in the same chapter can open directly with `## <Inline Heading>` — no second preamble required.
- The **last section of the last chapter** ends the overall story with a short `## What the Story Was Really About` reflection, then a final scene that closes the arc of the end-customer + family member. End with an italicised `*End of story.*` line before the final nav line.

### Diagram rules

- Exactly one ASCII diagram per section — this is why we split chapters into sections.
- Render inside a fenced code block (no language tag).
- Prefer boxes, arrows (`│`, `▼`, `►`), and clear column alignment. Use placeholders like `HK$XXX`, `XXXX-XXXX`, or anonymised phone numbers where the requirements show sensitive data.
- Anchor the diagram to named characters from the cast (e.g., show `ORD-0071` for the end-customer, use worker first-names).

### Narrative rules

- Write like a writer, not a technical specifier. Short sentences. Concrete details. One or two sensory anchors per section (a Post-it note on a monitor, a phone buzzing at 11:42 p.m., a printed bank statement on a desk).
- Every feature's **Problem** identified in the requirements must be felt in prose before the **Solution** is shown. Do not paraphrase the requirements' bullets — dramatise them.
- Acceptance-criteria bullets and field lists pulled from the requirements map into diagrams, not into prose. Keep the prose about people.
- Use present tense for the current ERP-enabled flow; use past tense for the "before" world.
- Never invent regulatory, medical, or legal facts. If the requirements name something specific (e.g., "HK MPF", "CRM", "RACI"), use the exact term.
- Keep the scope honest: do not promise features that are not in the requirements.
- Write the narrative in **English** even when the source document is Chinese. Translate domain terms inline the first time they appear.
- Apply the **parenthesised-title-before-name** convention from Step 6 to **every** prose reference to a cast character — full names, bare first names, and bare surnames alike. Write `(Program Director) Mei called (Admin) Tung`, `(Student) Jia said yes`, and `(Principal) Wong asked if the programme would return`. The only exceptions are: (a) self-references inside a character's own cast-block body paragraph, and (b) anything inside a fenced code block (ASCII diagrams, tables), which stay bare to preserve column alignment.

## Step 10: Cross-Link and Validate

Record step start time. After writing all files:

1. Walk every section file and verify each navigation link resolves to an existing file.
2. Verify that `narrative_user_story/index.md` lists every section file that exists on disk.
3. Verify that every feature area identified in Step 5 is represented by a chapter (or is intentionally merged into a combined chapter, and the merge is noted in `narrative_user_story/index.md`).
4. Verify that `narrative_user_story/index.md` contains the `## The People in This Story` cast block (between the framing paragraph and the `## Chapters` list), that no chapter section duplicates the cast block, and that every named character in the cast is referenced by name at least once somewhere in the story.
5. Verify there is exactly one ASCII-diagram code block per section file.
6. Verify the parenthesised-title-before-name convention: every prose reference to a cast character — full name, bare first name, and bare surname — carries its Step 6 `(<Title>)` prefix. Grep for bare names (e.g., `\bMei\b`, `\bTung\b`, `\bWong\b`) and confirm the only remaining un-prefixed hits are inside fenced code blocks or inside the same character's own cast-block body paragraph (self-reference exception).

Fix any issues found.

## Step 11: Display Summary

Record step start time and compute total elapsed time (current ms minus the global start ms from Step 0).

Report:

```
User story generated for <project display name>.

  Source:    <URL or local folder>
  Language:  <English | Chinese (bilingual pair saved)>
  Location:  <folder>/narrative_user_story/
  Chapters:  <N>
  Sections:  <total section count>
  Cast size: <number of named characters>

Chapter list:
  Ch1 — <title> (<section count> sections)
  Ch2 — <title> (<section count> sections)
  ...

Open <folder>/narrative_user_story/index.md to read from the top.

--- Timing ---
Step 0  Classify Input       <Xs>
Step 1  Fetch Document       <Xs>
Step 2  Detect / Slug        <Xs>
Step 3  Create Folder        <Xs>
Step 4  Write Requirements   <Xs>
Step 5  Identify Features    <Xs>
Step 6  Design Cast          <Xs>
Step 7  Plan Chapters        <Xs>
Step 8  Write Index          <Xs>
Step 9  Write Sections       <Xs>
Step 10 Validate Links       <Xs>
Step 11 Display Summary      <Xs>
─────────────────────────────────
Total                        <Xs>
```

## Notes

- The output is documentation, not marketing copy. It stays faithful to the requirements' scope — no invented features.
- Do not duplicate content into `MEMORY.md` or any central index outside the `narrative_user_story/` folder.
- Do not write images or external assets; diagrams are ASCII only.
- Chapter folder names use `ch<N>_<snake_case_slug>`. Slugs may combine multiple feature names with underscores when features are merged (e.g., `ch5_worker_management_timesheet_payslip_and_mpf`).
- When the requirements define a domain-specific term (for example a platform name, a process name, or an appendix-style definition), use it verbatim throughout the narrative.
- Generate markdown only. No scripts, no binaries, no JSON. Use the Write tool directly per file.
- The `read_yjs_content.py` script requires the `y-py` and `websockets` Python packages. If they are missing, tell the user to install them (`pip install y-py websockets`) and stop.
