"""Generate a TTS audio file for each narrative user-story .md file.

Walks a directory of .md files, extracts only paragraph text (skipping code
blocks / ASCII diagrams, navigation links, and separators), sends it to the
Gemini TTS model, writes a WAV alongside the .md, and inserts an audio link
into the .md right after the H1 title.

Usage:
    python generate_story_audio.py \
        --root data/customer_requirements/260422_butterfly_plan/narrative_user_story \
        [--voice Kore] [--force]

Reads GEMINI_API_KEY from the project-root .env or the environment.
"""

import argparse
import os
import re
import sys
import time
from pathlib import Path

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tts import DEFAULT_VOICE, VOICE_NAMES, synthesize, write_wav  # noqa: E402

RETRY_ATTEMPTS = 3
RETRY_BACKOFF_SECONDS = (2, 5)
CHUNK_TARGET_CHARS = 1800


def _try_once(text: str, voice: str, api_key: str, label: str) -> bytes:
    last_exc: Exception | None = None
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            return synthesize(text, voice, api_key)
        except Exception as exc:  # pylint: disable=broad-except
            last_exc = exc
            if attempt < RETRY_ATTEMPTS:
                wait = RETRY_BACKOFF_SECONDS[attempt - 1]
                print(
                    f"  retry {attempt}/{RETRY_ATTEMPTS - 1} for {label} in {wait}s: "
                    f"{exc.__class__.__name__}: {exc}"
                )
                time.sleep(wait)
    assert last_exc is not None
    raise last_exc


def _chunk_paragraphs(text: str, target: int = CHUNK_TARGET_CHARS) -> list[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for p in paras:
        added = len(p) + (2 if cur else 0)
        if cur and cur_len + added > target:
            chunks.append("\n\n".join(cur))
            cur = [p]
            cur_len = len(p)
        else:
            cur.append(p)
            cur_len += added
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def synthesize_with_retry(text: str, voice: str, api_key: str, label: str) -> bytes:
    try:
        return _try_once(text, voice, api_key, label)
    except Exception as exc:  # pylint: disable=broad-except
        chunks = _chunk_paragraphs(text)
        if len(chunks) < 2:
            raise
        print(
            f"  splitting {label} into {len(chunks)} chunks after failure: "
            f"{exc.__class__.__name__}"
        )
        pcm_parts: list[bytes] = []
        for i, chunk in enumerate(chunks, 1):
            sub_label = f"{label}[chunk {i}/{len(chunks)}, {len(chunk)} chars]"
            pcm_parts.append(_try_once(chunk, voice, api_key, sub_label))
        return b"".join(pcm_parts)

CODE_FENCE_RE = re.compile(r"^```")
NAV_CHAR_RE = re.compile(r"[↑←→]")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
BLOCKQUOTE_RE = re.compile(r"^>\s?")
HR_RE = re.compile(r"^-{3,}$")
AUDIO_LINE_RE = re.compile(r"^🎧\s*\[")


def extract_speech_text(md: str) -> str:
    """Strip diagrams, nav links, separators, and markdown syntax from an .md."""
    lines = md.splitlines()
    out: list[str] = []
    in_code = False
    for raw in lines:
        line = raw.rstrip()
        if CODE_FENCE_RE.match(line):
            in_code = not in_code
            continue
        if in_code:
            continue
        stripped = line.strip()
        if not stripped:
            if out and out[-1] != "":
                out.append("")
            continue
        if HR_RE.match(stripped):
            continue
        if stripped.startswith("[") and NAV_CHAR_RE.search(stripped):
            continue
        if AUDIO_LINE_RE.match(stripped):
            continue
        if stripped.startswith("*") and stripped.endswith("*") and "All characters" in stripped:
            continue
        m = HEADING_RE.match(stripped)
        if m:
            stripped = m.group(2).strip()
        stripped = BLOCKQUOTE_RE.sub("", stripped)
        stripped = MD_LINK_RE.sub(r"\1", stripped)
        stripped = BOLD_RE.sub(r"\1", stripped)
        stripped = ITALIC_RE.sub(r"\1", stripped)
        out.append(stripped)
    text = "\n".join(out).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def insert_audio_link(md: str, audio_rel_path: str) -> str:
    """Insert an audio link line right after the first H1, replacing any prior one."""
    lines = md.splitlines()
    new_link = f"🎧 [Listen]({audio_rel_path})"
    h1_idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1_idx is None:
        return md
    result = lines[: h1_idx + 1]
    cursor = h1_idx + 1
    while cursor < len(lines) and not lines[cursor].strip():
        result.append(lines[cursor])
        cursor += 1
    if cursor < len(lines) and AUDIO_LINE_RE.match(lines[cursor].strip()):
        lines[cursor] = new_link
    else:
        result.append(new_link)
        result.append("")
    result.extend(lines[cursor:])
    return "\n".join(result) + ("\n" if md.endswith("\n") else "")


def find_story_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.name != "index.md")


def project_root() -> Path:
    return Path(__file__).resolve().parents[4]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--root",
        required=True,
        help="Directory to walk for story .md files",
    )
    ap.add_argument("--voice", default=DEFAULT_VOICE)
    ap.add_argument("--force", action="store_true", help="Regenerate existing audio files")
    args = ap.parse_args()

    if args.voice not in VOICE_NAMES:
        print(f"unknown voice: {args.voice!r}", file=sys.stderr)
        return 2

    load_dotenv(dotenv_path=project_root() / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set in environment or project .env", file=sys.stderr)
        return 2

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        return 2

    files = find_story_files(root)
    if not files:
        print(f"no .md files found under {root}", file=sys.stderr)
        return 1

    print(f"Found {len(files)} story files under {root}")
    generated = 0
    skipped = 0
    failed = 0

    for md_path in files:
        rel = md_path.relative_to(root)
        audio_dir = md_path.parent / "audio"
        audio_path = audio_dir / f"{md_path.stem}.wav"
        audio_rel = f"./audio/{audio_path.name}"

        if audio_path.exists() and not args.force:
            print(f"  skip  {rel}  (audio exists: {audio_rel})")
            skipped += 1
            continue

        md_text = md_path.read_text(encoding="utf-8")
        speech = extract_speech_text(md_text)
        if not speech:
            print(f"  warn  {rel}  (no speech text extracted)")
            failed += 1
            continue

        print(f"  tts   {rel}  ({len(speech)} chars)")
        try:
            pcm = synthesize_with_retry(speech, args.voice, api_key, str(rel))
        except Exception as exc:  # pylint: disable=broad-except
            print(f"  FAIL  {rel}: {exc.__class__.__name__}: {exc}", file=sys.stderr)
            failed += 1
            continue

        write_wav(pcm, audio_path)
        updated = insert_audio_link(md_text, audio_rel)
        if updated != md_text:
            md_path.write_text(updated, encoding="utf-8")
        print(f"  ok    {rel} -> {audio_path.name} ({audio_path.stat().st_size} bytes)")
        generated += 1

    print(f"\nDone: {generated} generated, {skipped} skipped, {failed} failed")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
