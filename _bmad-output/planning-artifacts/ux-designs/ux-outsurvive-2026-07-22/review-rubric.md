# Spine Pair Review — OutSurvive

## Overall verdict

Hai spine là một contract **adequate** cho kiến trúc sơ bộ: source resolve, token hợp lệ, component parity hoàn chỉnh, IA/state tables có cấu trúc và ba journey bao phủ vòng lặp chính. Chúng chưa final-ready vì một số state multiplayer/post-match vẫn là `[NOTE FOR UX]`, timing lộ bo kế tiếp chưa được mang vào behavior contract và bốn visual reference load-bearing của UX-014 chưa được dựng/distill.

Finding counts: **Critical 0 · High 2 · Medium 4 · Low 1**.

## 1. Flow coverage — adequate

Đã đối chiếu vòng đời trận, Solo/Squad, Training, Settings, Profile, kết quả, network confirmation, bot disclosure, report và failure paths với GDD. Ba Key Flow đều có protagonist được đặt tên, bước đánh số, climax và failure path: Minh (core loop), Lan (Squad/DBNO), Quân (settings/training/network).

### Findings

- **[medium]** Surface Closure gộp “Training/onboarding” và tự đánh dấu đã có journey, nhưng hành trình Quân chỉ chủ động vào Training; onboarding curriculum vẫn được ghi là open nên phần onboarding chưa thực sự có flow hoặc surface contract. (`EXPERIENCE.md:212`, `EXPERIENCE.md:256`, `EXPERIENCE.md:290`). *Fix:* tách hàng Training khỏi Onboarding; hoặc định nghĩa một onboarding flow tối thiểu với entry/skip/complete/failure, hoặc ghi rõ onboarding deferred/out-of-scope thay vì tuyên bố closure.

## 2. Token completeness — adequate

Frontmatter parse được; cả 17 color token đều là hex; typography/rounded/spacing/components đúng shape; 34 `{path.to.token}` reference đều resolve. Contrast target được nêu cho text, icon và focus, nhưng còn một tổ hợp load-bearing chưa đạt chính floor đã cam kết.

### Findings

- **[medium]** `minimap-zone-panel` dùng `{colors.border-default}` (`#657168`) trên `{colors.surface-map}` (`#202A25`); tỷ lệ tính từ token là khoảng **2,90:1**, thấp hơn floor non-text 3:1 được spine cam kết. (`DESIGN.md:15`, `DESIGN.md:21`, `DESIGN.md:147`, `DESIGN.md:152`, `DESIGN.md:244`; floor được nhắc lại tại `EXPERIENCE.md:167`). *Fix:* tăng nhẹ độ sáng/độ tương phản của `border-default` hoặc dùng border token riêng đã kiểm thử ≥3:1 trên `surface-map`, rồi kiểm lại sau opacity/compositing trong Godot.

## 3. Component coverage — strong

Đã trích 24 component key từ `DESIGN.md` frontmatter. Cả 24 đều có visual row thực chất trong `DESIGN.md.Components` và behavioral row thực chất, cùng tên chính xác, trong `EXPERIENCE.md.Component Patterns`; không có key thừa hoặc thiếu và mọi token component đều resolve.

### Findings

Không có.

## 4. State coverage — thin

Mỗi surface trong IA đều có một hàng State Patterns tương ứng; cold/empty/focus/error/offline/permission được phân bổ hợp lý. Tuy nhiên một số state chuyển tiếp ảnh hưởng trực tiếp tới multiplayer và post-match mới chỉ được liệt kê như gap, chưa đủ làm contract implementation.

### Findings

- **[high]** Reconnect timeout, AFK, party leader/ready và các chuyển tiếp ownership vẫn mở; bảng chỉ nói “thử reconnect” hoặc gắn nhãn mà không khóa trigger, thời hạn, authority, destination và hậu quả trận. Đây là blocker cho matchmaking/party/match lifecycle stories. (`EXPERIENCE.md:101`, `EXPERIENCE.md:104`, `EXPERIENCE.md:105`, `EXPERIENCE.md:116`, `EXPERIENCE.md:153`, `EXPERIENCE.md:290`). *Fix:* thêm state-transition table tối thiểu cho Party, Queue, Pre-match và Live Match với trigger → visible state → timeout/authority → next state; những con số cần backend quyết định có thể giữ `[NOTE FOR UX]` nhưng phải chỉ rõ owner và acceptance gate.
- **[medium]** Spectator switching, replay-summary payload và report taxonomy vẫn open dù Results/Spectator/Report đã được coi là closed surfaces và xuất hiện trong journey Lan/Minh. (`EXPERIENCE.md:110`–`116`, `EXPERIENCE.md:209`–`214`, `EXPERIENCE.md:237`, `EXPERIENCE.md:254`, `EXPERIENCE.md:290`). *Fix:* khóa minimum viable payload và transition cho ba surface này, hoặc đánh dấu rõ surface nào deferred để downstream không tự phát minh camera/data/category.

