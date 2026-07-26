---
title: "OutSurvive — Sprint Change Proposal: Five-Platform v1.0"
project: "outsurvive"
date: "2026-07-22"
status: "approved"
change_scope: "major"
mode: "incremental"
approved: "2026-07-22"
implementation_status: "completed"
trigger: "V1.0 phải hỗ trợ Windows, Linux, macOS, Android và iOS"
source_documents:
  - "gdds/gdd-outsurvive-2026-07-22/gdd.md"
  - "gdds/gdd-outsurvive-2026-07-22/epics.md"
  - "ux-designs/ux-outsurvive-2026-07-22/DESIGN.md"
  - "ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md"
  - "../game-architecture.md"
---

# Sprint Change Proposal — Five-Platform v1.0

## 1. Issue Summary

Trong Game Architecture Step 3, chủ dự án bổ sung yêu cầu bắt buộc: OutSurvive v1.0 phải phát hành trên **Windows, Linux, macOS, Android và iOS**. Hai input family thuộc phạm vi là **Keyboard/Mouse** và **Touch**; controller và console vẫn ngoài phạm vi.

Yêu cầu này xung đột trực tiếp với GDD 1.0.0 và UX 1.0 đang khóa PC Windows/Linux, chuột–bàn phím và loại mobile khỏi v1.0. Đây là **new stakeholder requirement + strategic scope expansion**, không phải lỗi implementation; chưa có code cần rollback.

### Problem statement

OutSurvive phải trở thành sản phẩm desktop–mobile dùng chung core survival gameplay, authoritative match state, balance data và network protocol. Khác biệt nền tảng chỉ được tồn tại ở input adapter, presentation, quality profile, platform service và release pipeline; mobile không được nhận thêm thông tin hoặc trợ chiến làm suy yếu P1–P4.

### Evidence

- Chỉ dẫn trực tiếp: “Android + iOS + MacOS, Incremental”.
- GDD hiện ghi Windows/Linux, keyboard–mouse và mobile ngoài v1.0.
- UX final hiện ghi PC desktop, canvas 720p–4K và chỉ Keyboard/Mouse.
- Architecture Project Context hiện chỉ có Windows/Linux và desktop client requirements.
- Godot iOS export yêu cầu macOS/Xcode; macOS release cần signing/notarization; Android release cần Gradle/AAB/signing; mobile cần renderer/performance profile riêng.

## 2. Impact Analysis

### 2.1 Epic impact

Không tạo một Mobile Epic cuối chuỗi. Cả E1–E9 được mở rộng để mobile viability xuất hiện từ foundation thay vì thành port muộn.

| Epic | Impact chính |
|---|---|
| E1 | Semantic input command layer; Touch/Gyro adapter; mobile controller prototype |
| E2 | Touch aim/fire; cross-platform hitreg; input-rate independence; aim-assist fairness gate |
| E3 | Tap-first inventory/loot; touch parity; không tăng auto-loot |
| E4 | Background/resume, OS interruption, process eviction, network handoff |
| E5 | Mobile renderer, LOD/streaming, dynamic resolution, thermal/memory và vehicle touch controls |
| E6 | Platform identity, party, voice permission, signed input family và matchmaking pools |
| E7 | Adaptive mobile HUD, control editor, safe area, haptic, gyro, mobile audio/accessibility |
| E8 | Store privacy, account/data lifecycle và entitlement integrity không monetization |
| E9 | Five-platform CI/sign/release, device lab, cellular, thermal, compatibility và certification |

Thêm 12 high-level stories: E1-S8/S9, E2-S9, E3-S9, E4-S9, E5-S9, E6-S9, E7-S10/S11, E8-S8, E9-S9/S10. Không epic nào obsolete; thứ tự E1–E9 giữ nguyên, nhưng platform smoke/viability gates bắt đầu từ E1.

### 2.2 Artifact conflicts

| Artifact | Conflict | Required state |
|---|---|---|
| GDD 1.0.0 | PC-only platform/input/performance/out-of-scope | Nâng 1.1.0; five-platform ready-for-architecture |
| Epics 1.0.0 | Story/DoD không có mobile/platform release | Nâng 1.1.0; bổ sung story và cross-platform gates |
| DESIGN.md | Desktop layout/components; 25 component | Mở revision; thêm 5 mobile component và 2 visual reference |
| EXPERIENCE.md | PC KBM form factor, flow và input routing | Mở revision; thêm Touch/lifecycle/pool/journey mobile |
| UX validation | Chỉ chứng minh desktop | Giữ historical; chạy targeted mobile delta review |
| Game Architecture | Project Context desktop-only; Engine Step 3 bị gián đoạn | Sửa scope/requirements/assumptions; tiếp tục Step 3 trên baseline mới |
| CI/CD/Test | Chưa khóa five-platform signing/device matrix | Đưa vào Architecture/E9 trước implementation |

