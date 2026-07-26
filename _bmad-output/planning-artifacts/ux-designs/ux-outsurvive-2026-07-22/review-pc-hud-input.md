# Reviewer Gate — PC HUD & Input Usability

## Overall verdict

Hướng thiết kế **Field Instrument** và giới hạn thông tin cạnh tranh là phù hợp; camera TPP, armor, vehicle và Leave Match đã có contract tốt hơn mức khái niệm. Tuy vậy, cặp spine chưa handoff-ready cho PC vì responsive layout, tranh chấp overlay, input capture của Map/Inventory, remapping, party communication và reconnect/spectate còn thiếu luật đủ để implementation không tự suy diễn.

**Findings:** **0 Critical · 6 High · 6 Medium · 2 Low**

## Critical (0)

Không phát hiện lỗi Critical trong lens này.

## High (6)

### H-01 — Competitive safe frame chưa có công thức triển khai và breakpoint

`DESIGN.md:90,254-260`; `EXPERIENCE.md:168,187-189` dùng `5%`, central 16:9, 720p–4K và 80–140%, nhưng không khóa reference rect, clamp, reflow, overflow hay text truncation. Nếu implementation tính `5%` theo toàn viewport ultrawide, squad/minimap sẽ bị đẩy xa tâm; ở 720p/140%, Inventory và overlay có thể chồng hoặc crop.

**Fix tối thiểu:** định nghĩa safe frame là hình 16:9 đặt giữa viewport, margin tính trên hình đó; thêm breakpoint/reflow và scroll/ellipsis rules cho 720p/140%.  
**Acceptance:** tại 1280×720, 1920×1080, 2560×1440, 3840×2160, 3440×1440 và 5120×1440 ở 80/100/140%, không module critical nào crop/chồng; tất cả nằm trong central 16:9 và Inventory vẫn giữ world strip ≥32%.

### H-02 — Contextual overlays chưa có priority/lane/suppression matrix

`DESIGN.md:256,264-266,283-303`; `EXPERIENCE.md:74-94,105,131,149,151` cho phép damage, network, friendly-fire, revive/heal, armor break, vehicle fire, prompt và subtitle cùng xuất hiện nhưng chỉ giới hạn một `status-banner`; không khóa z-order, lane, stacking hoặc trường hợp cue nào được trì hoãn.

**Fix tối thiểu:** lập bảng priority + anchor lane + lifetime + suppression cho từng overlay; reticle, damage cue, HP/ammo và fire countdown không được che nhau.  
**Acceptance:** stress scene 720p/140% đồng thời có fire countdown, damage 2 hướng, high ping, teammate down, context prompt và subtitle; không che reticle/HP/ammo/phase, critical cue đọc được trong ≤1 giây và không có hai card tranh cùng anchor.

### H-03 — Map/Inventory không pause nhưng input capture chưa được khóa

`EXPERIENCE.md:37-39,85-88,107,122,133,149` chưa nói rõ khi panel mở thì WASD, camera, fire/ADS, drive, mouse wheel, pointer lock và hotkey gameplay nào còn hoạt động. Điều này dễ tạo phát súng, drop item, đổi zoom hoặc lái xe ngoài ý muốn khi click/scroll UI.

**Fix tối thiểu:** thêm input-routing matrix cho Match HUD / Inventory / Map / Pause, gồm cursor mode, movement, camera, weapon, vehicle và đóng panel; keyboard path phải tương đương drag/drop.  
**Acceptance:** mở/đóng Inventory và Map khi đi bộ, ADS, ngồi ghế lái/ghế phụ và bị bắn; click/scroll UI không kích hoạt gameplay ngoài contract, close binding luôn hoạt động và audio thế giới không bị giảm.

### H-04 — “Full remap” chưa đủ luật để triển khai an toàn

`EXPERIENCE.md:109,120-125,137-143` yêu cầu remap và bắt conflict nhưng chưa có action inventory đầy đủ, primary/secondary slot, duplicate-by-context, reserved binding, unbound-required action, mouse wheel/button hoặc recovery khi người chơi bỏ binding điều hướng/confirm.

