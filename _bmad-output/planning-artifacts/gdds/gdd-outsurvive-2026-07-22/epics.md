# OutSurvive - Development Epics

**GDD:** [gdd.md](./gdd.md)  
**Phiên bản:** 1.1.0  
**Ngày:** 2026-07-22

## Nguyên tắc phân rã

- Mỗi epic kết thúc bằng một giá trị có thể chơi hoặc kiểm chứng, không chỉ hoàn thành hạ tầng.
- Thứ tự ưu tiên chứng minh cảm giác và rủi ro kỹ thuật trước khi sản xuất toàn bộ nội dung.
- Mọi input adapter tạo cùng semantic gameplay command; Definition of Done của story ảnh hưởng người chơi phải kiểm tra đường Keyboard/Mouse và Touch tương ứng, không phân nhánh luật gameplay theo platform.
- Build smoke và mobile viability bắt đầu ở E1. Certification hoàn chỉnh vẫn thuộc E9; mobile không phải một port làm sau cùng.
- Story dưới đây là high-level story; tiêu chí chấp nhận chi tiết được tạo trong workflow `gds-create-epics-and-stories` sau kiến trúc.

## Chuỗi phụ thuộc

- `E1 → E2 → E3 → E4`
- `E1 + E3 + E4 → E5` (greybox và representative slice)
- `E1–E5 → E6` (mở rộng multiplayer từ 8/24 lên 100)
- `E2 + E5 + E6 → E7` (art/content pass toàn bản đồ sau cổng tải)
- `E4 + E6 + E7 → E8`
- `E1–E8 → E9`

E2 chứa network combat slice tối thiểu 8 người để kiểm chứng hitreg. E5 chỉ sản xuất greybox 8×8 km và hai POI đại diện; E6 chứng minh tải 100 người trước khi E7 cho phép art/content pass toàn bản đồ.

---

## E1 — Nền tảng người sống sót đa nền tảng

**Giá trị:** Người chơi Keyboard/Mouse hoặc Touch di chuyển, quan sát và tương tác qua cùng semantic command layer với nhịp độ đúng tinh thần OutSurvive.  
**Trụ cột:** P1, P2.  
**Cổng hoàn thành:** 8 người chơi thử trên desktop/mobile hoàn thành course; thông số tốc độ/tư thế nằm trong ±5% GDD, không có lỗi nhìn xuyên cover nghiêm trọng và build smoke chạy trên cả năm nền tảng.

### High-level stories

1. E1-S1 — Di chuyển đứng, đi bộ, chạy và chạy nước rút với gia tốc/giảm tốc có thể tinh chỉnh.
2. E1-S2 — Ngồi, nằm, nghiêng và chuyển tư thế với collision/readability đúng.
3. E1-S3 — Nhảy, rơi, leo/vượt vật cản và sát thương rơi.
4. E1-S4 — Camera TPP, đổi vai, ADS và chống nhìn xuyên góc.
5. E1-S5 — Tương tác nhặt, mở cửa, dùng vật thể và ưu tiên mục tiêu tương tác.
6. E1-S6 — Gán lại phím hoặc Touch layout, độ nhạy, FOV và tùy chọn toggle/hold nền tảng.
7. E1-S7 — Course kiểm thử tự động/thủ công cho mọi thông số di chuyển.
8. E1-S8 — Semantic `GameplayCommand` dùng chung cho InputMap, Touch, Gyro, prediction và network input frame.
9. E1-S9 — Mobile survivor controller landscape với safe area, left-stick, right-look và context actions không auto-play.

---

## E2 — Đấu súng đáng tin cậy

**Giá trị:** Người chơi có thể đấu súng 1v1/4v4 với đạn, giật, sát thương và feedback đủ rõ để đánh giá kỹ năng.  
**Trụ cột:** P2, P4.  
**Cổng hoàn thành:** Combat Sandbox network slice 8 người đạt profile desktop/mobile tương ứng; hitreg có thẩm quyền trong điều kiện 80 ms/1% loss sai lệch ≤0,5 m ở p95 và không phụ thuộc input sampling rate. E6 chịu trách nhiệm mở rộng mô hình này tới 100 người.

### High-level stories

