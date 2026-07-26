# Validation Report — OutSurvive

- **DESIGN.md:** `DESIGN.md`
- **EXPERIENCE.md:** `EXPERIENCE.md`
- **Run at:** 2026-07-22T02:27:58+07:00
- **Raw reviewer counts:** Critical 0 · High 13 · Medium 15 · Low 4

## Resolution update — Final

Reviewer Gate bên dưới được giữ nguyên như snapshot tại thời điểm review. Sau resolution, mock promotion, visual check và editorial pass, trạng thái chuẩn là **12 Closed · 5 Accepted dependency · 0 Open**. Hai spine hiện `status: final`; chi tiết bằng chứng ở `final-ux-verification.md` và `.working/visual-checks/README.md`.

## Overall verdict

Tại Reviewer Gate, hai spine là một contract **adequate** cho định hướng kiến trúc: source và token resolve, component có parity đầy đủ, IA có cấu trúc và ba hành trình bao phủ vòng lặp chính. Các khoảng trống được liệt kê bên dưới đã được resolve; xem mục **Resolution update — Final** để biết trạng thái hiện tại.

Ba lens đồng thuận rằng ranh giới cạnh tranh cốt lõi đang đúng: không footstep radar, damage number, loot score/recommendation, enemy outline hoặc lợi thế thông tin HUD trên ultrawide. Các finding High được xử lý theo cụm nguyên nhân trước khi dựng mockup; Medium/Low được sửa hoặc ghi rõ dependency/acceptance gate.

## Category verdicts

- Flow coverage — **adequate**
- Token completeness — **adequate**
- Component coverage — **strong**
- State coverage — **thin**
- Visual reference coverage — **adequate at Reviewer Gate**
- Bloat & overspecification — **adequate**
- Inheritance discipline — **adequate**
- Shape fit — **strong**

## Findings by severity

### Critical (0)

Không có.

### High (13)

**[Rubric · State coverage] — Multiplayer transition states chưa đủ contract** (`EXPERIENCE.md:101–116,153,290`)
Reconnect, AFK, party leader/ready và ownership transition chưa khóa trigger, authority, timeout và destination.
Fix: thêm transition table cho Party, Queue, Pre-match và Live Match; số backend chưa khóa phải có owner và acceptance gate.

**[Rubric · Inheritance] — Timing lộ bo kế tiếp bị rơi khỏi spine** (`gdd.md:374`; `EXPERIENCE.md:38,81,107,149`)
Map/minimap có thể vô tình lộ bo sớm.
Fix: chỉ render next-zone geometry khi máy chủ xác nhận pha chờ bắt đầu; không prediction/placeholder trước đó.

**[Accessibility/Fairness] — Contrast chưa được khóa sau compositing** (`DESIGN.md:237,244,258,264`)
HUD/panel bán trong chưa có backplate/opacity rule trên cảnh sáng, tối, sương hoặc muzzle flash.
Fix: khóa cơ chế bảo toàn contrast và acceptance screenshot Godot: text ≥4,5:1; icon/focus/state cần thiết ≥3:1.

**[Accessibility/Fairness] — Camera ultrawide chưa có fairness policy** (`DESIGN.md:254`; `EXPERIENCE.md:124,187`)
Mở rộng world view có thể lộ silhouette/góc cover sớm hơn 16:9.
Fix: khóa projection/FOV scaling và matrix 16:9–32:9 cho hai vai, FOV min/max, tường/cửa sổ.

**[Accessibility/Fairness] — Critical alerts tranh chấp** (`DESIGN.md:266`; `EXPERIENCE.md:74,84,131`)
Fire countdown, zone, damage, revive interruption và network có thể xóa/che nhau.
Fix: priority/preemption/lane/lifetime matrix; deadline gây chết phải có kênh không bị banner thấp hơn chiếm.

**[Accessibility/Fairness] — Reticle và ba preset mù màu thiếu visual contract** (`DESIGN.md:11–217`; `EXPERIENCE.md:170`)
Reticle/zone/marker/hit effect chưa có anatomy và mapping triển khai được.
Fix: thêm component reticle, geometry/outline, preset mapping và parity acceptance trên nhiều nền.