**Fix tối thiểu:** khóa danh sách action v1.0 và conflict classes; cho biết duplicate nào hợp lệ theo context, action nào không được bỏ trống, cách reset/rollback và prompt update sau Apply.  
**Acceptance:** remap Map, Ping/Radial, shoulder swap, zeroing, breath hold, ADS, lean và Inventory sang keyboard + mouse extra buttons; conflict nêu cả hai action, không thể Apply trạng thái làm UI mất đường thoát, prompt đổi ngay và binding còn sau restart.

### H-05 — Party/voice/8 ping vẫn là blocker của Squad flow

`EXPERIENCE.md:89-90,101,116,153,205,243-254,290` hiển thị ready/network/voice và dùng ping trong hành trình nhưng vẫn để mở channel, PTT default, leader/ready, invite provider và toàn bộ vocabulary 8 ping. Không có TTL/cooldown, nguồn ping, cancel/replace hay hành vi spam.

**Fix tối thiểu:** khóa MVP team-only voice, PTT/mute/volume, leader/ready transitions và 8 ping với icon/label/source/TTL/cooldown/place-cancel rules.  
**Acceptance:** squad 4 người join–ready–đổi mode–disconnect/rejoin; từng người mute/volume độc lập; bốn người ping gần nhau vẫn phân biệt nguồn trên world/compass/map và spam không che combat HUD.

### H-06 — Reconnect và spectator chưa có state machine handoff được

`EXPERIENCE.md:104-116,209,215,251-254,290` chỉ nói “thử reconnect”, không free camera và để timeout/camera switching mở. Chưa khóa trạng thái avatar khi mất mạng, timeout, input bị giữ, đội bị loại trong lúc reconnect, switching controls hay HUD nào spectator được phép xem.

**Fix tối thiểu:** vẽ state machine Connecting → Reconnecting → Restored/Timed out/Team eliminated; định nghĩa spectator target cycling, valid info subset và exit/result transition.  
**Acceptance:** ngắt mạng ở sảnh chờ, máy bay, alive, DBNO và spectator; mỗi case có timer/status/cancel rõ, không lộ free-cam/enemy info và luôn kết thúc ở đúng Match HUD, Spectator hoặc Results.

## Medium (6)

### M-01 — “Phase” chưa có anatomy đủ cho glance hierarchy

`DESIGN.md:147-152,289-290`; `EXPERIENCE.md:56,81,129-131` nói minimap/phase nhưng visual contract chỉ phân biệt hai vòng bo; không khóa phase number, wait/shrink state, countdown hoặc trạng thái outside-zone.

**Fix tối thiểu:** thêm anatomy phase + timer + state label vào `minimap-zone-panel`.  
**Acceptance:** ở 720p và 4K, ≥90% người test xác định đúng phase, đang chờ/thu và thời gian còn lại trong ≤1 giây mà không mở Map.

### M-02 — Danh tính marker đội không nhất quán giữa các surface

`DESIGN.md:131,135,183-197,240,286-299`; `EXPERIENCE.md:77,90,243-248` dùng cyan cho compass/squad nhưng green cho team trên map, đồng thời không khóa identity cho từng thành viên dù hành trình yêu cầu cùng một marker.

**Fix tối thiểu:** một mapping teammate ID (số/shape/label, màu chỉ phụ trợ) dùng chung squad row, world ping, compass và map.  
**Acceptance:** với bốn thành viên và ba preset mù màu, người test ghép đúng người → ping → marker trên ba surface ≥95% trong bài test 20 lần.

### M-03 — Vehicle warning có thể mất khi vừa rời xe

`EXPERIENCE.md:84,131,151,232` quy định card tự thu khi hết ngữ cảnh và vehicle state thu khi rời xe, nhưng fire countdown là hiểm họa còn tồn tại sau khi thoát ghế.

**Fix tối thiểu:** khóa lifecycle riêng cho countdown: HUD card có thể chuyển thành world cue/audio cue sau exit và không biến mất trước nổ khi người chơi còn trong vùng nguy hiểm.  
**Acceptance:** driver, passenger và người vừa exit đều nhận cue đủ 3,0 giây; lốp hỏng, HP thấp và cháy không bị nhầm; cue kết thúc đúng lúc server xác nhận nổ/hủy.

