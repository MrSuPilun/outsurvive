---
name: "OutSurvive Experience Spine"
title: "OutSurvive - Game UX Experience Specification"
project: "outsurvive"
document: "EXPERIENCE.md"
status: "final"
form_factor: "Desktop keyboard/mouse + mobile landscape touch"
created: "2026-07-22"
updated: "2026-07-26"
sources:
  - "../../gdds/gdd-outsurvive-2026-07-22/gdd.md"
---

# OutSurvive — Experience Spine

## Foundation

OutSurvive v1.0 hỗ trợ Windows, Linux, macOS, Android và iOS, dựng trên Godot 4.x. Standard là battle royale TPP 100 người với ADS góc nhìn thứ nhất; Keyboard/Mouse và Touch là hai input family, còn controller/console ngoài phạm vi. `DESIGN.md` là hợp đồng thị giác; tài liệu này sở hữu IA, hành vi, trạng thái, input, phản hồi và hành trình.

[ASSUMPTION: UX-004] North-star là indie/commercial, phát hành Việt/Anh. Mọi chuỗi UI phải đi qua `StringId` + `LocaleCatalog` immutable/versioned, hỗ trợ độ dài tiếng Anh dài hơn mà không cắt gameplay-critical label; English là fallback khi thiếu key. Locale/label provider sở hữu plural/date/number và tên phím theo OS; text entry dùng logical Unicode/IME, tách khỏi physical-key identity của gameplay.

GDD là nguồn chuẩn. Hai spine thắng khi xung đột với `.working/`, `imports/`, wireframe hoặc mockup. Hiện `imports/` không có input thị giác; bốn mockup desktop và hai mobile delta reference đã được promote vào `mockups/`, còn mọi quyết định bố cục phải được distill vào hai spine.

[ASSUMPTION: UX-036] Training Grounds là sandbox luyện tập đã có trong GDD; nó không đồng nghĩa với onboarding. Onboarding v1.0 là **Field Orientation** tùy chọn, có thể bỏ qua và chơi lại, dạy thao tác nền mà không tạo reward funnel hoặc trợ chiến trong Standard.

## Information Architecture

[ASSUMPTION: UX-008] IA nông, chống meta-loop thương mại; từ launch đến xác nhận Deploy tối đa ba hành động. Không có News, Store, Reward rail, Daily, Battle Pass hay event carousel.

| Bề mặt | Điểm vào | Mục đích / lối ra |
|---|---|---|
| Sảnh chính | App mở xong | Deploy; party/mode/region; Training; Profile; Settings; Exit |
| Party / Mode / Region | Sảnh chính | Chọn Solo/Duo/Squad, quản lý nhóm/ready/leader, vùng mạng; quay lại hoặc Deploy |
| Xác nhận mạng | Deploy khi không vùng nào đạt ngưỡng | Hiện ping/loss; Continue hoặc Cancel |
| Ghép trận | Deploy | Trạng thái hàng chờ, Cancel; công bố bot nếu là hàng chờ thử nghiệm |
| Sảnh chờ trước trận | Match found | Chuẩn bị 60 giây; vào máy bay |
| Máy bay / Đổ bộ | Tự động | Đọc flight path, chọn điểm rơi, bung dù; vào trận mặt đất |
| Match HUD | Tiếp đất đến khi bị loại/thắng | Chiến đấu, loot, di chuyển, bo và phối hợp |
| Inventory | Trong trận qua Tab | Nearby/backpack và equipment/weapons; đóng về Match HUD |
| Map / Phase | Trong trận qua action được bind | Flight path, bo hiện tại; bo tiếp theo chỉ khi server-confirmed wait bắt đầu; marker, pan/zoom; đóng về Match HUD |
| Pause | Trong trận | Resume; Settings; Leave Match; không pause máy chủ |
| Spectator đồng đội | Bị loại khi đội còn sống | Theo camera đồng đội còn sống với information parity; chuyển mục tiêu; xem tới khi đội bị loại hoặc rời |
| Results / Summary | Trận kết thúc | Placement, thời gian, combat/survival summary tối thiểu từ dữ liệu xác nhận; Report/Block; Play Again; Sảnh chính |
| Profile / Mastery | Sảnh chính | Stats, lịch sử mùa, mastery không sức mạnh; quay lại |
| Field Orientation | Lần mở đầu tiên; Training → Field Orientation | Bốn checkpoint tùy chọn: movement/camera; loot/inventory; fire/ADS; zone/cover; Skip hoặc Complete đều về Sảnh chính |
| Training Grounds | Sảnh chính | Sandbox luyện bia/bot; Settings; Exit to Lobby; không ảnh hưởng stats Standard; Field Orientation là route riêng |
| Settings | Sảnh chính, Pause, Training | Input, gameplay, video, audio, accessibility, language; ngưỡng tự nhặt đạn theo cỡ nằm trong Gameplay → Loot |
| Touch Layout | Settings → Input → Touch | Chỉnh vị trí/kích thước/opacity, left-fire và Gyro; Apply/Cancel/Reset theo lớp thiết bị |
| Report / Block | Results hoặc nguồn friendly-fire | Chọn đối tượng, category tối thiểu và ghi chú tùy chọn; gửi/receipt/retry; quay lại Results |

Party, Inventory, Map và Settings là một cấp từ bề mặt mẹ. Modal xác nhận chỉ sâu thêm một cấp và không xếp chồng.

## Voice and Tone

Giọng hệ thống ngắn, bình tĩnh, có số liệu và không phán xét. Brand voice “survival grounded” nằm trong `DESIGN.md`; microcopy ở đây phải giúp ra quyết định dưới áp lực.

| Ngữ cảnh | Dùng | Tránh |
|---|---|---|
| Mạng | “Ping 168 ms — trận này có thể phản hồi chậm.” | “Kết nối tệ!” |
| Bo | “Pha 4 thu sau 01:30.” | “CHẠY NGAY!!!” |
| Gục/cứu | “Lan đang cứu — 6,2 giây.” | “Heroic revive!” |
| Kho đầy | “Thiếu 12 sức chứa.” | “Loot thất bại.” |
| Friendly fire | “Sát thương đồng đội từ TênNgườiChơi.” | Lời kết tội trước khi có log |
| Kết quả | “Hạng 4 · sống 27:18.” | “Nhận thưởng ngay!” |
| Training | “Kết quả luyện tập không ảnh hưởng thống kê Standard.” | “Cày mastery tại đây.” |

Không dùng giọng hô hào, exclamation mark liên tục, FOMO, scarcity thương mại hoặc lời chế giễu người thua.

## Component Patterns

Hành vi dưới đây ghép 1:1 với `DESIGN.md.Components`.