### 2.3 Technical impact

- Một `GameplayCommand` semantic dùng chung cho InputMap, Touch và Gyro.
- Server authority và protocol không phân nhánh theo platform.
- Matchmaking theo Touch, Keyboard/Mouse và Mixed/KBM pool; input family match-lock và signed claim.
- Forward+ trên desktop; Mobile renderer trên Android/iOS; common gameplay/collision data với platform visual variants.
- Platform SDK nằm sau identity/invite/permission/lifecycle/secure-storage/build-info adapters.
- macOS Universal 2 + signing/notarization; iOS Xcode/provisioning/TestFlight; Android ARM64 AAB/Gradle/signing.
- Mobile lifecycle, cellular impairment, device memory/thermal/battery và safe-area trở thành first-class acceptance.
- Content targets 25 vũ khí, 6 phương tiện, 18 POI, 420 công trình là provisional tới khi server scale và mobile viability cùng đạt.

### 2.4 Product and schedule impact

- Change scope: **Major**.
- Effort: **High**.
- Risk: **High**, giảm xuống Medium–High nếu platform gates chạy từ E1.
- Timeline impact: đáng kể; phải tái lập kế hoạch và resource envelope, không coi mobile là port cuối dự án.
- Không implementation rollback; tài liệu desktop hiện tại vẫn là desktop baseline.
- Platform parity, core loop và server stability được ưu tiên hơn content breadth nếu MVP review buộc cắt giảm.

## 3. Recommended Approach

### Selected path: Hybrid

Kết hợp **Direct Adjustment** và **MVP Review**.

#### Non-negotiable

- Classic survival fantasy; 100 người và 8×8 km vẫn là v1.0 north-star.
- Server-authoritative damage, loot, zone và result.
- Cùng weapon/loot/zone/gameplay data trên mọi nền tảng.
- Không hero skill, hồi sinh/mua lại, pay-to-win, storefront, battle pass hoặc FOMO.
- Không target snap, auto-fire, enemy detection, visual footstep radar hoặc silent bots.

#### Input and matchmaking policy

- Keyboard/Mouse pool: Windows, Linux và macOS.
- Touch pool: Android và iOS.
- Mixed-input party vào Mixed/Keyboard-Mouse pool sau disclosure.
- External keyboard/mouse trên mobile không đổi input family giữa trận; phải requeue ngoài trận.
- Gyro tùy chọn. Touch aim slowdown/friction chỉ được xem xét trong Touch pool sau fairness prototype; không mặc định.
- Population gate phải chứng minh mỗi pool đủ trận 100 người; không fallback ngầm sang bot hoặc pool khác.

#### MVP review rule

Không tự động cắt map hoặc 100-player core loop. Content breadth được re-estimate sau mobile greybox/device soak. Bất kỳ cắt giảm vũ khí, phương tiện, POI, công trình, weather hoặc profile tooling cần GDD change riêng.

## 4. Detailed Change Proposals

### 4.1 GDD 1.1.0

#### Metadata

```yaml
platforms:
  - "PC - Windows"
  - "PC - Linux"
  - "macOS"
  - "Mobile - Android"
  - "Mobile - iOS"
input_families:
  - "Keyboard and Mouse"
  - "Touch"
version: "1.1.0"
```

#### Platform and input contract

- Windows 10/11 x64; Linux x64; macOS 13+ Intel/Apple Silicon; Android 10+ ARM64; iOS 16+ ARM64.
- Mobile landscape; configurable Touch controls, optional Gyro, tap-first inventory and safe-area support.
- Gameplay consumes semantic commands, not raw keys/gestures.
- Controller/console remains out of scope.

#### Cross-platform contract

- Shared account/progression/party/backend.
- Touch, Keyboard/Mouse and Mixed/KBM pools.
- Same authority, balance and information contract.
- No silent bot fill or mid-match family switching.

#### Client profiles

| Profile | Target |
|---|---|
| Desktop minimum | Existing 60 FPS/1080p profile + macOS equivalent |
| Desktop recommended | Existing 90 FPS/1080p profile |
| Mobile minimum | Snapdragon 778G/Dimensity 920 class or iPhone 11/A13; 45 FPS median, p95 ≤33.3 ms |
| Mobile recommended | Snapdragon 8 Gen 1/Dimensity 8100 class or iPhone 13/A15; 60 FPS median, p95 ≤25 ms |

Mobile: working memory ≤3 GB, installed size ≤12 GB, pre-match load ≤60 s p95, no OS termination in 45-minute match and median FPS degradation ≤15% after 30-minute thermal soak.

