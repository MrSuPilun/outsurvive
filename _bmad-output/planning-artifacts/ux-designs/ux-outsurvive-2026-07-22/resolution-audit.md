# Resolution Audit — OutSurvive UX Reviewer Gate

**Mục đích:** hợp nhất 32 finding thô từ ba reviewer thành các cụm quyết định không trùng lặp, chỉ ra quyền sở hữu và acceptance tối thiểu trước khi cập nhật spine.  
**Nguồn:** `review-rubric.md`, `review-pc-hud-input.md`, `review-accessibility-fairness.md`, và GDD `../../gdds/gdd-outsurvive-2026-07-22/gdd.md`.  
**Trạng thái:** đề xuất audit read-only; chưa phải quyết định đã ghi log và không tự sửa `DESIGN.md`/`EXPERIENCE.md`.

## Quy ước phân loại

- **source-confirmed:** GDD đã khóa nhu cầu hoặc giới hạn; UX chỉ được đặc tả cách truyền đạt, không đổi lượng thông tin hay luật chơi.
- **UX assumption:** reviewer/spine đề xuất chi tiết chưa có trong GDD; phải được chấp nhận và ghi log trước khi trở thành contract.
- **architecture dependency:** cần chính sách từ camera/input/network/backend/server authority trước khi UX có thể khóa state/flow.
- **deferred v1.0:** GDD đã loại khỏi v1.0; không được đưa trở lại bằng một “fix UX”.

## Kết quả de-duplication

32 finding thô được hợp nhất thành **17 cụm**, dùng dải ID ổn định **UX-021–UX-037**.

| ID | Cụm quyết định | Finding được hợp nhất | Phân loại chính |
|---|---|---|---|
| UX-021 | Responsive safe frame, UI/text scale và overflow | PC H-01, PC L-02, AF M1 | UX assumption; source-confirmed cho dải resolution/ultrawide |
| UX-022 | Contrast sau compositing và boundary map | Rubric Token, AF H1, AF L1 | UX assumption; source-confirmed cho color redundancy |
| UX-023 | Priority/lane/suppression của overlay và subtitle | PC H-02, AF H3, AF M5 | UX assumption |
| UX-024 | Camera ultrawide và anti-peek fairness | AF H2 | source-confirmed + architecture dependency |
| UX-025 | Colorblind preset, reticle và teammate marker identity | PC M-02, AF H4 | source-confirmed + UX assumption |
| UX-026 | Input routing Map/Inventory và keyboard focus parity | PC H-03, AF M2 | UX assumption + architecture dependency |
| UX-027 | Action inventory, full remap và persistence | PC H-04, PC L-01 | source-confirmed + architecture dependency |
| UX-028 | Party, team voice và 8 contextual pings | PC H-05; phần Party của Rubric State | source-confirmed + UX assumption + architecture dependency |
| UX-029 | Reconnect/AFK multiplayer state machine | phần Reconnect/AFK của Rubric State và PC H-06 | architecture dependency; chưa được GDD xác nhận |
| UX-030 | Basic teammate spectator và information parity | AF H5; phần Spectator của PC H-06/Rubric State | source-confirmed; advanced spectator = deferred v1.0 |
| UX-031 | Results, replay summary, report/block payload | phần Results/Replay/Report của Rubric State | source-confirmed + architecture dependency; full replay/kill-cam = deferred v1.0 |
| UX-032 | Zone phase anatomy, next-zone timing và HUD group wording | Rubric next-zone, Rubric HUD count, PC M-01 | source-confirmed + UX assumption |
| UX-033 | Contextual combat-state microcontracts | PC M-03, M-04, M-05, M-06 | source-confirmed + UX assumption |
| UX-034 | Audio/HRTF accessibility và information parity | AF M3 | source-confirmed + UX assumption |
| UX-035 | Reduce Motion/Flash và photosensitivity budget | AF M4 | source-confirmed + UX assumption |
| UX-036 | Onboarding scope và flow | Rubric Flow | source-confirmed + UX assumption |
| UX-037 | Bốn visual reference load-bearing | Rubric Visual Reference | UX assumption / workflow dependency |

## Scope and fairness guardrails

Các guardrail dưới đây thắng mọi fix reviewer nếu có xung đột:

1. **Ping/voice:** GDD chỉ xác nhận giao tiếp đội bằng voice, ping vị trí và 8 ping ngữ cảnh; ping không tự nhận dạng địch xuyên vật cản (`gdd.md:350`). Proximity/global voice, speech-to-text, voice command recognition, auto-enemy tagging, ping xuyên cover hoặc ping suy ra thông tin chưa quan sát đều là **scope mới** và cần cập nhật GDD. TTL/cooldown chỉ được chống spam, không được tăng độ chính xác hoặc tuổi thọ thông tin quá mức.
2. **Reconnect/AFK:** GDD không khóa rejoin, avatar protection, AI takeover, timeout hay trạng thái nhân vật khi mất mạng. Thêm invulnerability, ẩn avatar, bot điều khiển, giữ vị trí an toàn hoặc hoàn tác cái chết sẽ thay đổi luật cạnh tranh. UX-029 chỉ được hiển thị policy do gameplay/network architecture phê duyệt; không tự đặt policy.
3. **Spectator:** v1.0 chỉ cho xem đồng đội tới khi đội bị loại (`gdd.md:152`). Advanced spectator bị loại khỏi v1.0 (`gdd.md:609`). Không free camera, x-ray, enemy outline, thêm directional audio, loot/enemy marker hoặc HUD data ngoài những gì teammate còn sống có.
4. **Colorblind/reticle:** GDD xác nhận đúng ba preset cho bo, marker, hit effect và reticle (`gdd.md:471-473`). Preset phải giữ nguyên geometry, timing và lượng thông tin; không enemy-reactive reticle/outline, không tăng phát hiện silhouette và không chuyển âm thanh chiến thuật thành marker.
5. **Audio accessibility:** system/ping subtitle là source-confirmed; visual footstep radar bị cấm vì đổi cân bằng thông tin (`gdd.md:473`). Mixer/HRTF hoặc dynamic processing không được tạo preset làm bước chân/súng dễ phát hiện hơn baseline ngoài policy âm thanh đã kiểm chứng.
6. **Replay/post-death:** GDD yêu cầu thống kê + replay tóm tắt (`gdd.md:141`) và report/block/log điều tra (`gdd.md:508-510`), nhưng full replay, competitive kill-cam và advanced spectator bị defer (`gdd.md:609`). “Replay summary” không được âm thầm trở thành kill-cam hoặc công cụ scout.
7. **Onboarding:** E7 đưa onboarding vào phạm vi v1.0 (`gdd.md:551`). Đánh dấu deferred là thay đổi scope, cần chủ dự án chấp thuận; onboarding không được thêm reward, mastery progress hoặc trợ chiến vào Standard.

## Acceptance tối thiểu theo ID

### UX-021 — Responsive safe frame, UI/text scale và overflow

**Quyết định cần khóa:** công thức central 16:9 safe frame, breakpoint/reflow, minimum rendered size và wrap/overflow cho tiếng Việt, tiếng Anh và key label dài. `5%`, UI scale 80–140% và world strip Inventory ≥32% hiện là UX assumptions; GDD chỉ khóa 1280×720–3840×2160 và ultrawide (`gdd.md:481-482`).

**Acceptance tối thiểu:** snapshot 1280×720, 1920×1080, 2560×1440, 3840×2160 và ít nhất hai ultrawide tại 80/100/140%; không critical HUD crop/chồng, không đẩy module ra khỏi central 16:9, Inventory giữ world strip ≥32%, và ammo/timer/ping/revive/fire/friendly-fire copy không truncate hoặc thiếu glyph.

### UX-022 — Contrast sau compositing và boundary map

**Quyết định cần khóa:** opacity/backplate cho surface bán trong, contrast matrix sau compositing và vai trò load-bearing của border. Palette/opacity là UX assumption; GDD chỉ yêu cầu colorblind presets và không dùng màu đơn độc cho cấp vật phẩm (`gdd.md:471-473`).

**Acceptance tối thiểu:** ảnh chụp Godot trong cảnh sáng, tối, sương và hiệu ứng chiến đấu đạt text thường ≥4,5:1, icon/focus/state cần thiết ≥3:1 sau compositing; kiểm cả ba preset. `border-default` trên `surface-map` phải đạt ≥3:1 nếu là boundary chức năng, hoặc có separation không phụ thuộc màu và được ghi là không load-bearing.

### UX-023 — Priority/lane/suppression của overlay và subtitle