| Component | Behavioral contract |
|---|---|
| `action-button` | Click/Enter kích hoạt; disabled nói rõ lý do; hành động rời trận dùng xác nhận, không đặt cạnh Resume mà thiếu khoảng cách. |
| `navigation-item` | Tab/arrow hoặc pointer đổi focus; active route duy nhất; không badge engagement. |
| `focus-ring` | Chỉ ra keyboard focus trên mọi control; không bị ẩn khi pointer đã từng dùng; traversal theo thứ tự đọc. |
| `status-banner` | Ưu tiên severity, không quá một banner gameplay-critical cùng lúc; có nhãn, icon và hành động nếu cần. |
| `network-warning` | Hiện khi ping >150 ms hoặc trạng thái mạng cần xác nhận; không tiết lộ dữ liệu đối thủ; tự hạ khi ổn định. |
| `match-hud` | Luôn giữ sáu module persistent và áp priority/lane/preemption của UX-023 cho overlay; không nhận nội dung thương mại. |
| `reticle` | Aim affordance tại tâm: HUD form dùng cho hip-fire/over-shoulder; khi ADS, sight/scope form của cùng contract tiếp quản và HUD form ẩn. Hit confirm chỉ sau server confirmation; không enemy lock, lead/range cue hay damage number. |
| `compass` | Bearing theo camera; marker dùng teammate identity 1–4 nhất quán với squad/map/world ping; không tự khóa/nhận dạng địch. |
| `squad-panel` | Hiện teammate identity 1–4, HP/state, speaking/mute và gục/chết; Reconnecting khác Disconnected/Eliminated bằng label + icon. |
| `health-boost-bar` | Cập nhật theo trạng thái máy chủ; low-health feedback có Reduce Motion fallback; không báo heal hoàn tất trước xác nhận. |
| `weapon-ammo-panel` | Hiện ammo current/reserve, fire mode, stance/weapon context; reload không dự đoán hoàn tất trước server state. |
| `minimap-zone-panel` | Hiện phase number, `WAIT`/`SHRINK`, countdown theo timestamp máy chủ, current/outside-zone state và next zone chỉ từ lúc server xác nhận pha chờ bắt đầu; trước đó không outline/placeholder/prediction. Không loot/enemy/visual footstep radar. |
| `context-prompt` | Chỉ xuất hiện khi action hợp lệ; keycap lấy binding hiện hành; tên động từ trước đối tượng; khi nhiều target dùng arbitration UX-033 và luôn cho truy cập action phụ. |
| `damage-direction-indicator` | Hiện cung 30° theo nguồn hit; trên Map vẫn screen-relative theo camera thế giới tại thời điểm hit, không theo hướng/zoom bản đồ; nhiều hit xếp theo recency, không thành radar lịch sử. |
| `context-action-card` | Dùng chung cho healing, revive, throwable, scope/breath, armor break và vehicle state; xe hiện fuel/HP, bốn lốp và fire countdown 3,0 giây. Fire countdown không đóng chỉ vì người chơi rời ghế; các context khác tự đóng khi quyết định hết hiệu lực. |
| `inventory-panel` | Mở không pause; hai panel tổng ≤68%; đóng bằng Tab/Esc; mọi thay đổi chờ xác nhận inventory server. |
| `item-row` | Quick pickup F mất 0,20 giây/món; drag/drop hoặc action menu thực hiện move/split/drop; lỗi sức chứa giữ item tại nguồn. |
| `equipment-slot` | Chỉ nhận item hợp lệ; attachment gần weapon; giáp/mũ hiện durability current/max bằng bar + số + broken icon; không tự chọn “tốt nhất” hoặc auto-equip vũ khí/giáp/phụ kiện. |
| `map-marker-layer` | Pan/zoom, đặt/xóa marker đội; marker mang identity 1–4 giống squad/compass/world; map không pause, audio thế giới giữ nguyên và không tự suy diễn vị trí địch. |
| `party-panel` | Tối đa bốn thành viên; leader/ready/reconnect/network/voice có label; roster/mode/region đổi thì clear ready; Deploy bị gate tới khi mọi thành viên kết nối đã Ready và không có roster unresolved. |
| `voice-ping-indicator` | Team-only voice với PTT mặc định, mute/volume từng người; quick/radial ping dùng tám intent UX-028, identity 1–4, TTL/cooldown và subtitle no-drop; không biến audio bước chân thành marker. |
| `progress-timer` | Dùng cho heal/revive/hold; di chuyển/chịu sát thương ngắt đúng luật và báo lý do ngắn; không chạy đến 100% giả. |
| `results-table` | Ưu tiên placement, survival time, kills/assists và dữ liệu tự cải thiện; replay summary tối thiểu chỉ dùng event/stat đã xác nhận, không giả kill-cam. Profile dùng đúng field set được định nghĩa trong GDD; Mastery chỉ số/huy hiệu không hết hạn; stats chưa xác nhận hiện Pending. |
| `settings-control` | Value preview không đồng nghĩa lưu; remap được stage, bắt conflict, Apply atomically/Cancel rollback và lưu local qua restart; slider có số; dangerous reset cần xác nhận. |
| `subtitle-line` | System và teammate-ping không bị silently drop: critical line preempt vị trí nhưng line bị preempt vào queue, repeat giống nhau coalesce kèm count; speaker/identity, size và nền tùy chỉnh; không che reticle/prompt. |
| `safe-area-root` | Đọc safe inset từ OS ở launch, rotate/resume và display change; critical control không vượt boundary, layout lỗi phải fallback về preset an toàn. |
| `touch-stick` | Pointer đầu tiên trong vùng nhận movement vector, có dead zone và cancel khi touch mất/OS interrupt; không kéo nhân vật sau khi finger up. |
| `touch-look-zone` | Drag điều khiển camera, tap không tự bắn/ADS; multi-touch tách theo pointer ID để look không cướp fire/action và không đi qua UI control. |
| `touch-action-button` | Press/release phát semantic command tương ứng; hold/toggle theo setting; button bị ẩn/disable phải nêu context và không để stuck action khi interruption. |
| `control-layout-editor` | Drag/resize/sắp opacity theo safe area; Apply atomically, Cancel rollback, Reset theo preset phone/tablet; chặn overlap làm mất fire/exit/close hoặc đường mở Pause. |

## State Patterns

| Bề mặt | Cold / empty / focus | Error / offline / permission / recovery |
|---|---|---|
| Sảnh chính | Skeleton tối giản rồi focus Deploy; không news placeholder | Offline: Deploy disabled, Training/Settings vẫn vào được; retry có trạng thái |
| Party / Mode / Region | Solo là state không party; focus đọc mode + region; roster/mode/region đổi clear Ready | Party service sở hữu roster/leader; invite failure giữ nhóm; Reconnecting có nhãn và gate Deploy tới khi resolved theo UX-029 |
| Xác nhận mạng | Focus Cancel an toàn; số ping/loss và lý do hiện rõ | Continue chỉ sau explicit confirm; Cancel về chọn vùng |
| Ghép trận | Matchmaker sở hữu ticket; elapsed/region/mode; Cancel luôn truy cập trước match lock | Reconnect reattach cùng ticket; timeout/error về sảnh với nguyên nhân; không tự đổi region/mode/trận; bot disclosure trước confirm |
| Sảnh chờ / Máy bay | Match service sở hữu seat; loading giữ weather/flight status đã xác nhận | Reconnect bằng cùng seat/token khi còn hợp lệ; không tự chuyển trận; khi timeout của server hết hạn, chuyển theo outcome do backend đã khóa |
| Match HUD | Alive bình thường; low HP, giáp hỏng, gục, chết, high ping là state riêng | Match server sở hữu avatar/result; Reconnecting → Restored/Timed out/Team eliminated; client không tự suy diễn outcome; armor break là cue ngắn |
| Mobile lifecycle | Active nhận input; Interrupted trung hòa held command; Backgrounded giữ match identity nhưng không giả pause | Reconnecting dùng cùng token; Restored rehydrate server state; Timed out/Team eliminated/Match ended đi đúng destination, không auto-queue trận mới |
| Inventory | Nearby empty giữ label; deterministic focus; input route UX-026 | Over capacity/invalid slot/server reject giữ item nguồn, focus và nêu lý do; không click-through gameplay |
| Map / Phase | Phase + WAIT/SHRINK/timer; next zone chỉ sau server-confirmed wait start; input route UX-026 | Data chậm giữ last-confirmed; [ASSUMPTION: UX-015/UX-033] damage không tự đóng Map, cue screen-relative theo world camera |
| Pause | Focus Resume; trận/world audio vẫn chạy; input route UX-026 | Khi còn hiệu lực, Leave xác nhận “Rời bây giờ được tính là thất bại.”; sau khi đội đã bị loại, bỏ cảnh báo thất bại/hình phạt sai |
| Settings | Rebind staged; Apply/Cancel rõ; Gameplay → Loot có ngưỡng theo cỡ đạn, 0 = tắt | Conflict nêu hai action/context; invalid required action chặn Apply; mic permission denied không loop prompt |
| Spectator | Theo một teammate sống; target cycle remappable; HUD/audio chỉ phản ánh thông tin hợp lệ mà target có | Target mất stream → next valid target/Retry; không free camera; hết teammate → Results |
| Results / Summary | Pending stats có skeleton; minimum summary là placement, survival time, combat/survival stats đã xác nhận | Replay payload sâu deferred; unavailable nêu rõ, không thay bằng kill-cam giả; report offline dùng UX-016 |
| Profile / Mastery | Chưa có trận Standard: empty state trung tính; hiển thị đầy đủ field set được định nghĩa trong GDD và huy hiệu không hết hạn | [ASSUMPTION: UX-016] offline dùng cache có timestamp; không giả cập nhật mastery |
| Field Orientation | Lần đầu focus Bắt đầu; Skip luôn có và cần confirm một lần; checkpoint đã xong có dấu + nhãn | Failure/thoát giữa checkpoint lưu checkpoint gần nhất cục bộ; Retry hoặc về Sảnh chính; không ghi stats/mastery/reward |
| Training Grounds | Sandbox preset có default an toàn; không tutorial gate/reward progress | Asset/server lỗi cho phép quay Sảnh chính; không ghi stats Standard; Field Orientation là route riêng |
| Report / Block | Tối thiểu: target, category, optional note, submit và receipt; taxonomy sâu deferred | Network failure giữ draft; block local có thể áp dụng dù report chờ gửi; retention/security do backend khóa |