**[Accessibility/Fairness] — Spectator information parity còn mở** (`EXPERIENCE.md:110,116,209,251–254`)
Người chết có nguy cơ nhận camera/audio/marker nhiều hơn đồng đội còn sống.
Fix: chỉ follow teammate sống, không free camera/orbit, giữ cùng LOS/audio/data subset và chuyển Results đúng lúc.

**[PC HUD/Input] — Safe-frame và breakpoint chưa triển khai được** (`DESIGN.md:90,254–260`; `EXPERIENCE.md:168,187–189`)
5% chưa gắn với central 16:9 reference rect; 720p/140% có nguy cơ crop/overlap.
Fix: định nghĩa central 16:9 safe-frame, clamp/reflow/overflow và test 720p–4K, 21:9, 32:9 ở 80/100/140%.

**[PC HUD/Input] — Overlay thiếu priority/lane/suppression matrix** (`DESIGN.md:256,264–303`; `EXPERIENCE.md:74–94,131`)
Reticle, damage, HP/ammo, context card và subtitle có thể cùng chiếm một anchor.
Fix: matrix z-order/anchor/lifetime/suppression và stress scene 720p/140%.

**[PC HUD/Input] — Map/Inventory thiếu input-routing contract** (`EXPERIENCE.md:37–39,85–88,107,122,149`)
Click/scroll có thể kích hoạt bắn, ADS, lái hoặc zoom ngoài ý muốn.
Fix: matrix cursor, movement, camera, weapon, vehicle, world audio và close binding cho HUD/Inventory/Map/Pause.

**[PC HUD/Input] — Full remap thiếu action/conflict/recovery rules** (`EXPERIENCE.md:109,120–125,137–143`)
Chưa khóa action bắt buộc, duplicate theo context, reserved binding, mouse extra buttons và rollback.
Fix: action inventory v1.0, conflict classes, required escape path, Apply/Cancel/reset và persistence.

**[PC HUD/Input] — Party/voice/8 ping chặn Squad flow** (`EXPERIENCE.md:89–90,101,116,153,205,243–254`)
Channel, PTT, leader/ready, vocabulary, TTL/cooldown và spam handling còn mở.
Fix: khóa MVP team-only voice và 8 ping có icon/label/source/TTL/cooldown/cancel rules.

**[PC HUD/Input] — Reconnect/spectator thiếu state machine** (`EXPERIENCE.md:104–116,209,251–254`)
Avatar, timeout, DBNO, đội bị loại, target cycling và destination chưa rõ.
Fix: Connecting → Reconnecting → Restored/Timed out/Team eliminated, với acceptance cho từng lifecycle state.

### Medium (15)

**[Rubric · Flow] — Training và onboarding bị gộp** (`EXPERIENCE.md:212,256,290`)
Fix: tách Training; đánh dấu onboarding deferred hoặc định nghĩa flow entry/skip/complete/failure.

**[Rubric · Tokens] — Viền minimap chỉ khoảng 2,90:1** (`DESIGN.md:15,21,147,152,244`)
Fix: đổi border token/cơ chế separation để đạt ≥3:1 nếu load-bearing.

**[Rubric · States] — Spectator/replay/report payload còn mở** (`EXPERIENCE.md:110–116,209–214,254`)
Fix: khóa payload/transition tối thiểu hoặc defer rõ surface không thuộc v1.0.

**[Rubric · Visual references] — Bốn mockup UX-014 chưa được dựng** (`DESIGN.md:260`; `EXPERIENCE.md:193–204`)
Fix: dựng Lobby, Match HUD, Inventory và Map/Phase sau khi đóng High; link inline và distill ngược vào spine.

**[Accessibility/Fairness] — UI scale thiếu minimum rendered size** (`DESIGN.md:53–63,250`; `EXPERIENCE.md:168,187`)
Fix: critical text không dùng caption/label dưới floor; co spacing trước, không truncate ammo/timer/network/revive/fire/friendly-fire.

**[Accessibility/Fairness] — Keyboard focus lifecycle và Map parity chưa khóa** (`EXPERIENCE.md:73,122,140,174`)
Fix: initial focus, trap/return focus và keyboard path cho pan/zoom/marker/action menu.

