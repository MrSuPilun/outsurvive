# Accessibility & Fairness Review — OutSurvive

## Phạm vi

Review read-only `DESIGN.md` và `EXPERIENCE.md`, đối chiếu GDD và `.working/ux-research.md`. Lens tập trung vào contrast/color redundancy, text/UI scale, keyboard/focus, subtitle/audio alternatives, motion, ultrawide fairness, information parity, anti-peek và khả năng đọc trạng thái quan trọng.

## Overall verdict

**Adequate, chưa sẵn sàng làm contract implementation cuối.** Hai spine đã khóa đúng ranh giới cạnh tranh quan trọng: màu không là tín hiệu duy nhất, keyboard focus/remap có floor, anti-peek TPP có acceptance, ultrawide không thêm HUD data, và cấm footstep radar, damage number, loot recommendation/score. Tuy nhiên, năm rủi ro High vẫn để implementation tự quyết những vấn đề có thể ảnh hưởng trực tiếp tới khả năng đọc hoặc công bằng: contrast trên nền bán trong, camera ultrawide, tranh chấp cảnh báo critical, reticle/colorblind presets và spectator information parity.

## Điểm mạnh đã xác nhận

- Color redundancy được lặp nhất quán bằng icon/shape/label; ammo, rarity, team, danger, gục/chết và progress không chỉ dùng hue (`DESIGN.md:232`, `DESIGN.md:272`, `DESIGN.md:287-300`; `EXPERIENCE.md:170-171`).
- Baseline keyboard tốt: focus luôn hiện, traversal theo thứ tự đọc, remap đầy đủ, prompt lấy binding hiện hành và drag không phải đường duy nhất (`EXPERIENCE.md:73`, `EXPERIENCE.md:122`, `EXPERIENCE.md:137-143`, `EXPERIENCE.md:174`).
- Anti-peek TPP có rule và acceptance qua shoulder/FOV/aspect ratio (`EXPERIENCE.md:124`; GDD `gdd.md:236-238`).
- Information parity được bảo vệ rõ: không footstep radar, enemy outline, damage number, loot recommendation/score hoặc map loot/enemy (`EXPERIENCE.md:81`, `EXPERIENCE.md:133`, `EXPERIENCE.md:157`, `EXPERIENCE.md:183`; GDD `gdd.md:296-298`, `gdd.md:456-459`, `gdd.md:471-473`).
- Reduce Motion/Flash giữ cue tương đương thay vì bỏ thông tin; critical states chủ yếu có icon + label + số/progress (`EXPERIENCE.md:84`, `EXPERIENCE.md:91`, `EXPERIENCE.md:159-161`).

## Critical (0)

Không có finding Critical.

## High (5)

### H1 — Contrast contract dừng trước bước compositing thực tế

Palette chỉ ghi tỷ lệ trên `{colors.surface-base}` và để việc kiểm lại opacity/compositing cho production, trong khi HUD, Inventory và Map được mô tả là bán trong trên nền thế giới thay đổi liên tục (`DESIGN.md:237`, `DESIGN.md:244`, `DESIGN.md:258`, `DESIGN.md:264`). Vì opacity hiệu dụng/backplate chưa phải token hay rule, các tỷ lệ đang ghi không chứng minh được text/icon/focus đạt floor trong rừng, sương, bầu trời hoặc muzzle flash. Điều này chưa đáp ứng chính floor nghiên cứu tại `.working/ux-research.md:33-35`.

*Fix cụ thể:* khóa opacity/backplate hoặc cơ chế bảo toàn contrast cho từng surface bán trong; thêm ma trận contrast cho mọi cặp foreground/background load-bearing sau compositing, qua cảnh sáng/tối/sương và ba preset mù màu. Acceptance phải fail nếu text thường <4,5:1 hoặc icon/focus/state cần thiết <3:1 trong ảnh chụp Godot thực tế.

### H2 — Ultrawide đang mở rộng world view nhưng chưa khóa camera fairness

Spine nói ultrawide “mở thêm world” trong khi chỉ cấm thêm HUD data (`EXPERIENCE.md:187`; `DESIGN.md:254`). Rule anti-peek có test qua aspect ratio (`EXPERIENCE.md:124`) nhưng chưa định nghĩa projection/FOV scaling, lượng world được nhìn thêm hay tiêu chí so sánh với 16:9. Đây là khoảng trống cạnh tranh: người chơi ultrawide có thể nhận thêm thông tin ngang dù HUD hoàn toàn tương đương.

*Fix cụ thể:* khóa chính sách camera theo aspect ratio/FOV và acceptance matrix 16:9–ultrawide: cùng vị trí/shoulder/FOV setting không được làm lộ mục tiêu, silhouette hoặc góc cover sớm hơn policy cho phép. Test cả hai vai camera, FOV min/max, sát tường/cửa sổ và các tỷ lệ ultrawide hỗ trợ; ghi rõ phần world nào được mở rộng/crop thay vì chỉ nói “không thêm HUD data”.