[DECISION: ADR-21] Reconnect/AFK timeout và authoritative outcome đã khóa ở phần dưới. Provider invite, taxonomy report sâu và replay payload sâu là capability/dependency của story tương ứng, không phải gate để bắt đầu Foundation Wave; UX chỉ hiển thị state do owner trả về.

### Reconnect ownership và gate

[DECISION: ADR-21; UX-029/UX-043] Luồng chung là `Connected/Active → Interrupted | Connection lost → Backgrounded | Reconnecting → Restored | Timed out | Team eliminated/Match ended`. Party service sở hữu roster/leader và disconnect clear Ready; matchmaker/match service giữ ticket/seat tối đa 60 giây trong queue/loading/pre-aircraft; live match server giữ cùng seat tối đa 120 giây sau aircraft. Khi OS interrupt/background, client phát neutral command frame cuối, bỏ mọi held fire/move/PTT local và giữ cùng identity/token; avatar live vẫn vulnerable/lootable, không invulnerability, autopilot hoặc bot replacement. Death, team elimination hoặc match end trong grace thắng timeout. Hết 120 giây sau aircraft, server direct-eliminate, drop loot tại authoritative position và áp leave-after-aircraft defeat, không tạo DBNO/revive window; connected-AFK chỉ tạo telemetry/moderation signal. Token bind account/match/seat, có expiry/nonce/replay protection, rotate sau success và chỉ một session active trên mỗi seat.

### Spectator information parity

[DECISION: ADR-22; UX-030] Spectator chỉ follow teammate còn sống, không free camera. Sáu module HUD, damage cue, map/compass/phase và audio đều phản ánh đúng dữ liệu mà target hiện có thể biết; không hiện inventory riêng, enemy outline, camera xa hơn, âm thanh mở rộng hoặc marker bí mật. `spectate_next`/`spectate_previous` remappable và bỏ qua target không hợp lệ; khi không còn target, chuyển Results. Spectator được giữ đúng team voice channel theo PTT/mute/block/permission, nhưng mọi world/context/Map ping hoặc tactical marker mới sau elimination bị server từ chối bằng `spectator_ping_forbidden`.

## Interaction Primitives

- Di chuyển WASD; chuột camera/ngắm; Shift sprint; Ctrl walk; C crouch; Z prone; Space jump/vault; Q/E lean; F interact; R reload; G chọn throwable; Tab Inventory.
- Touch landscape dùng `touch-stick` trái, `touch-look-zone` phải, right fire bắt buộc và left fire tùy chọn; action context phát cùng semantic command như Keyboard/Mouse. Pinch/pan/long-press chỉ hoạt động trong surface Map/Inventory được chỉ định, không xuyên sang gameplay.
- ADS, lean, crouch và sprint hỗ trợ hold/toggle. Hip-fire, ADS và từng mức zoom có sensitivity riêng.
- Pointer và keyboard dùng cùng focus model. Esc lùi một cấp; trong Match HUD mở Pause. Mọi chuyển surface tuân focus lifecycle UX-026, không để focus vô hình hoặc mắc trong modal.
- Destructive action như Leave Match dùng confirm surface với hậu quả theo trạng thái trận: trước khi đội bị loại phải nói rõ tính là thất bại; sau khi đội bị loại không gắn hình phạt sai. [NOTE FOR UX: Thời lượng hold và default key cho Map, Ping/Radial, shoulder swap, zeroing, breath hold chưa được nguồn khóa.]
- Ba state ngắm là TPP hip-fire → TPP over-shoulder aim → ADS thứ nhất. Shoulder swap là action remappable. Camera bị đẩy vào phía trước khi sát tường; đối thủ/vật thể bị che hoàn toàn khỏi đường nhìn từ đầu nhân vật không được render chỉ vì camera TPP thấy góc đó. [ASSUMPTION: UX-024] Standard v1.0 render live world trong viewport 16:9 đặt giữa; màn ultrawide dùng side matte/chrome không tương tác, không mở thêm world view. Menu, Settings và Profile có thể dùng toàn chiều rộng. Acceptance: test corner-peek ở hai vai, FOV min/max và mọi aspect ratio không lộ mục tiêu trước head line-of-sight; không pixel ngoài viewport 16:9 chứa player, loot, vehicle, projectile hoặc cue gameplay.
- Không target snap, auto-fire, enemy detection, magnetism hoặc đạn bẻ hướng. Gyro là tùy chọn; aim slowdown/friction không bật mặc định và chỉ được xem xét trong Touch pool sau fairness gate. Prompt luôn lấy binding thực tế từ InputMap hoặc semantic Touch action.

### Input routing khi trận không pause

[ASSUMPTION: UX-026] Server/mô phỏng luôn chạy khi mở Inventory, Map hoặc Pause; input được route rõ để UI click không xuyên sang gameplay.

| Surface | Pointer / focus | World input còn hoạt động | World input bị chặn | Đóng / re-arm |
|---|---|---|---|---|
| Match HUD | Mouse captured; focus thuộc thế giới | Toàn bộ gameplay theo binding | — | Esc mở Pause |
| Inventory | Pointer visible; UI sở hữu click/scroll; keyboard focus riêng | WASD và stance/sprint đã bind vẫn điều khiển nhân vật | Camera-look, fire/ADS, reload, interact, weapon/throwable và vehicle control | Tab/Esc đóng; fire/ADS phải key-up rồi mới re-arm |
| Map | Pointer visible; drag/scroll/arrow điều khiển map | WASD và vehicle drive bindings vẫn live | Camera-look, fire/ADS, reload, interact và weapon/throwable | Map binding/Esc đóng; fire/ADS phải key-up rồi mới re-arm |
| Pause | Pointer visible; focus Resume | Không input gameplay mới; server và world audio vẫn chạy | Movement, camera, weapon, interact, vehicle; held input được release về neutral khi mở | Esc/Resume trở Match HUD; action held cần key-up trước re-arm |

Acceptance: mở/đóng cả ba surface khi đi bộ, ADS, ghế lái, ghế phụ và đang chịu damage; UI click/scroll không tạo phát bắn, drop, zoom hoặc drive ngoài contract, close binding luôn hoạt động và không action nào click-through ở frame chuyển.

[ASSUMPTION: UX-040/UX-043] Trên Touch, mỗi pointer được owner hóa từ touch-down đến release/cancel: movement, look hoặc một action button. Mở Inventory/Map/Pause gửi neutral cho look/fire/ADS/reload/interact/vehicle và chỉ giữ movement nếu surface contract cho phép; close yêu cầu các pointer cũ release trước re-arm. OS interruption, Control Center/Notification Center, cuộc gọi, permission dialog hoặc audio-route change phải cancel toàn bộ pointer và PTT, không replay touch cũ khi trở lại.