**Quyết định cần khóa:** một bảng duy nhất cho priority, anchor lane, z-order, lifetime, queue, preemption và suppression của damage, fire countdown, revive/heal, zone, network, friendly-fire, prompt, ping và subtitle.

**Acceptance tối thiểu:** stress test 720p/140% đồng thời có fire countdown, damage hai hướng, high ping, teammate down, context prompt và subtitle; reticle/HP/ammo/phase không bị che, không có hai card tranh cùng anchor, fatal deadline không bị network/system banner xóa, và critical system subtitle không bị drop.

### UX-024 — Camera ultrawide và anti-peek fairness

**Quyết định cần khóa:** camera/FOV projection policy theo aspect ratio và owner phê duyệt delta world view. GDD xác nhận ultrawide và anti-corner-peek (`gdd.md:236-238`, `gdd.md:482`) nhưng không cho UX tự quyết lượng world được mở rộng.

**Acceptance tối thiểu:** matrix 16:9 và các ultrawide được hỗ trợ, cả hai shoulder, FOV min/max, sát tường/cửa sổ/cover; không aspect ratio nào bypass head line-of-sight hoặc làm lộ mục tiêu trước policy đã phê duyệt. Mọi khác biệt world view phải được ghi rõ, không chỉ nói “HUD data bằng nhau”.

### UX-025 — Colorblind preset, reticle và teammate marker identity

**Quyết định cần khóa:** mapping của ba preset cho bo/marker/hit/reticle; visual contract của reticle; một teammate identity bằng number/shape/label dùng thống nhất world ping–compass–map–squad, màu chỉ phụ trợ.

**Acceptance tối thiểu:** mỗi preset giữ cùng geometry/timing/data; reticle đọc được trên cảnh sáng/tối/sương/lá/bê tông và không phản ứng với enemy; với squad bốn người, người test ghép đúng teammate → ping → marker trên các surface ≥95% trong bài test định trước. Không preset nào thêm outline/radar/detection.

### UX-026 — Input routing Map/Inventory và keyboard focus parity

**Quyết định cần khóa:** input-routing matrix cho Match HUD, Inventory, Map và Pause: cursor/pointer lock, WASD, camera, fire/ADS, vehicle, scroll, close binding; initial/return focus và keyboard equivalent.

**Acceptance tối thiểu:** mở/đóng Inventory và Map khi đi bộ, ADS, ở ghế lái/ghế phụ và đang nhận damage; UI click/scroll không kích hoạt gameplay ngoài contract, close binding luôn hoạt động, audio thế giới giữ nguyên, mọi drag/drop/pan/zoom/marker có đường keyboard và focus trở về đúng phần tử/surface.

### UX-027 — Action inventory, full remap và persistence

**Quyết định cần khóa:** danh sách action v1.0, primary/secondary binding, conflict classes, duplicate-by-context, required/reserved actions, mouse extra button/wheel, Apply/Cancel/rollback và local/profile persistence. Full remap/hold-toggle/sensitivity là source-confirmed (`gdd.md:235-238`, `gdd.md:471`).

**Acceptance tối thiểu:** remap được Map, Ping/Radial, shoulder swap, zeroing, breath hold, ADS, lean và Inventory; conflict nêu cả hai action, không Apply trạng thái mất đường confirm/back/close, prompt cập nhật ngay, Cancel/Apply/restart/reset cho kết quả dự đoán được và binding hợp lệ còn sau restart.

### UX-028 — Party, team voice và 8 contextual pings

**Quyết định cần khóa:** state join/ready/leader/mode/disconnect; team voice PTT/mute/volume; đúng tám ping với label/icon/source, placement, replace/cancel, TTL/cooldown. Invite provider và voice transport là architecture dependency.

**Acceptance tối thiểu:** squad bốn người join–ready–đổi mode–disconnect/rejoin theo policy UX-029; mute/volume từng người; bốn người ping gần nhau vẫn phân biệt nguồn trên world/compass/map và spam không che combat HUD. Ping không nhận dạng enemy xuyên cover hoặc tự suy diễn thông tin. Mọi channel ngoài team voice cần GDD change.

### UX-029 — Reconnect/AFK multiplayer state machine

**Quyết định cần khóa bởi gameplay/network architecture trước:** avatar authority khi disconnect, có/không rejoin, timeout, AFK policy, input/state preservation, team eliminated during reconnect và destination cuối. Đây không phải source-confirmed UX requirement.

