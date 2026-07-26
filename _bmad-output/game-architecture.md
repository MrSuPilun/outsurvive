---
title: 'Game Architecture'
project: 'outsurvive'
date: '2026-07-22'
author: 'Project Owner'
version: '1.1'
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]
status: 'complete'
engine: 'Godot Engine Standard 4.7.1-stable'
platform:
  - 'Windows 10/11 x64'
  - 'Linux x64'
  - 'macOS 13+ Intel/Apple Silicon'
  - 'Android 10+ ARM64'
  - 'iOS 16+ ARM64'

# Source Documents
gdd: '_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md'
epics: '_bmad-output/planning-artifacts/epics.md'
brief: null
ux_design: '_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/DESIGN.md'
ux_experience: '_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md'
last_revalidated: '2026-07-26'
---

# Game Architecture

## Executive Summary

**OutSurvive** sử dụng Godot Engine Standard 4.7.1-stable và typed GDScript, nhắm tới Windows, Linux, macOS, Android và iOS ngay từ v1.

**Các quyết định kiến trúc then chốt:**

- Dedicated server 30 Hz xác nhận mọi trạng thái cạnh tranh; ENet/UDP chỉ là transport dưới custom binary replication, relevance, prediction và bounded lag compensation.
- Gameplay core dùng chung giữa client, server và test harness nhưng không phụ thuộc renderer, UI, raw input, platform SDK hoặc backend.
- Bản đồ 8×8 km dùng hierarchical multi-grid streaming, Terrain3D chỉ ở editor, dữ liệu terrain/world được bake và kiểm định parity trước khi promote.
- Nakama/CockroachDB vận hành control plane; Agones/Kubernetes cấp một Linux headless process cho mỗi trận; combat realtime không đi qua backend control plane.
- Windows, Linux, macOS, Android và iOS dùng cùng luật gameplay, semantic command và visibility contract; mọi khác biệt chỉ nằm sau presentation/platform adapter.

**Project Structure:** domain-driven monorepo với ports-and-adapters, phân ownership cho 16 hệ thống cốt lõi và cô lập client, authoritative simulation, dedicated server, platform, backend, infrastructure, content pipeline cùng test harness.

**Implementation Patterns:** 16 pattern đã được khóa, gồm 6 pattern đặc thù OutSurvive và 10 pattern chuẩn, nhằm giữ implementation của người và AI agent nhất quán.

**Sẵn sàng cho:** tạo project context, kiểm tra implementation readiness và triển khai Combat Sandbox theo các empirical gate; chưa được khóa production content chỉ dựa trên tài liệu kiến trúc.

## Document Status

Tài liệu kiến trúc đã hoàn tất theo GDS Architecture Workflow và sẵn sàng làm nguồn chuẩn cho implementation agent.

**Steps Completed:** 9 of 9 (Initialize, Project Context, Engine & Framework, Architectural Decisions, Cross-cutting Concerns, Project Structure, Implementation Patterns, Architecture Validation, Completion)

---

_Mọi thay đổi kiến trúc sau thời điểm này phải đi qua ADR và cập nhật validation tương ứng._

## Project Context

### Game Overview

**OutSurvive** là battle royale sinh tồn chiến thuật theo nền tảng PUBG cổ điển: 100 người xuất phát tay trắng trên bản đồ 8×8 km, loot tại chỗ, di chuyển theo chín pha bo và chiến đấu tới người hoặc đội sống cuối cùng.

Thiết kế ưu tiên tài nguyên khan hiếm, thông tin không hoàn hảo, hậu quả tử vong và công bằng cạnh tranh. Không có hero skill, hồi sinh, loadout ngoài trận, pay-to-win, storefront, battle pass hoặc live-event trong v1.0.

### Technical Scope

- **Engine:** Godot 4.7.1 Standard baseline.
- **Nền tảng:** Windows 10/11 x64, Linux x64, macOS 13+ Intel/Apple Silicon, Android 10+ ARM64 và iOS 16+ ARM64.
- **Input family:** Keyboard/Mouse và Touch; full remap/layout editor, Gyro tùy chọn; controller/console ngoài phạm vi.
- **Thể loại:** Online third-person shooter / battle royale.
- **Quy mô:** 100 người, Solo/Duo/Squad, một bản đồ 8×8 km.
- **Project level:** High-complexity networked game.
- **Mô hình tin cậy:** Máy chủ xác nhận mọi trạng thái ảnh hưởng gameplay.
- **Lộ trình chứng minh:** Combat Sandbox 8 client + five-platform smoke → Vertical Slice 24 mixed clients → Alpha 50/100 protocol mix + device/pool gates.

### Core Systems

| Hệ thống | Độ phức tạp | Nguồn |
|---|---|---|
| Semantic command, Keyboard/Mouse, Touch/Gyro, movement, stance, vault và interaction | Cao | GDD “Điều khiển và đầu vào”; E1-S8/S9 |
| TPP camera, shoulder swap, ADS và anti-peek | Cao | GDD “Điều khiển và đầu vào”; E1-S4; UX-024 |
| Vũ khí, projectile, recoil, armor và hit registration | Cao | GDD “Hệ thống vũ khí”; E2 |
| Client prediction, reconciliation và lag compensation giới hạn | Cao | GDD “Mô hình hit registration”; E2-S8, E6 |
| Loot generation, inventory, equipment và consumable actions | Trung bình–cao | GDD “Kho đồ/Hệ thống loot”; E3 |
| Match/mobile lifecycle, máy bay, dù, DBNO, reconnect và kết quả | Cao | GDD “Vòng lặp trận đấu”; E4-S8/S9; UX-043 |
| Chín pha bo và deterministic server timing | Trung bình–cao | GDD “Cấu trúc vùng an toàn”; E4-S3; UX-032 |
| World partition và streaming bản đồ 8×8 km | Cao | GDD “Đảo Vọng”; E5 |
| Vehicle physics, replication, fuel, tire và explosion | Cao | GDD “Phương tiện”; E5-S5 |
| Platform identity, party, input pools, matchmaking, region và reconnect | Cao | GDD “Nhiều người chơi”; E6-S4/S5/S9; UX-028–UX-030/UX-039 |
| Team voice và tám ping ngữ cảnh | Trung bình–cao | E6-S4; UX-028 |
| Desktop/mobile HUD, Touch editor, safe area, input routing và accessibility | Cao | E7-S10/S11; DESIGN/EXPERIENCE 1.1 final |
| Spatial audio/HRTF và gameplay audio mix | Cao | GDD “Âm thanh”; E7; UX-034 |
| Profile, statistics, report và block | Trung bình–cao | E8; E9-S4; UX-031 |
| Replay sự kiện, telemetry, observability và anti-cheat | Cao | E6-S8; E9 |
| Five-platform build/sign/certification, patch, dedicated server và regional operations | Cao | GDD “Phạm vi sản xuất”; E9-S9/S10 |

### Technical Requirements

**Desktop client — Windows/Linux/macOS**

- 60 FPS trung vị, p95 frame time ≤25 ms trên máy tối thiểu ở 1080p/Low.
- 90 FPS trung vị, p95 ≤16,7 ms trên máy đề nghị ở 1080p/High.
- RAM ≤6 GB sau trận 45 phút.
- Hỗ trợ 1280×720–3840×2160 và ultrawide; macOS 13+ Intel x64/Apple Silicon.
- Standard ultrawide giữ live-world viewport 16:9 ở giữa để bảo toàn fairness.
- Tối đa sáu khói dày trong bán kính 100 m mà vẫn đạt budget máy tối thiểu.
- Bản cài ≤25 GB; load vào pre-match ≤45 giây p95.

**Mobile client — Android/iOS**

- Android 10+ ARM64; iOS 16+ ARM64; landscape phone/tablet với safe-area/cutout.
- Minimum class Snapdragon 778G/Dimensity 920, 6 GB hoặc iPhone 11/A13: 45 FPS median, p95 ≤33,3 ms ở Low.
- Recommended class Snapdragon 8 Gen 1/Dimensity 8100, 8 GB hoặc iPhone 13/A15: 60 FPS median, p95 ≤25 ms ở Medium.
- Working memory ≤3 GB; installed size ≤12 GB; pre-match load ≤60 giây p95.
- Không OS termination trong trận 45 phút; FPS median không giảm quá 15% sau 30 phút thermal soak.
- Mobile renderer/LOD/dynamic resolution không thay collision, cover, silhouette, openings hoặc information contract.

**Dedicated match server**

- Authoritative cho movement validity, shot, damage, loot, zone và result.
- Simulation 30 Hz với 100 người và tối thiểu 10% headroom.
- Damage event được xử lý trong ≤1 tick ở p95.
- Lag compensation giới hạn 150 ms.
- Sai lệch vị trí xác nhận ≤0,5 m p95 tại 80 ms RTT/1% packet loss.
- Băng thông trung bình ≤1,5 Mbps mỗi chiều trên client.
- Mỗi trận Alpha hướng tới envelope ≤8 vCPU/16 GB, cần benchmark xác minh.

**Backend và vận hành**

- Shared account/progression/party/backend qua platform identity/invite adapter.
- Matchmaking theo vùng và soft MMR tân thủ, tách Touch, Keyboard/Mouse và Mixed/Keyboard-Mouse pool; signed family claim + match-lock + disclosure.
- Match allocation, secure reconnect token và authoritative outcome khi mất mạng.
- Profile/statistics không ảnh hưởng sức mạnh.
- Report/block, retention/privacy và evidence policy.
- Match log/replay sự kiện phục vụ hitreg investigation và anti-cheat.
- Crash reporting, metrics, alerts, rollback và patch pipeline.
- Build/sign/certification pipeline cho macOS Universal 2/notarization, Android ARM64 AAB và iOS archive/TestFlight; secret không vào source hoặc công cụ MCP.

**Input và platform boundary bắt buộc**

```text
Desktop InputMap / Touch / Gyro
              -> GameplayCommand
              -> Client Prediction
              -> NetworkInputFrame
              -> Authoritative Simulation
```

- Gameplay không đọc raw key/gesture trực tiếp ngoài input adapter.
- Platform service nằm sau `PlatformIdentity`, `PlatformEntitlement`, `PlatformInvite`, `PlatformVoicePermission`, `PlatformAppLifecycle`, `PlatformSecureStorage` và `PlatformBuildInfo`.
- Adapter failure phải trả capability/state rõ; không được làm gameplay core phụ thuộc SDK hoặc store cụ thể.

### Complexity Drivers

**High complexity**

- Replication và interest management cho 100 người, projectile, loot, xe và smoke.
- Prediction/reconciliation mà không để client quyết định kết quả cạnh tranh.
- World streaming 8×8 km với 420 công trình có thể vào.
- TPP camera fairness và server-valid visibility.
- Cross-platform năm client target cho input, audio, renderer, lifecycle, build/sign và certification; Linux headless cho match server.
- Hai renderer profile và asset variants phải giữ gameplay visibility parity.
- Touch reach/multi-touch/Gyro phải đạt usability mà không thêm aim/information assist.
- Voice, reconnect, spectator và replay đều phải giữ information parity.
- Performance phải được chứng minh trước khi sản xuất toàn bản đồ.

**Novel or project-specific constraints**

- Central 16:9 competitive viewport trên màn ultrawide.
- Head line-of-sight quyết định visibility chống corner peek.
- Spectator chỉ được biết đúng tập thông tin của teammate đang theo dõi.
- Accessibility không được chuyển âm thanh thành radar hoặc tăng cue chiến thuật.
- Cổng sản phẩm cấm storefront/FOMO/live-event trở thành dependency của gameplay.

### Technical Risks

