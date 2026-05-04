"""Text-to-speech CLI via Gemini.

Usage:
    python tts.py --text "Hello world" [--voice Kore] [--output out.wav]

Reads GEMINI_API_KEY from the environment (loads ../../../../.env if present).
Writes a 24 kHz / 16-bit / mono WAV file.
"""

import argparse
import base64
import os
import sys
import wave
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

VOICE_NAMES = frozenset(
    {
        "Zephyr", "Puck", "Kore", "Leda", "Fenrir", "Aoede", "Enceladus",
        "Iapetus", "Achernar", "Sulafat", "Achird", "Schedar", "Sadaltager",
        "Gacrux", "Algieba", "Algenib", "Alnilam", "Autonoe", "Callirrhoe",
        "Charon", "Despina", "Erinome", "Laomedeia", "Orus", "Pulcherrima",
        "Rasalgethi", "Sadachbia", "Umbriel", "Vindemiatrix", "Zubenelgenubi",
    }
)
DEFAULT_VOICE = "Kore"
TTS_MODEL = "gemini-3.1-flash-tts-preview"
SAMPLE_RATE = 24_000
SAMPLE_WIDTH = 2
CHANNELS = 1

_BASE64_BYTES = frozenset(
    b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/-_="
)


def _coerce_pcm(raw: bytes) -> bytes:
    """google-genai sometimes returns inline_data.data as base64-ASCII text
    under uvicorn instead of raw bytes. Detect and decode defensively.
    """
    if not raw:
        return raw
    sample = raw[:256]
    if all(b in _BASE64_BYTES for b in sample):
        try:
            return base64.b64decode(raw, validate=False)
        except (ValueError, base64.binascii.Error):
            return raw
    return raw


def synthesize(text: str, voice: str, api_key: str) -> bytes:
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=TTS_MODEL,
        contents=text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name=voice,
                    ),
                ),
            ),
        ),
    )
    candidates = getattr(response, "candidates", None) or []
    if not candidates:
        raise RuntimeError("Gemini TTS returned no candidates")
    parts = candidates[0].content.parts or []
    if not parts or getattr(parts[0], "inline_data", None) is None:
        raise RuntimeError("Gemini TTS returned no inline_data audio part")
    raw = parts[0].inline_data.data
    if not raw:
        raise RuntimeError("Gemini TTS returned empty PCM")
    return _coerce_pcm(raw)


def write_wav(pcm: bytes, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(SAMPLE_WIDTH)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(pcm)


def project_root() -> Path:
    return Path(__file__).resolve().parents[4]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--text", required=True, help="Text to synthesize")
    ap.add_argument("--voice", default=DEFAULT_VOICE, help=f"Voice name (default: {DEFAULT_VOICE})")
    ap.add_argument(
        "--output",
        default=str(Path(__file__).resolve().parent / "out" / "tts.wav"),
        help="Output WAV path",
    )
    args = ap.parse_args()

    if args.voice not in VOICE_NAMES:
        print(f"unknown voice: {args.voice!r}", file=sys.stderr)
        print(f"valid voices: {', '.join(sorted(VOICE_NAMES))}", file=sys.stderr)
        return 2

    load_dotenv(dotenv_path=project_root() / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY not set in environment or .env", file=sys.stderr)
        return 2

    try:
        pcm = synthesize(args.text, args.voice, api_key)
    except Exception as exc:  # pylint: disable=broad-except
        print(f"TTS FAIL: {exc.__class__.__name__}: {exc}", file=sys.stderr)
        return 1

    out = Path(args.output).resolve()
    write_wav(pcm, out)
    print(f"OK: wrote {out} ({out.stat().st_size} bytes, voice={args.voice})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
