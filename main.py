"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry text to <output>/entry.txt.
"""
import os

TEXT = "WARNING: Contents may claim to be five minutes away while still in bed, still in the shower, and still three hours away by car."


def validated_text(text: str) -> str:
    """Enforce the competition gate: UTF-8, 1-160 chars, one line, not blank."""
    text.encode("utf-8")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry must be 1-160 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    text = validated_text(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Re-read the file and prove the bytes are exactly what was validated.
    with open(path, "rb") as f:
        if f.read() != data:
            raise RuntimeError("entry.txt bytes differ from validated text")


if __name__ == "__main__":
    main()