1. **Godot networking scale:** high-level multiplayer mặc định có thể không đủ cho 100 người; cần benchmark transport, serialization và interest management từ Combat Sandbox.
2. **Server authority và responsiveness:** movement/shooting phải phản hồi nhanh phía client nhưng không mở cửa cho speed hack, fire-rate hack hoặc hit fabrication.
3. **World streaming:** tải/unload terrain, building, collision và audio zone không được gây hitch hoặc làm projectile xuyên vùng chưa sẵn sàng.
4. **Physics:** vehicle và projectile behavior giữa client/server cần validation rõ, không phụ thuộc giả định deterministic tuyệt đối.
5. **Bandwidth:** replicate mọi node theo scene tree sẽ vượt budget; cần relevance graph, snapshot delta và nhiều tần số cập nhật.
6. **Reconnect/AFK/mobile lifecycle:** policy đã khóa tại ADR-21; rủi ro còn lại là implementation/impairment/device evidence, không còn product-decision gate.
7. **Security:** secure session token, protocol validation, replay evidence và anti-cheat boundary phải tồn tại từ network slice, không chỉ thêm ở E9.
8. **Spatial audio:** HRTF, occlusion, permission và route recovery phải đạt metric định hướng trên Windows/Linux/macOS/Android/iOS.
9. **Smoke và final circle:** overdraw, particles, audio, projectile và 100-player clustering có thể phá budget đồng thời.
10. **Chi phí vận hành:** mục tiêu 30 Hz/100 người phải được đo bằng cost per match và cost per player-hour trước cổng R3.
11. **Mobile thermal/memory:** 100-player density, smoke, streaming và 45-minute session có thể vượt RAM/thermal budget dù scene trung bình đạt FPS.
12. **Pool population:** tách Touch/Keyboard-Mouse/Mixed có thể làm thời gian chờ hoặc mật độ 100 người không khả thi tại vùng phát hành.
13. **Cellular transport:** handoff, jitter, NAT và packet loss mobile có thể phá prediction/reconnect/token assumptions.
14. **Apple/Google delivery:** signing, provisioning, notarization, store review và privacy manifest có thể chặn release dù gameplay build ổn định.

### Assumption & Validation Gate Register

| ID | Giả định chưa được chứng minh | Tin cậy | Tác động nếu sai | Cổng bắt buộc |
|---|---|---:|---:|---|
| ARC-A01 | Godot 4.x có thể chạy match server 100 người ở 30 Hz trong ≤8 vCPU/16 GB | Thấp | Critical | Benchmark 8 → 24 → 50 → 100 client trước production toàn bản đồ |
| ARC-A02 | Godot MultiplayerAPI/replication mặc định đủ cho OutSurvive | Thấp | Critical | So sánh high-level replication với custom snapshot/interest management |
| ARC-A03 | Simulation 30 Hz vẫn đạt hitreg ≤1 tick và sai lệch ≤0,5 m | Trung bình | Critical | Network combat replay tại 80 ms/1% loss và burst impairment |
| ARC-A04 | Băng thông ≤1,5 Mbps/client khả thi | Trung bình | Cao | Đo snapshot delta, update tiers và relevance radius ở final-circle load |
| ARC-A05 | Bản đồ 8×8 km, 420 công trình và collision có thể chạy trên desktop 8 GB RAM | Thấp | Critical | Streaming benchmark bằng greybox trước khi làm art/content đầy đủ |
| ARC-A06 | Client prediction và server physics không cần deterministic tuyệt đối | Cao | Cao | Server giữ authority; reconciliation test trên cả năm client target |
| ARC-A07 | Vehicle physics có thể replicate ổn định trong cùng budget với combat | Trung bình–thấp | Cao | Benchmark va chạm nhiều xe, passenger và explosion dưới packet loss |
| ARC-A08 | Godot audio backend đạt HRTF/spatial metric trên cả năm client target | Trung bình–thấp | Cao | Replay âm thanh chuẩn trên từng output/nền tảng cạnh tranh |
| ARC-A09 | Invite và voice có thể ẩn sau provider adapter; reconnect policy/ownership đã khóa ở ADR-21 | Trung bình | Cao | Provider spike + token/owner contract tests; không thay reconnect outcome bằng provider default |
| ARC-A10 | Replay sự kiện đủ cho hitreg, report và anti-cheat mà không cần full replay | Trung bình | Cao | Thiết kế event schema và tái dựng một dispute từ log |
| ARC-A11 | Chi phí máy chủ 100 người bền vững | Thấp | Critical | Đo cost per match và cost per player-hour tại R3 |
| ARC-A12 | Envelope PC-first 12–20 người đủ cho v1.0 | Đã thay thế | Critical | Không dùng làm cam kết; re-estimate five-platform staffing trước R2 |
| ARC-A13 | Godot Mobile renderer giữ gameplay readability và 45/60 FPS target trên device class đã khóa | Thấp | Critical | Mobile greybox benchmark trên Android/iOS minimum/recommended trước R2 |
| ARC-A14 | 100-player density + streaming + smoke giữ ≤3 GB và thermal degradation ≤15% | Thấp | Critical | 45-minute device soak với final-circle stress trước content lock |
| ARC-A15 | Touch/Keyboard-Mouse/Mixed pool đủ dân số cho trận 100 người trong ngưỡng chờ | Thấp | Critical | Population simulation + regional beta; không silent bot/fallback |
| ARC-A16 | Cellular transport/reconnect hoạt động qua jitter, loss, NAT và Wi-Fi↔cellular handoff | Trung bình–thấp | Cao | Impairment lab + device handoff test trước E6 gate |
| ARC-A17 | Desktop/mobile asset variants giữ cover/silhouette/openings/visibility tương đương | Trung bình | Critical | Automated collision/query parity + screenshot/readability review mỗi content batch |
| ARC-A18 | macOS/iOS build-sign-test và notarization/TestFlight có thể tự động hóa an toàn | Trung bình | Cao | Apple CI spike; signing secrets ngoài repo/MCP; release dry-run trước E9 |
| ARC-A19 | Touch layout, multi-touch ownership và optional Gyro đủ khả dụng không cần auto-aim | Trung bình–thấp | Critical | Device-hand playtest + fairness harness trong Touch pool trước R2 |
| ARC-A20 | Store privacy/data lifecycle/entitlement đáp ứng Apple/Google mà không tạo monetization loop | Trung bình | Cao | Privacy/security/store checklist và submission rehearsal trước RC |

### Architectural Boundaries Carried Forward

- Không client authority cho damage, loot, zone hoặc result.
- Không giả định physics deterministic giữa client và server; server quyết định, client dự đoán và hòa giải.
- Interest management, snapshot delta và replication tiers là năng lực bắt buộc; cách triển khai phải qua benchmark.
- Security và protocol validation bắt đầu từ Combat Sandbox E2, không chờ tới E9.
- Không bot âm thầm trong Standard.
- Không kill-cam/full replay cho người chơi ở v1.0.
- Không visual footstep radar, enemy outline hoặc ultrawide information advantage.
- Không target snap, auto-fire, enemy detection hoặc mobile-only information; aim friction chỉ qua Touch-pool fairness gate và mặc định tắt.
- Input family được signed/match-locked; mixed party disclosure bắt buộc; không silent pool switch hoặc external-input switch giữa trận.
- Một gameplay data model và authoritative protocol cho cả năm client target; khác biệt chỉ sau input, presentation/quality, lifecycle và platform adapters.
- LOD/renderer/asset variant không được thay collision, cover, silhouette, opening hoặc visibility semantics.
- Signing key, provisioning profile, production token và player data không được đưa vào source, prompt hoặc MCP development tools.
- Không coupling gameplay với storefront, currency, battle pass hoặc live-event.
- Không production pass toàn bộ 420 công trình hoặc khóa 25 vũ khí/6 xe/18 POI trước khi E6 chứng minh tải 100 người và mobile viability cùng đạt.
- Mọi hệ thống phải có cấu hình/test path tương ứng cho các cổng 8, 24, 50 và 100 người.
- Nếu 100 người không đạt 30 Hz/headroom hoặc chi phí vận hành không bền vững, giữ sản phẩm ở quy mô đã chứng minh thay vì giảm tính toàn vẹn cạnh tranh.

## Engine & Framework

### Selected Engine

**Godot Engine Standard 4.7.1-stable** với **typed GDScript** là baseline sản xuất của OutSurvive.

**Rationale:** Godot phù hợp định hướng dự án đã khóa, hỗ trợ một codebase cho năm client target, có scene/resource workflow gọn cho đội nhỏ và cho phép kiểm soát sâu các tầng input, rendering, networking và dedicated server. Tuy nhiên, lựa chọn engine không mặc nhiên chứng minh khả năng vận hành 100 người, bản đồ 8×8 km hay mobile 45/60 FPS; các mục tiêu này vẫn phải vượt qua benchmark và validation gate riêng.

### Project Initialization

- Khởi tạo một dự án Godot Standard sạch, không kế thừa starter kit hoặc framework gameplay bên thứ ba.
- Dùng typed GDScript làm ngôn ngữ gameplay/client chính ở giai đoạn đầu; chỉ đưa GDExtension/native module vào sau profiling và ADR chứng minh nhu cầu.
- Các dự án mẫu TPS và `godot-demo-projects` chính thức chỉ dùng để tham khảo API, camera, animation và convention; không được sao chép thành kiến trúc nền.
- Pin phiên bản editor/export template ở 4.7.1-stable cho CI và máy phát triển. Mọi nâng cấp engine phải có compatibility branch, five-platform smoke test và quyết định nâng cấp được ghi nhận.

### Platform Rendering Baseline

| Target | Renderer/profile ưu tiên | Graphics driver ưu tiên | Quy tắc |
|---|---|---|---|
| Windows | Forward+ | D3D12 | Chỉ mở fallback sau benchmark tương thích và parity |
| Linux | Forward+ | Vulkan | Baseline desktop/Linux headless tách khỏi client rendering |
| macOS | Forward+ | Metal | Kiểm tra cả Intel và Apple Silicon |
| Android | Mobile | Vulkan | Device matrix minimum/recommended bắt buộc |
| iOS | Mobile | Metal | Kiểm tra safe area, lifecycle, thermal và memory pressure |

Fallback driver không được tự động trở thành baseline. Mọi driver/profile được chấp nhận phải giữ nguyên collision, cover, silhouette, opening, visibility và gameplay-readable effects; chỉ được khác chất lượng trình bày và chi phí render.

### Engine-Provided Architecture

| Component | Godot solution | Architectural use in OutSurvive |
|---|---|---|
| Rendering | RenderingServer, Forward+ và Mobile renderer | Hai presentation profile dùng chung gameplay data và visibility contract |
| Physics | Jolt Physics mặc định cho 3D | Collision/query local; server vẫn là authority và không giả định deterministic tuyệt đối giữa máy |
| Scene management | Node, SceneTree, PackedScene | Composition và lifecycle cục bộ; không dùng scene-tree replication nguyên trạng cho toàn trận |
| Game data | Resource và custom Resource | Dữ liệu vũ khí, vật phẩm, phương tiện và world definition có schema/version rõ |
| Input | InputMap và input events | Chỉ input adapter đọc raw input; gameplay nhận `GameplayCommand` semantic |
| Audio | AudioServer, bus và 3D audio nodes | Mix, routing và spatial presentation; fairness/occlusion cần test riêng trên năm target |
| Scripting | Typed GDScript | Gameplay orchestration, client systems và tooling ban đầu |
| Build/export | Export presets, headless/dedicated execution | Năm client pipeline và Linux dedicated-server artifact độc lập |
| Profiling/debug | Profiler, monitors, debugger và remote inspection | Dùng trong spike; production telemetry vẫn cần giải pháp riêng |

Godot cung cấp primitives, không cung cấp sẵn kiến trúc battle royale quy mô OutSurvive. High-level MultiplayerAPI có thể được dùng trong prototype nhưng chưa được chấp nhận làm transport/replication production cho đến khi so sánh được với snapshot, delta serialization và interest management tùy chỉnh.

### Starter Template Decision

**Decision:** bắt đầu từ dự án sạch.

Không có starter template nào được chấp nhận làm dependency kiến trúc. Official TPS demo và kho `godot-demo-projects` chỉ là nguồn tham khảo có kiểm soát; bất kỳ đoạn code nào được tiếp nhận phải qua review ownership, licensing, performance và khả năng chạy trên cả desktop/mobile.

### Optional AI Development Tooling

| Tool | Baseline đã xác minh | Vai trò | Điều kiện |
|---|---|---|---|
| GoPeak | 2.3.9 | Cho AI quan sát/thao tác editor và hỗ trợ workflow Godot | Godot 4.x, Bun 1.3.3+; cài từ release chính thức của `HaD0Yun/Doyunha-Gopeak` |
| Context7 | 3.2.4 | Tra cứu tài liệu Godot/API hiện hành | Node.js 18+; thiết lập bằng `npx ctx7 setup` |

Hai MCP là công cụ phát triển tùy chọn, không phải runtime dependency, build dependency hay service production. Không đưa signing key, provisioning profile, production token, player data hoặc bí mật vận hành vào prompt, cấu hình MCP hay repository.

**MCP preference:** chấp nhận GoPeak và Context7 như development tooling tùy chọn; dự án vẫn phải build, test và vận hành được khi không cài hai công cụ này.

### Required Architecture Spikes