### Focus lifecycle

[ASSUMPTION: UX-026] Khi surface mở bằng keyboard, focus đi tới target xác định: Inventory → item hợp lệ đầu/empty action; Map → map canvas; Pause → Resume; Settings → heading/control hiện hành; modal → safe action. Khi item biến mất hoặc server reject, focus chuyển tới sibling gần nhất thay vì về đầu trang. Đóng surface/modal trả focus về control đã gọi hoặc fallback hợp lệ; pointer click đổi active target nhưng không vô hiệu `focus-ring` cho lần điều hướng keyboard tiếp theo. Không có keyboard trap; `ui_cancel` luôn thoát một cấp.

## HUD & Diegetic UI

[ASSUMPTION: UX-006] `match-hud` là overlay phi diegetic tối giản. `compass` trên giữa; `squad-panel` trái; `health-boost-bar` dưới giữa; `minimap-zone-panel` phải; `weapon-ammo-panel` phải dưới; `context-prompt` gần tâm dưới. Các biển báo, landmark, vật liệu và âm thanh trong thế giới là lớp diegetic hỗ trợ định hướng.

[Mockup Match HUD](mockups/match-hud.html) — minh họa sáu module anchor không đổi và alternate vehicle fire chiếm P0 critical action lane.

[ASSUMPTION: UX-040/UX-041] Mobile giữ đúng sáu module và bảy content group: chúng reflow trong `safe-area-root` nhưng không thêm radar/loot/enemy cue. `touch-stick` ở trái dưới, `touch-look-zone` bao phần phải còn trống, fire phải ≥64 và fire trái tùy chọn; stance/ADS/reload/interact/throwable/Map/Inventory/vehicle là `touch-action-button` theo context/reach. [Mobile Match HUD](mockups/mobile-match-hud.html) minh họa phone landscape với safe area và control reach, không phải pixel-perfect implementation.

[ASSUMPTION: UX-017] GDD có đúng **bảy content group** persistent: (1) HP/boost, (2) ammo, (3) stance, (4) direction, (5) minimap, (6) squad state, (7) zone phase. Chúng đi qua **sáu module**: `health-boost-bar`; `weapon-ammo-panel` (ammo + stance); `compass`; `minimap-zone-panel` (minimap + phase); `squad-panel` (ẩn ở Solo); và `reticle` là aim affordance, không phải content group thứ tám. `match-hud` chỉ là container.

[ASSUMPTION: UX-023] Overlay dùng bốn priority và lane cố định:

| Priority | Nội dung | Lane / preemption |
|---:|---|---|
| P0 — lethal/immediate | `damage-direction-indicator`, vehicle fire countdown, action interrupted | Center ring + critical action lane; không bao giờ bị network/prompt/subtitle che |
| P1 — active commitment | heal/revive/use `context-action-card`, `progress-timer` | Lower-center action lane; preempt prompt, không preempt P0 |
| P2 — match/system | `network-warning`, friendly-fire source, reconnect và system `status-banner` | Upper-side system lane; cùng loại coalesce, severity cao hơn thay vị trí và mục cũ vào queue nếu còn giá trị |
| P3 — contextual | `context-prompt`, armor break, throwable/zero/breath hint | Context lane; bị P0/P1 preempt, stale item bị drop thay vì phát muộn |

Sáu module persistent không bị overlay che. `subtitle-line` dùng caption lane riêng: critical system/ping có thể lên đầu nhưng không silently drop line còn giá trị. Stress acceptance tại 1280×720/140% với fire 3 giây + hai hướng damage + high ping + teammate down + prompt + subtitle: reticle, HP/ammo/phase và P0 đọc được trong ≤1 giây; không có hai card tranh cùng anchor.

Không có kill-feed toàn cục dày, damage number, loot recommendation, enemy outline, prediction zone, footstep radar hay banner ngoài trận. Map và Inventory không pause; khi mở Map âm thanh thế giới giữ nguyên, khi mở Inventory dải trung tâm vẫn đọc được.

## Input Schemes

V1.0 có hai input family: Keyboard/Mouse trên Windows/Linux/macOS và Touch trên Android/iOS. Gameplay nhận semantic command chung; prompt cập nhật ngay sau Apply. Godot InputMap/Touch adapter là nguồn binding/action, không hard-code glyph trong scene.

- Mouse: camera/aim và pointer UI; desktop aim dùng captured unaccumulated relative delta với `Input.use_accumulated_input = false`, không dùng delta đã qua viewport stretch/UI scale. Platform thiếu capability tương đương phải công bố fallback state.
- Keyboard: gameplay binding theo GDD; full keyboard navigation cho menu/inventory/settings.
- Touch: layout landscape chỉnh vị trí/kích thước/opacity theo phone/tablet preset; left fire tùy chọn; tap-first UI; Gyro tùy chọn theo hip-fire/ADS/scope.
- Sensitivity: hip-fire, ADS và từng độ phóng; không dùng một slider chung che các value.
- Accessibility: hold/toggle per action; haptic, Gyro, touch dead-zone/reach và Reduce Motion/Flash; Reset theo category và Reset All tách nhau.

[ASSUMPTION: UX-039] Input family được ký và khóa khi match bắt đầu. External Keyboard/Mouse trên mobile chỉ đổi family ngoài trận và buộc requeue. Party thuần Touch vào Touch pool; thuần Keyboard/Mouse vào Keyboard/Mouse pool; party trộn vào Mixed/Keyboard-Mouse pool sau disclosure “Bạn sẽ đấu trong hàng chờ có chuột và bàn phím.” Mọi thành viên phải acknowledge trước Ready; không silent bot, silent pool switch hoặc mid-match family switch.

[ASSUMPTION: UX-027] Danh mục action remappable gồm mọi action được implementation đưa vào gameplay, tối thiểu: movement/sprint/walk/jump-vault/crouch/prone/lean; fire/over-shoulder aim/ADS/reload/fire-mode/hold-breath/zero up-down; select/cycle weapon và throwable; interact; Inventory, Map, Pause; quick ping/radial ping; PTT/mute; shoulder swap; spectate next/previous. Mỗi action nhận primary + secondary từ keyboard, mouse button hoặc wheel khi hợp lệ.

Conflict được kiểm theo active context: binding trùng trong hai context loại trừ nhau được phép và phải ghi context; trùng trong cùng context chặn Apply tới khi Replace/Swap/Cancel. `ui_accept`, `ui_cancel`, Pause, Inventory-close và Map-close luôn phải còn ít nhất một đường keyboard/mouse; OS-reserved combination bị từ chối kèm lý do. Rebind được stage; Apply atomically vào local config và cập nhật prompt ngay; Cancel/thoát rollback; Reset category/Reset All cần confirm; binding đã Apply tồn tại qua restart. Gameplay binding lưu physical-key identity; logical Unicode chỉ dành text entry; tên phím hiển thị do OS/localized label provider tạo. Acceptance bao gồm keyboard layout khác QWERTY, Linux display-name mapping, mouse extra button và raw-mouse capture/release qua UI focus.

## Inventory, Map & Party

[ASSUMPTION: UX-007] Inventory: `inventory-panel` trái hiển thị Nearby/Backpack; phải hiển thị weapons/equipment. Composition chuẩn tại 1920×1080 là 34% trái — 32% world strip — 34% phải và luôn reflow trong contract hai panel ≤68% / world strip ≥32%. `item-row` hỗ trợ quick pickup, drag/drop, split/drop; `equipment-slot` từ chối item sai loại và hiện durability áo/mũ current/max bằng bar + số + broken state. Capacity luôn là used/total; ammo, heal, throwable có weight. Ammo có màu + box shape + icon; rarity có label/icon ngoài màu. Không auto-pick weapon/armor/attachment; auto-pick ammo đúng cỡ dừng ở ngưỡng người chơi đặt trong Settings → Gameplay → Loot. [Mockup Inventory](mockups/inventory.html) — minh họa composition 34/32/34, world risk strip và durability.

