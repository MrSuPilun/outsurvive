# Post-Resolution Verification — OutSurvive UX

> **Historical checkpoint — superseded.** Báo cáo này ghi trạng thái trước khi đóng UX-034 và UX-037. Kết quả chuẩn hiện tại là **12 Closed · 5 Accepted dependency · 0 Open** trong `final-ux-verification.md`.

**Scope:** `DESIGN.md`, `EXPERIENCE.md`, `.decision-log.md`, đối chiếu 32 finding qua crosswalk `resolution-audit.md:163-196`.  
**Kết quả:** **10 Closed · 5 Accepted dependency · 2 Still open**.  
**High-equivalent còn lại:** **UX-037 — thiếu bốn visual reference load-bearing**.  
**Medium-equivalent còn lại:** **UX-034 — chưa khóa danh sách audio controls/output modes**.

## Quy ước

- **Closed:** spine + log đã khóa contract và acceptance ở mức tài liệu; test implementation vẫn phải chạy khi build.
- **Accepted dependency:** policy ngoài UX chưa khóa nhưng spine đã nêu owner/gate/default an toàn, nên implementation không được tự suy diễn.
- **Still open:** acceptance của audit chưa được đáp ứng và chưa có gate đủ chặt để ngăn implementation tự chọn.

## Verification UX-021–UX-037

| ID | Status | Exact evidence | Verification |
|---|---|---|---|
| UX-021 | **Closed** | `DESIGN.md:76-85,112-118,314,326-336`; `EXPERIENCE.md:243-249`; `.decision-log.md:39` | Có text floor, key-label overflow, central 16:9 formula, Compact/Base/Large reflow và snapshot matrix 720p–4K/21:9/32:9 ở 80/100/140%; Inventory ≥32% world strip. |
| UX-022 | **Closed** | `DESIGN.md:21,138-156,292-294`; `.decision-log.md:40` | Backplate chữ ≥92%, target 4,5:1/3:1 sau compositing; `border-default` được nâng và ghi khoảng 3,20:1 trên map; `border-subtle` không load-bearing. |
| UX-023 | **Closed** | `DESIGN.md:338-354`; `EXPERIENCE.md:98,163-172,217`; `.decision-log.md:41` | Lane A–E, z-order, P0–P3, preemption/queue/coalesce và subtitle no-drop đã thống nhất; có stress acceptance 720p/140%. |
| UX-024 | **Closed** | `DESIGN.md:318,326-328`; `EXPERIENCE.md:137,243`; `.decision-log.md:42` | V1.0 khóa live-world 16:9 + side matte/chrome không tương tác trên ultrawide; anti-peek theo head line-of-sight và acceptance hai vai/FOV/aspect ratio. Không còn camera policy để implementation tự chọn. |
| UX-025 | **Closed** | `DESIGN.md:29-40,192-205,296-304,383,388-389`; `EXPERIENCE.md:80-82,92-94,201`; `.decision-log.md:43` | Ba preset chỉ đổi token, reticle dual-stroke không enemy-reactive, teammate Circle/1–Diamond/4 nhất quán world/compass/map/squad; geometry/timing/data parity được giữ. |
| UX-026 | **Closed** | `EXPERIENCE.md:110-112,135,140-155`; `.decision-log.md:44` | Input-routing matrix khóa pointer/WASD/camera/fire/vehicle/close/re-arm cho HUD–Inventory–Map–Pause; initial/return focus, sibling recovery, keyboard escape và acceptance click-through đã có. |
| UX-027 | **Accepted dependency** | `EXPERIENCE.md:178-187,370`; `.decision-log.md:45` | Action inventory, primary/secondary, context conflict, required escape, Apply/Cancel/reset/local persistence đã khóa. Raw-input default và Linux display-name được nêu rõ là Architecture gate (`EXPERIENCE.md:180,187`), nên implementation không được tự đặt. |
| UX-028 | **Accepted dependency** | `EXPERIENCE.md:93-94,105,199-201,265,370`; `.decision-log.md:46` | Leader/Ready gate, team-only PTT/mute/volume, đúng 8 ping, identity, TTL/cooldown/replace/cancel đã khóa. Invite provider/voice transport được giao Architecture và channel ngoài team cần GDD change; không còn quyền tự mở proximity/global voice. |
| UX-029 | **Accepted dependency** | `EXPERIENCE.md:107-109,121-125,276,370`; `.decision-log.md:47` | State machine và owner party/matchmaker/match service/live server rõ; story ghi **chưa Ready** tới khi API, timeout/AFK outcome và token security được duyệt. UX cấm tự thêm protection, bot takeover hoặc outcome. |
| UX-030 | **Accepted dependency** | `EXPERIENCE.md:114,127-129,269,313-316,370`; `.decision-log.md:48` | Basic spectator teammate-follow, target cycle, HUD/audio/data parity, no free camera và Results transition đã khóa. Voice sau elimination là Gameplay gate; mặc định không cho tạo marker mới nên implementation không tự tăng thông tin. |
| UX-031 | **Accepted dependency** | `EXPERIENCE.md:115,119,203-207,270,275,316,370`; `.decision-log.md:49` | Minimum Results/replay/report, Pending/Unavailable, receipt/retry/block và no kill-cam đã khóa. Deep payload, retention/privacy/evidence/SLA được defer đúng owner; Report story bị gate tới API/security/privacy. |
| UX-032 | **Closed** | `DESIGN.md:388,396`; `EXPERIENCE.md:85,111,161,195,261`; `.decision-log.md:50` | Đúng 7 content groups qua 6 modules; phase number/wait-shrink/timer/outside state; next-zone chỉ render sau server-confirmed wait start, không placeholder/prediction. |
| UX-033 | **Closed** | `DESIGN.md:387`; `EXPERIENCE.md:88,91,193-197,268,293-295`; `.decision-log.md:51` | Vehicle fire cue sống qua exit, armor durability current/max/broken, context arbitration + action phụ, Map damage cue screen-relative và ≤30° đều có contract/acceptance. |
| UX-034 | **Still open** | Yêu cầu audit: `resolution-audit.md:135-139`; phần hiện có: `EXPERIENCE.md:217,228`; `.decision-log.md:52` | Audio parity/HRTF metric và cấm tactical amplification đã có, nhưng spine chưa liệt kê audio controls/output modes được hỗ trợ hoặc owner gate để khóa danh sách đó. Implementation hiện vẫn có thể tự chọn mode/control. |
| UX-035 | **Closed** | `DESIGN.md:398-406`; `EXPERIENCE.md:215-217,227`; `.decision-log.md:53` | Có budget 120–180ms/≤120ms, pulse ≤1,5Hz, flash area/rate, Reduce Motion/Flash fallback và timing parity; cue gameplay không bị bỏ. |
| UX-036 | **Closed** | `EXPERIENCE.md:24,45-46,117-118,273,324-332`; `.decision-log.md:54` | Field Orientation v1.0 có entry, 4 checkpoint, Skip/Continue/Restart/Complete/failure, replayable, không reward/mastery/stats; Training vẫn là sandbox riêng. |
| UX-037 | **Still open** | `DESIGN.md:324`; `EXPERIENCE.md:22,253-264`; `.decision-log.md:55,61`; filesystem scan: **0** file trong `mockups/`/`wireframes/` | Lobby, Match HUD, Inventory và Map/Phase vẫn chỉ ghi `Mockup planned`; chưa có artifact, inline links, kiểm tra 720p/140%–1080p/100% hoặc distillation ngược. Đây là High-equivalent workflow blocker trước Finalize. |

