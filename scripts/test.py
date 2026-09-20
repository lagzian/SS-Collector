#!/usr/bin/env python3
"""TCP-reachability test (assumption a): drop configs whose host can't connect.
Ponytail: TCP connect only — enough for public VPN servers; upgrade to
v2ray-core protocol handshake if TCP reachability proves too permissive.
"""
import concurrent.futures
import json
import re
import socket
import sys
import time

TIMEOUT_S = 8
MAX_LATENCY_MS = 3000  # >3s = dead-ish


def host_port(line: str):
    m = re.match(r"^(?:([a-z0-9]+)://)?(?:[^@]+@)?([^:/?#]+):(\d+)", line, re.I)
    if not m:
        return None
    proto, host, port = m.group(1).lower(), m.group(2), int(m.group(3))
    return proto, host, port


def check(line: str) -> tuple[str, bool, float, str]:
    hp = host_port(line)
    if not hp:
        return line, False, 0.0, "unparseable"
    proto, host, port = hp
    t0 = time.time()
    try:
        with socket.create_connection((host, port), timeout=TIMEOUT_S) as s:
            lat = (time.time() - t0) * 1000
            if lat > MAX_LATENCY_MS:
                return line, False, lat, f"slow {lat:.0f}ms"
            return line, True, lat, "ok"
    except OSError as e:
        return line, False, (time.time() - t0) * 1000, str(e)[:80]


def main() -> int:
    with open("scraped.json") as f:
        data = json.load(f)
    lines = [l for v in data.values() for l in v["configs"]]
    seen: dict[str, tuple[bool, float, str]] = {}
    uniq = list(dict.fromkeys(lines))
    with concurrent.futures.ThreadPoolExecutor(max_workers=128) as ex:
        for r in ex.map(check, uniq):
            seen[r[0]] = (r[1], r[2], r[3])
    alive = {l: m for l, m in seen.items() if m[0]}
    with open("tested.json", "w") as f:
        json.dump({"alive": alive, "total": len(uniq)}, f)
    print(f"alive {len(alive)}/{len(uniq)}")
    return 0 if alive else 1


if __name__ == "__main__":
    sys.exit(main())
