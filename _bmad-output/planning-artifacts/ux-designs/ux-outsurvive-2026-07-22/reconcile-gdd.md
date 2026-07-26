# Reconcile GDD → Game UX

**Nguồn:** `../../gdds/gdd-outsurvive-2026-07-22/gdd.md`  
**Đích:** `DESIGN.md`, `EXPERIENCE.md`, `.decision-log.md`  
**Kết quả:** **0 Critical · 5 High · 5 Medium**

## High

### H-01 — Cam kết mockup tự mâu thuẫn

- Decision log UX-014 yêu cầu tạo HTML mockup cho Lobby, Match HUD, Inventory và Map/Phase (`.decision-log.md:32`).
- Hai spine lại tuyên bố lượt này không tạo mockup và tất cả surface là spine-only (`DESIGN.md:260`; `EXPERIENCE.md:22,190-212,282`).
- **Cần xử lý:** hoặc hoàn thành bốn mockup, hoặc sửa UX-014 thành quyết định hoãn có lý do; không thể final khi canonical log và spine trái nhau.

### H-02 — Rơi mất contract camera/aim TPP ảnh hưởng công bằng

- GDD bắt buộc chuyển vai camera, đẩy camera khi sát tường và không render đối thủ/vật thể khi đường nhìn từ đầu nhân vật bị che (`gdd.md:236-237`); đồng thời có ba trạng thái hip-fire, ngắm qua vai và ADS (`gdd.md:302`).
- EXPERIENCE chỉ nêu TPP + ADS và để key shoulder swap mở (`EXPERIENCE.md:18,120-124`), không đặc tả over-shoulder aim, camera collision hay anti-corner-peek visibility.
- **Cần xử lý:** thêm behavioral contract, input action/state và acceptance test; đây là rào chắn P4, không phải chi tiết mỹ thuật.

### H-03 — Luồng Leave Match không nói rõ hậu quả

- GDD quy định rời sau khi máy bay khởi hành tính là thất bại (`gdd.md:152`), nhưng không phạt sau khi đội đã bị loại (`gdd.md:510`).
- EXPERIENCE chỉ yêu cầu confirm/hold-to-confirm (`EXPERIENCE.md:39,71,108,123`) mà không đổi copy/state theo hai trường hợp.
- **Cần xử lý:** confirm phải nêu rõ “tính là thất bại” khi còn hiệu lực và bỏ cảnh báo/hình phạt sai sau khi đội đã bị loại.

### H-04 — Trạng thái phương tiện thiếu lốp và cảnh báo cháy đúng 3 giây

- GDD khóa nhiên liệu, lốp bị phá và cảnh báo cháy 3 giây trước nổ (`gdd.md:227-231`).
- EXPERIENCE chỉ đóng gói `vehicle fuel/HP/fire` chung (`EXPERIENCE.md:130,205`), không có tire state hoặc timing/cue 3 giây.
- **Cần xử lý:** thêm state anatomy, cue hình+âm và timer server-confirmed cho fire countdown; phân biệt lốp hỏng với HP thấp.

### H-05 — Độ bền giáp không có surface đọc được

- GDD cho áo/mũ độ bền cụ thể và phá hủy sau hit (`gdd.md:176-194`), nên condition là thông tin quyết định giữ/đổi trang bị.
- EXPERIENCE chỉ nhắc `armor break` theo ngữ cảnh (`EXPERIENCE.md:130`); `equipment-slot` không có durability/current-broken contract (`EXPERIENCE.md:87,146`).
- **Cần xử lý:** đặc tả durability/condition trong Inventory và cue break trong HUD mà không biến thành thêm radar dữ liệu.

## Medium

### M-01 — Chưa hòa giải “HUD chỉ hiển thị” với overlay bổ sung