[ASSUMPTION: UX-042] Mobile Inventory là một panel tabbed tối đa 62% viewport với ba tab Nearby/Backpack/Equipment và world-risk strip tối thiểu 38%. Tap chọn row, tap action hoặc contextual menu thực hiện Pick up/Equip/Move/Split/Drop; drag là shortcut tùy chọn, không phải đường duy nhất. Close 64 units nằm trong safe area. [Mobile Inventory / Map](mockups/mobile-inventory-map.html) là delta reference cho anatomy này.

[ASSUMPTION: UX-033] Context arbitration lấy target hợp lệ gần reticle trước; nếu cùng độ ưu tiên thì revive/assist DBNO → vehicle exit/safety → door/traversal/enter vehicle → pickup. Prompt luôn hiện primary action; `context_next` remappable hoặc hold-interact mở danh sách ngắn cho action phụ. Trong xe, interact ưu tiên Exit. Server reject giữ target/focus, không tự chạy action kế tiếp và nêu lý do ngắn. Acceptance dùng cụm doorway + loot + teammate DBNO + vehicle: primary dự đoán được, action phụ truy cập được và không revive/enter/pickup nhầm.

[DECISION: ADR-26; UX-009/UX-032] Full Map cố định north-up, không pause, pan/zoom/marker, hiển thị flight path, current zone, team marker và place name; minimap player-heading-up. Full Map zoom clamp 0,75×–6× theo authored extent và pan clamp để ít nhất 20% authored bounds còn trong viewport. Header neo góc trên trái, phase/timer góc trên phải, legend góc dưới trái và bindings góc dưới phải. Next zone chỉ xuất hiện sau khi server xác nhận phase wait bắt đầu, không prediction, và dùng nét đứt để phân biệt current-zone nét liền. `map-marker-layer` giữ audio đầy đủ. [ASSUMPTION: UX-015/UX-033] Damage không tự đóng Map; cung 30° luôn screen-relative theo camera thế giới tại thời điểm hit, không theo north/map rotation/zoom, và nằm trên Map tới hết lifetime. [Mockup Map / Phase](mockups/map-phase.html) — minh họa bốn corner anchor và next-zone đã reveal bằng nét đứt.

Trên Touch, một ngón pan, pinch zoom, tap đặt/chọn marker và long-press mở radial marker; close 64 units luôn trong safe area. Damage vẫn không tự đóng Map và cue giữ screen-relative như desktop; không gesture nào tạo enemy marker tự động.

[ASSUMPTION: UX-033] Vehicle overlay phân biệt fuel, HP thân xe, bốn tire state và cháy. Khi server xác nhận sắp nổ, `context-action-card` + `progress-timer` đếm 3,0 giây bằng số, bar, icon lửa và cue âm; lốp hỏng không dùng cùng cue với HP thấp. Countdown không đóng chỉ vì driver/passenger rời ghế: nó giữ tới server-confirmed explosion/cancel, trong khi world fire/audio tiếp tục là cue vị trí; state xe không cháy mới thu khi rời context.

[ASSUMPTION: UX-008/UX-028] Lobby đặt điều hướng dọc bên trái, `party-panel` và hành động Deploy bên phải, giữ world scene ở giữa. Party dùng `party-panel` cho 1–4 người: leader chọn mode/region và Deploy; thành viên kết nối phải Ready; đổi roster/mode/region clear Ready; Reconnecting gate Deploy; leader rời thì party service chuyển quyền cho thành viên connected lâu nhất. Invite provider là adapter kiến trúc, không đổi state UX. [Mockup Lobby](mockups/lobby.html) — minh họa left navigation, right party/action panel và world center.

Party panel hiển thị input family cạnh từng thành viên. Khi tổ đội chuyển sang mixed, Ready bị clear và disclosure pool xuất hiện một lần cho mọi thành viên; Cancel giữ party nhưng không vào queue, Acknowledge cho phép Ready lại.

Voice v1.0 là **team-only**, PTT mặc định; open-mic là option, mỗi teammate có mute + volume. Hai action remappable là quick ping và radial ping. Tám intent MVP: **Đi tới, Nguy hiểm, Địch nhìn thấy, Loot ở đây, Cần vật tư, Giữ vị trí, Tập hợp, Phương tiện**. “Địch nhìn thấy” là điểm manual, không track/ID mục tiêu và không tự xuyên cover. Danger/Enemy TTL 8 giây; Need/Regroup 12 giây; các ping còn lại 20 giây. Mỗi người có một positional ping active; ping mới thay ping cũ, ping lại cùng target hủy. Tối đa 3 ping/2 giây rồi cooldown 3 giây. Mọi ping dùng teammate identity 1–4 + shape + label nhất quán trên `squad-panel`, world, `compass`, `map-marker-layer`, `voice-ping-indicator`; màu chỉ phụ trợ.

## Reporting & Replay Summary

[ASSUMPTION: UX-031] Report MVP từ Results hoặc friendly-fire source có: target thuộc roster/recent encounter hợp lệ, category **Cheating, Team-kill/Friendly-fire abuse, Harassment/Voice, Teaming, Exploit, Other**, optional note, Submit, receipt ID/status và retry. Block là hành động local tách khỏi report. Taxonomy chi tiết, evidence attachment, retention và moderation SLA deferred cho Backend/Safety; story Report bị gate tới khi API/security/privacy được khóa.

Replay Summary v1.0 không phải video playback, kill-cam hay replay đầy đủ. Minimum là placement, survival time, kills/assists và timeline chỉ gồm event server-confirmed mà người/đội được phép biết (drop, DBNO/revive, elimination và result); payload chưa đến hiện `Pending`, không được suy diễn vị trí/POV địch. Damage breakdown, map path và event detail sâu deferred cho Gameplay/Backend; nếu không có payload thì ghi `Unavailable`, không dựng kill-cam giả.

## Game Feel & Juice

UI củng cố phản hồi có thể tin cậy, không tạo spectacle. Mỗi phát bắn được truyền đạt bằng tiếng nổ/cơ khí, muzzle flash, vỏ đạn và recoil camera. Hit feedback dùng máu/bụi theo setting, âm nhẹ và body reaction; không damage number, và hạ gục chỉ hiện sau server confirmation. Người bị bắn nhận `damage-direction-indicator`, không vị trí chính xác.

Heal/revive/reload dùng `progress-timer` bám đúng server state; ngắt có cue hình + âm. Low HP pulse, flash, camera shake đều tuân slider/toggle. Chiến thắng mới cho phép nhạc và một chuyển động ngắn; khi còn sống không có nhạc nền. Menu/Results có nhạc tiết chế, không reward stinger lặp.

[ASSUMPTION: UX-005] Motion mang tính dụng cụ: fade/slide ngắn, không overshoot, không bounce. [ASSUMPTION: UX-012/UX-035] Reduce Motion/Flash bỏ pulse/shake/flash nhưng không đổi timing, priority, server state hoặc bỏ cue: giữ label + icon tĩnh + audio tương đương.

[ASSUMPTION: UX-023/UX-034/UX-035] Khi người chơi còn sống, Inventory, Map và Pause không duck/mute tiếng bước chân, súng, xe, bo hoặc voice; HRTF vẫn theo camera thế giới, không theo map rotation. UI sound không được che combat band. Spectator nghe đúng mix/perspective của teammate đang follow, không có gain/range rộng hơn. System/ping subtitle không silently drop: critical line lên trước, line bị preempt trở lại queue; repeat coalesce kèm count. Acceptance: cùng một replay audio cho Match HUD/Inventory/Map/Pause phải giữ khả năng xác định cung nguồn âm trong biên test GDD; bật Reduce Motion/Flash không làm mất bất kỳ warning/state nào.

