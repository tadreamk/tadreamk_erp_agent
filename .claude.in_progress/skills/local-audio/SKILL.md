---
name: local-audio
description: Generate a Gemini text-to-speech audio file for each narrative-style
  .md file in a directory tree, and attach a Listen link at the top of every file.
  Strips ASCII diagrams, navigation, and separators before synthesis — only
  paragraph prose is spoken. Use when user says "generate story audio",
  "text to speech for stories", "tts for markdown", "attach audio to stories",
  or "local-audio".
model: claude-sonnet-4-6
---

# Local Audio — Narrative .md to WAV

Walks a directory of narrative `.md` files, sends each file's paragraph text to the Gemini TTS model, writes one WAV per file under a sibling `audio/` folder, and inserts a `🎧 [Listen](./audio/<file>.wav)` line right after the H1 title of every file.

## Input

The skill argument is a **directory path** (absolute or relative to the project root) containing the `.md` files to narrate. Typical shape:

```
data/customer_requirements/<project>/narrative_user_story/
  index.md                                # skipped automatically
  ch1_<slug>/01_<section>.md
  ch1_<slug>/02_<section>.md
  ch2_<slug>/...
```

If no argument is given, ask the user for the directory before proceeding.

## Output

Per source file `chN_<slug>/<file>.md`:

- `chN_<slug>/audio/<file>.wav` — 24 kHz / 16-bit / mono WAV spoken by Gemini.
- A new line inserted in `<file>.md` right after the H1 title:
  ```
  🎧 [Listen](./audio/<file>.wav)
  ```

`index.md` files are skipped by design. Files that already have a WAV are skipped unless `--force` is passed.

## Prerequisites

- `GEMINI_API_KEY` must be set in `.env` at the project root, or exported in the environment.
- Python 3.11+ with `google-genai` and `python-dotenv` available on the system Python (`python3 -c "from google import genai; from dotenv import load_dotenv"` must succeed).

If the key is missing, stop and ask the user to add it to `.env` before running.

## What Gets Spoken vs. Skipped

The script's text extractor keeps only prose suitable for narration:

- **Kept** — H1/H2/H3 headings (hash markers stripped), narrative paragraphs, blockquoted prose.
- **Skipped** — fenced code blocks (so ASCII diagrams are never read aloud), navigation lines containing `↑`/`←`/`→`, horizontal-rule `---` separators, and the closing `*All characters in this story are fictional…*` footer.
- **Inlined** — markdown links `[text](url)` become `text`; `**bold**` and `*italic*` markers are dropped.

## Step 1: Confirm Target Directory

Verify the argument resolves to a directory that contains at least one `.md` file other than `index.md`. If not, report the problem and stop.

## Step 2: Run the Generator

Invoke the Python generator. The script is idempotent (re-running skips files that already have audio):

```bash
python3 .claude/skills/local-audio/scripts/generate_story_audio.py \
  --root <directory> \
  [--voice Kore] \
  [--force]
```

Flags:

- `--voice` — prebuilt Gemini voice name. Default `Kore`. Valid names are listed in `scripts/tts.py` (`VOICE_NAMES`).
- `--force` — regenerate audio even if the target WAV already exists.

The script:

1. Loads `GEMINI_API_KEY` from the project-root `.env` (via `python-dotenv`).
2. Walks the tree for `*.md` files (skipping `index.md`).
3. For each file, extracts speech text, calls Gemini `generate_content` with `response_modalities=["AUDIO"]` and a `PrebuiltVoiceConfig`, wraps the returned 24 kHz PCM in a WAV header, and writes it to `audio/<file>.wav`.
4. Edits the `.md` to insert/replace the `🎧 [Listen]` line directly after the H1 title.

## Step 3: Handle Transient Failures

The generator already retries each file up to 3 times with 2 s → 5 s backoff on `RemoteProtocolError` or other Gemini-side disconnects. If all retries fail, it splits the text on paragraph boundaries into ~1800-char chunks, synthesizes each chunk separately, and concatenates the raw PCM before WAV-wrapping (all chunks share format, so concatenation is byte-safe).

If a file still fails after chunking, the script prints a `FAIL` line and exits with code 1. Re-run the same command — already-generated files are skipped and only the remaining failure is retried.

## Step 4: Verify

After the generator reports `Done: X generated, Y skipped, Z failed`:

1. Confirm every non-`index.md` file has a corresponding `audio/<file>.wav`:
   ```bash
   find <directory> -name "*.md" ! -name "index.md" | wc -l
   find <directory> -name "*.wav" | wc -l
   ```
   The two counts must match.
2. Spot-check that a `🎧 [Listen](./audio/...)` line appears after the H1 of each file.
3. Report total audio size per chapter with `du -sh <directory>/*/audio`.

## Step 5: Display Summary

Report:

```
Audio generated for <directory>.

  Files processed: <N>
  Audio written:   <M> WAV files
  Voice:           <voice_name>
  Total size:      <human-readable>
  Skipped:         <index.md + already-present audio>
  Failed:          <count, if any>
```

## Notes

- **Why `audio/` subfolder per chapter** — keeps WAVs out of the chapter's top level so the story's `.md` files stay the visible surface; the Listen link uses a relative `./audio/...` path so markdown viewers resolve it correctly.
- **Why `index.md` is skipped** — indexes are navigation, not narrative. Hand-author an audio introduction separately if one is needed.
- **Why PCM → WAV wrapping** — Gemini returns raw 24 kHz / 16-bit / mono L16 PCM on `response.candidates[0].content.parts[0].inline_data.data`. Browsers and most players cannot play raw PCM, so the script prepends a RIFF/fmt/data header (adds ~44 bytes).
- **Character pronunciation** — Gemini speaks parenthesised titles literally (`"(Program Director) Audrey"` becomes "open parenthesis Program Director close parenthesis Audrey"). This is intentional for these narrative files since the titles carry role context; strip them upstream only if producing a non-narrated variant.
- **Regenerating** — delete the target `.wav` (or pass `--force`) to regenerate a specific file. The `🎧 [Listen]` line is overwritten in place, not duplicated.
- **Model & voice** — the call uses `gemini-3.1-flash-tts-preview` with a `PrebuiltVoiceConfig`; change `TTS_MODEL` in `scripts/tts.py` to switch models.