1. **Network Arena:** tăng từ 8 lên 24 headless client trong arena nhỏ, chạy simulation 30 Hz; đo CPU, RAM, băng thông, correction và packet impairment. Không client nào được có authority với damage, loot hoặc kết quả. Đây là cổng chọn hướng networking, chưa phải bằng chứng 100 người.
2. **World Streaming Slice:** greybox 2×2 km gồm một POI dày, một compound thưa, đường, cầu, bờ biển và hành trình xe ở tốc độ tối đa. Việc qua ranh giới streaming không được tạo gameplay-breaking hitch hoặc làm sai projectile, door, vehicle, collision và audio state.
3. **Mobile Device Slice:** chạy cùng lát cắt trên Android/iOS minimum và recommended class; kiểm tra mục tiêu 45/60 FPS, working memory ≤3 GB, lifecycle interruption và thermal soak theo budget đã khóa.
4. **Water & Boat Slice:** dùng `WaterVolume` gameplay mang tính giải tích, swimming và boat authority; visual shader có biến thể desktop/mobile. Mặt sóng hình ảnh không thay độ cao/norm gameplay và server/client không được bất đồng trạng thái nước.

Sau các spike ban đầu, scale gate tiếp tục theo 50 rồi 100 protocol-mixed client, final-circle stress và 45-minute mobile soak trước khi khóa production content.

### World and Map Production Implications

- Cell logic 250×250 m chỉ là giả thuyết benchmark, không phải quyết định đã khóa. Một lưới duy nhất không được ép gánh terrain tile, entity streaming, building HLOD, navigation, audio zone và server query nếu cadence của chúng khác nhau.
- Chuỗi chứng minh bắt buộc: **0,5 km² Combat Sandbox → 2×2 km World/Network/Mobile Slice → 8×8 km streaming greybox → 100-client và mobile gates → khóa 18 POI/420 building**.
- Quy trình authoring bản đồ: coast/hydrology → terrain → POI graph → road graph → modular building placement → cover/loot → seed, traversal, sightline, streaming và performance validation.
- Nước gameplay không dùng fluid simulation thời gian thực. Server dùng volume/depth/flow giản lược và buoyancy có kiểm soát; client render sóng, bọt và phản chiếu theo quality profile.
- Building phải tách gameplay shell/collision/opening khỏi desktop/mobile visual variant để automated parity test có thể chứng minh cùng một cover và line of sight.

### Architecture Decision Scope

Các phạm vi dưới đây được khóa tại phần Architectural Decisions và được triển khai chi tiết qua Cross-cutting Concerns, Project Structure và Implementation Patterns:

- Ranh giới module, ownership, dependency direction và lifecycle giữa client, authoritative simulation, shared protocol, backend và tooling.
- Network transport, snapshot schema, delta compression, interest/relevance graph, update tiers, prediction, reconciliation và lag compensation.
- Terrain technology, cell hierarchy, streaming scheduler, origin/coordinate strategy, HLOD, navigation và world-state persistence trong một trận.
- POI/road graph schema, modular building kit, collision/visibility parity, water/swimming/buoyancy và automated map validation.
- Player controller, camera/animation, projectile/vehicle physics và server query contract.
- Platform adapters, semantic input pipeline, signed input-family claim, pool lock, lifecycle/reconnect và device capability handling.
- Backend service boundaries cho identity, party, matchmaking, allocation, statistics, report/block và regional operations.
- Build layout, dependency/version policy, CI, signing, notarization, AAB/TestFlight và secret management.
- Replay-event schema, observability, anti-cheat evidence, privacy/retention và incident investigation.
- Performance budgets, automated gates và failure policy cho desktop, Android, iOS, macOS và dedicated server.

## Architectural Decisions

### Decision Summary

| ADR | Category | Decision | Version | Rationale |
|---|---|---|---|---|
| ADR-01 | Runtime state | Modular authoritative simulation; SceneTree chỉ composition/presentation | Godot 4.7.1 | Client, server và test dùng chung core mà không kéo theo renderer |
| ADR-02 | Networking | ENet/UDP + custom binary replication protocol | Godot 4.7.1 | Kiểm soát bandwidth, relevance và validation ở quy mô battle royale |
| ADR-03 | World partition | Hierarchical multi-grid, một server cho toàn trận | Single precision | Mỗi lớp dữ liệu có cadence riêng mà không chia authority trận |
| ADR-04 | Terrain | Terrain3D editor-only, bake sang `TerrainTileData` | Terrain3D 1.0.2 | Tránh rủi ro runtime GDExtension và Metal trên năm nền tảng |
| ADR-05 | Map authoring | Handcrafted layout + schema/graph + modular kit | Custom Resources | Giữ chất lượng chiến thuật thủ công nhưng vẫn tự động kiểm định |
| ADR-06 | Simulation | Fixed 30 Hz; custom character motor; server-authoritative Jolt vehicles | Jolt built-in | Thứ tự mô phỏng rõ mà không giả định physics engine deterministic |
| ADR-07 | Lifecycle | Explicit application và match phase state machines | Typed GDScript | Bao phủ reconnect, interruption và trạng thái mobile tường minh |
| ADR-08 | Gameplay data | Custom Resources được validate/bake thành immutable manifest | Versioned schema | Giữ client/server parity bằng manifest và hash bất biến |
| ADR-09 | Asset loading | Threaded cell streaming, prefetch corridor và bounded cache | ResourceLoader | Khống chế hitch và working memory của bản đồ 8×8 km trên mobile |
| ADR-10 | Persistence | Local settings + secure token; profile backend; match state in-memory | ConfigFile/backend | Không trao authority gameplay cho dữ liệu local |
| ADR-11 | Control plane | Nakama + CockroachDB; không xử lý combat realtime | Nakama 3.40.0; CockroachDB 26.2.3 | Dùng đường database production được Nakama hỗ trợ chính thức |
| ADR-12 | Server fleet | Một Linux headless server/pod; Agones/Kubernetes allocation | Agones 1.59.0; Kubernetes 1.35.6 | Dùng cặp phiên bản nằm trong ma trận tương thích Agones |
| ADR-13 | Platform/input | Semantic command, platform adapter, signed input-family claim | Shared protocol v1 | Giữ pool công bằng nhưng dùng chung giao thức gameplay |
| ADR-14 | UI | Godot Control + presenter/view-state | UX contract v1 | Chia sẻ state giữa desktop/mobile mà không khóa layout |
| ADR-15 | Audio/voice | Godot native audio; EOS Voice sau cross-platform spike | Godot 4.7.1; portal artifact gated | Cô lập provider và không để SDK chưa chứng minh chặn core |
| ADR-16 | AI | Không bot trong Standard; Training AI là module riêng | Training module v1 | Bảo toàn định vị sinh tồn PvP, không giấu bot trong trận thường |
| ADR-17 | Security/replay | Server-first anti-cheat + evidence event log | Evidence schema v1 | Điều tra từ bằng chứng server thay vì tin client |
| ADR-18 | Build/versioning | Five-platform CI; exact match protocol/content compatibility | Build manifest v1 | Ngăn client và server khác luật vào cùng trận |
| ADR-19 | Observability | Correlated logs/metrics/crashes, PII boundary | Telemetry schema v1 | Chẩn đoán xuyên control/match plane mà không trộn PII |
| ADR-20 | Dependency policy | Plugin/native service chỉ được promote sau spike và parity gate | ADR-controlled | Chỉ đưa dependency vào production khi đã có bằng chứng |
| ADR-21 | Reconnect/AFK | Phase-specific 60s/120s grace; neutral input, vulnerable avatar, authoritative timeout outcome | Reconnect policy v1 | Không cho disconnect tạo protection, bot replacement hoặc kết quả mơ hồ |
| ADR-22 | Spectator communication | Teammate-follow; team voice được giữ, mọi world/context/Map ping mới bị cấm sau elimination | Spectator policy v1 | Giữ social continuity nhưng không tạo kênh information/marker ngoài hợp đồng |
| ADR-23 | Player audio controls | Chỉ expose Master/World/Team Voice/UI/Music; tactical child buses nội bộ | Audio controls v1 | Ngăn footstep boost/EQ/night-mode tạo lợi thế |
| ADR-24 | Localization | `StringId` + immutable Việt/Anh `LocaleCatalog`; English fallback; domain không phát display string | Locale schema v1 | Loại hard-coded UI string và giữ presenter/domain boundary |
| ADR-25 | Input identity | Physical key cho gameplay, logical Unicode cho text; captured unaccumulated relative mouse delta | Input policy v1 | Giữ remap nhất quán qua layout/OS và tránh sensitivity bị UI/stretch chi phối |
| ADR-26 | Map interaction | Full Map north-up, minimap heading-up; zoom 0,75×–6× và bounded pan | Map UX policy v1 | Giữ orientation/extent nhất quán và không mở thêm thông tin theo platform |

### State Management

**Approach:** Modular authoritative simulation kết hợp composition và state machine.

- Gameplay core không phụ thuộc UI, renderer, raw input hoặc platform SDK.
- Authoritative entities dùng typed data/component composition; không xây ECS/native core trước khi profiling chứng minh nhu cầu.
- Direct call/interface dùng cho command có một owner; typed events dùng khi có nhiều consumer.
- Không dùng global event bus cho combat state.
- Autoload chỉ dành cho `AppKernel`, `BuildInfo`, `PlatformGateway` và service thực sự sống toàn ứng dụng.

Application lifecycle:

```text
Boot
 -> Authenticate
 -> Frontend
 -> Matchmaking
 -> LoadingMatch
 -> InMatch
 -> Results
 -> Frontend
```

`Interrupted`, `Backgrounded` và `Reconnecting` là nhánh có kiểm soát, không phải scene tùy ý.

Match lifecycle:

```text
Allocated
 -> Warmup
 -> Aircraft
 -> Active
 -> Finished
 -> ResultCommitted
 -> Shutdown
```

#### ADR-21 — Reconnect/AFK ownership và outcome

- Party service sở hữu roster/Ready; disconnect phải clear Ready ngay.
- Queue/match service giữ ticket/seat tối đa **60 giây** trong queue/loading/pre-aircraft; hết hạn release seat/ticket, không tạo match defeat vì aircraft chưa rời.
- Sau aircraft, live match server giữ cùng seat tối đa **120 giây**. Server phát neutral command, avatar vẫn hoàn toàn vulnerable/lootable; không invulnerability, autopilot hoặc bot replacement.
- Nếu avatar chết, team bị loại hoặc match kết thúc trong grace, authoritative outcome đó thắng timeout; reconnect chỉ vào spectator/Results tương ứng.
- Hết 120 giây sau aircraft: áp leave-after-aircraft defeat, direct-eliminate avatar và drop loot tại authoritative position; không tạo DBNO/revive window do timeout. Team còn sống tiếp tục.
- Connected-AFK sau 120 giây không input chỉ tạo telemetry/moderation signal; avatar giữ neutral input và vulnerability, không auto-kick/protect/move.
- Reconnect token bind account/match/seat, có expiry/nonce/replay protection, rotate sau success và chỉ lưu secure storage. Một seat chỉ có một session active.

#### ADR-22 — Spectator communication

- Spectator chỉ follow teammate sống, không free camera và chỉ nhận information target hợp lệ.
- Spectator được nghe/nói trong đúng team voice channel theo cùng PTT/mute/block/permission cho tới team elimination/leave.
- Sau elimination, mọi world/context/Map ping hoặc tactical marker mới bị server từ chối bằng `spectator_ping_forbidden`; spectator vẫn nhận ping hợp lệ của teammate sống.

### Networking and Replication

- Dedicated server giữ authority với movement validity, projectile, damage, inventory, loot, vehicle, zone và result.
- ENet/UDP chỉ là transport; protocol không phụ thuộc NodePath, RPC name hoặc scene tree.
- Mỗi message có type ID, protocol version, sequence, tick, payload length và validation rule.
- Không dùng `var_to_bytes()`/object deserialization cho packet không tin cậy.
- Reliable ordered channels dành cho session, phase, inventory và interaction state.
- Unreliable-sequenced channels dành cho input và snapshots; input/snapshot dùng channel riêng để tránh head-of-line blocking.
- Snapshot delta, relevance graph và update tier theo loại thực thể.
- Client prediction/reconciliation chỉ áp dụng cho state được phép; client impact/hit marker vẫn chờ server confirmation.
- Handshake phải khớp `build_id`, `protocol_version`, `gameplay_schema_version` và `content_manifest_hash`.
- Voice không đi qua game transport.

### World, Terrain and Map