**Acceptance tối thiểu nếu rejoin được duyệt:** test disconnect tại sảnh chờ, máy bay, alive, DBNO và spectator; mỗi case có visible state/timer/cancel, server-authoritative result và destination Match HUD/Spectator/Results; không invulnerability, bot takeover, vị trí ẩn hoặc hoàn tác death nếu chưa có GDD approval. **Nếu deferred:** spine phải nói rõ không hỗ trợ rejoin v1.0 và không hiển thị promise “Reconnecting”.

### UX-030 — Basic teammate spectator và information parity

**Quyết định cần khóa:** target cycling, camera mode, HUD/audio/marker subset, lỗi stream và exit/result transition cho basic teammate spectator; advanced features vẫn deferred.

**Acceptance tối thiểu:** spectator không nhận world view, line-of-sight, directional audio, enemy/loot data hoặc marker nhiều hơn teammate đang xem; không fallback free camera; khi không còn teammate sống chuyển đúng Results. Thử các case alive teammate, DBNO, disconnect, team eliminated và stream unavailable.

### UX-031 — Results, replay summary, report/block payload

**Quyết định cần khóa:** minimum payload của results/replay summary, Pending/error state, report taxonomy/retention owner và retry/block behavior. Full replay/kill-cam không thuộc cụm v1.0.

**Acceptance tối thiểu:** Results luôn có placement, survival time và combat/survival summary đã xác nhận hoặc `Pending`; thiếu summary không được thay bằng kill-cam giả. Report network failure giữ draft theo policy đã duyệt, Block có trạng thái rõ, và không surface nào lộ dữ liệu cạnh tranh bị GDD defer.

### UX-032 — Zone phase anatomy, next-zone timing và HUD group wording

**Quyết định cần khóa:** liệt kê đúng bảy content groups GDD (HP/boost, ammo, stance, direction, minimap, squad, zone phase), dù render qua sáu module; anatomy phase gồm number, wait/shrink, countdown và outside-zone state.

**Acceptance tối thiểu:** next-zone geometry không render/placeholder/predict trước server-confirmed start của wait phase (`gdd.md:374`); sau mốc đó Map/Minimap nhất quán. Ở 720p và 4K, người test xác định phase, wait/shrink và thời gian còn lại trong ≤1 giây mà không mở Map.

### UX-033 — Contextual combat-state microcontracts

**Quyết định cần khóa:** bốn contract nhỏ, không thêm persistent HUD group ngoài whitelist:

- vehicle fire cue sống tới hết **remaining server-confirmed** countdown sau khi rời ghế;
- armor/mũ current-max/broken có visual anatomy trong Inventory;
- context prompt arbitration khi nhiều action cùng vùng;
- nếu giữ assumption Map không tự đóng khi nhận damage, cung 30° phải screen-relative theo camera thế giới tại hit, không theo orientation map.

**Acceptance tối thiểu:** (a) driver/passenger/người vừa exit không mất fire cue trước nổ/hủy; (b) giáp nguyên/vỡ và durability so sánh được ở 720p, 80–140%, ba preset mà không chỉ dùng màu; (c) doorway + loot + DBNO teammate + vehicle cho action ưu tiên dự đoán được và action phụ vẫn truy cập; (d) damage-on-map không chính xác hơn cung 30° GDD và không mắc focus khi đóng Map.

### UX-034 — Audio/HRTF accessibility và information parity

**Quyết định cần khóa:** danh sách audio controls/output modes, parity rule cho mixer/dynamic processing và visual+audio redundancy cho system/ping/heal-revive interruption/zone/vehicle fire.

**Acceptance tối thiểu:** metric GDD xác định đúng cung 30° đạt ≥85% ở 20–80 m trên mọi output mode/preset cạnh tranh được hỗ trợ (`gdd.md:467`); accessibility setting không khuếch đại/tách cue tactical thành lợi thế mới; không footstep radar, enemy marker hoặc audio-to-visual detection.

### UX-035 — Reduce Motion/Flash và photosensitivity budget

**Quyết định cần khóa:** motion/flash budget theo cue và hành vi chính xác của Reduce Motion/Reduce Flash. GDD xác nhận camera shake và flash intensity chỉnh được (`gdd.md:471`); transition style/budget là UX assumption.

