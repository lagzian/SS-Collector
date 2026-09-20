#!/usr/bin/env python3
"""Publish: configs/{country}/{protocol}.txt + .b64, per-country & per-protocol
subscriptions (base64), mixed/ protocol files, subscription-all,
test_report.json, and a beautiful auto-generated README with country flags.
"""
import base64
import datetime
import json
import os
import re

def flag(code: str) -> str:
    """ISO-3166-1 alpha-2 → flag emoji. A=0x1F1E6, B=0x1F1E7, …"""
    c = code.upper()
    if len(c) == 2 and c.isalpha():
        return chr(0x1F1E6 + ord(c[0]) - 65) + chr(0x1F1E6 + ord(c[1]) - 65)
    return c


PROTOS = ["vless", "vmess", "ss", "trojan", "hy2", "hysteria", "outline"]
RAW = "https://raw.githubusercontent.com/lagzian/SS-Collector/main"


def proto_of(line: str) -> str:
    m = re.match(r"^([a-z0-9]+)://", line, re.I)
    p = m.group(1).lower() if m else "unknown"
    return "hy2" if p in ("hysteria", "hy2") else p


def b64encode(lines: list[str]) -> str:
    return base64.b64encode("\n".join(lines).encode()).decode()


def main() -> None:
    with open("scraped.json") as f:
        data = json.load(f)
    with open("tested.json") as f:
        tested = json.load(f)
    alive = tested["alive"]

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # ---- build per-country / per-protocol maps ----
    by_code: dict[str, dict[str, list[str]]] = {}
    for code, v in data.items():
        for line in v["configs"]:
            if not alive.get(line, (False,))[0]:
                continue
            by_code.setdefault(code, {}).setdefault(proto_of(line), [])
            if line not in by_code[code][proto_of(line)]:
                by_code[code][proto_of(line)].append(line)

    # ---- write files ----
    for code, protos in by_code.items():
        for p, lines in protos.items():
            os.makedirs(f"configs/{code}", exist_ok=True)
            with open(f"configs/{code}/{p}.txt", "w") as fh:
                fh.write("\n".join(lines) + "\n")
            with open(f"configs/{code}/{p}.b64", "w") as fh:
                fh.write(b64encode(lines))
        all_c = [l for p in PROTOS for l in by_code[code].get(p, [])]
        if all_c:
            with open(f"configs/{code}/all.b64", "w") as fh:
                fh.write(b64encode(all_c))

    # mixed per-protocol
    mixed = {p: [] for p in PROTOS}
    for code in by_code:
        for p, lines in by_code[code].items():
            for l in lines:
                if l not in mixed[p]:
                    mixed[p].append(l)
    for p, lines in mixed.items():
        if lines:
            os.makedirs("configs/mixed", exist_ok=True)
            with open(f"configs/mixed/{p}.txt", "w") as fh:
                fh.write("\n".join(lines) + "\n")
            with open(f"configs/mixed/{p}.b64", "w") as fh:
                fh.write(b64encode(lines))

    # global all
    all_lines = [l for p in PROTOS for l in mixed[p]]
    os.makedirs("configs", exist_ok=True)
    with open("configs/subscription-all.txt", "w") as fh:
        fh.write(b64encode(all_lines))
    with open("configs/subscription-all.b64", "w") as fh:
        fh.write(b64encode(all_lines))

    # ---- test report ----
    counts = {code: sum(len(v) for v in p.values()) for code, p in by_code.items()}
    with open("test_report.json", "w") as fh:
        json.dump(
            {
                "generated_at": ts,
                "total_scraped": tested.get("total", 0),
                "alive": len(all_lines),
                "per_country": counts,
                "per_country_proto": {c: p for c, p in by_code.items()},
            },
            fh, indent=2,
        )

    # ---- README ----
    total = len(all_lines)
    rows = []
    for code in sorted(by_code.keys()):
        protos = by_code[code]
        cnt = sum(len(v) for v in protos.values())
        proto_cell = "  ".join(
            f'<a href="{RAW}/configs/{code}/{p}.b64">{p}×{len(v)}</a>'
            for p, v in sorted(protos.items())
        )
        rows.append(
            f'| {flag(code)} **{code.upper()}** | {cnt} | {proto_cell} | '
            f'[🔗]({RAW}/configs/{code}/all.b64) |'
        )

    protocol_bars = "\n".join(
        f'| 🌐 **{p.upper()}** | {len(mixed[p])} | '
        f'[subscribe]({RAW}/configs/mixed/{p}.b64) |'
        for p in PROTOS if mixed[p]
    )

    country_table = "\n".join(rows)

    readme = f"""<div align="center">

<img src="{RAW}/.github/banner.svg" alt="SS-Collector" width="100%"/>

# 🚀 SS-Collector

### Fresh V2Ray/Xray configs — scraped, tested & published automatically

[![GitHub Stars](https://img.shields.io/github/stars/lagzian/SS-Collector?style=for-the-badge&logo=github&color=yellow)](https://github.com/lagzian/SS-Collector/stargazers)
[![Views](https://hits.sh/github.com/lagzian/SS-Collector.svg?style=for-the-badge&label=Views&color=orange)](https://github.com/lagzian/SS-Collector)
[![Last Update](https://img.shields.io/badge/last-update-{ts.replace(' ', '%20').replace(':', '%3A')}?style=for-the-badge&color=blue)](https://github.com/lagzian/SS-Collector/commits/main)
[![Configs](https://img.shields.io/badge/configs-{total}?style=for-the-badge&color=green)](configs/)
[![License](https://img.shields.io/badge/license-MIT?style=for-the-badge&color=green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@lagzian-blue?style=for-the-badge&logo=telegram)](https://t.me/lagzian)

> 🔍 **{total} working configs** across {len(by_code)} countries • auto-tested every 2h • dead configs dropped

</div>

---

## 📥 Quick Subscribe

<details open>
<summary><b>🔗 All protocols, all countries (one link)</b></summary>

```
{RAW}/configs/subscription-all.b64
```
</details>

---

## 🌐 By protocol

| Protocol | Working | Subscribe |
|:--------:|:-------:|:---------:|
{protocol_bars}

---

## 🌍 By country

| Country | Working | Protocols | Subscribe |
|:-------:|:-------:|:----------|:---------:|
{country_table}

---

## 📂 Browse raw configs

`configs/{{country}}/{{protocol}}.b64` — e.g. `configs/sg/vless.b64`

---

⚠️ Educational use only. No warranty. Use at your own risk.

*Generated {ts} by GitHub Actions.*
"""
    with open("README.md", "w") as fh:
        fh.write(readme)
    print(f"published {total} configs, {len(by_code)} countries")


if __name__ == "__main__":
    main()
