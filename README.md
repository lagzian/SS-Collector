<div align="center">

<img src="https://raw.githubusercontent.com/lagzian/SS-Collector/main/.github/banner.svg" alt="SS-Collector" width="100%"/>

# 🚀 SS-Collector

### Fresh V2Ray/Xray configs — scraped, tested & published automatically

[![GitHub Stars](https://img.shields.io/github/stars/lagzian/SS-Collector?style=for-the-badge&logo=github&color=yellow)](https://github.com/lagzian/SS-Collector/stargazers)
[![Last Update](https://img.shields.io/github/last-commit/lagzian/SS-Collector?style=for-the-badge&color=blue&label=Updated)](https://github.com/lagzian/SS-Collector/commits/main)
[![Configs](https://img.shields.io/badge/configs-285?style=for-the-badge&color=green)](configs/)
[![License](https://img.shields.io/badge/license-MIT?style=for-the-badge&color=green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-@lagzian-blue?style=for-the-badge&logo=telegram)](https://t.me/lagzian)

> 🔍 **285 working configs** across 41 countries • auto-tested every 2h • dead configs dropped

</div>

---

## 📖 What is SS-Collector?

**SS-Collector** automatically scrapes, tests, and publishes working V2Ray/Xray proxy configurations from public sources. Updated every 2 hours via GitHub Actions.

### 🎯 Key Features

- **Country-specific IPs** — need a Japanese IP? Subscribe to `configs/jp/vless.b64`. Need multiple countries? Chain them.
- **Protocol-sorted** — separate subscriptions for VLESS, Shadowsocks, Trojan
- **Auto-tested** — TCP reachability check every run; dead configs dropped instantly
- **Zero setup** — paste the subscription link, that's it

### 🔒 Security & Privacy

- **Public configs only** — no private servers, no authentication harvesting
- **Open source** — audit the scraper yourself ([scripts/](scripts/))
- **No logs, no tracking** — GitHub hosts the files; we don't see who subscribes
- **Educational purpose** — test your client, understand proxy protocols, learn automation

> ⚠️ **Legal Notice:** Respect local laws. SS-Collector provides tools, not legal advice. Use at your own risk.

---

## 🚀 Quick Start

### 1️⃣ Choose your subscription

| Need | Link |
|------|------|
| 🌍 **All countries** | `https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/subscription-all.b64` |
| 🇯🇵 **Japan only** | `https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/jp/all.b64` |
| 🇺🇸 **US only** | `https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/us/all.b64` |
| 🌐 **VLESS only (all countries)** | `https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/mixed/vless.b64` |

### 2️⃣ Add to your client

<details>
<summary><b>V2RayNG (Android)</b></summary>

1. Open V2RayNG
2. Tap `+` → **Import config from clipboard** or **Subscription**
3. Paste the link above
4. Tap **Update subscription**
5. Select a server → Connect
</details>

<details>
<summary><b>V2RayN (Windows)</b></summary>

1. Open V2RayN
2. **Subscription** → **Subscription settings**
3. Add subscription URL
4. **Update subscription**
5. Right-click a server → **Set as active server**
</details>

<details>
<summary><b>Shadowrocket (iOS)</b></summary>

1. Open Shadowrocket
2. Tap `+` → **Type: Subscribe**
3. Paste URL → **Save**
4. Swipe left on the subscription → **Update**
5. Tap a config → Connect
</details>

### 3️⃣ Advanced: Chain for specific country IPs

Need a Japanese IP but your current VPN doesn't have Japan servers?

1. **Add your main VPN** to your client (e.g., WireGuard, Outline)
2. **Import Japan configs** from `configs/jp/all.b64`
3. **Connect to your main VPN first**, then connect to a Japan config from SS-Collector
4. Your traffic: `You → Main VPN → Japan SS-Collector node → Internet`

Result: websites see a Japanese IP, even if your main VPN doesn't offer Japan.

---

## 📥 Quick Subscribe

<details open>
<summary><b>🔗 All protocols, all countries (one link)</b></summary>

```
https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/subscription-all.b64
```
</details>

---

## 🌐 By protocol

| Protocol | Working | Subscribe |
|:--------:|:-------:|:---------:|
| 🌐 **VLESS** | 230 | [subscribe](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/mixed/vless.b64) |
| 🌐 **SS** | 38 | [subscribe](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/mixed/ss.b64) |
| 🌐 **TROJAN** | 17 | [subscribe](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/mixed/trojan.b64) |

---

## 🌍 By country

| Country | Working | Protocols | Subscribe |
|:-------:|:-------:|:----------|:---------:|
| 🇦🇪 **AE** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ae/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ae/all.b64) |
| 🇦🇱 **AL** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/al/ss.b64">ss×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/al/all.b64) |
| 🇦🇲 **AM** | 2 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/am/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/am/all.b64) |
| 🇦🇹 **AT** | 4 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/at/vless.b64">vless×4</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/at/all.b64) |
| 🇦🇺 **AU** | 4 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/au/vless.b64">vless×4</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/au/all.b64) |
| 🇧🇬 **BG** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/bg/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/bg/all.b64) |
| 🇧🇷 **BR** | 2 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/br/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/br/all.b64) |
| 🇨🇦 **CA** | 23 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ca/ss.b64">ss×11</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ca/vless.b64">vless×12</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ca/all.b64) |
| 🇨🇭 **CH** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ch/ss.b64">ss×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ch/all.b64) |
| 🇩🇪 **DE** | 16 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/de/vless.b64">vless×16</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/de/all.b64) |
| 🇩🇰 **DK** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/dk/ss.b64">ss×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/dk/all.b64) |
| 🇪🇪 **EE** | 7 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ee/vless.b64">vless×7</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ee/all.b64) |
| 🇪🇸 **ES** | 10 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/es/ss.b64">ss×2</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/es/vless.b64">vless×8</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/es/all.b64) |
| 🇫🇮 **FI** | 11 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fi/ss.b64">ss×2</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fi/vless.b64">vless×9</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fi/all.b64) |
| 🇫🇷 **FR** | 19 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fr/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fr/trojan.b64">trojan×11</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fr/vless.b64">vless×7</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/fr/all.b64) |
| 🇬🇧 **GB** | 7 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/gb/vless.b64">vless×7</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/gb/all.b64) |
| 🇬🇷 **GR** | 2 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/gr/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/gr/all.b64) |
| 🇬🇹 **GT** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/gt/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/gt/all.b64) |
| 🇭🇰 **HK** | 9 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/hk/trojan.b64">trojan×3</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/hk/vless.b64">vless×6</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/hk/all.b64) |
| 🇮🇩 **ID** | 3 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/id/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/id/trojan.b64">trojan×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/id/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/id/all.b64) |
| 🇮🇳 **IN** | 2 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/in/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/in/all.b64) |
| 🇮🇹 **IT** | 14 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/it/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/it/vless.b64">vless×13</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/it/all.b64) |
| 🇯🇵 **JP** | 20 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/jp/ss.b64">ss×3</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/jp/trojan.b64">trojan×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/jp/vless.b64">vless×16</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/jp/all.b64) |
| 🇰🇷 **KR** | 13 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/kr/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/kr/vless.b64">vless×12</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/kr/all.b64) |
| 🇰🇿 **KZ** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/kz/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/kz/all.b64) |
| 🇱🇹 **LT** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/lt/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/lt/all.b64) |
| 🇲🇾 **MY** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/my/trojan.b64">trojan×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/my/all.b64) |
| 🇳🇱 **NL** | 13 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/nl/ss.b64">ss×2</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/nl/vless.b64">vless×11</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/nl/all.b64) |
| 🇳🇴 **NO** | 3 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/no/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/no/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/no/all.b64) |
| 🇵🇱 **PL** | 15 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/pl/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/pl/vless.b64">vless×14</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/pl/all.b64) |
| 🇷🇴 **RO** | 3 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ro/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ro/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ro/all.b64) |
| 🇷🇺 **RU** | 2 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ru/vless.b64">vless×2</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/ru/all.b64) |
| 🇸🇦 **SA** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/sa/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/sa/all.b64) |
| 🇸🇪 **SE** | 16 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/se/vless.b64">vless×16</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/se/all.b64) |
| 🇸🇬 **SG** | 18 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/sg/ss.b64">ss×1</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/sg/vless.b64">vless×17</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/sg/all.b64) |
| 🇹🇭 **TH** | 5 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/th/vless.b64">vless×5</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/th/all.b64) |
| 🇹🇷 **TR** | 7 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/tr/vless.b64">vless×7</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/tr/all.b64) |
| 🇹🇼 **TW** | 3 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/tw/ss.b64">ss×2</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/tw/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/tw/all.b64) |
| 🇺🇸 **US** | 18 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/us/ss.b64">ss×2</a>  <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/us/vless.b64">vless×16</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/us/all.b64) |
| 🇺🇿 **UZ** | 1 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/uz/vless.b64">vless×1</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/uz/all.b64) |
| 🇿🇦 **ZA** | 3 | <a href="https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/za/ss.b64">ss×3</a> | [🔗](https://raw.githubusercontent.com/lagzian/SS-Collector/main/configs/za/all.b64) |

---

## 📂 Browse raw configs

`configs/{country}/{protocol}.b64` — e.g. `configs/sg/vless.b64`

---

⚠️ Educational use only. No warranty. Use at your own risk.

*Generated 2026-09-21 03:38 UTC by GitHub Actions.*
