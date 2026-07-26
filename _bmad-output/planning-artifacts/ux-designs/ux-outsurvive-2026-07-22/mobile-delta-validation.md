# Mobile UX Delta Validation — OutSurvive 1.1

**Ngày:** 2026-07-22  
**Phạm vi:** Delta UX cho Android/iOS landscape và tác động đa nền tảng lên party/input/lifecycle.  
**Kết quả:** **Pass · 8 Closed · 0 Open · 3 implementation dependencies**.

## Kết luận Reviewer Gate có mục tiêu

| Lens | Kết quả | Bằng chứng / nhận xét |
|---|---|---|
| Touch reachability | **Pass tài liệu** | `touch-stick`, right fire, optional left fire và action group nằm trong safe area; target thường ≥48 logical units, fire/exit/close ≥64. Device-hand playtest vẫn là implementation gate. |
| Information parity | **Pass** | Mobile giữ đúng 7 content group/6 HUD module; không enemy cue, visual footstep, auto-fire, target snap hoặc loot recommendation. |
| Phone/tablet occlusion | **Pass reference** | HUD và Inventory/Map render ở 2340×1080 (20:9), 1920×1080 (16:9), 2048×1536 (4:3); không crop critical control, reticle, close, phase hoặc damage cue. |
| Inventory risk | **Pass** | Single tabbed panel khóa ≤62%; world-risk strip ≥38%; tap-first, drag tùy chọn. |
| Map gestures | **Pass contract** | Pan/pinch/tap/long-press có owner rõ; damage không tự đóng Map; close 64 nằm trong safe area. |
| Lifecycle/recovery | **Pass contract** | Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended; held touch/PTT neutralize. |
| Party/input disclosure | **Pass contract** | Touch, Keyboard/Mouse, Mixed/Keyboard-Mouse pool; Ready clear + acknowledgement; match-lock; không silent bot/pool switch. |
| Accessibility/audio | **Pass contract** | Gyro/haptic tùy chọn, permission theo ngữ cảnh, audio-route interruption; không đổi accessibility thành thông tin chiến thuật. |

## Mechanical verification

| Check | Result |
|---|---|
| Component parity | **Pass** — 30 YAML component = 30 visual rows = 30 behavioral rows; 0 thiếu/thừa. |
| Mobile component delta | **Pass** — đúng 5: `safe-area-root`, `touch-stick`, `touch-look-zone`, `touch-action-button`, `control-layout-editor`. |
| Mock coverage | **Pass** — 6 actual = 6 linked; đúng 2 file có prefix `mobile-`. |
| Mock structure | **Pass** — 2/2 mobile HTML tự chứa; không script, network reference hoặc asset dependency. |
| Lifecycle vocabulary | **Pass** — đủ mọi trạng thái đã phê duyệt trong `EXPERIENCE.md`. |
| Pool policy | **Pass** — đủ Touch/Keyboard-Mouse/Mixed, disclosure, match-lock và no-silent-fallback. |
| Evidence set | **Pass** — 6 PNG: 2 reference × 3 viewport. |

## Visual evidence

- `.working/mobile-visual-checks/hud-20x9.png`
- `.working/mobile-visual-checks/hud-16x9.png`
- `.working/mobile-visual-checks/hud-4x3.png`
- `.working/mobile-visual-checks/inventory-map-20x9.png`
- `.working/mobile-visual-checks/inventory-map-16x9.png`
- `.working/mobile-visual-checks/inventory-map-4x3.png`

## Dependencies được chấp nhận

1. Godot/device lab phải snapshot thêm notch/cutout thật, system gesture, left-handed preset và UI scale 100/120/140% trên thiết bị Android/iOS đại diện.
2. Gameplay/Network Architecture phải khóa reconnect timeout, avatar outcome, signed input-family claim và token recovery; UX chỉ hiển thị state owner trả về.
3. Playtest tay thật phải đo reach, multi-touch ownership, Gyro fatigue, haptic và thermal frame pacing; static HTML không thay thế device playtest.

Các dependency này đã có owner và default an toàn, nên không còn blocker tài liệu UX 1.1.
