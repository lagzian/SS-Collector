#!/usr/bin/env python3
"""Write configs/{country}/{protocol}.txt, mixed/, subscription (base64), test_report.json, README.md."""
import base64
import datetime
import json
import os
import re

PROTOS = ["vless", "vmess", "ss", "trojan", "hy2", "hysteria", "outline"]


def proto_of(line: str) -> str:
    m = re.match(r"^([a-z0-9]+)://", line, re.I)
    p = (m.group(1).lower() if m else "unknown")
    return "hy2" if p in ("hysteria", "hy2") else ("outline" if p in ("outline",) else p)


def main() -> None:
    with open("scraped.json") as f:
        data = json.load(f)
    with open("tested.json") as f:
        tested = json.load(f)
    alive = tested["alive"]  # line -> (ok, latency_ms, note)

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # per-country / per-protocol
    country_proto_counts: dict[str, dict[str, int]] = {}
    for code, v in data.items():
        for line in v["configs"]:
            p = proto_of(line)
            if not alive.get(line, (False,))[0]:
                continue
            os.makedirs(f"configs/{code}", exist_ok=True)
            path = f"configs/{code}/{p}.txt"
            with open(path, "a") as fh:
                fh.write(line + "\n")
            country_proto_counts.setdefault(code, {}).setdefault(p, 0)
            country_proto_counts[code][p] += 1

    # ---- mixed per-protocol (all countries) ----
    mixed = {p: [] for p in PROTOS}
    for code, v in data.items():
        for line in v["configs"]:
            if not alive.get(line, (False,))[0]:
                continue
            mixed[proto_of(line)].append(line)
    for p, lines in mixed.items():
        if lines:
            os.makedirs("configs/mixed", exist_ok=True)
            with open(f"configs/mixed/{p}.txt", "w") as fh:
                fh.write("\n".join(dict.fromkeys(lines)) + "\n")

    # ---- subscription base64 (all protocols, all countries, deduped) ----
    all_lines: list[str] = []
    for p, lines in mixed.items():
        all_lines.extend(dict.fromkeys(lines))
    os.makedirs("configs", exist_ok=True)
    with open("configs/subscription-all.txt", "w") as fh:
        fh.write(base64.b64encode("\n".join(all_lines).encode()).decode())
    with open("configs/subscription-all.b64", "w") as fh:
        fh.write(base64.b64encode("\n".join(all_lines).encode()).decode())

    # ---- test report (transparency) ----
    with open("test_report.json", "w") as fh:
        json.dump(
            {
                "generated_at": ts,
                "total_scraped": tested.get("total", 0),
                "alive": len(alive),
                "alive_lines": alive,
                "per_country": country_proto_counts,
            },
            fh, indent=2,
        )

    # ---- README ----
    total_alive = len(all_lines)
    rows = []
    for code in sorted(data.keys()):
        pc = country_proto_counts.get(code, {})
        if not pc:
            continue
        proto_cell = " ".join(f"{p}×{n}" for p, n in sorted(pc.items()))
        link = (
            "https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/"
            + "/".join([code, sorted(pc.keys())[0]])
            + ".txt"
        ) if len(pc) == 1 else (
            "https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/mixed/"
            + sorted(pc.keys())[0] + ".txt"
        )
        rows.append((code, sum(pc.values()), proto_cell, link))

    badges = "\n".join(
        f"| `{c.upper()}` | {tot} | {pc} | [subscribe]({link}) |"
        for c, tot, pc, link in rows
    )
    readme = f"""<div align="center">

<img src="https://raw.githubusercontent.com/lagzian/SS-Collector/main/.github/banner.svg" alt="SS-Collector" width="100%"/>

# 🚀 SS-Collector

### Fresh V2Ray/Xray configs — scraped, tested & published automatically

[![GitHub Stars](https://img.shields.io/github/stars/lagzian/SS-Collector?style=for-the-badge&logo=github&color=yellow)](https://github.com/lagzian/SS-Collector/stargazers)
[![Views](https://hits.sh/github.com/lagzian/SS-Collector.svg?style=for-the-badge&label=Views&color=orange)](https://github.com/lagzian/SS-Collector)
[![Last Update](https://img.shields.io/badge/last-update-{ts.replace(' ', '%20').replace(':', '%3A')}?style=for-the-badge&color=blue)](https://github.com/lagzian/SS-Collector/commits/main)
[![Configs](https://img.shields.io/badge/configs-{total_alive}?style=for-the-badge&color=green)](configs/)
[![License](https://img.shields.io/badge/license-MIT?style=for-the-badge&color=green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@lagzian-blue?style=for-the-badge&logo=telegram)](https://t.me/lagzian)

> 🔍 **{total_alive} working configs** across {len(rows)} countries • auto-tested every 2h • dead configs dropped

</div>

---

## 📥 Subscription (all protocols, all countries)

```
https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/subscription-all.txt
```
<sub>📋 paste into V2RayNG / Shadowrocket / V2RayN</sub>

---

## 🌍 By country & protocol

| Country | Working | Protocols | Subscribe |
|:-------:|:-------:|:----------|:---------:|
{badges}

---

## 📂 Browse raw configs

`configs/{{country}}/{{protocol}}.txt` — e.g. `configs/sg/vless.txt`

---

⚠️ Educational use only. No warranty. Use at your own risk.

*Generated {ts} by GitHub Actions.*
"""
    with open("README.md", "w") as fh:
        fh.write(readme)
    print(f"published {total_alive} configs, {len(rows)} countries")


if __name__ == "__main__":
    main()