#### Gates and scope

- R1 includes desktop + Android + iOS command/network path.
- R2 includes 24 mixed clients, Touch HUD and lifecycle.
- R3 includes 100-client protocol mix, device lab and input-pool population.
- R4 requires release candidate family on all five platforms.
- Remove mobile/cross-platform desktop–mobile from v1.0 exclusions.
- Mark existing content targets provisional until server/mobile gates pass.

### 4.2 Epics 1.1.0

Add stories:

| Story | Outcome |
|---|---|
| E1-S8 | Cross-platform semantic input command layer |
| E1-S9 | Mobile survivor touch controller |
| E2-S9 | Mobile aiming/firing/Gyro fairness harness |
| E3-S9 | Tap-first mobile loot/inventory |
| E4-S9 | Background/resume/network-handoff lifecycle |
| E5-S9 | Mobile streaming/LOD/dynamic-resolution/thermal gate |
| E6-S9 | Platform identity and input-pool policy |
| E7-S10 | Adaptive mobile HUD and control layout editor |
| E7-S11 | Mobile accessibility, haptic, Gyro and audio interruption |
| E8-S8 | Platform privacy and entitlement integrity |
| E9-S9 | Five-platform build/sign/release pipeline |
| E9-S10 | Mobile device, thermal, lifecycle and cellular matrix |

Modify E1-S6, E2-S8, E4-S8, E5-S8, E6-S4/S5/S6, E7-S2 and E9-S6 so their acceptance covers relevant desktop/mobile paths. Platform smoke builds start at E1; certification remains E9.

### 4.3 UX 1.1

#### Status and scope

- Reopen DESIGN/EXPERIENCE as `revision-in-progress`.
- Add desktop KBM + mobile landscape Touch form factors.
- Return to `final` only after targeted mobile validation.

#### New components

Increase exact component parity from 25 to 30:

- `safe-area-root`
- `touch-stick`
- `touch-look-zone`
- `touch-action-button`
- `control-layout-editor`

#### Mobile interaction

- Landscape HUD with left movement, right look, context actions and optional left fire.
- Touch target ≥48 logical units; critical fire/exit/close ≥64 where safe area permits.
- Single mobile Inventory panel ≤62% width, ≥38% world-risk strip, tabbed Nearby/Backpack/Equipment.
- Map supports pan/pinch/tap/long-press while retaining server reveal and damage cue rules.
- Touch layout is configurable and saved per device class.
- Add input-pool disclosure, lifecycle/reconnect states, permission flows and Gyro configuration.
- Add mobile journey “Mai” and phone/tablet/safe-area/accessibility acceptance matrix.

#### Visual references

Keep four desktop mocks and add exactly two mobile mocks:

- `mobile-match-hud.html`
- `mobile-inventory-map.html`

Run targeted Reviewer Gate for Touch reachability, information parity, phone/tablet occlusion, lifecycle and party/input-pool disclosure.

### 4.4 Game Architecture

#### Core input flow

```text
Desktop InputMap / Touch / Gyro
              -> GameplayCommand
              -> Client Prediction
              -> NetworkInputFrame
              -> Authoritative Simulation
```

#### Engine baseline

- Godot 4.7.1 Standard; typed GDScript baseline.
- Forward+ on Windows/Linux/macOS; Mobile renderer on Android/iOS.
- Jolt Physics common; no client physics authority.
- Linux headless dedicated server with stripped visuals.
- Clean project; official TPS demo is reference only.

#### Platform adapters

- `PlatformIdentity`
- `PlatformEntitlement`
- `PlatformInvite`
- `PlatformVoicePermission`
- `PlatformAppLifecycle`
- `PlatformSecureStorage`
- `PlatformBuildInfo`

#### Shared assets and protocol

- One gameplay Resource ID with server collision/query data and desktop/mobile visual variants.
- LOD/profile cannot alter cover, silhouette, openings or visibility semantics.
- Same protocol version/authoritative state across clients; only presentation/non-critical update tiers may vary.

#### New assumptions

Add ARC-A13–ARC-A20 for mobile renderer/performance, 100-player thermal/memory, pool population, cellular transport, asset fairness, Apple CI/signing, Touch viability and store compliance.

#### Development tools

Record GoPeak 2.3.9 and Context7 3.2.4 as optional development tools. They receive no signing key, production token or player data and are not runtime dependencies.

## 5. Implementation Handoff

### Scope classification

**Major — fundamental replan with Product/Game Design, UX and Architecture ownership.**

### Responsibilities

