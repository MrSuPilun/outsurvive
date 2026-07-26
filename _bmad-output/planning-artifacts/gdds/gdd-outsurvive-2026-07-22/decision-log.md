# OutSurvive - Nhật ký quyết định GDD

## Trạng thái

- Phiên bản: 1.1.0-ready-for-architecture
- Ngày cập nhật: 2026-07-22
- Trạng thái: Đang kiểm định và hoàn thiện

## Quyết định và tín hiệu thay đổi

| ID | Ngày | Trạng thái | Quyết định / tín hiệu | Lý do | Tác động |
|---|---|---|---|---|---|
| D-001 | 2026-07-22 | Đã xác nhận | Tên dự án là **OutSurvive** và engine mục tiêu là **Godot**. | Yêu cầu trực tiếp của người sáng lập. | GDD, kiến trúc và kế hoạch sản xuất dùng OutSurvive/Godot làm ngữ cảnh nền. |
| D-002 | 2026-07-22 | Đã xác nhận | Khôi phục bản sắc sinh tồn của battle royale đời đầu; skin và sự kiện thương mại không được lấn át gameplay. | Tầm nhìn trực tiếp của người sáng lập. | Trụ cột, vòng lặp, kinh tế và live-ops phải truy vết về giá trị sinh tồn. |
| D-003 | 2026-07-22 | Đã xác nhận | Phân loại BMAD chính là **Shooter**; battle royale/survival là cấu trúc và fantasy. | Người sáng lập chọn PUBG cổ điển làm nền tảng; shooter guide phù hợp với ngắm bắn, vũ khí, hitreg và map flow. | GDD có đầy đủ weapon feel, combat, hitreg, multiplayer và arena/map design. |
| D-004 | 2026-07-22 | Đã xác nhận | Làm việc theo chế độ **Express**, dùng PUBG cổ điển làm chuẩn cho các quyết định còn thiếu. | Chỉ dẫn “Cứ lấy lối chơi của game PUBG cổ điển làm nền tảng” trao quyền dùng reference thay cho facilitation từng mục. | GDD được draft trọn bộ, các suy luận ngoài reference được đánh dấu giả định. |
| D-005 | 2026-07-22 | Đã sửa bởi D-015 | Luật chuẩn: 100 người, 8×8 km, tay trắng, loot tại chỗ, bo thu hẹp, Solo/Duo/Squad, không hồi sinh; ràng buộc PC-first đã được bỏ. | Gameplay cốt lõi giữ nguyên khi phạm vi phát hành mở rộng. | Quy mô mạng, map và luật trận vẫn thiết kế quanh 100 người; platform/input do D-015/D-016 quản lý. |
| D-006 | 2026-07-22 | Đã xác nhận | Bốn trụ cột: đánh đổi sinh tồn; gunplay sát thương cao nhưng đọc được; thông tin/địa hình mạnh hơn đồ hiếm; sân chơi bình đẳng. | Chuyển động lực ban đầu thành tiêu chí ra quyết định đo được. | Mọi mechanic và epic phải truy vết về ít nhất một trụ cột. |
| D-007 | 2026-07-22 | Đã xác nhận | Standard không có hero/class, kỹ năng siêu nhiên, loadout, hồi sinh, self-revive hoặc pay-to-win. | Các hệ thống này làm giảm tính dễ tổn thương và hậu quả. | Được ghi là ngoài phạm vi vĩnh viễn của luật chuẩn. |
| D-008 | 2026-07-22 | Đề xuất có thể đổi | Bản đồ đầu tiên là **Đảo Vọng**, một quần đảo Đông Nam Á hư cấu. | Tạo bản sắc riêng thay vì sao chép Erangel trong khi giữ cấu trúc map cổ điển. | Art, audio và level framework dùng bối cảnh này; core loop không phụ thuộc tên/chủ đề. |
| D-009 | 2026-07-22 | Đã xác nhận cho v1.0 | v1.0 không có storefront, premium currency, microtransaction, battle pass, login streak, quảng cáo, collab hoặc live-event; mô hình phát hành thương mại chưa khóa. | Tránh tái tạo chính trọng tâm skin/sự kiện mà dự án phản đối. | E8 chuyển thành rào chắn tính toàn vẹn sản phẩm; business validation tách khỏi core gameplay. |
| D-010 | 2026-07-22 | Đã xác nhận | Dùng mốc Combat Sandbox → Vertical Slice 24 → Alpha tải 100 → Beta kín → v1.0. | Giữ mục tiêu 100 người nhưng kiểm chứng rủi ro theo tầng. | Không sản xuất toàn bộ content trước khi gunplay, mạng và streaming vượt cổng. |
| D-011 | 2026-07-22 | Đã xác nhận | Mọi nội dung hậu phát hành phải củng cố P1–P4 và vượt metric fairness/tension/readability; doanh thu không đủ để phê duyệt. | Chống dự án trượt khỏi tầm nhìn sau khi ra mắt. | GDD có cổng chống lệch tầm nhìn; đề xuất không đạt bị loại hoặc tách khỏi Standard. |
| D-012 | 2026-07-22 | Đã xác nhận | E2 chứng minh network combat 8 người; E5 chỉ greybox/2 POI; E6 chứng minh tải 100; E7 mới hoàn thiện art/content toàn bản đồ. | Loại vòng phụ thuộc giữa map content với multiplayer scale. | Epic DAG không còn yêu cầu E5 hoàn chỉnh trước chính cổng tải mà E5 phụ thuộc. |
| D-013 | 2026-07-22 | Đã thay thế bởi D-017 | Envelope PC-first 1–3 người Sandbox, 5–8 Vertical Slice, 12–20 core/24–36 tháng không còn đủ cơ sở cho phạm vi năm nền tảng. | Thêm macOS/Android/iOS làm tăng đáng kể build, signing, device QA, UX và performance work. | Architecture và production planning phải re-estimate trước R2; không dùng envelope cũ để cam kết lịch. |
| D-014 | 2026-07-22 | Đã hoàn tất | GDD 1.0.0 được đánh dấu **ready-for-architecture**. | Input reconciliation đã đóng 3 gap; revalidation đóng Q-2, G-1, S-2, S-3 và STK-1; không còn blocker kiến trúc. | `gdd.md`, `epics.md` và decision log là nguồn thiết kế chuẩn cho workflow kiến trúc tiếp theo. |
| D-015 | 2026-07-22 | Đã xác nhận | v1.0 hỗ trợ Windows, Linux, macOS, Android và iOS; input family là Keyboard/Mouse và Touch, controller/console ngoài phạm vi. | Chỉ dẫn trực tiếp “Android + iOS + MacOS, Incremental”. | GDD, UX, Epics, Architecture, QA và release pipeline đều phải đa nền tảng từ foundation. |
| D-016 | 2026-07-22 | Đã xác nhận | Keyboard/Mouse pool, Touch pool và Mixed/Keyboard-Mouse pool; input family khóa theo trận, mixed party phải disclosure, không silent bot/fallback. | Bảo vệ công bằng mà vẫn cho phép party đa thiết bị. | Matchmaking, party UX, signed input claim, telemetry và population gate trở thành yêu cầu bắt buộc. |
| D-017 | 2026-07-22 | Đã xác nhận | 100 người/8×8 km vẫn là north-star; 25 vũ khí, 6 xe, 18 POI và 420 công trình là provisional đến khi mobile viability và server scale cùng đạt. | Giữ bản sắc game nhưng không khóa content breadth trước khi chứng minh rủi ro lớn nhất. | R1–R4 có platform gate; mọi cắt giảm breadth cần change proposal riêng. |
| D-018 | 2026-07-22 | Đã hoàn tất | GDD và Epics 1.1.0 được đánh dấu **ready-for-architecture** theo phạm vi năm nền tảng. | Sprint Change Proposal đã được phê duyệt và các mâu thuẫn PC-only đã được xử lý. | Architecture tiếp tục từ Engine & Framework trên baseline mới. |