- Bản đồ đặt tâm tại origin, phạm vi ±4 km và dùng single-precision build.
- Một process quản lý toàn trận; không có zone-server handoff trong v1.0.
- `WorldCellId` là định danh logic ổn định, không phải NodePath.
- Terrain, entity streaming, building HLOD, navigation, audio và server spatial query dùng grid/cadence độc lập.
- Cell 250×250 m chỉ là baseline thử nghiệm cho entity streaming.

`MapDefinition` là schema tiến hóa theo consumer, không phải “setup all world models”:

1. Story 5.1 chỉ tạo terrain tile index, height/collision/material mask, coastline/`WaterBody` reference và dependency manifest.
2. Streaming Story thêm `WorldCellId`, bounds, readiness/lease metadata.
3. Layout/building/weather Story mới thêm `PoiDefinition`/compound, `RoadGraph`, `BuildingPlacement`, cover/loot/vehicle/dock, navigation/connectivity và validation rules tương ứng.
4. Mỗi extension cần schema version, migration, validator, generated-file guard và client/server gameplay hash; không tạo field trước consumer.

Terrain3D chỉ dùng trong editor. Bake pipeline tạo `TerrainTileData` có version gồm height, collision, material mask, mesh LOD và dependency manifest.

Hình học POI/đường/nhà được thiết kế thủ công. Seed trận chỉ điều khiển loot, phương tiện, đường bay, thời tiết và bo; không sinh lại hình học runtime.

Map presentation policy (ADR-26):

- Full Map của Standard cố định north-up; minimap player-heading-up.
- Full Map zoom clamp 0,75×–6× theo authored map extent; pan clamp để ít nhất 20% authored bounds còn trong viewport.
- Zoom/pan không thay layer được phép, information distance hoặc damage cue world-camera-relative giữa platform.

### Physics and Combat Simulation

- Authoritative gameplay tick cố định 30 Hz; rendering/interpolation chạy độc lập.
- Người chơi dùng custom kinematic `CharacterMotor`, không dùng client-owned rigid body.
- Jolt xử lý collision/query và vehicle rigid bodies nhưng server luôn quyết định kết quả.
- Không giả định Jolt deterministic giữa client và server.
- Đạn dùng ballistic integration và swept collision segment; không tạo một `RigidBody3D` cho mỗi viên.
- Server giữ hitbox history giới hạn để lag compensation tối đa 150 ms; không rewind toàn bộ world.
- Shot timestamp bị clamp theo session clock và latency envelope.
- Xe được dự đoán hạn chế ở client, nhận server correction và không được tự báo va chạm gây sát thương.
- `WaterVolume` cung cấp mặt nước gameplay, depth, swimming state và buoyancy giản lược. Visual wave không thay đổi gameplay surface.

### Gameplay Data and Asset Management

Authoring flow:

```text
Typed Custom Resources
 -> Schema validation
 -> Stable ID assignment
 -> Bake
 -> Gameplay manifest + platform asset packs
```

- Gameplay definitions dùng stable ID, không dùng đường dẫn file làm network identity.
- Client và server cùng tải immutable gameplay manifest.
- Server artifact không chứa texture, mesh presentation, shader hoặc audio không cần thiết.
- Desktop/mobile visual packs được phép khác LOD/material nhưng phải chung collision và visibility contract.
- Không có remote live-event hoặc DLC dependency trong v1.0.

Loading flow:

- Critical combat assets preload trước trận.
- World cells dùng `ResourceLoader.load_threaded_request()`.
- `WorldStreamManager` dự đoán corridor theo camera, hướng di chuyển và tốc độ xe.
- Main-thread instantiation có frame budget.
- Cache có high/low-water mark; mobile dùng budget riêng.
- Cell không được unload khi còn projectile, vehicle, door transition hoặc gameplay reference chưa giải quyết.

### Scene and UI Architecture

Scene roots:

- `BootRoot`
- `FrontendRoot`
- `MatchClientRoot`
- `MatchServerRoot`
- `TrainingRoot`

`MatchClientRoot` chứa presentation world, replicated proxies, camera, input adapters, HUD và audio. `MatchServerRoot` chỉ chứa simulation, spatial query, protocol và telemetry.

UI dùng Godot `Control`, `Container`, `Theme` và 30-component UX contract đã hoàn tất. UI nhận immutable `ViewState` từ presenter; widget không đọc packet hoặc authoritative entity trực tiếp.

Desktop và mobile dùng cùng presenter/state nhưng layout composition khác. Safe area, Touch layout editor và interruption state nằm ở presentation/platform layer.

Localization boundary (ADR-24):

- Domain/presenter phát stable `StringId` + typed formatting arguments, không phát display string.
- `LocaleCatalog` immutable, versioned, có Việt/Anh; English là fallback và missing key phát bounded telemetry.
- Number/date/plural/OS-key alias thuộc locale/label provider; text entry dùng logical Unicode/IME, không trộn với gameplay key identity.
- Theme/presenter/StringId foundation phải xuất hiện trong Foundation Wave Story 1.7–1.8; production hardening thuộc Story 8.1–8.3.

### Audio and Voice

- Godot `AudioServer` và `AudioStreamPlayer3D` là baseline cho SFX, attenuation, bus, occlusion và near/far gun layers.
- Player-facing controls chỉ gồm `Master`, `World`, `Team Voice`, `UI`, `Music`.
- `Ambience`, `Footsteps`, `Weapons` và `Vehicles` là child buses nội bộ dưới `World`; không expose volume riêng, EQ, compressor preset hoặc night mode có thể boost tactical cue.
- `Voice` route nội bộ map tới player-facing `Team Voice`; Music có owner riêng và chỉ chạy menu/Results/sau server-confirmed victory.
- Spatial-audio implementation phải vượt bài kiểm tra xác định cung 30° ≥85%; nếu native audio không đạt, chỉ thay spatial-renderer adapter thay vì đưa toàn bộ gameplay sang middleware.
- Competitive propagation gate đo sprint/run/walk footsteps 70/45/20 m; unsuppressed gunshot tới 1.000 m và suppressed 400–600 m theo weapon profile. Surface material cần phổ âm phân biệt; aircraft/airdrop ambience không được che hoàn toàn nearby gunfire.
- EOS Voice là provider ưu tiên cho voice đội sau five-platform spike.
- `VoiceProvider` quản lý join/leave channel, mute/block, permission, route change và background behavior.
- Voice channel chỉ dành cho đội; không proximity voice trong v1.0.
- Eliminated teammate spectator vẫn dùng đúng team voice channel nhưng không được tạo tactical ping/marker mới theo ADR-22.
- EOS SDK/GDExtension không được truy cập gameplay state hoặc signing secrets.
- EOS Voice là lựa chọn service-level; artifact SDK lấy từ Epic Developer Portal phải được ghi version, checksum và license provenance trước khi `native/eos_voice` được promote. Khi chưa vượt voice spike trên năm nền tảng, build dùng `UnsupportedVoiceAdapter` hoặc test double; v1 không qua E6-S4 nếu cổng này thất bại.

### Persistence and Backend

Local:

- `ConfigFile` lưu graphics, audio, accessibility và control preferences.
- Touch layout lưu theo device class.
- Session/reconnect token chỉ lưu qua platform secure storage.
- Local file không có authority với profile hoặc match result.

Backend:

- Nakama quản lý account linking, session, party, queue, input pool, profile/statistics và report/block workflow.
- CockroachDB lưu account link, profile, statistics, audit và idempotent match result theo đường production được Nakama hỗ trợ chính thức.
- Nakama realtime socket phục vụ party/matchmaking; không mang combat snapshots.
- Matchmaker tìm nhóm người chơi nhưng `MatchAllocator` riêng chịu trách nhiệm cấp Godot match server.
- Match state sống trong RAM của dedicated server; reconnect chỉ nối lại trận còn tồn tại.
- Match server ghi evidence log/checkpoint ra object storage và gửi result có chữ ký theo API idempotent.

### Match Server Fleet

- Dedicated server xuất thành Linux x86-64 headless OCI image.
- Một pod/process phục vụ đúng một trận.
- Agones quản lý `Fleet`, `GameServerAllocation`, health và shutdown.
- Kubernetes chạy theo vùng; Nakama chọn vùng trước khi allocation.
- Local/CI dùng container trực tiếp; production dùng cùng server artifact.
- Server nhận một allocation secret ngắn hạn, không nhận database credential.
- Scale gate đo đồng thời CPU, RAM, network egress, cost/match và cost/player-hour.

### Platform, Identity and Input Pools

```text
Keyboard/Mouse | Touch | Gyro
              -> GameplayCommand
              -> NetworkInputFrame
              -> Authoritative Simulation
```

- Platform token được trao đổi lấy internal `AccountId`; gameplay không dùng trực tiếp Apple/Google/store ID.
- Input family claim do backend ký, server xác minh và khóa suốt trận.
- Mixed party được công bố trước khi ready.
- Gắn keyboard/mouse trên mobile không âm thầm đổi pool.
- Platform SDK nằm sau identity, entitlement, invite, voice permission, lifecycle, secure storage và build-info adapters.
- Adapter failure trả capability/state rõ, không thay luật gameplay.
- Gameplay binding lưu physical key identity; logical/Unicode chỉ dành text entry. Binding label do OS/localized label provider tạo, không dùng làm command identity.
- Desktop aim đọc captured unaccumulated relative mouse delta (`Input.use_accumulated_input = false`) và không dùng delta đã bị viewport stretch/UI scale biến đổi. Platform thiếu capability tương đương phải công bố fallback state, không silently đổi acceleration/sensitivity.

### AI Scope

- Standard match không chứa bot hoặc NPC chiến đấu.
- Training bots dùng finite-state machine và navigation đơn giản trong module riêng.
- Training AI không dùng production matchmaking, stats hoặc match result.
- Không có đường code tự động thay người chơi rời trận bằng bot.

### Security, Anti-cheat and Evidence Replay

- Validate message type, length, range, cadence, sequence, ownership và state transition trước khi sử dụng.
- Session, join và reconnect ticket có expiry, nonce và replay protection.
- Server kiểm tra speed, acceleration, stance, fire cadence, ammo, inventory mutation và shot origin.
- Client integrity/attestation chỉ là tín hiệu bổ sung; desktop-only anti-cheat không được trở thành điều kiện công bằng mà mobile không thể đáp ứng.
- Evidence replay gồm event log có sequence, shot/damage/loot/zone/result events và periodic state checkpoint.
- Không cung cấp full replay hoặc kill-cam cho người chơi trong v1.0.
- Report liên kết với match ID, player ID và evidence window; block không thay đổi kết quả trận.

### Observability and Privacy

- `trace_id`, `match_id`, `account_id_hash`, `build_id` và region được liên kết từ control plane tới match server.
- Metrics gồm tick time, relevance count, snapshot bytes, correction, hit validation, streaming hitch, memory và thermal session.
- Crash reporting nằm sau adapter để thay provider mà không đổi gameplay.
- PII/account data tách khỏi combat telemetry.
- Không ghi raw voice, signing secret hoặc platform token vào log.
- Retention, consent, deletion và export tuân theo policy đã khóa tại **Security and Privacy Rules**.

### Build, Deployment and Compatibility

- CI tạo Windows, Linux, macOS Universal 2, Android ARM64 AAB, iOS archive và Linux headless server.
- Dependency lock/SBOM/canonical CI/five-platform build smoke và signing-secret boundary thuộc Foundation Wave Story 1.3–1.5; không được chờ release qualification.
- Linux headless OCI hardening thuộc Story 6.9 ngay sau allocator; telemetry/dashboard/runbook/canary/rollback foundation thuộc Story 6.10 trước secure admission và scale.
- Release Epic chỉ qualification, performance/security hardening và RC decision; không tạo lần đầu dependency, CI, container hoặc observability control.
- Apple signing/notarization chạy trên isolated macOS runner; secret không xuất hiện trong repository, artifact log hoặc MCP.
- Dependency được pin bằng version/checksum và tạo SBOM.
- Người chơi chỉ vào cùng trận khi `protocol_version` và `content_manifest_hash` tương thích chính xác.
- Backend có thể phục vụ N/N-1 trong staged rollout nhưng không trộn client build trong cùng match.
- Plugin/GDExtension mới chỉ được promote sau desktop, Android, iOS và macOS build/parity spike.

### Verified Technology Baselines

Xác minh ngày **2026-07-22**:

| Technology | Version/status |
|---|---|
| Godot | 4.7.1-stable |
| Terrain3D | 1.0.2-stable, editor-only |
| Nakama | 3.40.0 |
| Nakama Common | 1.47.0 |
| Nakama Godot SDK | 3.4.0; bọc adapter và contract test vì release đã cũ |
| CockroachDB | 26.2.3; Regular release cho production control-plane data |
| Agones | 1.59.0 |
| Kubernetes | 1.35.6; nằm trong dải 1.33–1.35 được Agones 1.59.0 hỗ trợ |
| Go | 1.26.5 cho standalone backend tooling |
| EOS Voice | Service đã chọn; chỉ promote portal SDK artifact sau khi pin version/checksum và vượt five-platform voice spike |

Nguồn xác minh: [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/), [Terrain3D](https://github.com/TokisanGames/Terrain3D), [Nakama release notes](https://heroiclabs.com/docs/nakama/getting-started/release-notes/), [Nakama production database support](https://heroiclabs.com/docs/nakama/getting-started/install/linux/), [Nakama Godot SDK](https://github.com/heroiclabs/nakama-godot), [CockroachDB releases](https://www.cockroachlabs.com/docs/releases), [CockroachDB 26.2 version](https://www.cockroachlabs.com/docs/v26.2/cockroach-version), [Agones compatibility](https://agones.dev/site/docs/installation/), [Kubernetes releases](https://kubernetes.io/releases/), [Go releases](https://go.dev/dl/), [EOS Voice](https://onlineservices.epicgames.com/en-US/services/voice).

### Architecture Decision Records

- **ADR-01 — Modular authoritative simulation:** chọn ranh giới domain rõ thay cho Node-centric state để client, server và test harness dùng chung luật mà không kéo theo rendering.
- **ADR-02 — ENet/custom protocol:** giữ ENet như transport đã có trong Godot nhưng sở hữu serialization, relevance và validation để đáp ứng 100 người/budget băng thông.
- **ADR-03/04/05 — Data-driven handcrafted world:** giữ quyền kiểm soát chiến thuật của level designer đồng thời cho phép streaming, bake và automated validation trên desktop/mobile.
- **ADR-11/12 — Control plane tách match plane:** Nakama/CockroachDB xử lý identity/social/persistence; Agones cấp tiến trình Godot authoritative riêng cho từng trận trên cặp phiên bản Kubernetes được hỗ trợ.
- **ADR-13/15 — Provider adapters:** platform SDK và voice không được xuyên vào gameplay core; mọi provider phải vượt five-platform parity gate.
- **ADR-17 — Server-first integrity:** anti-cheat nền tảng là validation/evidence phía server; client attestation không được tự quyết định kết quả.
- **ADR-20 — Evidence-based promotion:** plugin, native module hoặc middleware chỉ trở thành production dependency sau spike đo được và ADR cập nhật.
- **ADR-21/22 — Reconnect và spectator fairness:** disconnect không tạo protection; timeout/outcome do live server quyết định, spectator giữ team voice nhưng mất quyền tạo tactical marker.
- **ADR-23/24 — Audio/localization boundary:** tactical buses không được expose; mọi text đi qua `StringId`/`LocaleCatalog` thay vì display string trong domain.
- **ADR-25/26 — Input/Map identity:** physical gameplay key + unaccumulated relative mouse; Full Map north-up với zoom/pan bounds cố định.

## Cross-cutting Concerns

Các quy tắc dưới đây áp dụng bắt buộc cho mọi module và mọi implementation agent.

### Error Handling

**Strategy:** typed result object cho lỗi dự kiến, fail-closed tại security/authority boundary và process-level fatal handler cho lỗi không thể phục hồi.

Không dùng exception vì GDScript không cung cấp `try/catch`.

| Cấp | Ý nghĩa | Xử lý |
|---|---|---|
| Rejected | Input không hợp lệ hoặc hành động không được phép | Trả result code; không log ERROR |
| Recoverable | Lỗi network, asset, voice hoặc platform có thể thử lại | Log WARN, chuyển state phục hồi |
| Match-critical | Có thể làm sai authoritative result | Fail closed, loại hành động hoặc kết thúc trận có evidence |
| Process-fatal | Corrupt state, manifest sai hoặc invariant bị phá | Flush diagnostics và thoát an toàn |

Online match không bao giờ pause vì lỗi của một client. Lỗi presentation được fail-soft; lỗi authority, protocol và content compatibility phải fail-closed.

```gdscript
class_name OperationResult
extends RefCounted

var is_ok: bool
var code: StringName
var value: Variant
var context: Dictionary

static func success(result_value: Variant = null) -> OperationResult:
    var result := OperationResult.new()
    result.is_ok = true
    result.code = &"OK"
    result.value = result_value
    return result

static func failure(
    error_code: StringName,
    error_context: Dictionary = {}
) -> OperationResult:
    var result := OperationResult.new()
    result.is_ok = false
    result.code = error_code
    result.context = error_context
    return result
```

```gdscript
func request_cell(cell_id: Vector2i) -> OperationResult:
    if not _manifest.has_cell(cell_id):
        return OperationResult.failure(
            &"WORLD_CELL_UNKNOWN",
            {"cell_x": cell_id.x, "cell_y": cell_id.y}
        )

    return OperationResult.success(_queue_cell_load(cell_id))
```

- Error code được khai báo tập trung, có prefix như `NET_`, `WORLD_`, `AUTH_`, `PLATFORM_`.
- Không hiển thị raw backend/SDK error cho người chơi; UI dùng localized message key.
- `assert()` chỉ dùng cho invariant trong debug build, không thay runtime validation.
- Không được bỏ qua result hoặc dùng empty `else` để nuốt lỗi.

### Logging

**Format:** structured JSON event.
**Destination:** console/local ring buffer trên client; stdout collector trên server.

Trường chuẩn:

```text
timestamp_utc
level
service
subsystem
event
build_id
trace_id
match_id
server_tick
region
account_id_hash
fields
```

| Level | Sử dụng |
|---|---|
| ERROR | Hệ thống thất bại hoặc authoritative integrity bị đe dọa |
| WARN | Lỗi đã phục hồi, input bị reject bất thường hoặc degraded service |
| INFO | Lifecycle milestone: login, queue, allocation, match start/end |
| DEBUG | State transition và diagnostic chi tiết trong development |
| TRACE | Packet/entity-level diagnostics, chỉ bật trong phiên điều tra giới hạn |

```gdscript
GameLog.warn(
    &"world_cell_load_failed",
    {
        "cell_id": cell_id,
        "result_code": result.code,
        "attempt": retry_count
    }
)
```

Quy tắc:

- Production code không gọi `print()`/`printerr()` trực tiếp ngoài bootstrap logger.
- Không log raw token, email, IP đầy đủ, voice data, signing secret hoặc platform identifier.
- Hot path không ghi log theo entity/tick; dùng counter/histogram.
- DEBUG/TRACE bị compile hoặc runtime-gate và có expiry.
- Client release giữ bounded ring buffer để đính kèm crash/report sau khi lọc dữ liệu.
- Server log ra stdout; collector chịu trách nhiệm lưu, index và rotation.
- Event name dùng `snake_case`, mô tả sự việc đã xảy ra.

### Configuration Management

Configuration được chia thành năm lớp:

1. **Build identity:** version, platform, protocol và feature compilation.
2. **Gameplay data:** Custom Resources được validate/bake và hash.
3. **Platform profile:** renderer, memory, LOD và device capability.
4. **Player settings:** graphics, audio, accessibility và input layout.
5. **Operations configuration:** endpoint, maintenance, telemetry sampling và service kill switch.

```gdscript
class_name BuildIdentity
extends Resource

@export var build_id: StringName
@export var protocol_version: int
@export var gameplay_schema_version: int
@export var content_manifest_hash: String
@export var target_platform: StringName
```

Quy tắc:

- Gameplay code truy cập config qua typed facade, không đọc file tùy ý.
- Gameplay balance không hardcode trong controller hoặc UI.
- Mọi config có schema version, range validation và default rõ ràng.
- Client và server phải dùng cùng gameplay manifest hash.
- Environment secret đi qua secret mount/environment injection, không nằm trong Resource hoặc repository.
- Remote operations config không được đổi damage, recoil, loot odds, bo, pool policy hoặc số bot.
- Kill switch chỉ được tắt queue, region hoặc provider lỗi và phải hiện trạng thái rõ cho người chơi.
- Không remote live-event, FOMO schedule hoặc runtime asset injection trong v1.0.

Ví dụ: nếu EOS Voice lỗi, operations config có thể tắt voice và hiển thị degraded-service banner; nó không được thay voice bằng gameplay ping tự phát hiện kẻ địch.

### Event and Signal System

**Pattern:** ba communication lane riêng biệt.

1. **Direct typed call** cho command có một owner.
2. **Godot signal** cho notification local/presentation.
3. **Deterministic domain event queue** cho authoritative simulation và evidence replay.

Không dùng một global string-based event bus cho mọi hệ thống.

```gdscript
signal health_view_changed(current: int, maximum: int)

func apply_snapshot(snapshot: PlayerSnapshot) -> void:
    if snapshot.health != _view_state.health:
        _view_state.health = snapshot.health
        health_view_changed.emit(
            _view_state.health,
            _view_state.maximum_health
        )
```

```gdscript
_domain_events.push(
    DomainEvent.damage_applied(
        server_tick,
        sequence_id,
        attacker_id,
        victim_id,
        weapon_id,
        damage
    )
)
```

Quy tắc:

- Command dùng thể chủ động: `FireWeaponCommand`.
- Domain event dùng quá khứ: `DamageApplied`.
- Signal dùng `snake_case` quá khứ: `health_changed`.
- Authoritative event có `tick`, `sequence`, stable type ID và schema version.
- Domain events được xử lý theo thứ tự xác định tại tick boundary.
- Presentation signal không được ghi vào evidence replay.
- Backend async command có idempotency key.
- Không emit signal để yêu cầu một thao tác cần phản hồi đồng bộ; dùng interface/direct call.

### Time, Seeds and Identity

- Gameplay dùng `ServerTick`, không dùng wall-clock time.
- Timeout local dùng monotonic clock.
- UTC chỉ dành cho log, certificate, retention và operations.
- Match seed do server tạo và ghi vào match metadata.
- Mỗi random stream có purpose ID riêng: loot, vehicle, zone, weather.
- Không dùng một global RNG khiến thêm hiệu ứng hình ảnh làm đổi kết quả loot.
- Network/gameplay identity dùng stable numeric/string ID, không dùng NodePath hoặc scene instance ID.

```gdscript
var loot_rng := MatchRandom.stream(match_seed, &"loot")
var zone_rng := MatchRandom.stream(match_seed, &"zone")
```

### Concurrency and Thread Ownership

- Main thread sở hữu SceneTree, Node lifecycle và Jolt interaction.
- Worker thread chỉ đọc immutable DTO hoặc xử lý IO, decompress, decode và validation không chạm SceneTree.
- Dữ liệu qua thread boundary phải immutable hoặc ownership-transfer rõ.
- Async world request có generation/cancellation ID để kết quả cũ không instantiate sau khi người chơi đã rời vùng.
- Không giữ Node reference trong background task.

Ví dụ: cell request generation 42 hoàn tất sau khi corridor đã chuyển sang generation 43 thì dữ liệu generation 42 bị đưa vào cache hoặc hủy, không được attach vào world.

### Debug and Development Tools

Available tools:

- debug command registry có permission;
- network/tick/bandwidth overlay;
- relevance-cell và streaming overlay;
- terrain seam/collision/LOD overlay;
- TPP head-line-of-sight visualizer;
- projectile và lag-compensation history viewer;
- vehicle correction và physics-contact viewer;
- water depth/buoyancy viewer;
- audio radius/occlusion viewer;
- input-family/Touch/Gyro ownership overlay;
- deterministic seed runner;
- network impairment và headless client harness;
- evidence-log inspector.

```gdscript
if OS.has_feature("debug"):
    DebugRegistry.register_command(
        &"world.show_stream_cells",
        _show_stream_cells,
        DebugPermission.DEV_LOCAL
    )
```

Activation rules:

- Development tools cần debug build và `--dev-tools`.
- Không dùng hidden key sequence trong player release.
- Cheat command không được gửi từ client vào production online match.
- Server operator command cần authenticated control plane, permission và audit event.
- Release client có thể giữ read-only performance overlay nếu không lộ thông tin đối thủ.
- Debug draw và TRACE capture có bounded duration để không phá performance.

### Security and Privacy Rules

Telemetry được phân loại:

- **Essential operations:** crash, security, matchmaking, server health và integrity evidence.
- **Optional analytics:** UX/funnel và tuning telemetry không cần cho vận hành trận.

Retention baseline:

| Data | Retention |
|---|---:|
| Operational logs | 30 ngày |
| Crash diagnostics | 90 ngày |
| Raw gameplay telemetry | 90 ngày |
| Aggregated non-PII metrics | 13 tháng |
| Unreported match evidence | 30 ngày |
| Evidence gắn report/dispute | 180 ngày hoặc tới khi case đóng |
| Raw voice | Không ghi/không lưu |

- Account/profile tồn tại tới khi người chơi yêu cầu xóa hoặc tài khoản bị đóng.
- Luồng xóa mục tiêu hoàn tất trong 30 ngày, trừ legal/security hold được ghi nhận.
- Region/legal review có thể rút ngắn retention; kéo dài cần ADR và privacy approval.
- Account identity và combat telemetry lưu ở boundary khác nhau.
- `account_id_hash` dùng keyed hash theo environment; raw ID chỉ xuất hiện trong access-controlled account/evidence store.
- Player-facing privacy UI phân biệt essential data với optional analytics.

### Mandatory Implementation Checklist

Mọi subsystem mới phải có:

- typed public interface;
- explicit owner và lifecycle;
- error/result contract;
- structured log events;
- metrics cho hot path thay vì per-frame log;
- config schema và validation;
- test seam hoặc failure injection;
- cleanup/disconnect behavior;
- platform/mobile lifecycle behavior nếu liên quan;
- security/privacy classification;
- debug inspection path;
- server/client authority declaration.

## Project Structure

### Organization Pattern

**Pattern:** Domain-driven monorepo, với layer boundary trước và gameplay domain bên trong.

**Rationale:** OutSurvive cần chia sẻ luật gameplay giữa client và dedicated server nhưng phải ngăn rendering, UI, platform SDK và backend xâm nhập authoritative simulation.

### Directory Structure

```text
outsurvive/
├── game/
│   ├── project.godot
│   ├── export_presets.cfg
│   ├── addons/
│   │   ├── nakama/
│   │   └── third_party/
│   ├── src/
│   │   ├── shared/
│   │   │   ├── kernel/
│   │   │   ├── contracts/
│   │   │   ├── diagnostics/
│   │   │   ├── simulation/
│   │   │   │   ├── movement/
│   │   │   │   ├── combat/
│   │   │   │   ├── ballistics/
│   │   │   │   ├── inventory/
│   │   │   │   ├── loot/
│   │   │   │   ├── health/
│   │   │   │   ├── match/
│   │   │   │   ├── zone/
│   │   │   │   ├── vehicles/
│   │   │   │   ├── water/
│   │   │   │   └── training/
│   │   │   ├── world/
│   │   │   │   ├── coordinates/
│   │   │   │   ├── cells/
│   │   │   │   ├── spatial/
│   │   │   │   └── map_schema/
│   │   │   ├── protocol/
│   │   │   │   ├── codec/
│   │   │   │   ├── messages/
│   │   │   │   ├── snapshots/
│   │   │   │   ├── validation/
│   │   │   │   └── versions/
│   │   │   └── data/
│   │   │       ├── definitions/
│   │   │       ├── identifiers/
│   │   │       ├── manifests/
│   │   │       └── validation/
│   │   ├── client/
│   │   │   ├── bootstrap/
│   │   │   ├── application/
│   │   │   ├── networking/
│   │   │   ├── prediction/
│   │   │   ├── replication/
│   │   │   ├── input/
│   │   │   │   ├── semantic/
│   │   │   │   ├── keyboard_mouse/
│   │   │   │   ├── touch/
│   │   │   │   └── gyro/
│   │   │   ├── presentation/
│   │   │   │   ├── characters/
│   │   │   │   ├── weapons/
│   │   │   │   ├── vehicles/
│   │   │   │   ├── effects/
│   │   │   │   └── camera/
│   │   │   ├── streaming/
│   │   │   ├── ui/
│   │   │   │   ├── presenters/
│   │   │   │   ├── view_states/
│   │   │   │   ├── navigation/
│   │   │   │   └── components/
│   │   │   ├── audio/
│   │   │   ├── voice/
│   │   │   ├── settings/
│   │   │   └── lifecycle/
│   │   ├── server/
│   │   │   ├── bootstrap/
│   │   │   ├── match_host/
│   │   │   ├── connections/
│   │   │   ├── authority/
│   │   │   ├── replication/
│   │   │   ├── relevance/
│   │   │   ├── lag_compensation/
│   │   │   ├── spatial/
│   │   │   ├── evidence/
│   │   │   ├── allocation/
│   │   │   └── shutdown/
│   │   ├── platform/
│   │   │   ├── ports/
│   │   │   ├── desktop/
│   │   │   ├── android/
│   │   │   ├── ios/
│   │   │   ├── macos/
│   │   │   └── mock/
│   │   └── devtools/
│   │       ├── commands/
│   │       ├── overlays/
│   │       ├── inspectors/
│   │       └── impairment/
│   ├── scenes/
│   │   ├── boot/
│   │   ├── frontend/
│   │   ├── match_client/
│   │   ├── match_server/
│   │   ├── training/
│   │   ├── entities/
│   │   │   ├── characters/
│   │   │   ├── weapons/
│   │   │   ├── projectiles/
│   │   │   ├── loot/
│   │   │   └── vehicles/
│   │   ├── world/
│   │   │   ├── buildings/
│   │   │   ├── props/
│   │   │   ├── water/
│   │   │   └── generated_cells/
│   │   └── ui/
│   │       ├── shell/
│   │       ├── frontend/
│   │       ├── hud/
│   │       ├── inventory/
│   │       ├── map/
│   │       ├── settings/
│   │       └── touch_editor/
│   ├── content/
│   │   ├── definitions/
│   │   │   ├── weapons/
│   │   │   ├── ammunition/
│   │   │   ├── attachments/
│   │   │   ├── equipment/
│   │   │   ├── consumables/
│   │   │   ├── throwables/
│   │   │   ├── vehicles/
│   │   │   └── surfaces/
│   │   ├── maps/
│   │   │   └── dao_vong/
│   │   │       ├── map_definition/
│   │   │       ├── terrain_tiles/
│   │   │       ├── world_cells/
│   │   │       ├── poi/
│   │   │       ├── road_graph/
│   │   │       ├── water_bodies/
│   │   │       ├── navigation/
│   │   │       └── validation/
│   │   ├── balance/
│   │   ├── platform_profiles/
│   │   └── generated_manifests/
│   ├── assets/
│   │   ├── characters/
│   │   ├── weapons/
│   │   ├── vehicles/
│   │   ├── buildings/
│   │   ├── environment/
│   │   ├── effects/
│   │   ├── shaders/
│   │   ├── audio/
│   │   │   ├── ambience/
│   │   │   ├── footsteps/
│   │   │   ├── weapons/
│   │   │   ├── vehicles/
│   │   │   ├── ui/
│   │   │   └── music/
│   │   └── ui/
│   │       ├── icons/
│   │       ├── fonts/
│   │       ├── textures/
│   │       └── themes/
│   ├── tools/
│   │   ├── content_bake/
│   │   ├── terrain_bake/
│   │   ├── map_validation/
│   │   ├── asset_validation/
│   │   ├── manifest_builder/
│   │   └── protocol_codegen/
│   └── tests/
│       ├── unit/
│       │   ├── simulation/
│       │   ├── protocol/
│       │   ├── world/
│       │   └── client/
│       ├── integration/
│       ├── deterministic/
│       ├── fixtures/
│       └── golden/
├── native/
│   ├── platform_bridge/
│   ├── eos_voice/
│   └── performance_extensions/
├── backend/
│   ├── nakama/
│   │   ├── modules/
│   │   ├── migrations/
│   │   ├── configuration/
│   │   └── tests/
│   ├── allocator/
│   │   ├── cmd/
│   │   ├── internal/
│   │   └── tests/
│   └── contracts/
│       ├── source/
│       └── generated/
├── infrastructure/
│   ├── containers/
│   ├── agones/
│   ├── kubernetes/
│   │   ├── base/
│   │   ├── development/
│   │   ├── staging/
│   │   └── production/
│   ├── observability/
│   ├── secrets_templates/
│   └── ci/
├── content-source/
│   ├── characters/
│   ├── weapons/
│   ├── vehicles/
│   ├── buildings/
│   ├── environment/
│   ├── terrain/
│   ├── audio/
│   ├── ui/
│   └── licenses/
├── prepare-asset/
│   └── godot-weapons/
├── test-harness/
│   ├── headless_clients/
│   ├── network_impairment/
│   ├── server_load/
│   ├── replay_runner/
│   ├── map_analysis/
│   ├── device_lab/
│   └── reports/
├── docs/
│   ├── architecture/
│   ├── protocols/
│   ├── content_pipeline/
│   ├── operations/
│   └── runbooks/
├── _bmad/
├── _bmad-output/
├── .github/
│   └── workflows/
├── .gitignore
├── .gitattributes
├── LICENSE
└── README.md
```

`prepare-asset/` hiện có được giữ nguyên như khu vực quarantine/staging. Godot không được import trực tiếp asset từ đây; asset chỉ được promote sau khi kiểm tra nguồn, license, naming, scale, topology, LOD và collision.

### System Location Mapping

| System | Location | Responsibility |
|---|---|---|
| Core result/log/config/time | `game/src/shared/kernel`, `diagnostics` | Primitive dùng chung |
| Gameplay identifiers/contracts | `game/src/shared/contracts`, `data` | Stable IDs và typed DTO |
| Movement/stance/vault | `game/src/shared/simulation/movement` | Luật authoritative/prediction |
| Weapons/ballistics/damage | `game/src/shared/simulation/combat`, `ballistics`, `health` | Combat rules |
| Inventory/loot | `game/src/shared/simulation/inventory`, `loot` | Capacity và item state |
| Match/zone/DBNO | `game/src/shared/simulation/match`, `zone`, `health` | Match rules |
| Vehicles/water | `game/src/shared/simulation/vehicles`, `water` | Vehicle và WaterVolume rules |
| Network codec/messages | `game/src/shared/protocol` | Binary protocol |
| Client prediction/replication | `game/src/client/prediction`, `replication` | Local prediction và remote proxies |
| Semantic input | `game/src/client/input` | Keyboard/Mouse, Touch và Gyro adapters |
| Camera/TPP anti-peek | `game/src/client/presentation/camera` | Camera và visibility presentation |
| World streaming | `game/src/client/streaming` | Cell loading/cache/prefetch |
| Dedicated authority | `game/src/server/authority`, `match_host` | Server match state |
| Relevance/snapshots | `game/src/server/relevance`, `replication` | Per-client replication |
| Lag compensation | `game/src/server/lag_compensation` | Bounded hitbox history |
| UI | `game/src/client/ui`, `game/scenes/ui` | Presenter, view state và Control scenes |
| Audio | `game/src/client/audio`, `game/assets/audio` | Gameplay sound presentation |
| Voice | `game/src/client/voice`, `native/eos_voice` | Provider-neutral voice |
| Platform services | `game/src/platform`, `native/platform_bridge` | Identity, lifecycle, storage và permission |
| Training AI | `game/src/shared/simulation/training` | Training-only FSM/navigation |
| Map schema/content | `game/src/shared/world/map_schema`, `game/content/maps` | Map definition và baked data |
| Terrain/map validation | `game/tools`, `test-harness/map_analysis` | Bake và automated gates |
| Backend/control plane | `backend/nakama` | Account, party, queue, profile |
| Match allocation | `backend/allocator` | Nakama-to-Agones allocation |
| Fleet/deployment | `infrastructure/agones`, `kubernetes` | Server hosting |
| Evidence replay | `game/src/server/evidence`, `test-harness/replay_runner` | Investigation log |
| Load/device tests | `test-harness/server_load`, `device_lab` | Scale/mobile gates |
| Raw production assets | `content-source` | DCC/source files và license |
| Unreviewed assets | `prepare-asset` | Quarantine only |

### Naming Conventions

#### Files and folders

- Tất cả folder/file: `snake_case`, ASCII, không khoảng trắng.
- GDScript: `player_motor.gd`.
- Scene: `match_client_root.tscn`.
- Resource: `weapon_ar_556_01.tres`.
- Test: `test_player_motor.gd`.
- Golden fixture: `ballistics_ar_556_100m_v01.json`.
- Generated file thêm header hoặc metadata `generated_do_not_edit`.

#### Code elements

| Element | Convention | Example |
|---|---|---|
| Class | `PascalCase` | `PlayerMotor` |
| Function | `snake_case` + verb | `apply_input_frame()` |
| Variable | `snake_case` | `current_stance` |
| Private member | `_snake_case` | `_snapshot_buffer` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_LAG_COMPENSATION_MS` |
| Enum | `PascalCase` | `MatchPhase` |
| Enum member | `UPPER_SNAKE_CASE` | `AIRCRAFT` |
| Signal | past-tense `snake_case` | `health_changed` |
| Command | `PascalCase` + `Command` | `FireWeaponCommand` |
| Domain event | past-tense `PascalCase` | `DamageApplied` |
| Port | `PascalCase` + `Port` | `PlatformIdentityPort` |
| Adapter | provider/platform + `Adapter` | `IosSecureStorageAdapter` |
| DTO/message | role + `Message`/`Snapshot` | `InputFrameMessage` |
| ID value | domain + `Id` | `WeaponId` |

Stable content ID dùng lowercase namespace:

```text
weapon.ar_556_01
ammo.556_standard
vehicle.jeep_01
map.dao_vong
poi.dao_vong.cang_bac
```

#### Game assets

```text
chr_survivor_base_lod00.glb
wpn_ar_556_01_lod00.glb
veh_jeep_01_lod01.glb
bld_village_a_wall_01.glb
sfx_wpn_ar_556_01_fire_near_01.ogg
sfx_surface_concrete_run_03.ogg
ui_icon_ammo_556.svg
```

- LOD đánh số `lod00`, `lod01`, `lod02`.
- Không dùng tên nguồn không rõ nghĩa như `Object001`.
- Mỗi asset nguồn bên ngoài có license/provenance record.
- Scale 3D luôn theo mét.
- Collision/gameplay shell không có hậu tố platform; visual variant dùng `_desktop` hoặc `_mobile`.

### Architectural Boundaries

Dependency direction:

```text
platform adapters ─┐
client application ├──> shared ports/contracts/simulation
server application ┘

tools ────────────────> shared schemas
backend ──────────────> generated contracts
shared ───────────────> Godot primitives only
```

Quy tắc bắt buộc:

- `shared/` không import `client/`, `server/`, `platform/`, UI hoặc rendering.
- `client/` không import implementation trong `server/`.
- `server/` không import scene, UI, audio hoặc visual assets.
- Platform SDK chỉ xuất hiện trong adapter/native bridge.
- Backend không import GDScript; hai phía chia sẻ generated contract/schema.
- Production runtime không phụ thuộc `tools/`, `test-harness/` hoặc `prepare-asset/`.
- Generated content là read-only; thay đổi phải đi qua source và bake tool.
- Cross-domain call dùng typed port hoặc domain command; không dùng absolute NodePath.
- `res://` path không được dùng làm network/content identity.
- Autoload mới cần ADR; không được tự tạo manager singleton.
- Addon chỉ nằm trong `game/addons` và phải có version, license, checksum, wrapper và owner.
- Native extension chỉ nằm trong `native/`; hot-path extension cần profiling evidence.
- Server export preset phải loại toàn bộ client presentation và raw visual/audio content.
- Mỗi module có test cùng domain hoặc mapping rõ trong `game/tests`.
- `prepare-asset/godot-weapons/_unresolved` không được đi vào build hoặc manifest.

## Implementation Patterns

Các pattern này là quy tắc bắt buộc để mọi implementation agent tạo code tương thích.

### Novel Patterns

#### N-01 — Authority Mirror Pattern

**Purpose:** dùng chung luật gameplay giữa server authoritative và client prediction mà không chia sẻ mutable state hoặc scene tree.

```text
Raw input
 -> GameplayCommand(sequence, client_tick)
 -> Client prediction buffer
 -> ENet input frame
 -> Server validation
 -> Shared simulation
 -> Authoritative snapshot(ack_sequence)
 -> Client restore + replay
 -> Presentation smoothing
```

Components:

- `GameplayCommand`
- `PredictionBuffer`
- shared `CharacterMotor`
- `AuthoritativeSimulation`
- `SnapshotBuilder`
- `ReconciliationController`
- `PresentationSmoother`

```gdscript
func reconcile(snapshot: PlayerSnapshot) -> void:
    _predicted_motor.restore(snapshot.motor_state)

    for frame in _input_history.after(snapshot.ack_input_sequence):
        _predicted_motor.simulate(frame.command, FIXED_DELTA)

    _presentation_smoother.set_target(_predicted_motor.position)
    _input_history.discard_through(snapshot.ack_input_sequence)
```

Rules:

- Client không copy authoritative world thành Node tree rồi tự sửa.
- Simulation correction được áp dụng ngay; presentation offset mới được làm mượt.
- Inventory, loot, damage và result không optimistic-commit.
- Shared simulation không đọc camera, input device hoặc renderer.

#### N-02 — Competitive Visibility Contract

**Purpose:** giữ quy tắc chống nhìn xuyên góc và parity giữa desktop/mobile.

Components:

- gameplay occluder shell;
- head-origin visibility query;
- target sample points;
- door/smoke visibility state;
- server `render_eligible` decision;
- client `VisibilityGate`;
- parity validator.

```text
Head position + target bounds + world occluders
 -> VisibilityQuery
 -> FullyOccluded / Partial / Visible
 -> Replication eligibility tier
 -> Client render gate
```

```gdscript
var visibility := _visibility_query.evaluate(
    viewer.head_position,
    target.visibility_sample_points,
    world_state
)

target_proxy.set_render_eligible(
    visibility != VisibilityResult.FULLY_OCCLUDED
)
```

Rules:

- Query dùng gameplay shell, không dùng visual mesh hoặc platform LOD.
- Cửa, cửa sổ, smoke và tư thế là input của visibility query.
- Server quyết định eligibility; client chỉ có thể ẩn thêm, không tự mở.
- Hidden opponent update có thể bị giảm tần suất/độ chính xác nhưng audio cue phải đi qua contract riêng.
- Mobile asset không được làm mất occluder hoặc mở thêm sightline.

#### N-03 — World Cell Lease Pattern

**Purpose:** ngăn unload cell khi projectile, xe, cửa hoặc entity vẫn còn phụ thuộc.

Cell lifecycle:

```text
Unloaded
 -> Requested
 -> DataReady
 -> GameplayReady
 -> PresentationReady
 -> Active
 -> Draining
 -> Unloaded
```

Một cell chỉ rời `Draining` khi:

- không player/entity residency;
- không projectile/vehicle traversal lease;
- không pending door/world mutation;
- không async job đang commit;
- grace period đã hết.

```gdscript
var lease := _cell_leases.acquire(
    cell_id,
    CellLeaseReason.VEHICLE_TRAVERSAL,
    vehicle_id
)

# Lease được release khi xe đã đi qua và cell kế tiếp GameplayReady.
lease.release()
```

Rules:

- Terrain, entity, HLOD, navigation và audio dùng grid riêng nhưng liên kết qua `WorldCellId`.
- Entity đi qua ranh giới không bị destroy/recreate.
- Async result có generation ID; kết quả cũ không được attach.
- Gameplay readiness phải hoàn tất trước presentation readiness.

#### N-04 — Signed Input Family Claim Pattern

**Purpose:** khóa Touch, Keyboard/Mouse và Mixed pool minh bạch, không silent switch.

Claim chứa:

```text
account_id
input_family
pool_id
party_id
build_id
issued_at
expires_at
nonce
signature
```

```gdscript
func accept_join(request: JoinRequest) -> OperationResult:
    var claim_result := _claim_verifier.verify(request.input_claim)

    if not claim_result.is_ok:
        return OperationResult.failure(&"AUTH_INPUT_CLAIM_INVALID")

    if claim_result.value.input_family != request.reported_input_family:
        return OperationResult.failure(&"AUTH_INPUT_FAMILY_MISMATCH")

    return _lock_input_family(claim_result.value)
```

Rules:

- Claim do control plane ký và match server xác minh.
- Input family bị khóa khi vào trận.
- Platform adapter chỉ tạo semantic command được phép cho family đã khóa.
- Thiết bị ngoài family không làm đổi pool giữa trận.
- Mixed disclosure được ghi vào party/ready state và evidence log.

#### N-05 — Evidence Event Spine Pattern

**Purpose:** một nguồn sự thật cho replay điều tra, anti-cheat, moderation và kết quả trận.

```text
Validated command
 -> Domain state mutation
 -> Committed DomainEvent
 -> Evidence writer
 -> Result projector
 -> Metrics projector
 -> Debug replay runner
```

```gdscript
var event := DamageApplied.new(
    server_tick,
    _event_sequence.next(),
    attacker_id,
    victim_id,
    weapon_id,
    damage
)

_domain_events.commit(event)
```

Rules:

- Event chỉ phát sau khi mutation authoritative thành công.
- Consumer không được sửa ngược simulation state.
- Event có tick, sequence, type ID và schema version.
- Checkpoint định kỳ cho phép dựng lại evidence window.
- Presentation signal và speculative client event không đi vào spine.
- Match result được project từ committed events và gửi idempotently.

#### N-06 — Content Promotion and Bake Gate

**Purpose:** kiểm soát asset nguồn, mobile parity và dữ liệu bản đồ trước khi vào build.

```text
Quarantine
 -> Provenance/license review
 -> Naming/scale/topology validation
 -> Source promotion
 -> Platform import
 -> Gameplay shell generation
 -> Bake
 -> Collision/visibility parity
 -> Manifest hash
 -> Release candidate
```

```gdscript
var report := ContentGate.validate(candidate)

if not report.is_pass:
    return OperationResult.failure(
        &"CONTENT_PROMOTION_REJECTED",
        {"asset_id": candidate.asset_id, "failures": report.failures}
    )

_manifest_builder.include(candidate)
```

Rules:

- `prepare-asset/` không phải runtime source.
- Generated file không chỉnh tay.
- Asset phải có stable ID và provenance record.
- Desktop/mobile variant phải chung gameplay shell.
- Map bake phải chạy route, sightline, seam, water và cell-budget validators.
- Manifest chỉ được ký sau khi mọi gate bắt buộc đạt.

### Standard Patterns

#### S-01 — Ports and Composition-root Injection

Known owner dùng direct typed call; dependency được cung cấp tại bootstrap/composition root.

```gdscript
func configure(
    catalog: GameplayCatalog,
    event_sink: DomainEventSinkPort
) -> void:
    _catalog = catalog
    _event_sink = event_sink
    _is_configured = true

func start() -> void:
    assert(_is_configured)
```

- Không service locator.
- Không `get_node("/root/...")`.
- Optional capability dùng nullable port hoặc explicit `UnsupportedAdapter`.

#### S-02 — Factory and Pool Creation

Authoritative entity và presentation scene dùng factory riêng.

```gdscript
var entity_state := _entity_factory.create_authoritative(
    entity_id,
    definition_id,
    spawn_transform
)

var proxy := _presentation_factory.create_proxy(
    entity_state.kind,
    entity_state.entity_id
)
```

- Chỉ factory được gọi `PackedScene.instantiate()` cho replicated entity.
- VFX, casing, impact và UI marker có thể pool.
- Object pool bắt buộc gọi `reset_for_reuse()`.
- Không pool object giữ authoritative identity nếu reset chưa được kiểm chứng.

#### S-03 — Guarded State Machine

Mọi state transition quan trọng dùng enum, transition table và guard.

```gdscript
func try_transition(next: MatchPhase) -> OperationResult:
    if not _allowed_transitions[current_phase].has(next):
        return OperationResult.failure(
            &"MATCH_TRANSITION_REJECTED",
            {"from": current_phase, "to": next}
        )

    var previous := current_phase
    current_phase = next
    phase_changed.emit(previous, current_phase)
    return OperationResult.success()
```

Không dùng nhóm boolean như `is_alive`, `is_dead`, `is_knocked`, `is_reviving` để mô tả cùng một state machine.

#### S-04 — Read-only Catalog Access

Runtime truy cập gameplay data bằng stable ID qua catalog đã validate.

```gdscript
var weapon_result := _gameplay_catalog.get_weapon(command.weapon_id)

if not weapon_result.is_ok:
    return OperationResult.failure(&"COMBAT_WEAPON_UNKNOWN")

var weapon: WeaponDefinition = weapon_result.value
```

- Không gọi `load()` rải rác trong gameplay.
- Không dùng path làm ID.
- Catalog immutable sau match start.
- Missing definition là match-critical manifest error.

#### S-05 — Fixed-tick Phase Scheduler

Không để từng gameplay Node tự quyết định thứ tự `_physics_process()`.

```gdscript
const PHASES: Array[SimulationPhase] = [
    SimulationPhase.INGEST_INPUT,
    SimulationPhase.MOVEMENT,
    SimulationPhase.PHYSICS_QUERY,
    SimulationPhase.COMBAT,
    SimulationPhase.INVENTORY,
    SimulationPhase.ZONE,
    SimulationPhase.COMMIT_EVENTS,
    SimulationPhase.BUILD_SNAPSHOTS
]

func simulate_tick(context: TickContext) -> void:
    for phase in PHASES:
        for system in _systems_by_phase[phase]:
            system.simulate_tick(context)
```

Phase order là protocol contract; thay đổi cần deterministic regression test và ADR.

#### S-06 — Decode, Validate, Apply Protocol

Packet không bao giờ mutate state trực tiếp sau decode.

```gdscript
var decode_result := _codec.decode(packet)

if not decode_result.is_ok:
    return _reject_peer(&"NET_DECODE_FAILED")

var validation_result := _validator.validate(
    peer_context,
    decode_result.value
)

if not validation_result.is_ok:
    return _reject_message(validation_result.code)

_command_router.apply(peer_context, decode_result.value)
```

- Reader kiểm tra bounds trước mọi read.
- Message dùng numeric type ID.
- Dictionary/Variant serialization bị cấm trên untrusted transport.
- Unknown type/version bị reject rõ ràng.

#### S-07 — Presenter and Immutable View State

UI không đọc entity, packet hoặc backend SDK trực tiếp.

```gdscript
func present(snapshot: PlayerSnapshot) -> void:
    var next_state := HudViewState.from_snapshot(snapshot)

    if next_state != _current_state:
        _current_state = next_state
        view_state_changed.emit(_current_state)
```

Desktop/mobile view cùng nhận `HudViewState`; chỉ layout scene khác nhau.

#### S-08 — Async Generation and Cancellation

Mọi async request có owner, generation và cancellation path.

```gdscript
func request_corridor(cells: Array[WorldCellId]) -> void:
    _generation += 1
    var request_generation := _generation

    _loader.request_cells(cells, func(result: CellLoadResult) -> void:
        if request_generation != _generation:
            return
        _commit_loaded_cells(result)
    )
```

Callback cũ không được thay state mới hoặc giữ Node reference sau owner shutdown.

#### S-09 — Idempotent Backend Command

Command thay đổi persistence cần idempotency key và version/precondition.

```text
command_id: match:{match_id}:result:{result_sequence}
expected_profile_version: 42
payload_hash: sha256(...)
```

Gửi lại cùng `command_id` phải trả cùng kết quả; payload khác với cùng ID là security error.

#### S-10 — Deterministic and Golden Testing

```gdscript
func test_ballistic_trace_is_stable() -> void:
    var simulation := BallisticSimulationFixture.create(12345)

    simulation.fire(&"weapon.ar_556_01", Vector3.ZERO, Vector3.FORWARD)
    simulation.advance_ticks(90)

    assert_eq(
        simulation.state_hash(),
        &"ballistics_ar_556_90_ticks_v03"
    )
```

- Simulation test dùng fixed seed/tick.
- Protocol codec dùng golden byte fixture.
- Map validator dùng golden reports.
- Bug network/hitreg phải có replay fixture trước khi sửa.

### Consistency Rules

| Pattern | Convention | Enforcement |
|---|---|---|
| Dependencies | Ports + composition root | Dependency scan/review |
| Entity spawn | Factory only | Static search + test |
| State | Guarded state machine | Unit tests |
| Data | Stable ID + catalog | Manifest validation |
| Simulation update | Fixed scheduler phases | Deterministic tests |
| Networking | Decode → validate → apply | Protocol tests/fuzzing |
| UI | Presenter → immutable view state | Boundary review |
| Async | Generation/cancellation | Lifecycle tests |
| Backend writes | Idempotency key | Integration tests |
| Randomness | Purpose-specific seeded stream | Deterministic tests |
| Asset promotion | Content gate only | Bake CI |
| Errors | Typed result; no silent failure | Lint/review |
| Logging | `GameLog`; no direct `print()` | Static check |
| Platform SDK | Adapter boundary only | Dependency scan |
| Generated files | Read-only | CI regeneration check |
| Client authority | Forbidden for competitive state | Security tests |

### Prohibited Shortcuts

Implementation agents không được:

- tạo manager/autoload mới để né dependency injection;
- replicate trực tiếp scene tree;
- dùng client transform làm authoritative hit position;
- load asset bằng arbitrary path trong gameplay;
- instantiate replicated entity ngoài factory;
- thêm `_physics_process()` tùy ý cho authoritative system;
- thêm boolean state chồng chéo thay cho state machine;
- chỉnh generated terrain/world/protocol file bằng tay;
- đưa asset từ `_unresolved` vào manifest;
- gọi platform SDK ngoài adapter;
- thêm desktop/mobile gameplay branch;
- dùng raw wall time hoặc global RNG cho gameplay;
- nuốt lỗi hoặc chỉ ghi log rồi tiếp tục mutation không hợp lệ.

## Architecture Validation

### Validation Summary

| Check | Result | Notes |
|---|---|---|
| Decision compatibility | PASS | 26 ADR nhất quán; reconnect, spectator communication, audio controls, localization, input và Map policy đã khóa |
| GDD coverage | PASS | 16/16 hệ thống cốt lõi và 5/5 nhóm yêu cầu kỹ thuật được bao phủ |
| Pattern completeness | PASS | 6 novel patterns và 10 standard patterns bao phủ toàn bộ 10 tình huống implementation bắt buộc |
| Epic mapping | PASS | 10/10 Epic trong backlog chuẩn có module, boundary, owner và pattern triển khai tương ứng |
| Document completeness | PASS | Có executive summary, decision/version/rationale, cross-cutting rules, project tree, naming và prohibited shortcuts |
| Placeholder and conflict scan | PASS | Không còn template marker, placeholder hoặc quyết định kiến trúc chưa khóa |

### Coverage Report

**Core systems — 16/16:** input/movement, camera, combat, prediction/lag compensation, loot/inventory, match lifecycle, zone, world streaming, vehicles/water, platform/matchmaking, voice/ping, desktop/mobile UI, audio, profile/report, evidence/observability và five-platform build/operations đều có ownership cùng vị trí triển khai.

**Technical requirement groups — 5/5:** desktop, Android/iOS, authoritative server, backend/operations và platform/input đều có baseline, budget hoặc validation gate.

| Epic | Architecture mapping |
|---|---|
| E1 — Nền tảng người sống sót | Shared movement simulation, semantic input, client camera/presentation; N-01, N-04 |
| E2 — Đấu súng đáng tin cậy | Combat/ballistics, server lag compensation, evidence; N-01, N-05, S-05, S-06 |
| E3 — Loot và quản trị sinh tồn | Inventory/loot simulation, immutable catalog, evidence events; S-04, N-05 |
| E4 — Vòng đời battle royale | Match/zone state machines, lifecycle/reconnect, match host; S-03, S-05 |
| E5 — Khám phá/thoát hiểm vùng thử nghiệm | Progressive map schema, multi-grid cells, vehicles/water, content bake; N-03, N-06 |
| E6 — Multiplayer cạnh tranh | Protocol, allocation, container, observability, authority, relevance, signed input family; N-01, N-04, N-05, S-06 |
| E7 — Đảo Vọng production | Full-map content/validators, streaming/parity gates; N-03, N-06, S-10 |
| E8 — Độ rõ và tiếp cận | Presenter/view state, UI/audio/voice/platform adapters; S-07 |
| E9 — Hồ sơ và tính toàn vẹn | Nakama/CockroachDB, account/profile/report/product-integrity policy; S-09 |
| E10 — Qualification và release | Platform qualification, performance/security hardening, RC evidence/decision; S-10 |

**Decision coverage — 26/26:** 20 boundary/technology ADR gốc cộng reconnect/AFK, spectator communication, player audio controls, localization, input identity và Map interaction đều có quyết định owner + testable contract.

### Issues Resolved

- Chuyển database baseline development-only sang CockroachDB 26.2.3 để dùng đường production được Nakama hỗ trợ chính thức.
- Khóa Kubernetes 1.35.6 để nằm trong ma trận 1.33–1.35 của Agones 1.59.0.
- Bổ sung Executive Summary và rationale cho toàn bộ Decision Summary.
- Chuyển EOS Voice thành service-level decision có portal artifact version/checksum gate và five-platform spike bắt buộc.
- Ghi nhận GoPeak/Context7 là MCP development tooling tùy chọn, không thuộc runtime, build hoặc production dependency.
- Đồng bộ các mô tả quyết định và privacy policy đã được khóa; loại bỏ câu chữ tương lai không còn đúng.
- Cập nhật source reference sang `_bmad-output/planning-artifacts/epics.md` chuẩn 10 Epic và loại bản 9-Epic khỏi validation input.
- Khóa reconnect/AFK 60s/120s, spectator voice/ping, player-facing audio bus, localization boundary, physical-key/raw-mouse và Map north-up/zoom policy.
- Đưa dependency/SBOM/CI vào Foundation Wave, container/observability vào online Epic và giữ release Epic chỉ qualification/hardening.

### Validation Date

2026-07-26

**Overall result:** PASS. Kiến trúc đã revalidate theo backlog chuẩn 10 Epic; không còn UX/Architecture decision gate mở. Scale, mobile, network, streaming, water/boat, voice và release vẫn phải vượt empirical Story gates trước content lock/v1.

## Development Environment

### Prerequisites

| Nhóm | Yêu cầu |
|---|---|
| Engine | Godot Engine Standard 4.7.1-stable và export templates 4.7.1; không dùng .NET editor |
| Source/content | Git và Git LFS; asset chưa duyệt chỉ ở `prepare-asset/`, không import vào Godot project |
| Automation | Python 3.12+ cho BMAD/validation scripts; Go 1.26.5 cho standalone backend tooling |
| Server/backend | OCI-compatible container runtime cho local integration; Nakama 3.40.0, CockroachDB 26.2.3 và Agones/Kubernetes chỉ được đưa vào theo version manifest đã khóa |
| Android | OpenJDK 17; Platform-Tools 35.0.0+, Build-Tools 35.0.1, Platform 35, CMake 3.10.2.4988404 và NDK r28b 28.1.13356709 |
| Apple | Máy macOS có Xcode và command-line tools; Godot export templates, Apple Team/Bundle ID và signing assets được quản lý ngoài repository/MCP |
| Device lab | Ít nhất một Android và một iOS thuộc minimum class, cộng thiết bị recommended class cho performance/thermal gate |

Yêu cầu mobile được đối chiếu theo [Godot 4.7 Android export](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_android.html) và [Godot 4.7 iOS export](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_ios.html). macOS release phải tuân theo [code signing và notarization của Godot 4.7](https://docs.godotengine.org/en/4.7/tutorials/export/exporting_for_macos.html).

### AI Tooling (MCP Servers)

| MCP Server | Purpose | Install Type |
|---|---|---|
| GoPeak 2.3.9 | Quan sát/thao tác Godot editor và hỗ trợ scene workflow | Tùy chọn; cài từ official `HaD0Yun/Doyunha-Gopeak` release, yêu cầu Bun 1.3.3+ |
| Context7 3.2.4 | Tra cứu tài liệu Godot/API theo phiên bản | Tùy chọn; Node.js 18+ và `npx ctx7 setup` |

Hai MCP không phải runtime/build dependency. Không đưa signing key, provisioning profile, production token, player data hoặc bí mật vận hành vào prompt, MCP config hay repository. Build, test và release pipeline phải chạy được khi không có MCP.

### Setup Commands

Chạy từ repository root sau khi story scaffold đã tạo `game/project.godot`:

```bash
godot --version
git lfs install
python3 --version
go version
godot --headless --path game --editor --quit
godot --editor --path game
```

Lệnh đầu tiên phải trả đúng Godot `4.7.1.stable`. Import headless phải kết thúc thành công trước khi chạy editor hoặc test; CI dùng cùng editor/export-template version và checksum.

### First Steps

1. Tạo `project-context.md` từ tài liệu này để mọi AI implementation agent tự động nhận boundary, pattern, budget và prohibited shortcuts.
2. Implementation Readiness đã được re-run trên GDD, backlog chuẩn 10 Epic, UX và Architecture; chỉ bắt đầu Phase 4 khi report mới nhất là `READY`.
3. Chạy Sprint Planning, rồi Create Story cho Story 1.1 Clean Godot Standard local bootstrap; chưa promote asset từ `prepare-asset/`.
4. Cấu hình GoPeak/Context7 nếu muốn dùng, nhưng giữ chúng ngoài runtime/build graph.
5. Triển khai Combat Sandbox 8 client trước; chỉ mở rộng World Streaming Slice và 24→50→100 client sau khi gate trước vượt chuẩn.