### H3 — Cảnh báo critical có thể tranh chấp và che mất trạng thái quyết định

`status-banner` chỉ cho phép một banner gameplay-critical cùng lúc (`EXPERIENCE.md:74`), nhưng whitelist có network, friendly-fire, system banner và nhiều `context-action-card` (`EXPERIENCE.md:84`, `EXPERIENCE.md:131`). `DESIGN.md` chỉ nói network/gục/danger được ưu tiên bằng vị trí/nhịp mà không có thứ tự hoặc preemption (`DESIGN.md:266`). Khi cháy xe đếm 3 giây, nhận sát thương, revive bị ngắt, bo thu và ping tăng cùng lúc, downstream không biết cue nào được giữ.

*Fix cụ thể:* thêm priority/preemption table cho từng critical state và quy tắc đồng thời. Các tín hiệu có deadline gây chết như fire countdown/zone/damage/revive interruption phải có kênh không bị banner mạng hoặc thông báo hệ thống xóa; ghi rõ cue nào gộp, queue, thu lại hay được phép song song. Thêm acceptance scenario cho ít nhất các tổ hợp trên ở 720p và 140% UI scale.

### H4 — Reticle và ba preset mù màu chưa có visual contract triển khai được

Accessibility Floor yêu cầu ba preset cho bo, marker, hit effect và reticle (`EXPERIENCE.md:170`), nhưng token/component list của `DESIGN.md` không định nghĩa reticle hay variant của các preset (`DESIGN.md:11-28`, `DESIGN.md:92-217`). Reticle là thông tin chiến đấu load-bearing trên nền thế giới, nên một tuyên bố chung về color+shape không đủ chứng minh khả năng đọc và parity.

*Fix cụ thể:* thêm contract thị giác cho reticle và bảng mapping của cả ba preset đối với bo/marker/hit effect/reticle. Mỗi variant phải giữ cùng hình học, timing và lượng thông tin; chỉ đổi kênh tiếp cận đã cho phép. Kiểm thử reticle/marker trên cảnh sáng, tối, sương, lá cây, bê tông, scope và hip-fire; ghi tiêu chí visibility/contrast hoặc adaptive outline không tiết lộ thêm mục tiêu.

### H5 — Spectator information parity vẫn là blocker mở

Spine cho chuyển teammate nhưng camera switching và thông tin được phép xem vẫn để mở (`EXPERIENCE.md:110`, `EXPERIENCE.md:116`, `EXPERIENCE.md:209`, `EXPERIENCE.md:251-254`). GDD chỉ cho xem đồng đội tới khi đội bị loại và loại spectator nâng cao khỏi v1.0 (`gdd.md:609`). Nếu implementation tự chọn camera, người đã chết có thể scout góc, audio hoặc marker ngoài khả năng của teammate còn sống.

*Fix cụ thể:* khóa camera, HUD, audio, marker, độ trễ và switching được phép trong spectator. Acceptance: spectator không bao giờ nhận world view, line-of-sight, directional audio, enemy/loot data hoặc marker nhiều hơn người còn sống đang được xem; khi stream state thiếu, không fallback sang free camera.

## Medium (5)

### M1 — UI scale chưa có floor cho kích thước chữ gameplay-critical

Typography có `caption` 12 px và `label` 14 px (`DESIGN.md:53-63`), trong khi UI scale cho phép 80–140% (`DESIGN.md:250`; `EXPERIENCE.md:168`). Ở 80%, hai style tương ứng chỉ còn 9,6 px và 11,2 px; spine chưa cấm dùng chúng cho dữ liệu critical. `status-banner` chỉ được giới hạn hai dòng ở 100%, chưa nói hành vi 140%/720p/localization (`DESIGN.md:283`; `EXPERIENCE.md:20`, `EXPERIENCE.md:187`).

*Fix cụ thể:* khóa minimum rendered size và style được phép cho từng lớp dữ liệu critical; ở 720p phải co spacing trước và không giảm critical text dưới floor. Định nghĩa wrap/reflow cho 80%, 100%, 140% và Việt/Anh; cấm truncate ammo, timer, ping/loss, revive/fire countdown, friendly-fire source và system critical copy.

### M2 — Keyboard parity chưa khóa focus lifecycle và thao tác Map

Spine khẳng định full keyboard navigation nhưng mới mô tả traversal chung (`EXPERIENCE.md:73`, `EXPERIENCE.md:122`, `EXPERIENCE.md:140`, `EXPERIENCE.md:174`). Inventory có action menu cho move/split/drop (`EXPERIENCE.md:86`), còn Map chỉ nói pan/zoom/marker và focus không bắt world camera; binding Map/Ping vẫn mở (`EXPERIENCE.md:88`, `EXPERIENCE.md:107`, `EXPERIENCE.md:123`). Không có rule khôi phục focus khi đóng modal/surface.