1. E2-S1 — Trạng thái vũ khí: equip, hip-fire, aim, ADS, bắn, nạp và đổi súng.
2. E2-S2 — Đạn có vận tốc, rơi, va chạm và suy giảm sát thương theo cự ly.
3. E2-S3 — Pattern giật, độ tản, hồi giật và modifier theo tư thế/chuyển động.
4. E2-S4 — HP, vùng trúng, giáp, mũ, độ bền và tử vong.
5. E2-S5 — Feedback bắn/trúng/bị bắn bằng hình ảnh, âm thanh và camera.
6. E2-S6 — 8 archetype chuẩn và bảng dữ liệu cân bằng đầu tiên.
7. E2-S7 — Phụ kiện, scope, zeroing và giữ hơi.
8. E2-S8 — Network combat slice 8 người trên protocol/platform mix với shot authority, bù trễ giới hạn và bộ test TTK/đường đạn/giật/hitreg lặp lại.
9. E2-S9 — Mobile aim/fire/Gyro fairness harness; cấm target snap, auto-fire và enemy detection, chỉ cho phép thử friction trong Touch pool qua cổng dữ liệu.

---

## E3 — Loot và quản trị sinh tồn

**Giá trị:** Người chơi bắt đầu tay trắng, tìm trang bị, đưa ra đánh đổi kho đồ và sống sót sau giao tranh.  
**Trụ cột:** P1, P3.  
**Cổng hoàn thành:** 95% lượt test có súng sau 90 giây tại cụm nhà chuẩn; mọi vật phẩm có vai trò và chi phí sức chứa đo được.

### High-level stories

1. E3-S1 — Spawn loot theo loại không gian, rarity, seed và trọng số.
2. E3-S2 — Kho đồ, sức chứa, ô trang bị, thao tác nhặt/thả/đổi.
3. E3-S3 — Đạn theo cỡ, phụ kiện tương thích và tự nhặt có ngưỡng.
4. E3-S4 — Băng, cứu thương, tăng lực, thời gian dùng và ngắt hành động.
5. E3-S5 — Bốn vật ném với fuse, quỹ đạo, vùng ảnh hưởng và counter-play.
6. E3-S6 — Ba cấp ba lô, giáp, mũ và phản hồi độ bền.
7. E3-S7 — Thùng tiếp tế, khói báo hiệu và loot đặc biệt.
8. E3-S8 — Telemetry loot để đo thời gian có súng, phân bố tài nguyên và scarcity.
9. E3-S9 — Tap-first mobile loot/inventory với panel tabbed ≤62%, world-risk strip ≥38% và parity hành động không tăng auto-loot.

---

## E4 — Vòng đời battle royale

**Giá trị:** Một trận có thể đi từ sảnh chờ đến người sống cuối cùng với luật Solo/Duo/Squad.  
**Trụ cột:** P1, P3, P4.  
**Cổng hoàn thành:** Vertical Slice 24 mixed clients hoàn thành 20 trận liên tiếp không kẹt trạng thái, kể cả interruption/reconnect; thời lượng 12–15 phút trên map 2×2 km.

### High-level stories

1. E4-S1 — Sảnh chờ, khóa roster, đếm ngược và khởi tạo trận.
2. E4-S2 — Đường bay, nhảy, dù, tốc độ rơi và tiếp đất.
3. E4-S3 — Vùng an toàn chín pha, dự báo bo và sát thương ngoài bo.
4. E4-S4 — Trạng thái gục, bleed, cứu, kết liễu và toàn đội bị loại.
5. E4-S5 — Điều kiện thắng/thua, xử lý hòa, rời trận và kết quả.
6. E4-S6 — Solo, Duo, Squad, friendly fire và spectate đồng đội.
7. E4-S7 — Match timeline/telemetry cho số người sống, kill và nguyên nhân chết.
8. E4-S8 — Luồng reconnect có giới hạn cho mất kết nối, process restart và network handoff ngắn, không tạo lợi thế.
9. E4-S9 — Mobile lifecycle `Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended` với test OS interruption.

---

## E5 — Đảo Vọng và phương tiện

**Giá trị:** Người chơi đọc được một bản đồ lớn, chọn điểm rơi, route, cover và phương tiện thay vì chỉ chạy đến marker.  
**Trụ cột:** P1, P3.  
**Cổng hoàn thành:** Greybox 8×8 km và hai POI đại diện hỗ trợ vertical slice 24 mixed clients; mobile đạt memory/thermal/load gate đại diện, không có choke bắt buộc duy nhất hoặc final circle không thể chơi trong 1.000 seed bo. Tải 100 client thuộc E6/E9; content breadth vẫn provisional đến khi hai cổng cùng đạt.

### High-level stories