### M-04 — Armor durability có behavioral spec nhưng thiếu visual spec

`DESIGN.md:178-182,296`; `EXPERIENCE.md:87,105,147` yêu cầu bar + số + broken icon, trong khi `equipment-slot` phía DESIGN chỉ mô tả slot/outline/attachment.

**Fix tối thiểu:** bổ sung anatomy thị giác durability/current-max/broken và hierarchy khi so sánh giáp.  
**Acceptance:** tại 720p/80–140% và cả ba preset mù màu, người test phân biệt giáp nguyên/vỡ và chọn món durability cao hơn mà không dựa chỉ vào màu.

### M-05 — Context prompt chưa giải quyết nhiều action cùng vị trí

`EXPERIENCE.md:82,84-88,131` chỉ nói prompt xuất hiện khi action hợp lệ; không có arbitration khi cửa, loot, teammate DBNO và vehicle cùng nằm trong vùng F.

**Fix tối thiểu:** khóa priority, hold/tap hoặc cycle/secondary action và rule giữ focus khi server reject.  
**Acceptance:** test cụm doorway + item + downed teammate + vehicle; action ưu tiên luôn dự đoán được, action phụ vẫn truy cập được và không revive/enter/drop nhầm.

### M-06 — Damage cue trên full-screen Map thiếu hệ quy chiếu

`EXPERIENCE.md:107,149` giữ Map mở và đặt damage cue lên trên, nhưng map orientation còn mở nên cung 30° có thể bị hiểu là hướng bắc bản đồ thay vì screen/camera bearing.

**Fix tối thiểu:** ghi rõ cue luôn screen-relative theo camera thế giới tại thời điểm hit, không theo north-up/rotating map; thêm nhãn/âm xác nhận bị bắn.  
**Acceptance:** ở mọi orientation/zoom, ≥90% người test hiểu đúng bán cầu nguồn hit và đóng Map bằng binding mà focus không mắc trong map controls.

## Low (2)

### L-01 — Rebind persistence và unsaved-state chưa khóa

`EXPERIENCE.md:93,109,137-143` có Apply/conflict nhưng chưa nói auto-save hay Apply/Cancel, lưu local/profile, hoặc rollback khi thoát Settings.

**Fix tối thiểu:** chọn một persistence model và copy cho unsaved exit.  
**Acceptance:** đổi binding, Cancel/Apply, restart game và phục hồi default cho ra kết quả dự đoán được; không mất đường điều hướng.

### L-02 — Font/key-label overflow mới chỉ là NOTE

`DESIGN.md:228,248-250`; `EXPERIENCE.md:20,143,187-189` chưa khóa fallback/truncation cho dấu tiếng Việt, key name Linux, keyboard layout ngoài QWERTY và mouse-button label tại 720p.

**Fix tối thiểu:** quy định wrap/ellipsis/tooltip và fallback glyph/keycap.  
**Acceptance:** snapshot Vietnamese/English với key label dài ở 720p/140% không cắt gameplay-critical label, không vỡ hàng và không hiện missing glyph.

## Pass summary

- TPP hip-fire → over-shoulder → ADS, shoulder swap remappable và anti-corner-peek đã có acceptance rõ (`EXPERIENCE.md:124`).
- Inventory giữ dải thế giới, Map giữ audio, không surface nào pause server; damage-on-map được đánh dấu assumption thay vì fact (`DESIGN.md:258,264`; `EXPERIENCE.md:85,107,133,149`).
- Armor current/max/broken, bốn lốp và fire countdown 3,0 giây đã có behavioral contract (`EXPERIENCE.md:84,87,147,151`).
- Progressive disclosure, cấm radar/loot recommendation/damage number và server-confirmed feedback nhất quán với GDD/research (`EXPERIENCE.md:75-94,131,157-161`).
- Focus keyboard, hold/toggle, sensitivity theo scope, color+shape redundancy và Reduce Motion/Flash có floor rõ (`EXPERIENCE.md:137-176`).