## Mechanical checks

| Check | Result |
|---|---|
| YAML frontmatter | **Pass** — cả hai spine parse được; `status: draft`; mỗi file có 1 source. |
| Source resolution | **Pass** — `../../gdds/gdd-outsurvive-2026-07-22/gdd.md` tồn tại. |
| Color token shape | **Pass** — 29/29 color values là hex 6 chữ số. |
| Token references | **Pass** — 55 unique `{path.to.token}` references; 0 undefined. |
| Component parity | **Pass** — 25 YAML components = 25 behavioral rows; 0 missing/extra; exact `reticle`. |
| Resolution IDs | **Pass** — UX-021–UX-037 đủ 17/17 trong decision log và đủ 17/17 trong EXPERIENCE assumption index. |
| 32-finding coverage | **Pass** — mọi raw finding có ID trong `resolution-audit.md:163-196`; không finding bị bỏ ngoài 17 cụm. |

## Remaining action

1. **UX-037 / High-equivalent:** dựng và promote bốn mockup, link inline, chạy coverage ở 720p/140% và 1080p/100%, rồi distill quyết định mới vào spine.
2. **UX-034 / Medium-equivalent:** khóa danh sách audio controls/output modes và parity từng mode, hoặc ghi owner/story gate rõ để không cho implementation tự chọn.

Không có High-equivalent blocker nào khác; các mục UX-027–UX-031 được chấp nhận là dependency vì spine đã ghi owner/gate hoặc default an toàn và chặn implementation tự phát minh policy.