1. E5-S1 — Greybox 8×8 km với địa hình, coast, đường và 18 POI.
2. E5-S2 — Bộ module kiến trúc và hai POI đại diện; 420 công trình là content target sau E6.
3. E5-S3 — Quy tắc cover, sightline, roof access và tuyến rút.
4. E5-S4 — Biển báo, landmark, bản đồ/minimap và tên địa danh.
5. E5-S5 — Sáu archetype phương tiện, nhiên liệu, lốp, va chạm và nổ.
6. E5-S6 — Spawn phương tiện/thuyền và kiểm tra khả năng di chuyển theo seed bo.
7. E5-S7 — Trời quang, mưa, sương và tác động tầm nhìn/âm thanh.
8. E5-S8 — Streaming/performance gate 24 mixed clients cho greybox và hai POI đại diện trên desktop/mobile renderer profile.
9. E5-S9 — Mobile LOD/streaming/dynamic-resolution/memory/thermal gate cùng Touch controls cho sáu archetype phương tiện.

---

## E6 — Multiplayer cạnh tranh đa nền tảng

**Giá trị:** Network combat slice đã được chứng minh ở E2 mở rộng thành trận 100 người đáng tin cậy, dùng chung protocol và chính sách pool công bằng trên năm nền tảng.  
**Trụ cột:** P2, P4.  
**Cổng hoàn thành:** Ba soak test 100 client protocol mix +10% headroom, 30 Hz ổn định; xử lý sát thương ≤1 tick p95; từng input pool đạt population gate mà không silent bot/fallback.

### High-level stories

1. E6-S1 — Máy chủ trận đấu có thẩm quyền cho vị trí, bắn, sát thương, loot và kết quả.
2. E6-S2 — Đồng bộ chuyển động/tư thế/phương tiện với budget băng thông.
3. E6-S3 — Bù trễ giới hạn, hit validation và replay sự kiện bắn.
4. E6-S4 — Tổ đội đa nền tảng, platform identity, lời mời, ready, voice permission và ping ngữ cảnh.
5. E6-S5 — Ghép vùng theo ping, Solo/Duo/Squad, MMR mềm và Touch/Keyboard-Mouse/Mixed pool có disclosure.
6. E6-S6 — Reconnect, mobile lifecycle timeout, crash/process recovery, network handoff và xử lý người bỏ trận.
7. E6-S7 — Soak/load test 24→50→100 client với network impairment.
8. E6-S8 — Công cụ điều tra desync, hitreg và kết quả trận.
9. E6-S9 — Signed input-family claim, match-lock, population telemetry và cổng cấm silent bot/pool fallback.

---

## E7 — Độ rõ và khả năng tiếp cận đa thiết bị

**Giá trị:** Người chơi hiểu bản đồ, trạng thái, hướng nguy hiểm và lựa chọn qua art, HUD và audio hoàn chỉnh mà không bị thông báo thương mại che lấp.  
**Trụ cột:** P2, P3, P4.  
**Cổng hoàn thành:** ≥85% lần xác định đúng cung âm 30°; 100% thao tác chính gán lại được; HUD pass 720p–4K và phone/tablet landscape có safe area, không tăng thông tin trên mobile.

### High-level stories

1. E7-S1 — HUD HP, đạn, tư thế, đội, compass, minimap và bo.
2. E7-S2 — Kho đồ, loot panel, map và kết quả có interaction parity giữa chuột và tap/pan/pinch/long-press.
3. E7-S3 — Âm bước chân theo vật liệu, khoảng cách và tư thế.
4. E7-S4 — Âm súng gần/xa, giảm thanh, đạn bay/va chạm và occlusion.
5. E7-S5 — Âm phương tiện, môi trường, mưa/sương và mix ưu tiên chiến đấu.
6. E7-S6 — Preset mù màu, giảm flash/rung, phụ đề và scale UI.
7. E7-S7 — Training Grounds, bia, bot luyện tập và hướng dẫn điều khiển.
8. E7-S8 — Death summary giải thích nguồn sát thương mà không tiết lộ thông tin khi đội còn sống.
9. E7-S9 — Art, collision và gameplay-readability pass cho 18 POI/420 công trình sau khi E6 vượt cổng tải.
10. E7-S10 — Adaptive mobile HUD, `safe-area-root`, Touch components và control layout editor lưu theo device class.
11. E7-S11 — Mobile accessibility, Gyro, haptic, audio interruption/route change và contextual permission flows.

---

## E8 — Hồ sơ và tính toàn vẹn sản phẩm

**Giá trị:** Người chơi theo dõi tiến bộ kỹ năng mà không bị cửa hàng, tiền tệ cao cấp, lịch FOMO hoặc lớp meta cạnh tranh với gameplay.  
**Trụ cột:** P4.  
**Cổng hoàn thành:** Build v1.0 không có storefront, premium currency, microtransaction, battle pass, login streak hoặc reward hết hạn; dữ liệu hồ sơ không đi vào tính toán sức mạnh.

