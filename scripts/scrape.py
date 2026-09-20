#!/usr/bin/env python3
"""Fetch current v2nodes subscription links (keys rotate — scrape fresh every run)."""
import json
import re
import subprocess
import sys

BASE = "https://v2nodes.com"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def curl(url: str) -> str:
    r = subprocess.run(
        ["curl", "-sL", url, "-H", f"User-Agent: {UA}"],
        capture_output=True, text=True, timeout=60,
    )
    if r.returncode != 0:
        raise RuntimeError(f"curl {url} -> {r.returncode}: {r.stderr[:200]}")
    return r.stdout


def country_codes() -> list[str]:
    html = curl(f"{BASE}/")
    # nav links like /country/sg/
    codes = sorted(set(re.findall(r'href="/country/([a-z]{2})/"', html)))
    if not codes:
        raise RuntimeError("no country links found on v2nodes.com home")
    return codes


def subscription_url(code: str) -> str:
    """Scrape the current data-config (key rotates) for a country."""
    html = curl(f"{BASE}/country/{code}/")
    m = re.search(r'id="subscription"[^>]*data-config="([^"]+)"', html)
    if not m:
        # fallback: any data-config
        m = re.search(r'data-config="([^"]+)"', html)
    if not m:
        raise RuntimeError(f"no subscription data-config for /country/{code}/")
    return m.group(1)


def fetch_configs(url: str) -> list[str]:
    """Return list of raw config lines (decoded)."""
    import base64
    b64 = curl(url)
    b64 = b64.strip()
    try:
        raw = base64.b64decode(b64).decode("utf-8", "replace")
    except Exception:
        raw = b64  # maybe not base64
    return [l.strip() for l in raw.splitlines() if l.strip()]


def main() -> int:
    out: dict = {}
    try:
        codes = country_codes()
    except Exception as e:
        print(f"FATAL: {e}", file=sys.stderr)
        return 1
    for code in codes:
        try:
            url = subscription_url(code)
            lines = fetch_configs(url)
        except Exception as e:
            print(f"  ! {code}: {e}", file=sys.stderr)
            continue
        if not lines:
            continue
        out[code] = {"url": url, "configs": lines}
        print(f"  {code}: {len(lines)}")
    with open("scraped.json", "w") as f:
        json.dump(out, f)
    print(f"OK {len(out)}/{len(codes)} countries, {sum(len(v['configs']) for v in out.values())} configs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