### Audio controls và output parity

[ASSUMPTION: UX-034] V1.0 hỗ trợ output **Stereo Headphones** (HRTF On/Off), **Stereo Speakers** và **Mono accessibility downmix**. Device picker dùng System Default hoặc thiết bị do OS cung cấp; đổi thiết bị không đổi internal mix. Controls gồm Master, World, Team Voice, UI và Music; Music chỉ có ở menu/Results/victory. **World** là một bus tỷ lệ cố định chứa footsteps, gunshots, vehicles, zone và ambience—không tách Footstep/Ambience slider, EQ “footstep boost”, night-mode compressor hoặc preset tăng cue chiến thuật. Per-teammate voice volume/mute không tác động world mix.

HRTF chỉ áp dụng cho Stereo Headphones; Speakers dùng spatial stereo mix; Mono là downmix có nhãn “giảm khả năng xác định hướng” và không biến hướng âm thành visual marker. Audio/Gameplay Architecture sở hữu asset loudness, internal bus ratios và device backend; story Audio chưa Done nếu replay chuẩn không đạt metric GDD ≥85% xác định đúng cung 30° ở 20–80 m trên từng output cạnh tranh được hỗ trợ. Mono được kiểm tra để không tạo thêm thông tin, nhưng không bắt buộc đạt directional metric như stereo.

## Accessibility Floor

[ASSUMPTION: UX-012] Floor bắt buộc:

- Text thường ≥4,5:1; text lớn, icon cần thiết và `focus-ring` ≥3:1; xem token/combination ở `DESIGN.md`.
- UI scale 80–140%; safe-frame 16:9; không crop ở 1280×720, 3840×2160 hoặc ultrawide.
- Remap toàn bộ gameplay action hoặc Touch layout; hold/toggle; sensitivity theo aim state/scope; FOV, Gyro, haptic, camera shake, flash intensity chỉnh được.
- Ba preset mù màu cho bo, marker, hit effect, reticle; color+shape+label redundancy cho ammo, rarity, team, danger.
- Máu/hit effect giảm hoặc đổi màu nhưng giữ khả năng xác nhận hit; Reduce Motion/Flash không bỏ thông tin.
- `subtitle-line` cho system và teammate ping, có size/background và no-drop/coalesce contract UX-023; audio mixer và HRTF giữ công bằng thông tin theo UX-034 trên mọi surface không pause.
- Không visual footstep radar trong competitive queue; accessibility không tạo thêm thông tin chiến thuật.
- Keyboard focus đầy đủ, thứ tự đọc ổn định, không mouse-only drag làm đường duy nhất.
- Touch target ≥48 logical units; fire/exit/close ≥64 khi safe area cho phép; tap là đường chính, drag/pinch/long-press luôn có cue và fallback action rõ.
- Permission mic chỉ hỏi khi người chơi bật voice/PTT; denial không loop prompt. Audio interruption, route change và haptic disable không làm mất world-state cue bắt buộc.

[NOTE FOR UX: Screen-reader/menu narration, subtitle options chi tiết, motor playtest, photosensitivity limits và yêu cầu hearing-accessibility ngoài ping/subtitle cần scope riêng trước v1.0 readiness.]

## Inspiration & Anti-patterns

- **Học từ PUBG cổ điển:** world map/minimap, match-start tension và thông tin chức năng; không sao chép art, font, icon hoặc patch layout.
- **Học từ các update inventory/contextual UI của PUBG:** giảm bước thao tác và chỉ hiện throwable/action state đúng lúc; không tự chọn đồ “tốt nhất”.
- **Giữ từ GDD:** khoảng lặng, hậu quả tử vong, thông tin không hoàn hảo, không nhạc khi còn sống.
- **Loại:** live-service dashboard, neon/glassmorphism, full-screen inventory che thế giới, kill-feed dày, damage number, footstep radar, loot score, rarity chỉ bằng màu, store/news/reward rail, red badge và countdown FOMO.

## Responsive & Platform

[ASSUMPTION: UX-011/UX-021/UX-024] Desktop base là 1920×1080. Competitive reference rect `R` là hình 16:9 cao bằng viewport và đặt giữa; trên ultrawide, `R.width = viewport.height × 16/9`, không lấy 5% theo toàn chiều rộng ultrawide. Safe margin `{spacing.safe-frame}` tính trên `R`. Sáu HUD module, reticle, overlay lane và caption lane neo trong `R`; trong Standard v1.0, phần ngoài `R` là side matte/chrome không tương tác và không chứa live-world information.

- **Compact — 720p hoặc UI scale >120%:** co gap/padding trước; text gameplay-critical không xuống dưới size token; list/panel dùng scroll, long label ellipsis + tooltip; overlay preempt theo UX-023; Inventory vẫn giữ world strip ≥32%.
- **Base — 1080p/1440p, scale 80–120%:** dùng layout chuẩn từ `DESIGN.md`.
- **Large/4K:** scale UI/theme/vector độc lập world render; không tăng số module, marker hoặc line thông tin.

Desktop acceptance bắt buộc tại 1280×720, 1920×1080, 2560×1440, 3840×2160, 3440×1440 và 5120×1440 ở 80/100/140%: không crop/overlap module critical, focus ring hoặc subtitle; reticle đúng tâm `R`; squad/minimap không rời vùng quét central 16:9; Inventory giữ ≥32% world strip; Map/overlay vẫn đóng được bằng binding.

[ASSUMPTION: UX-038/UX-040] Mobile luôn landscape và dùng viewport thật sau OS safe inset. Profile bắt buộc: phone 20:9, phone 16:9 và tablet 4:3; mỗi profile kiểm notch trái/phải, gesture bar, 100/120/140% UI scale và left-handed layout. Reticle giữ đúng tâm live world; `safe-area-root` không cho fire/exit/close dưới system gesture; HUD không che central aim corridor; Inventory giữ ≥38% world strip; Map close/damage cue vẫn truy cập được. Font raster/SDF và label Việt/Anh trên Windows/Linux/macOS/Android/iOS cần snapshot trong Godot trước story UI Done.

## Surface Closure

Mọi nhu cầu nguồn có bề mặt giao; mọi bề mặt có hành trình bên dưới chạm tới. “Mocked” nghĩa là visual reference load-bearing đã được promote và distill; “Spine-only” nghĩa là contract đủ để dựng mà không cần mockup riêng ở vòng này.