## 5. Visual reference coverage — adequate

`imports/` không có input ngoài `.gitkeep`; chưa tồn tại `mockups/` hoặc `wireframes/`, vì vậy không có orphan hay broken inline link. Quy tắc spine-wins-on-conflict được nêu một lần ở Foundation.

### Findings

- **[medium]** UX-014 yêu cầu bốn visual reference load-bearing (Lobby, Match HUD, Inventory, Map/Phase); cả DESIGN và Surface Closure mới ghi “dựng sau Reviewer Gate”. Đây là trạng thái đúng tại gate nhưng chưa đủ để đóng Finalize hoặc xác nhận occlusion/eye-travel. (`DESIGN.md:260`, `EXPERIENCE.md:22`, `EXPERIENCE.md:193`–`204`). *Fix:* sau khi resolve High findings, dựng bốn mockup, link inline tại section liên quan, ghi rõ điều chúng minh họa và distill mọi quyết định mới ngược vào hai spine.

## 6. Bloat & overspecification — adequate

DESIGN.md dùng prose cho editorial posture và bảng cho token/component; EXPERIENCE.md ưu tiên IA/state/component/surface tables. Các chi tiết camera, vehicle, inventory và anti-pattern đều phục vụ fairness hoặc downstream acceptance, không phải trang trí. Sự lặp giữa frontmatter component token và body visual rationale là shape bắt buộc của Google Labs spec.

### Findings

Không có.

## 7. Inheritance discipline — adequate

Hai `sources` frontmatter cùng resolve tới GDD 1.0.0; terminology chính, component names và token references nhất quán. Các assumption UX-004–UX-017 được gắn và lập chỉ mục; các mục UX-018–UX-020 là quyết định xác nhận từ GDD nên không cần assumption tag.

### Findings

- **[high]** GDD khóa việc chỉ lộ tâm pha bo kế tiếp khi pha chờ bắt đầu, nhưng EXPERIENCE chỉ nói Map/Minimap hiển thị “current/next zone” mà không mang timing/visibility gate vào behavior hoặc state. Một consumer chỉ đọc spine có thể hiển thị bo kế tiếp quá sớm, làm rò thông tin cạnh tranh. (`gdd.md:374`, `EXPERIENCE.md:38`, `EXPERIENCE.md:81`, `EXPERIENCE.md:107`, `EXPERIENCE.md:149`). *Fix:* thêm một câu behavior/state duy nhất: next-zone geometry ẩn cho tới server-confirmed start của wait phase; trước đó không render placeholder/prediction.
- **[low]** HUD contract gọi “bảy nhóm persistent” nhưng câu liệt kê ghép `minimap/phase` thành một nhóm và chỉ tạo sáu cụm ngữ nghĩa, trong khi GDD liệt kê riêng hướng, minimap và pha bo. Component có thể vẫn gộp panel, nhưng wording/count hiện mơ hồ cho người triển khai. (`gdd.md:456`, `EXPERIENCE.md:131`, `EXPERIENCE.md:201`). *Fix:* liệt kê đúng bảy content groups (HP/boost; ammo; stance; direction; minimap; squad; zone phase), rồi nói rõ chúng có thể render qua sáu module vì `minimap-zone-panel` chứa hai nhóm.

## 8. Shape fit — strong

DESIGN.md tuân đúng thứ tự canonical: Brand & Style → Colors → Typography → Layout & Spacing → Elevation & Depth → Shapes → Components → Do's and Don'ts. EXPERIENCE.md có đủ Foundation, IA, Voice and Tone, Component Patterns, State Patterns, Interaction Primitives, Accessibility Floor và Key Flows; các section HUD, Input, Inventory/Map/Party, Game Feel, Inspiration, Responsive và Surface Closure đều được platform/source kích hoạt và có lý do tồn tại.

### Findings

Không có.

## Mechanical notes

- Frontmatter: cả hai file parse thành mapping; `status: draft`; source path tồn tại.
- Tokens: 17 colors đều `#RRGGBB`; 34 cross-reference path resolve; không có reference mồ côi.
- Components: 24 YAML keys = 24 visual rows = 24 behavioral rows; exact parity.
- Journeys: 3 protagonist; 3 climax; 3 failure paths; mọi bước được đánh số.
- States: 16 IA surfaces được phủ bởi 15 state rows vì “Sảnh chờ / Máy bay” được gộp có chủ đích.
- Visual artifacts: không có file trong `imports/`, `mockups/`, `wireframes` ngoài `.gitkeep`; không có orphan.
- Mermaid: không dùng.
- Open items: 12 `[NOTE FOR UX]`; phần lớn đã được triage, nhưng các finding High/Medium ở trên phải đóng hoặc defer rõ trước khi đổi spine sang `final`.