*Fix cụ thể:* với từng surface/modal, ghi initial focus, thứ tự traversal, focus trap nếu có và phần tử nhận lại focus khi đóng. Map phải có keyboard-equivalent cho pan/zoom/đặt/xóa marker; Inventory phải cho mọi thao tác drag bằng action menu. Thêm test keyboard-only từ launch → Deploy, Settings, Inventory, Map, Pause/confirm, Results và Report/Block mà không mất focus.

### M3 — Audio accessibility/fairness chưa có contract đo được

Spine chỉ nói audio mixer và HRTF “phải giữ công bằng” (`EXPERIENCE.md:172`) và để hearing-accessibility ngoài ping/subtitle thành scope mở (`EXPERIENCE.md:176`). Trong khi đó directional audio là tài nguyên chiến thuật và GDD đặt ngưỡng xác định đúng cung 30° ≥85% (`gdd.md:463-467`). Không có rule cho bus/slider/preset nào được phép thay đổi tỷ lệ footstep–gunshot–ambience hoặc cách kiểm thử HRTF khi settings khác nhau.

*Fix cụ thể:* khóa danh sách audio controls và parity rule: setting accessibility không được khuếch đại, lọc hoặc tách cue chiến thuật thành lợi thế mới. Chạy lại metric 30° ở mọi output mode/preset được hỗ trợ; định nghĩa visual+audio redundancy cho system, ping, heal/revive interruption, zone và vehicle fire, nhưng giữ nguyên lệnh cấm visual footstep radar.

### M4 — Reduce Motion/Flash đúng hướng nhưng chưa có giới hạn photosensitivity

Motion chỉ được mô tả là “ngắn”, không overshoot/bounce; pulse, shake và flash có fallback (`EXPERIENCE.md:159-161`; `DESIGN.md:312`). Photosensitivity limits vẫn được ghi là scope mở (`EXPERIENCE.md:176`), nên implementation chưa có trần tần suất, thời lượng, biên độ hay luminance change cho muzzle/hit/low-HP/win motion.

*Fix cụ thể:* thêm motion/flash budget đo được cho từng cue; chỉ rõ setting Reduce Motion và Reduce Flash tắt/giảm chính xác hiệu ứng nào. Mọi cue bị giảm phải giữ icon/label/audio hoặc state tĩnh tương đương; kiểm thử spam hit, low HP, nhiều grenade/vehicle fire và transition menu mà không vượt budget.

### M5 — Subtitle queue chưa bảo đảm không làm rơi thông báo critical

`subtitle-line` có “hàng đợi giới hạn” và ưu tiên system/ping hơn chatter nhưng không định nghĩa capacity, thời gian, preemption hay chính sách khi nhiều ping/system event cùng lúc (`EXPERIENCE.md:94`). Thiết kế chỉ yêu cầu không che reticle/prompt (`DESIGN.md:303`). Ở 720p hoặc UI scale 140%, một queue không khóa có thể che gameplay hoặc làm rơi cue cứu/bo/fire quan trọng.

*Fix cụ thể:* định nghĩa số dòng, thời gian tối thiểu/tối đa, dedupe, preemption và no-drop class cho critical system events; quy định reflow ở 720p/140% và collision với reticle, context prompt, revive/fire timer. Thêm scenario nhiều ping + system warning + voice state đồng thời.

## Low (1)

### L1 — Viền map load-bearing thấp hơn floor 3:1 theo chính token hiện tại

`minimap-zone-panel` dùng `{colors.border-default}` trên `{colors.surface-map}` (`DESIGN.md:147-152`). Từ hex hiện tại `#657168` và `#202A25`, contrast tính được khoảng **2,90:1**, thấp hơn floor 3:1 cho non-text UI cần thiết mà spine tự đặt (`DESIGN.md:244`).

*Fix cụ thể:* tăng contrast của border trên map hoặc bảo đảm boundary có thêm separation không phụ thuộc màu; ghi cặp đã kiểm chứng trong contrast matrix sau compositing. Nếu border chỉ trang trí, ghi rõ để downstream không dùng nó làm ranh giới tương tác/trạng thái.

## Finding counts

| Severity | Count |
|---|---:|
| Critical | 0 |
| High | 5 |
| Medium | 5 |
| Low | 1 |

## Kết luận lens

Ranh giới chống trợ chiến đã nhất quán với GDD và research: không footstep radar, damage number, loot score/recommendation, enemy detection hoặc ultrawide HUD advantage. Trước khi spine thành contract implementation, cần khóa năm High ở trên; đặc biệt H2 và H5 là fairness blockers, còn H1/H3/H4 là readability-accessibility blockers.