| Role | Responsibility |
|---|---|
| Product/Game Design | Apply GDD 1.1.0, protect P1–P4, resolve any later content reduction |
| Product Owner/Planning | Apply Epics 1.1.0, re-estimate resource envelope and maintain gates/dependencies |
| UX | Revise two spines, create two mobile mocks, run targeted validation and return UX to final |
| Architect | Update Project Context, finish Engine Step 3 and decide networking/platform/content patterns |
| Build/Platform Engineering | macOS/iOS/Android signing/export/CI and platform adapters |
| Gameplay/Network Engineering | Semantic commands, input lock, prediction/reconciliation and mobile lifecycle |
| QA/Performance | Five-platform device, thermal, cellular, accessibility and 100-client matrices |
| Security/Privacy | Token storage, protocol validation, store disclosures, account/data lifecycle |

### Sequencing

1. Apply GDD and Epics 1.1.0.
2. Reopen and revise UX 1.1; validate two mobile visual references.
3. Update Architecture Project Context and resume Step 3.
4. Lock semantic input, pool, renderer/content and platform adapter ADRs.
5. Re-estimate production envelope before R2.
6. Only then create detailed stories/implementation plans.

### Success criteria

- No planning artifact claims mobile/macOS is out of scope.
- GDD/Epics/UX/Architecture agree on five platforms, two input families and matchmaking policy.
- Desktop/mobile use one gameplay data model and authoritative protocol.
- UX contains touch/lifecycle/safe-area contracts and 30/30 component parity.
- Two mobile visual references pass phone/tablet/safe-area checks.
- R1–R4 include explicit cross-platform gates.
- Signing keys and production secrets remain outside source/MCP context.
- Architecture resumes only after updated sources are internally consistent.

## 6. Checklist Status

| Section | Status |
|---|---|
| 1. Trigger and context | Complete |
| 2. Epic impact | Complete |
| 3. Artifact conflict | Complete |
| 4. Path forward | Complete — Hybrid approved |
| 5. Proposal components | Complete |
| 6. Final review/handoff | Complete — approved for implementation |

## Approval Record

- Trigger framing: Approved.
- Epic impact: Approved.
- Artifact impact: Approved.
- Hybrid path/input-pool policy: Approved.
- GDD proposal: Approved.
- Epics proposal: Approved.
- UX proposal: Approved.
- Architecture proposal: Approved.
- Final implementation approval: **Approved by Project Owner on 2026-07-22.**

## Final Routing

- **Classification:** Major.
- **Routed to:** Product/Game Design, UX, Solution Architecture, Build/Platform Engineering và QA/Performance.
- **Sprint status:** N/A — không có `sprint-status.yaml`; dự án vẫn ở planning/architecture, chưa tạo trạng thái sprint giả.
- **Execution order:** GDD/Epics → UX delta + validation → Architecture resume → implementation planning.

## 7. Execution Record

**Applied:** 2026-07-22  
**Result:** Complete — source documents synchronized; Architecture may resume at Step 3.

| Artifact | Applied result |
|---|---|
| `gdd.md` | 1.1.0 ready-for-architecture; five platforms, two input families, pools, mobile budgets/gates; PC-only exclusion removed |
| `decision-log.md` | D-015–D-018 added; D-005/D-013 amended/superseded |
| `epics.md` | 1.1.0; 12 cross-platform stories, mobile/platform DoD and gates across E1–E9 |
| `DESIGN.md` / `EXPERIENCE.md` | UX 1.1 final; 30/30 component parity, Mai journey, Touch/pool/lifecycle/accessibility contracts |
| `mobile-match-hud.html` | Added as mobile HUD delta reference |
| `mobile-inventory-map.html` | Added as mobile Inventory/Map delta reference |
| `mobile-delta-validation.md` | Targeted gate Pass; 8 Closed, 0 Open; six viewport evidence PNGs |
| `final-ux-verification.md` | Updated to 20 Closed · 5 Accepted dependency · 0 Open |
| `game-architecture.md` | Project Context synchronized; Steps 1–2 remain complete; ARC-A13–ARC-A20 and platform/input boundaries added |

### Success criteria verification

- **Pass:** Không artifact nguồn hiện hành nào coi mobile/macOS ngoài phạm vi.
- **Pass:** GDD/Epics/UX/Architecture thống nhất Windows/Linux/macOS/Android/iOS, Keyboard/Mouse + Touch và matchmaking pool policy.
- **Pass:** Shared semantic command, gameplay data/authority/protocol và mobile lifecycle đã được mang vào architecture context.
- **Pass:** UX đạt 30/30 parity và có đúng hai mobile delta reference.
- **Pass:** R1–R4 chứa explicit cross-platform gates; content breadth được đánh dấu provisional.
- **Pass:** Tooling/signing boundary cấm secret, production token và player data trong source/MCP.