| Nhu cầu | Bề mặt / phần tử giao | Hành trình chạm tới | Coverage |
|---|---|---|---|
| Chọn Solo/Duo/Squad, region, party/input pool | Sảnh chính; Party / Mode / Region | Lan 1–3; Minh 1; Mai 1–2 | Mocked desktop — [Lobby](mockups/lobby.html); mobile spine-only |
| Mạng dưới ngưỡng | Xác nhận mạng; `network-warning` | Quân 7–8; Minh failure | Spine-only |
| Ghép trận / bot disclosure | Ghép trận; `status-banner` | Minh 2; Quân failure | Spine-only |
| Chuẩn bị, flight path, drop | Sảnh chờ; Máy bay / Đổ bộ; `compass` | Minh 3–4 | Spine-only |
| HUD sống sót | Match HUD; 7 content groups qua 6 module; Touch control layer | Minh 5–10; Lan 4–9; Mai 3–6 | Mocked — [Desktop](mockups/match-hud.html) + [Mobile](mockups/mobile-match-hud.html) |
| Loot nhanh | `context-prompt`; `item-row` | Minh 5 | Spine-only |
| Capacity/equipment/attachment/armor durability | Inventory; `inventory-panel`; `equipment-slot` | Minh 6; Mai 4 | Mocked — [Desktop](mockups/inventory.html) + [Mobile delta](mockups/mobile-inventory-map.html) |
| Bo, map, marker, địa danh | Map / Phase; `map-marker-layer`; `minimap-zone-panel` | Minh 7–9; Lan 5–6; Mai 5 | Mocked — [Desktop](mockups/map-phase.html) + [Mobile delta](mockups/mobile-inventory-map.html) |
| Voice + 8 ping context | `voice-ping-indicator`; `squad-panel`; teammate identity 1–4 | Lan 4–6 | Spine-only; MVP locked UX-028 |
| Gục/cứu/heal | `context-action-card`; `progress-timer` | Lan 7–8 | Spine-only |
| ADS/scope/throwable | `reticle`; `weapon-ammo-panel`; `context-action-card` | Minh 8–9 | Spine-only |
| Vehicle fuel/HP/tire/fire 3s | `context-action-card`; `progress-timer`; world cue sau exit | Minh 8 | Spine-only |
| Spectate đồng đội | Teammate-follow + information/audio parity | Lan failure | Spine-only; voice giữ trong team, tactical ping mới bị cấm theo ADR-22 |
| Results / replay summary | Results / Summary; `results-table`; minimum UX-031 | Minh 11; Lan 10 | Spine-only; deep payload deferred |
| Profile/history/mastery/no-expiry | Profile / Mastery; `results-table` | Quân 6 | Spine-only |
| Training sandbox | Training Grounds | Quân 3–5 | Spine-only |
| Onboarding curriculum | Field Orientation; bốn checkpoint; Skip/Retry/Complete | Quân 3–4 | Spine-only; MVP locked UX-036 |
| Settings/input/accessibility | Settings; `settings-control`; `subtitle-line`; `control-layout-editor` | Quân 1–3; Mai 1 | Spine-only |
| Friendly-fire source/report/block | `status-banner`; Report / Block; minimum UX-031 | Lan failure | Spine-only; deep taxonomy/backend gate |
| Party/Queue/Pre-match/Live reconnect | State machine + owner UX-029/UX-043 | Minh/Lan/Quân/Mai failure | Spine-only; policy/outcome khóa theo ADR-21, API được Story 6.15 hiện thực |
| Safe area/Touch/Gyro/haptic | `safe-area-root`; `touch-stick`; `touch-look-zone`; `touch-action-button` | Mai 1–6 | Mocked — [Mobile HUD](mockups/mobile-match-hud.html) |
| Mobile interruption/resume | Lifecycle state + reconnect surface | Mai 7–8 | Spine-only; dùng cùng ADR-21 và Story 6.15 |
| Pause/leave/error/input routing | Pause; UX-026; `action-button` | Minh failure; Quân failure | Spine-only |

## Key Flows

[ASSUMPTION: UX-013/UX-038] Bốn protagonist dưới đây là nhân vật giả định của Fast path; họ khóa coverage chứ không thay thế user research.

### Hành trình 1 — Minh trở lại cảm giác battle royale cổ điển

Minh là cựu người chơi PUBG, chơi Solo trên PC 1920×1080 và muốn mọi quyết định có hậu quả.

1. Minh mở game; Sảnh chính đặt focus vào Deploy, không có news/store/reward rail.
2. Anh giữ Solo + region đạt ngưỡng và Deploy; Ghép trận hiện mode/region/elapsed, không banner thương mại.
3. Sảnh chờ chuyển sang máy bay; weather và flight path đã biết từ đầu.
4. Minh đọc `compass`, quan sát dù và chọn cụm nhà ít người hơn.
5. Tiếp đất tay trắng, anh dùng `context-prompt` nhặt nhanh súng; mỗi món cần 0,20 giây và tiếng động thế giới vẫn quan trọng.
6. Anh mở Inventory; `inventory-panel` chỉ chiếm hai bên, dùng `item-row`/`equipment-slot`, thấy mình phải bỏ đạn để lấy smoke.
7. Anh mở Map / Phase; sau khi server xác nhận pha chờ, `map-marker-layer` mới cho thấy bo kế tiếp; không loot/địch và audio vẫn đầy đủ.
8. Minh lái xe vào rìa bo; vehicle state thường thu khi rời xe, nhưng fire countdown đang chạy vẫn giữ đủ tới nổ/cancel.
9. Trong giao tranh, anh đổi over-shoulder/ADS/zero, đọc `reticle`, ammo và cung `damage-direction-indicator`; không có damage number xác nhận thay anh.
10. **Climax:** bo cuối còn hai người. Minh không bắn vội, dùng smoke đã giữ từ bước 6, nghe hướng súng và thắng bằng vị trí; nhạc chiến thắng chỉ bắt đầu sau server-confirmed result.
11. Results / Summary hiện hạng 1, survival time và combat summary; Play Again trở về hàng chờ mà không trao sức mạnh ngoài trận.

Failure path: nếu ping vượt 150 ms, `network-warning` xuất hiện nhưng không che giao tranh. Nếu Minh chết sớm, Results giải thích bằng dữ liệu được xác nhận và replay tóm tắt khả dụng; không kill-cam giả, không “mua hồi sinh”. Nếu dữ liệu summary chưa về, state Pending được giữ.

### Hành trình 2 — Lan chỉ huy Squad qua một pha cứu nguy

Lan chơi Squad với ba người bạn, là caller và ưu tiên voice/ping hơn giao tranh vô nghĩa.

1. Lan mở Party / Mode / Region, tạo nhóm bốn người và chọn Squad Standard.
2. `party-panel` cho thấy từng thành viên, voice, ready/network state và cảnh báo xung đột về quy mô đội trước khi Deploy.
3. Cả đội Deploy; không ai chọn vũ khí, skill hoặc loadout.
4. Trong máy bay, Lan đặt marker khu làng; `compass`, `map-marker-layer` và `voice-ping-indicator` dùng cùng danh tính marker.
5. Sau khi loot, Lan mở Map / Phase, gọi tuyến rời bo sớm; không có ping tự nhận dạng kẻ địch xuyên cover.
6. Ở mép rừng, cô ping **Nguy hiểm** bằng MVP vocabulary; identity 1–4 giống nhau trên world/compass/map, và `squad-panel` cho thấy teammate đang nói thay vì thêm footstep radar.
7. Một đồng đội bị gục. `context-action-card` và `progress-timer` hiện revive 10 giây; người gục vẫn crawl/ping/voice.
8. **Climax:** Lan thả smoke, bắt đầu cứu; một viên đạn sượt làm progress ngắt với lý do rõ. Cô đổi cover, cứu lại đủ 10 giây và cả đội thoát bo với đúng một smoke còn lại.
9. Cuối trận, Lan bị loại trước nhưng chuyển Spectator teammate-follow; camera, sáu HUD module và audio chỉ phản ánh thông tin hợp lệ của target tới khi đội kết thúc.
10. Results / Summary cho phép xem số liệu đội và mở Report / Block nếu có friendly fire; sau đó trở Sảnh chính.

Failure path: nếu target rớt mạng, Spectator chuyển target hợp lệ/Retry; toàn đội bị loại thì chuyển Results. Nếu có team-kill, `status-banner` ghi nguồn sát thương trung tính; report tối thiểu có target/category/receipt, giữ draft khi offline và block có thể áp dụng cục bộ. Reconnect dùng outcome ADR-21; deep report taxonomy vẫn deferred tới story backend tương ứng.

### Hành trình 3 — Quân thiết lập game và học mà không bị dẫn dắt bởi phần thưởng

Quân là người mới, chơi ở 1280×720 trên Linux và cần giảm camera shake.