**Acceptance tối thiểu:** spam hit, low HP, grenade/vehicle fire và menu transition không vượt budget đã ghi; pulse/shake/flash bị tắt/giảm vẫn giữ icon/label/audio hoặc state tĩnh tương đương, không bỏ thông tin gameplay.

### UX-036 — Onboarding scope và flow

**Quyết định cần khóa:** hoặc một onboarding v1.0 tối thiểu với entry/skip/complete/failure và đường vào Training, hoặc GDD change chính thức để defer. Không được tiếp tục gọi Training journey là coverage đầy đủ của onboarding.

**Acceptance tối thiểu nếu giữ v1.0:** người mới có thể vào, bỏ qua, hoàn tất và quay lại; nội dung dạy input/loot/zone/feedback mà không cấp reward, mastery/stat Standard hoặc thông tin trợ chiến bị cấm. Nếu defer, Surface Closure và E7 phải được reconcile thay vì chỉ ghi NOTE.

### UX-037 — Bốn visual reference load-bearing

**Quyết định cần khóa:** đây là workflow dependency do UX-014 đề xuất, không phải yêu cầu GDD. Phạm vi hiện tại là Lobby, Match HUD, Inventory và Map/Phase.

**Acceptance tối thiểu:** bốn mockup kiểm tra occlusion/eye travel tại ít nhất 720p/140% và 1080p/100%; mỗi artifact được link inline, nêu rõ điều minh họa, và mọi quyết định mới được distill ngược vào spine. Mockup không được thêm surface, data hoặc component ngoài contract.

## Crosswalk 32 finding → ID

Finding hỗn hợp được tách sang hai ID theo owner; không có finding nào bị bỏ.

| Reviewer finding | Resolution ID |
|---|---|
| Rubric Flow — onboarding closure | UX-036 |
| Rubric Token — map border 2,90:1 | UX-022 |
| Rubric State — reconnect/AFK/party ownership | UX-028, UX-029 |
| Rubric State — spectator/replay/report | UX-030, UX-031 |
| Rubric Visual Reference — bốn mockup | UX-037 |
| Rubric Inheritance — next-zone timing | UX-032 |
| Rubric Inheritance — “bảy nhóm” mơ hồ | UX-032 |
| PC H-01 — safe frame/breakpoint | UX-021 |
| PC H-02 — overlay matrix | UX-023 |
| PC H-03 — Map/Inventory input capture | UX-026 |
| PC H-04 — full remap rules | UX-027 |
| PC H-05 — party/voice/8 ping | UX-028 |
| PC H-06 — reconnect/spectator | UX-029, UX-030 |
| PC M-01 — phase anatomy | UX-032 |
| PC M-02 — teammate marker identity | UX-025 |
| PC M-03 — vehicle warning after exit | UX-033 |
| PC M-04 — armor durability visual | UX-033 |
| PC M-05 — prompt arbitration | UX-033 |
| PC M-06 — damage cue on Map | UX-033 |
| PC L-01 — rebind persistence | UX-027 |
| PC L-02 — font/key-label overflow | UX-021 |
| AF H1 — composited contrast | UX-022 |
| AF H2 — ultrawide world fairness | UX-024 |
| AF H3 — critical-state contention | UX-023 |
| AF H4 — reticle/colorblind presets | UX-025 |
| AF H5 — spectator information parity | UX-030 |
| AF M1 — UI-scale text floor | UX-021 |
| AF M2 — keyboard/focus parity | UX-026 |
| AF M3 — audio/HRTF parity | UX-034 |
| AF M4 — motion/photosensitivity | UX-035 |
| AF M5 — subtitle queue | UX-023 |
| AF L1 — map border contrast | UX-022 |

## Resolution order đề xuất

1. **Gameplay/source leak blockers:** UX-024, UX-028, UX-029, UX-030, UX-032.
2. **HUD readability/input blockers:** UX-021, UX-022, UX-023, UX-025, UX-026, UX-027.
3. **Bounded surface contracts:** UX-031, UX-033, UX-034, UX-035, UX-036.
4. **Visual proof và distillation:** UX-037 sau khi các quyết định trên đã được chấp nhận.

Không ID nào trong audit này tự trở thành quyết định. Các cụm `UX assumption` cần chủ dự án chấp nhận; các cụm `architecture dependency` cần owner kỹ thuật/gameplay khóa policy trước khi spine được cập nhật.