## Audit truy vết quyết định

| Quyết định | Nơi được phản ánh |
|---|---|
| D-001 | frontmatter, Đặc tả kỹ thuật |
| D-002 | Tóm tắt, Bối cảnh, P4, Kinh tế, Ngoài phạm vi |
| D-003 | frontmatter, Thiết kế chuyên biệt: Shooter |
| D-004 | toàn bộ bản draft và mục Giả định |
| D-005 | Vòng lặp, Multiplayer, Đảo Vọng, Vùng an toàn, Technical Metrics |
| D-006 | Game Pillars, Traceability, Epics |
| D-007 | Win/Loss, Multiplayer, Ngoài phạm vi |
| D-008 | Level Design, Art/Audio, Assumptions A-003 |
| D-009 | Kinh tế, Out of Scope, Assumptions A-002 |
| D-010 | Phạm vi sản xuất, epics.md |
| D-011 | Chỉ số thành công, E8, Out of Scope |
| D-012 | Tóm tắt Epic, epics.md E2/E5/E6/E7 |
| D-013 | Phạm vi sản xuất, Assumptions A-004 (đã thay thế) |
| D-014 | frontmatter GDD, phiên bản epics.md, mục Trạng thái này |
| D-015 | frontmatter, Điều khiển và đầu vào, Mục tiêu nền tảng, Ngoài phạm vi |
| D-016 | Nhiều người chơi, Hợp đồng đa nền tảng, Chỉ số kỹ thuật |
| D-017 | Ngân sách nội dung, Cổng tăng quy mô, A-005 |
| D-018 | frontmatter GDD, phiên bản epics.md, biên bản Finalize 1.1 |

## Câu hỏi mở

- Không có câu hỏi chặn `gds-game-architecture`.
- Business validation cho hình thức phát hành và chi phí máy chủ phải hoàn tất trước kế hoạch thương mại.
- Chủ đề/tên Đảo Vọng có thể thay đổi trong art pre-production mà không thay đổi core loop.

## Biên bản Finalize

- Input reconciliation: **Pass** — tầm nhìn sinh tồn, phản đối skin/sự kiện khai thác và baseline PUBG cổ điển đều được giữ.
- GDD discipline validation: **Pass** — weapon feel, shooter conventions, epic DAG, assumption index và readiness đều đạt.
- Template/placeholders: **Pass** — không còn token hoặc mục trống.
- Doc standards tùy biến: không có tiêu chuẩn bổ sung trong cấu hình workflow; áp dụng discipline chuẩn của GDD.
- Assumptions còn mở: A-001 đến A-005; A-004 đã bị thay thế và A-003/A-005 chặn cam kết production/content scale nếu chưa được kiểm chứng.
- Amendment 1.1: **Pass** — năm nền tảng, hai input family, matchmaking pools, mobile budgets và platform release gates đã được đồng bộ vào GDD/Epics.
- Next gate: `gds-game-architecture` phải kiểm chứng networking, streaming, dedicated-server resource, mobile renderer/lifecycle và lộ trình 8→24→100 client.