- GDD giới hạn HUD ở bảy nhóm (`gdd.md:454-459`) nhưng đồng thời bắt buộc cảnh báo mạng, nguồn friendly-fire và các trạng thái gameplay khác (`gdd.md:298,313-314,351`).
- EXPERIENCE tự xem network/armor/vehicle/action cards là trạng thái của bảy nhóm (`EXPERIENCE.md:130`) nhưng mapping này chưa được GDD hay log xác nhận.
- **Cần xử lý:** khóa rõ “bảy nhóm persistent” và whitelist overlay contextual/critical để tránh implementation mở rộng HUD tùy ý.

### M-02 — Ngưỡng tự nhặt đạn chưa có nơi cấu hình

- GDD cho phép tự nhặt đúng cỡ tới ngưỡng do người chơi đặt (`gdd.md:201-203`).
- EXPERIENCE nhắc ngưỡng (`EXPERIENCE.md:146`) nhưng IA, Settings, state và Surface Closure không chỉ ra cách đặt theo cỡ đạn, lưu hay reset.
- **Cần xử lý:** gán control/surface và persistence contract, hoặc ghi rõ đây là open item cho story Inventory/Settings.

### M-03 — Hành vi đóng Map khi nhận damage vượt phạm vi decision log

- EXPERIENCE tự thêm setting “damage đóng map”, mặc định không đóng (`EXPERIENCE.md:148`).
- UX-009 trong log chỉ khóa map không pause, pan/zoom/marker và giữ audio (`.decision-log.md:27`); GDD không quyết định hành vi này.
- **Cần xử lý:** bổ sung assumption riêng vào log và Surface Closure/Settings, hoặc bỏ default này để tránh handoff coi là đã xác nhận.

### M-04 — Các giả định offline/backend chưa được gắn assumption

- EXPERIENCE khẳng định Training dùng được offline, report được queue retry cục bộ, block áp dụng local và Profile dùng cache timestamp (`EXPERIENCE.md:100,111-114,251,266`).
- GDD không khóa Training local/server, retry storage, block semantics hay profile cache.
- **Cần xử lý:** gắn `[ASSUMPTION]` + log và chuyển thành dependency kiến trúc/backend; không để các hành vi này thành contract ngầm.

### M-05 — Profile/Mastery làm rơi bộ dữ liệu và nguyên tắc phần thưởng dài hạn

- GDD khóa các trường số trận, top 10, thắng, cự ly hạ gục, độ chính xác, lịch sử mùa; Mastery chỉ mở số liệu sâu/huy hiệu và phần thưởng thành tích không hết hạn (`gdd.md:390-395`).
- EXPERIENCE chỉ nói `stats`, lịch sử mùa và mastery chung (`EXPERIENCE.md:41-43,92,208,262`), chưa giữ field set hoặc no-expiry/no-daily-pressure trong behavioral contract.
- **Cần xử lý:** thêm schema hiển thị tối thiểu và rào chắn không FOMO; payload chi tiết có thể tiếp tục là open item.

## Pass summary

- Giữ đúng nền tảng PC Windows/Linux, Godot 4.x, keyboard–mouse, TPP Standard và phạm vi 720p–4K/ultrawide.
- IA bảo vệ vòng lặp cổ điển: lobby nông, Solo/Duo/Squad, drop–loot–bo–survive, spectator đồng đội, Results, Training và Profile.
- HUD giữ đúng tinh thần thông tin không hoàn hảo: không damage number, enemy/loot radar, visual footstep, prediction zone hay ping xuyên vật cản.
- Inventory ≤70%, map không pause, flight path/current-next zone/team marker/place name và audio-world risk đều được giữ.
- Network warning >150 ms, bot disclosure, server-confirmed hit/result, friendly-fire source/report, DBNO/revive và no-respawn đều có surface.
- Accessibility nguồn được giữ: full remap, hold/toggle, sensitivity theo scope, FOV/shake/flash, colorblind presets, subtitle system/ping và color+shape redundancy.
- Anti-store/FOMO/live-event, không loadout/hero/pay-to-win và không nhạc khi còn sống được phản ánh nhất quán trong cả hai spine.