### High-level stories

1. E8-S1 — Hồ sơ, thống kê trận, lịch sử và thành tích.
2. E8-S2 — Weapon Mastery chỉ gồm số liệu và huy hiệu hồ sơ không sức mạnh.
3. E8-S3 — Audit loại storefront, premium currency và bề mặt FOMO khỏi v1.0.
4. E8-S4 — Chính sách cấm quảng cáo, collab và live-event trong HUD/map Standard.
5. E8-S5 — Cổng đánh giá mọi đề xuất hậu phát hành theo P1–P4 và metric gameplay.
6. E8-S6 — Audit telemetry để KPI doanh thu/engagement không ghi đè fairness, tension và readability.
7. E8-S7 — Decision record riêng cho mô hình phát hành và chi phí máy chủ, không chặn core gameplay.
8. E8-S8 — Platform privacy, account/data lifecycle, secure entitlement và store metadata không tạo monetization loop.

---

## E9 — Ổn định và chứng nhận đa nền tảng

**Giá trị:** OutSurvive có thể build, ký, chứng nhận và vận hành trận công bằng trên Windows, Linux, macOS, Android và iOS với hiệu năng, bảo mật và phản hồi đủ tin cậy.  
**Trụ cột:** P2, P4.  
**Cổng hoàn thành:** Đạt mọi Technical Metric và Gameplay Gate trong GDD qua ba release-candidate family liên tiếp trên Windows, Linux, macOS, Android và iOS.

### High-level stories

1. E9-S1 — Benchmark chuẩn cho client, server, khói, xe, thành phố và bo cuối.
2. E9-S2 — Profile/optimize tới ngân sách FPS, RAM, tải và băng thông.
3. E9-S3 — Crash reporting, log, metric, cảnh báo và runbook sự cố.
4. E9-S4 — Báo cáo người chơi, block, moderation và evidence replay.
5. E9-S5 — Phòng chống gian lận, giả mạo trạng thái và lạm dụng giao thức.
6. E9-S6 — Test matrix chức năng, network, hiệu năng, accessibility, compatibility và platform lifecycle trên desktop/mobile.
7. E9-S7 — Beta kín 100 người và quy trình cân bằng dựa trên dữ liệu.
8. E9-S8 — Release candidate, rollback, patch nhỏ và kiểm tra dữ liệu sau phát hành.
9. E9-S9 — Five-platform CI/build/sign/release: desktop packages, macOS Universal 2/notarization, Android ARM64 AAB và iOS archive/TestFlight.
10. E9-S10 — Mobile device lab cho thermal, memory, battery, cellular impairment, interruption, safe area và store certification.

---

## Ma trận truy vết Epic → cơ chế

| Cơ chế/hệ thống | Epic chính | Epic hỗ trợ |
|---|---|---|
| Semantic input, di chuyển, tư thế, camera | E1 | E2, E6, E7 |
| Vũ khí, đạn, giật, hitreg | E2 | E6, E9 |
| Loot, kho, hồi máu, vật ném | E3 | E4, E7 |
| Máy bay, dù, bo, thắng/thua | E4 | E5, E6 |
| Map, cover, weather, xe | E5 | E7, E9 |
| 100 người, platform identity, tổ đội, input pools | E6 | E4, E9 |
| Adaptive HUD, Touch UI, audio, accessibility, training | E7 | E1–E6 |
| Hồ sơ, mastery và rào chắn tính toàn vẹn sản phẩm | E8 | E6, E9 |
| Performance, anti-cheat, five-platform CI/certification, QA, ops | E9 | E1–E8 |

## Ma trận truy vết thay đổi đa nền tảng

| Yêu cầu 1.1 | Story sở hữu | Cổng liên quan |
|---|---|---|
| Semantic command + Touch/Gyro | E1-S8/S9, E2-S9 | E1/E2 |
| Tap-first inventory/map | E3-S9, E7-S2 | E3/E7 |
| Mobile lifecycle/network handoff | E4-S8/S9, E6-S6 | E4/E6 |
| Mobile renderer/streaming/thermal | E5-S8/S9, E9-S2/S10 | E5/E9 |
| Platform identity và input pools | E6-S4/S5/S9 | E6 |
| Adaptive HUD/safe area/accessibility | E7-S10/S11 | E7 |
| Privacy/entitlement integrity | E8-S8 | E8 |
| Five-platform build/sign/release | E9-S6/S9/S10 | E9 |