1. Quân mở Settings từ Sảnh chính; `focus-ring` và keyboard traversal cho phép thao tác không cần pointer.
2. Anh tăng UI scale, giảm shake/flash, chọn preset mù màu và đổi ADS sang toggle; `settings-control` hiện value và conflict rõ.
3. Ở lần mở đầu tiên, Quân chọn Field Orientation thay vì Skip; anh hoàn tất movement/camera và loot/inventory, có thể thoát rồi tiếp tục từ checkpoint gần nhất.
4. Anh hoàn tất fire/ADS và zone/cover; Complete chỉ đưa về Sảnh chính, không trao reward, mastery hoặc stats. Sau đó anh chủ động vào Training Grounds sandbox.
5. Anh luyện bia di động, đổi sensitivity ADS/scope; `weapon-ammo-panel` và hit feedback xác nhận trúng mà không có damage number.
6. **Climax:** Quân theo dõi recoil, điều chỉnh ngắn và gom được loạt bắn đầu vào bia; feedback âm–hình cho anh hiểu kỹ năng vừa cải thiện, không phải chỉ số nhân vật tăng.
7. Anh mở Profile / Mastery: empty state “Chưa có trận Standard” và không biến Training thành thành tích cạnh tranh.
8. Quân chọn Solo rồi Deploy; hệ thống phát hiện region hiện tại trên 150 ms và mở Xác nhận mạng.
9. Anh chọn Cancel, đổi region đạt ngưỡng rồi vào hàng chờ; lần đầu vào trận diễn ra với các setting đã giữ.

Failure path: nếu Quân bỏ dở Field Orientation, checkpoint gần nhất được lưu cục bộ và route luôn cho Continue/Restart/Skip; lỗi asset cho phép về Sảnh chính. Nếu mic permission bị từ chối, Settings giải thích cách cấp quyền mà không hỏi lặp; nếu hàng chờ timeout/offline, Quân trở Sảnh chính, Training và Settings vẫn dùng được. Nếu hàng chờ thử nghiệm có bot, số bot dự kiến phải được công bố trước khi anh xác nhận; Standard không được âm thầm lấp bot.

### Hành trình 4 — Mai sống sót trọn trận trên mobile

Mai chơi Squad trên điện thoại Android 20:9 bằng Touch, muốn điều khiển chính xác nhưng không cần game tự tìm địch hay tự bắn.

1. Mai mở Settings → Input → Touch; `control-layout-editor` hiện safe area của máy, cô đặt `touch-stick` vừa tầm trái, bật left fire, giảm haptic và bật Gyro chỉ khi ADS rồi Apply.
2. Cô vào party với hai người Touch và một người macOS Keyboard/Mouse. `party-panel` công bố Mixed/Keyboard-Mouse pool, clear Ready; cả đội acknowledge rồi Ready lại, không bị chuyển pool ngầm.
3. Trong máy bay và khi tiếp đất, `safe-area-root` giữ nút khỏi camera cutout; `touch-stick` điều khiển movement, `touch-look-zone` camera và action context nhặt khẩu súng đầu tiên mà không auto-loot vũ khí khác.
4. Mai mở mobile Inventory. Panel tabbed chiếm ≤62%, dải thế giới ≥38%; cô tap Backpack, chọn đạn và Drop qua action menu, không bắt buộc drag.
5. Cô mở Map, pinch zoom, pan rồi long-press đặt marker. Damage cue xuất hiện screen-relative nhưng không tự đóng Map; Mai dùng nút Close 64 units để trở lại trận.
6. **Climax:** ở bo cuối, Mai giữ right fire và tinh chỉnh ADS bằng Gyro; server xác nhận hit như mọi platform. HUD không hiện visual footstep/enemy cue, nên cô thắng nhờ tiếng động, cover và quyết định giữ smoke.
7. Một cuộc gọi làm app `Interrupted → Backgrounded`; tất cả held touch/PTT được trung hòa, UI không giả pause hay hứa avatar an toàn.
8. Mai quay lại: app dùng cùng match token vào Reconnecting rồi Restored từ state máy chủ; nếu slot hết hạn/đội bị loại/trận kết thúc, UI chuyển đúng Timed out/Results thay vì auto-queue.

Failure path: nếu mic permission bị từ chối, voice tắt và không hỏi lặp; nếu OS đổi audio route, world mix phục hồi mà không bật PTT. Nếu Keyboard/Mouse ngoài được kết nối giữa trận, input family không đổi; UI yêu cầu requeue sau trận. Nếu layout lưu bị invalid sau display/safe-area change, `safe-area-root` dùng preset an toàn và giữ đường vào Pause/Reset.

### Chỉ mục giả định và ghi chú mở

| ID | Áp dụng tại |
|---|---|
| UX-004 | Foundation; i18n/market posture |
| UX-005 | Game Feel & Juice; Field Instrument motion |
| UX-006 | Component Patterns; HUD & Diegetic UI |
| UX-007 | Component Patterns; Inventory, Map & Party |
| UX-008 | Information Architecture; Sảnh chính |
| UX-009 | Inventory, Map & Party; Map behavior |
| UX-010 | `DESIGN.md` Colors; state colors referenced tại đây |
| UX-011 | Responsive & Platform |
| UX-012 | Game Feel & Juice; Accessibility Floor |
| UX-013 | Key Flows; Minh/Lan/Quân |
| UX-014 | Foundation; Surface Closure — bốn desktop visual reference đã promote và được distill |
| UX-015 | State Patterns; Inventory, Map & Party — damage không tự đóng Map |
| UX-016 | State Patterns — offline cache/report retry là dependency kiến trúc |
| UX-017 | HUD & Diegetic UI — persistent groups và contextual whitelist |
| UX-021 | Responsive & Platform — safe-frame formula, breakpoint và acceptance matrix |
| UX-022 | `DESIGN.md` Colors — composited contrast và map boundary |
| UX-023 | HUD & Diegetic UI; Accessibility — overlay/subtitle priority, lane và preemption |
| UX-024 | Interaction Primitives; Responsive — ultrawide camera fairness và anti-peek |
| UX-025 | `DESIGN.md`; Accessibility — reticle, colorblind mapping và teammate identity |
| UX-026 | Interaction Primitives — input routing và focus lifecycle |
| UX-027 | Input Schemes — action inventory, conflict, Apply/Cancel và persistence |
| UX-028 | Inventory, Map & Party — ready/leader, team voice, 8 ping và teammate identity |
| UX-029 | State Patterns — reconnect/AFK owner, timeout, outcome và destination đã khóa bởi ADR-21 |
| UX-030 | State Patterns — spectator teammate-follow và information parity |
| UX-031 | Reporting & Replay Summary — MVP minimum và phần deferred |
| UX-032 | Component Patterns; Map/Phase — phase anatomy, next-zone timing và 7-group wording |
| UX-033 | Inventory, Map & Party — vehicle, armor, context arbitration và Map damage cue |
| UX-034 | Game Feel & Accessibility — audio/HRTF parity |
| UX-035 | Game Feel & Accessibility — motion/flash budget |
| UX-036 | Foundation; IA; Surface Closure; Quân flow — Field Orientation MVP |
| UX-037 | Foundation; Surface Closure — coverage desktop đã đóng; mobile delta do UX-045 bổ sung |
| UX-038 | Foundation; Responsive & Platform — five-platform và landscape Touch |
| UX-039 | Input Schemes; Inventory, Map & Party — input family và pool disclosure |
| UX-040 | Component Patterns; Interaction; HUD — safe area và Touch controls |
| UX-041 | HUD & Diegetic UI; Surface Closure — mobile Match HUD |
| UX-042 | Inventory, Map & Party; Surface Closure — tap-first mobile panels |
| UX-043 | State Patterns; Reconnect — interruption/background/recovery |
| UX-044 | Input/Accessibility/Game Feel — Gyro, haptic, permission và audio route |
| UX-045 | Foundation; Surface Closure — đúng hai mobile delta reference |

[NOTE FOR UX: Không còn product-decision gate chặn Foundation Wave. Provider invite, report taxonomy/replay payload sâu và accessibility/device evidence thuộc acceptance/dependency của story sở hữu; content wording/level scripting chi tiết thuộc E7. Reconnect/AFK, spectator communication, audio controls, localization, input identity/raw mouse và Map orientation/zoom đã khóa bằng ADR-21–ADR-26 và không được implementation tự suy diễn khác đi.]
