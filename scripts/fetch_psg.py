#!/usr/bin/env python3
"""Refresh the additional public PSG subscription feeds with ad filtering."""
import base64
import os
import re
import subprocess
import urllib.parse

FEEDS = {
    "reality": "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/reality.b64",
    "vmess": "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/vmess.b64",
    "xhttps": "https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/xhttp.b64",
    "mix": "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/mix.b64",
    "vless": "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/vless.b64",
    "ss_ipv4": "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/ss_ipv4.b64",
}
OUT = "configs/psg"

BLOCKED_PATTERNS = ["جاویدشاه", "kingrezapahlavi", "همکاریملی"]


def is_ad(line: str) -> bool:
    unquoted = urllib.parse.unquote(line).lower()
    norm = re.sub(r"[\s_\-\u200c\u200b\u0640]+", "", unquoted)
    return any(p in norm for p in BLOCKED_PATTERNS)


def fetch(url: str) -> bytes:
    return subprocess.run(
        ["curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "45", url],
        check=True, capture_output=True, timeout=50,
    ).stdout.strip()


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    for name, url in FEEDS.items():
        encoded = fetch(url)
        decoded = base64.b64decode(encoded).decode("utf-8", "replace")
        lines = [line.strip() for line in decoded.splitlines() if line.strip()]

        # Filter out political ads & comment-only directives
        clean_configs = []
        for line in lines:
            if line.startswith("#"):
                continue
            if "://" in line and not is_ad(line):
                clean_configs.append(line)

        if not clean_configs:
            raise RuntimeError(f"{name}: no configs left after filtering")

        clean_b64 = base64.b64encode("\n".join(clean_configs).encode("utf-8"))

        with open(f"{OUT}/{name}.b64", "wb") as f:
            f.write(clean_b64)
        with open(f"{OUT}/{name}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(clean_configs) + "\n")
        print(f"{name}: {len(clean_configs)} clean configs (from {len(lines)} raw lines)")

    # Remove the retired feed only after every replacement feed fetched cleanly.
    for suffix in (".b64", ".txt"):
        old_path = f"{OUT}/openai{suffix}"
        if os.path.exists(old_path):
            os.remove(old_path)


if __name__ == "__main__":
    main()
