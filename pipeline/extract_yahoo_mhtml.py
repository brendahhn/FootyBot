#!/usr/bin/env python3
"""Extract readable text + title-attribute values (for truncated names) from a
saved Yahoo Fantasy MHTML page. Stdlib only."""
import quopri
import re
import sys
from pathlib import Path


def extract(path: Path) -> tuple[str, list[str]]:
    raw = path.read_bytes()
    # isolate the first text/html MIME part (up to the next boundary line)
    text = raw.decode("utf-8", errors="replace")
    m = re.search(r'boundary="([^"]+)"', text)
    boundary = m.group(1) if m else None
    if boundary:
        parts = text.split("--" + boundary)
        html_part = next(p for p in parts if "Content-Type: text/html" in p)
    else:
        html_part = text
    # strip MIME headers of that part (blank line separates headers from body)
    body = html_part.split("\n\n", 1)[-1]
    decoded = quopri.decodestring(body.encode("utf-8", errors="replace"))
    html = decoded.decode("utf-8", errors="replace")

    titles = re.findall(r'title="([^"]*)"', html)

    html_no_script = re.sub(r"<script.*?</script>", " ", html, flags=re.DOTALL)
    html_no_script = re.sub(r"<style.*?</style>", " ", html_no_script, flags=re.DOTALL)
    plain = re.sub(r"<[^>]+>", "\n", html_no_script)
    plain = plain.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#39;", "'")
    lines = [l.strip() for l in plain.split("\n") if l.strip()]
    return "\n".join(lines), titles


if __name__ == "__main__":
    src = Path(sys.argv[1])
    text, titles = extract(src)
    out = src.with_suffix(".txt")
    out.write_text(text)
    titles_out = src.with_name(src.stem + "_titles.txt")
    titles_out.write_text("\n".join(titles))
    print(f"wrote {out} ({len(text)} chars), {titles_out} ({len(titles)} titles)")