**[Accessibility/Fairness] — Audio accessibility thiếu parity metric** (`EXPERIENCE.md:172,176`; `gdd.md:463–467`)
Fix: khóa controls/bus, cấm khuếch đại cue chiến thuật và chạy lại metric cung 30° trên mọi output mode.

**[Accessibility/Fairness] — Reduce Motion/Flash thiếu budget** (`DESIGN.md:312`; `EXPERIENCE.md:159–161,176`)
Fix: đặt trần frequency/duration/amplitude/luminance; cue giảm phải giữ state tĩnh/icon/label/audio tương đương.

**[Accessibility/Fairness] — Subtitle queue chưa có no-drop class** (`DESIGN.md:303`; `EXPERIENCE.md:94`)
Fix: capacity, duration, dedupe, preemption và collision rules ở 720p/140%.

**[PC HUD/Input] — Phase anatomy thiếu wait/shrink/countdown/outside state** (`DESIGN.md:147–152`; `EXPERIENCE.md:56,81`)
Fix: thêm phase number, state label, timer và outside-zone state vào minimap-zone-panel.

**[PC HUD/Input] — Teammate identity không nhất quán** (`DESIGN.md:131,183–197`; `EXPERIENCE.md:77,90`)
Fix: mapping số/shape/label nhất quán trên squad row, world ping, compass và map; màu chỉ phụ trợ.

**[PC HUD/Input] — Fire countdown mất khi rời xe** (`EXPERIENCE.md:84,131,151`)
Fix: chuyển card thành world/audio cue sau exit và giữ tới server-confirmed explosion/cancel.

**[PC HUD/Input] — Armor durability thiếu visual anatomy** (`DESIGN.md:178–182`; `EXPERIENCE.md:87,147`)
Fix: thêm current/max, bar và broken hierarchy vào equipment-slot visual spec.

**[PC HUD/Input] — Context prompt không arbitration nhiều action** (`EXPERIENCE.md:82,84–88,131`)
Fix: priority + tap/hold/cycle/secondary action và server-reject behavior.

**[PC HUD/Input] — Damage cue trên Map thiếu hệ quy chiếu** (`EXPERIENCE.md:107,149`)
Fix: luôn screen-relative theo world camera tại hit time, không theo north-up/rotating map.

### Low (4)

**[Rubric · Inheritance] — “7 nhóm HUD” đang được liệt kê thành 6 cụm** (`gdd.md:456`; `EXPERIENCE.md:131,201`)
Fix: nêu rõ 7 loại dữ liệu render qua 6 module vì minimap-zone-panel gộp minimap và phase.

**[Accessibility/Fairness] — Viền map thấp hơn floor 3:1** (`DESIGN.md:147–152,244`)
Fix: tăng contrast hoặc đánh dấu border chỉ trang trí.

**[PC HUD/Input] — Rebind persistence/unsaved state chưa khóa** (`EXPERIENCE.md:93,109,137–143`)
Fix: chọn Apply/Cancel, local/profile persistence và rollback.

**[PC HUD/Input] — Font/key-label overflow mới là NOTE** (`DESIGN.md:228,248–250`; `EXPERIENCE.md:20,143,187–189`)
Fix: fallback glyph/keycap, wrap/ellipsis/tooltip và snapshot Việt/Anh 720p/140%.

## Reviewer files

- `review-rubric.md`
- `review-accessibility-fairness.md`
- `review-pc-hud-input.md`

## Mechanical notes

- Snapshot Reviewer Gate dùng `status: draft`; trạng thái hiện tại của hai spine là `final`.
- Trạng thái hiện tại có 29 color token, đều là hex; mọi `{path.to.token}` reference resolve.
- Trạng thái hiện tại có 25 component và exact parity giữa YAML, DESIGN visual rows và EXPERIENCE behavior rows.
- Ba journey đều có protagonist, bước đánh số, climax và failure path.
- Bốn artifact UX-014 hiện đã được promote vào `mockups/`, link/distill và pass visual acceptance ở hai cấu hình đích.
