#!/usr/bin/env python3
"""Refresh the additional public PSG subscription feeds."""
import base64
import os
import subprocess

BASE = "https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/"
FEEDS = ("openai", "reality", "mix", "vless", "ss_ipv4")
OUT = "configs/psg"


def fetch(url: str) -> bytes:
    # curl uses the system CA store consistently and still verifies TLS.
    return subprocess.run(
        ["curl", "--fail", "--silent", "--show-error", "--location", "--max-time", "45", url],
        check=True, capture_output=True, timeout=50,
    ).stdout.strip()


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    for name in FEEDS:
        encoded = fetch(f"{BASE}{name}.b64")
        decoded = base64.b64decode(encoded, validate=True).decode("utf-8")
        lines = [line.strip() for line in decoded.splitlines() if line.strip()]
        configs = [line for line in lines if not line.startswith("#")]
        if not configs or any("://" not in line for line in configs):
            raise RuntimeError(f"{name}: feed is empty or contains invalid config lines")
        if not all(line.split("://", 1)[0].replace("+", "").replace("-", "").isalnum() for line in configs):
            raise RuntimeError(f"{name}: malformed protocol URI")

        with open(f"{OUT}/{name}.b64", "wb") as f:
            f.write(encoded)
        with open(f"{OUT}/{name}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"{name}: {len(lines)} lines")


if __name__ == "__main__":
    main()
