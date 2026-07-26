---
stepsCompleted:
  - step-01-document-discovery
  - step-02-gdd-analysis
  - step-03-epic-coverage-validation
  - step-04-ux-alignment
  - step-05-epic-quality-review
  - step-06-final-assessment
filesIncluded:
  gdd:
    - _bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md
    - _bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/decision-log.md
  architecture:
    - _bmad-output/game-architecture.md
  epics:
    - _bmad-output/planning-artifacts/epics.md
  ux:
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/DESIGN.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/reconcile-gdd.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/resolution-audit.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/review-pc-hud-input.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/final-ux-verification.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/.decision-log.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/resolution-verification.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/review-accessibility-fairness.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/validation-report.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/review-rubric.md
    - _bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/mobile-delta-validation.md
filesExcluded:
  - _bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/epics.md
---

# Implementation Readiness Assessment Report

**Date:** 2026-07-26
**Project:** outsurvive

## Document Inventory

### GDD

- Primary: `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md`
- Supporting decision record: `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/decision-log.md`
- Organization note: the GDD collection has no `index.md`.

### Architecture

- Primary: `_bmad-output/game-architecture.md`
- Location note: this document is outside the configured `planning_artifacts` directory.

### Epics and Stories

- Primary: `_bmad-output/planning-artifacts/epics.md`
- Excluded as superseded: `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/epics.md`

### UX Design

- Primary: `DESIGN.md` and `EXPERIENCE.md` in `_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/`
- Supporting: reconciliation, review, validation, verification, mobile-delta, and decision-log documents in the same collection.
- Organization note: the UX collection has no `index.md`.

### Discovery Issues and Resolution

- The Architecture document was accepted from outside `planning_artifacts`.
- The newer root-level `epics.md` was selected as authoritative; the older GDD-bundled copy was excluded.
- Non-indexed GDD and UX document collections were accepted for assessment.

## GDD Analysis

GDD không cung cấp mã FR/NFR nguyên bản. Các mã dưới đây được cấp trong lần đánh giá này để phục vụ truy vết; nội dung giữ các luật, thông số và ngưỡng chấp nhận của GDD 1.1.0 cùng decision log.

### Functional Requirements

FR1: Luật Standard phải hỗ trợ trận battle royale 100 người trên bản đồ 8 × 8 km; người chơi xuất phát tay trắng, tự chọn nơi tiếp đất, nhặt trang bị tại chỗ, di chuyển theo vùng an toàn thu hẹp và chiến đấu đến khi còn một người hoặc một đội sống sót.

FR2: Người chơi phải chọn được Solo, Duo hoặc Squad trước khi vào sảnh chờ 60 giây; không được chọn vũ khí, loadout hoặc kỹ năng trước trận.

FR3: Trận đấu phải triển khai đủ chuỗi quan sát đường bay 30–45 giây, đổ bộ 20–90 giây, trang bị ban đầu 2–5 phút, đọc vùng an toàn, di chuyển/giao tranh, kết thúc với 5–10 người cuối và màn hình kết quả.

FR4: Solo phải trao chiến thắng cho người chơi sống cuối cùng; Duo/Squad phải trao chiến thắng cho đội còn ít nhất một thành viên sống khi mọi đội khác đã bị loại.

FR5: Người chơi phải bị loại khi HP về 0 trong Solo, khi bị kết liễu trong trạng thái Gục, hoặc khi toàn đội không còn thành viên có thể chiến đấu.

FR6: Rời trận sau khi máy bay khởi hành phải được tính là thất bại; người đã bị loại phải có thể xem đồng đội cho đến khi đội bị loại.

FR7: Standard không được có hồi sinh, mua lại, tự hồi sinh hoặc trạm triệu hồi.

FR8: Hệ thống di chuyển phải hỗ trợ đi bộ 2,3 m/s, chạy 4,5 m/s, chạy nước rút 6,3 m/s, ngồi 1,8 m/s, nằm 0,8 m/s, nhảy cao tối đa 0,9 m, leo/vượt vật cản 0,6–1,4 m và nghiêng người tối đa 18° với các đánh đổi về tiếng động, bắn, ADS, độ giật và tốc độ như GDD quy định.

FR9: Trò chơi không được có thanh stamina; rơi từ trên 3 m phải bắt đầu gây sát thương và rơi từ 8 m có thể gây tử vong khi không đầy máu.

FR10: Nước sâu phải giảm tốc người chơi còn 2,0 m/s, khóa vũ khí và giới hạn lặn ở 20 giây trước khi mất HP.

FR11: Mỗi người chơi phải có 100 HP và HP không tự hồi; sát thương vùng phải áp dụng đầu ×2,20, ngực ×1,00, bụng ×0,90 và tay/chân ×0,75.

FR12: Áo giáp cấp 1/2/3 phải giảm sát thương thân 15%/30%/45% với độ bền 160/220/280; mũ cấp 1/2/3 phải giảm sát thương đầu 30%/45%/55% với độ bền 80/150/230. Giáp phải giảm sát thương của viên đạn làm độ bền về 0 rồi mới bị phá hủy.

FR13: Hệ thống hồi phục phải cung cấp băng cá nhân dùng 3,5 giây và hồi +10 HP trong 4 giây không vượt 75 HP; túi cứu thương dùng 6 giây đưa HP lên 75; bộ cứu thương lớn dùng 9 giây đưa HP lên 100; nước tăng lực dùng 4 giây cho +40 hồi phục theo thời gian; thuốc giảm đau dùng 6 giây cho +60 hồi phục theo thời gian.

FR14: Dùng túi cứu thương và các hành động hồi phục có quy định phải bị ngắt khi người chơi di chuyển hoặc chịu sát thương; điểm tăng lực không được vượt 100.

FR15: Trong Duo/Squad, HP về 0 phải tạo trạng thái Gục với 100 HP chảy máu, mất 2 HP/giây lần đầu và nhân đôi tốc độ sau mỗi lần gục tiếp theo.

FR16: Hồi đồng đội phải mất 10 giây và bị ngắt khi người cứu di chuyển hoặc chịu sát thương; người gục chỉ được bò 0,7 m/s, đánh dấu và nói chuyện, không được dùng súng, hồi máu hoặc tự cứu.

FR17: Kho đồ phải có 50 đơn vị sức chứa cơ thể; ba cấp ba lô phải nâng tổng sức chứa lên 120/180/250.

FR18: Trang bị phải có hai ô vũ khí chính, một ô súng ngắn, một ô cận chiến và một ô vật ném đang chọn; đạn, hồi máu và vật ném dùng sức chứa còn phụ kiện đã gắn trên súng không dùng sức chứa.

FR19: Nhặt nhanh phải mất 0,20 giây mỗi món; kéo thả trong giao diện không được làm chậm thời gian trận. Không được tự động nhặt vũ khí, giáp hoặc phụ kiện; người chơi có thể bật tự nhặt đạn đúng cỡ đến ngưỡng tự đặt.

FR20: Loot phải sinh theo nhóm logic của loại không gian, còn vật phẩm cụ thể phải được chọn ngẫu nhiên có trọng số mỗi trận.

FR21: Sau 90 giây loot một cụm nhà trung bình, hệ thống loot phải hướng đến 95% người chơi có ít nhất một súng, 70% có vũ khí chính, 50% có giáp hoặc mũ và 35% có hồi máu.

FR22: Khu dân cư nhỏ phải ưu tiên đồ cơ bản; cơ sở quân sự, cảng và công nghiệp phải có loot tốt hơn đồng thời có nhiều đường tiếp cận và tỷ lệ tranh chấp cao hơn.

FR23: Một thùng tiếp tế phải xuất hiện trong mỗi pha bo 1–5 tại vị trí có thể tiếp cận, phát khói nhìn thấy ở 800 m và chứa một vũ khí đặc biệt cùng giáp/hồi máu cấp cao; không vật phẩm thiết yếu nào được độc quyền trong thùng tiếp tế.

FR24: Hệ thống vật ném phải cung cấp lựu đạn mảnh ngòi 5 giây với vùng chí mạng 3 m và sát thương đến 8 m; lựu đạn khói phát sau 1,5 giây, tồn tại 25 giây với đường kính 12 m; lựu choáng ngòi 2,5 giây, hiệu lực tối đa 5 giây trong 5 m có đường nhìn; chai cháy tồn tại 12 giây trong vùng 4 m và gây 10 sát thương/giây.

FR25: Người chơi chỉ được mang tối đa 6 vật ném theo sức chứa; quỹ đạo dự kiến chỉ được hiện trong 1,5 giây đầu khi ngắm.

FR26: Phương tiện phải có sáu archetype: sedan 4 chỗ, jeep 4 chỗ, bán tải 4 chỗ, xe máy 2 chỗ, thuyền 4 chỗ và xe tải 6 chỗ.

FR27: Phương tiện phải đạt tốc độ tối đa 80–125 km/h tùy loại, cần nhiên liệu, có lốp có thể phá, phát nổ sau khi HP về 0 với cảnh báo cháy 3 giây và tạo tiếng nghe được từ 250–450 m.

FR28: Va chạm xe trên 35 km/h phải gây sát thương; trên 70 km/h có thể hạ gục người không có vật cản che. Standard không được có xe bọc thép mua ngoài trận.

FR29: Gameplay phải chỉ tiêu thụ lệnh ngữ nghĩa dùng chung; Keyboard/Mouse, Touch và Gyro tùy chọn phải là adapter đầu vào và không tạo luật gameplay riêng theo nền tảng.

FR30: Keyboard/Mouse phải hỗ trợ WASD di chuyển, chuột điều khiển camera/ngắm, Shift chạy nhanh, Ctrl đi bộ, C ngồi, Z nằm, Space nhảy/vượt, Q/E nghiêng, F tương tác, R nạp đạn, G chọn vật ném và Tab mở kho đồ.

FR31: Touch landscape phải có cần di chuyển trái, vùng nhìn phải, nút bắn phải, nút bắn trái tùy chọn và các nút ngữ cảnh cho tư thế, tương tác, nạp đạn, ADS, vật ném và phương tiện; bố cục, kích thước và độ trong suốt phải được lưu theo lớp thiết bị.

FR32: Gyro phải là tùy chọn ngắm bổ trợ. Touch không được có target snap, auto-fire, enemy detection hoặc chỉ báo bước chân trực quan; aim slowdown/friction chỉ được xem xét sau prototype công bằng trong Touch pool và không được bật mặc định.

FR33: TPP phải là góc nhìn chuẩn với khả năng chuyển vai camera; ADS phải chuyển sang góc nhìn thứ nhất qua thước ngắm/ống ngắm.

FR34: Camera phải bị đẩy về phía trước khi sát tường; vật thể hoặc đối thủ không được hiển thị nếu đường nhìn từ đầu nhân vật bị che hoàn toàn.

FR35: Người chơi phải gán lại được toàn bộ phím hoặc bố cục Touch, chỉnh riêng độ nhạy hip-fire/ADS/từng độ phóng và chọn giữ/nhấn cho ADS, nghiêng, ngồi và chạy.

FR36: Danh mục v1.0 phải hướng đến 25 vũ khí gồm 3 súng ngắn, 3 SMG, 3 shotgun, 5 assault rifle, 3 DMR, 3 sniper rifle, 2 LMG và 3 vũ khí cận chiến.

FR37: Hệ thống đạn phải có 9 mm, .45, 5,56 mm, 7,62 mm và 12 gauge, mỗi cỡ có màu, hình hộp và biểu tượng riêng; phụ kiện phải gồm 4 đầu nòng, 4 tay cầm, 3 băng đạn, 2 báng và 7 loại ngắm từ red dot đến 8×.

FR38: Vũ khí không được lên cấp, mang qua trận hoặc có skin trong v1.0.

FR39: Các archetype vũ khí phải triển khai sát thương, RPM, dung lượng băng, vận tốc, thời gian nạp, falloff và cự ly chủ đạo theo các bảng “Cảm giác vũ khí mục tiêu”; sau mốc falloff cuối, sát thương phải giữ ở 55% giá trị gốc.

FR40: AR ở 20 m phải hướng đến TTK 0,17–0,25 giây khi không giáp và 0,25–0,40 giây qua giáp cấp 2; từng vũ khí phải nằm trong dải sau thay đổi damage/RPM.

FR41: Đạn vũ khí chính phải có thời gian bay và độ rơi; không được dùng hitscan cho vũ khí chính.

FR42: Độ giật phải tăng trong 8 viên đầu, ổn định sau viên 12 và bắt đầu hồi sau khi ngừng bắn 0,25 giây; spread phải nhân theo tư thế: ngồi ×0,75, nằm ×0,55, đi bộ ×1,30, chạy ×2,20 và nhảy ×4,00 so với đứng yên.

FR43: Mỗi phát bắn phải phân biệt được bằng tiếng nổ, tiếng cơ khí, lóe nòng, vỏ đạn và phản lực camera; Standard không được hiển thị số sát thương nổi.

FR44: Trúng mục tiêu phải tạo phản hồi máu/bụi theo cài đặt nội dung, âm thanh nhẹ và phản ứng cơ thể; không được xác nhận hạ gục trước khi máy chủ xác nhận trạng thái.

FR45: Người bị bắn phải nhận chỉ báo hướng theo cung 30° nhưng không được hiển thị vị trí hoặc khoảng cách kẻ bắn.

FR46: Chiến đấu phải hỗ trợ TPP hip-fire, ngắm qua vai và ADS qua sight, chuyển trạng thái theo thời gian ADS của vũ khí.

FR47: Scope 4× trở lên phải hỗ trợ giữ hơi tối đa 8 giây; khi hết hơi, dao động phải tăng ×2 trong 4 giây. Scope phù hợp phải cho chỉnh zero 100–800 m theo bước 100 m.

FR48: Aim punch phải phụ thuộc năng lượng viên đạn và giáp, tối đa 1,5° mỗi hit với ngưỡng 0,12 giây; chuột không được có aim assist, magnetism hoặc đạn bẻ hướng.

FR49: Cận chiến phải có tầm 1,8 m, wind-up 0,35–0,55 giây và sát thương 35–60.

FR50: Vị trí, phát bắn, sát thương, loot và thắng/thua phải do máy chủ trận đấu xác nhận.

FR51: Hit trade phải được chấp nhận nếu hai phát bắn hợp lệ đã rời nòng trước khi một bên bị loại; replay phải thể hiện thứ tự xác nhận.

FR52: Đối thủ trong Standard phải là người thật; không được có quái, boss hoặc NPC chiến đấu. Bot không được âm thầm lấp đầy trận; hàng chờ thử nghiệm dùng bot phải công bố số bot dự kiến trước khi vào trận.

FR53: Training Grounds phải có bia tĩnh, bia di động 2–8 m/s và bot luyện tập với ba hành vi lao qua khoảng trống, đổi cover và peak/bắn trả; kết quả training không được ảnh hưởng thống kê cạnh tranh.

FR54: Đảo Vọng phải hướng đến bản đồ 8 × 8 km với khoảng 58% đất liền, 12% đảo nhỏ và 30% mặt nước/biên không đi bộ; target nội dung là 18 POI đặt tên, 55 cụm nhà nhỏ, tối thiểu 420 công trình có thể vào, 180 vị trí xe có trọng số và 12 bến thuyền.

FR55: Không gian giao tranh phải phục vụ cự ly 0–25 m trong nhà, 40–150 m ở làng/rừng, 150–400 m ở ruộng/sườn đồi/đường và chỉ cho sightline 400–800 m tại các vị trí có đánh đổi rõ.

FR56: Mỗi vùng trống dài trên 120 m phải có ít nhất hai lựa chọn trong cover cứng, địa hình lõm, khói, xe hoặc tuyến vòng; cầu và đèo phải có tuyến vòng chậm hơn, không được tạo choke bắt buộc duy nhất.

FR57: Vòng cuối không được đặt quá 50% diện tích trên nước, vách không thể đứng hoặc mái không thể tiếp cận; cover v1.0 phải tĩnh, không phá nhà, đào đất hoặc xây công sự.

FR58: Thời tiết phải được chọn khi bắt đầu trận với tỷ lệ trời quang 70%, mưa 15%, sương 15% và không đổi đột ngột giữa trận.

FR59: Mưa phải giảm khoảng nghe bước chân 15% và tăng tiếng môi trường; sương phải giới hạn độ tương phản mục tiêu sau 180–250 m. Không được có đêm tối hoàn toàn.

FR60: Multiplayer phải hỗ trợ Solo 100 người, Duo tối đa 50 đội và Squad 25 đội bốn người.

FR61: Ghép trận phải ưu tiên vùng mạng và thời gian chờ; MMR mềm chỉ được ngăn người mới gặp nhóm kỹ năng cao nhất trong 10 trận đầu.

FR62: Keyboard/Mouse pool phải phục vụ Windows, Linux và macOS; Touch pool phục vụ Android và iOS; party trộn input family phải vào Mixed/Keyboard-Mouse pool sau khi UI công bố rõ trước khi ready.

FR63: Input family phải khóa khi vào trận; Keyboard/Mouse ngoài trên mobile phải buộc rời hàng chờ và requeue; không được đổi input family giữa trận, âm thầm lấp bot, đổi pool hoặc nới quy tắc công bằng.

FR64: Tài khoản, progression, party và backend phải dùng chung; mọi nền tảng phải dùng cùng dữ liệu cân bằng, protocol và quyền quyết định của máy chủ, còn mobile không được nhận thêm thông tin chiến đấu.

FR65: Standard phải là luật chơi chính; ranked, custom server và giải đấu phải hoãn đến khi Standard ổn định. FPP-only chỉ là ứng viên sau v1.0 khi dân số đủ để không chia nhỏ cộng đồng.

FR66: Giao tiếp đội phải hỗ trợ voice, ping vị trí và 8 ping ngữ cảnh; ping không được tự nhận dạng kẻ địch xuyên vật cản.

FR67: Friendly fire phải bật ở 100% sát thương sau khi lên máy bay; UI phải ghi rõ nguồn sát thương và cung cấp luồng báo cáo.

FR68: Vùng an toàn phải triển khai đủ 9 pha với thời gian chờ/thu, bán kính, sát thương ngoài bo và dải người sống mục tiêu theo bảng GDD; tổng thời gian tối đa khoảng 32 phút 30 giây sau khi bo đầu bắt đầu.

FR69: Tâm pha tiếp theo phải được lộ khi pha chờ bắt đầu; không được có vật phẩm dự báo bo hoặc vùng ném bom ngẫu nhiên gây chết tức thời.

FR70: Tiến trình trong trận phải chuyển từ trang bị tự vệ ở phút 0–3, hoàn thiện hai vai trò vũ khí và đường di chuyển ở phút 3–10, tối ưu phụ kiện/hồi máu/vật ném/vị trí ở phút 10–22, sang ưu tiên vị trí, khói, thông tin và kỷ luật khai hỏa sau phút 22.

FR71: Tiến trình ngoài trận không được tăng chỉ số, perk, vũ khí, phụ kiện hoặc sức chứa.

FR72: Hồ sơ phải ghi số trận, top 10, chiến thắng, cự ly hạ gục, độ chính xác và lịch sử mùa; Weapon Mastery chỉ được mở số liệu chuyên sâu và huy hiệu hồ sơ, không mở skin hoặc sức mạnh; phần thưởng thành tích phải lâu dài, không hết hạn và không yêu cầu đăng nhập hằng ngày.

FR73: v1.0 không được có cửa hàng trong game, premium currency, microtransaction, loot box, gacha, battle pass, daily login streak, quảng cáo hoặc live-event; toàn bộ bản đồ, vũ khí và luật chơi ảnh hưởng gameplay phải thuộc cùng một quyền truy cập sản phẩm.

FR74: Không vũ khí loot thường nào được vượt 22% số hạ gục trong mẫu tối thiểu 10.000 mạng; vũ khí thùng tiếp tế không được vượt 8% tổng số hạ gục và phải có rủi ro tiếp cận đo được.

FR75: Tỷ lệ thắng theo điểm rơi không được vượt ±20% quanh trung bình sau khi kiểm soát kỹ năng và quy mô đội; mỗi archetype phải có ít nhất một tình huống hợp lý và một tình huống bất lợi rõ.

FR76: POI loot cao phải cách nhau 800–1.500 m và nối bằng ít nhất hai tuyến mặt đất; mỗi POI lớn phải có ít nhất một đường rút không cần xe, chậm hơn đường chính tối đa 70%.

FR77: Mái có lợi thế chiến đấu phải có ít nhất hai cách tiếp cận hoặc một điểm mù buộc người giữ mái di chuyển; 80% cửa sổ chiến đấu phải dùng chiều cao/silhouette thống nhất và vật liệu xuyên/không xuyên đạn phải có ngôn ngữ hình ảnh nhất quán.

FR78: Biển báo, màu vật liệu và địa danh phải hỗ trợ định hướng mà không phụ thuộc hoàn toàn vào minimap.

FR79: Nhân vật phải là người sống sót bình thường; không được có hero silhouette, hào quang, cánh, thú cưng chiến đấu hoặc trang phục phát sáng. Vũ khí phải dùng tên, hình dáng và âm thanh hư cấu.

FR80: Máu phải có tùy chọn giảm hoặc đổi màu nhưng vẫn giữ hit feedback rõ tương đương.

FR81: HUD chỉ được hiển thị HP/tăng lực, đạn, tư thế, hướng, minimap, trạng thái đội và pha bo; không được có banner cửa hàng, nhiệm vụ, quảng cáo hoặc tiến trình battle pass trong HUD trận.

FR82: Kho đồ desktop phải chiếm tối đa 70% màn hình; kho đồ mobile phải là panel tabbed tối đa 62% chiều ngang và giữ ít nhất 38% dải nhìn thế giới.

FR83: Bản đồ toàn màn hình phải hiển thị đường bay, bo hiện tại/tiếp theo, marker đội và địa danh; không được hiển thị loot hoặc đối thủ.

FR84: Khi người chơi còn sống, không được phát nhạc nền; nhạc chỉ được dùng ở menu, kết quả và khoảnh khắc chiến thắng.

FR85: Bước chân phải phân biệt phổ âm đất, cỏ, gỗ, bê tông, kim loại và nước; tiếng súng phải có âm xa khác âm gần; máy bay và thùng tiếp tế không được che hoàn toàn tiếng súng trong bán kính chiến đấu gần.

FR86: Trò chơi phải hỗ trợ gán lại toàn bộ phím/bố cục Touch, toggle/hold, FOV, độ nhạy, Gyro, haptic, rung camera và cường độ flash.

FR87: Phải có ba preset mù màu cho bo, marker, hit effect và reticle; cấp vật phẩm không được biểu đạt chỉ bằng màu.

FR88: Phải có phụ đề cho thông báo hệ thống và đồng đội ping; hàng chờ cạnh tranh không được có chỉ báo bước chân trực quan.

FR89: Quyền voice chỉ được hỏi theo ngữ cảnh; mất focus, cuộc gọi hoặc thay đổi audio route không được làm kẹt input hoặc phát voice ngoài ý muốn.

FR90: Bản phát hành phải hỗ trợ báo cáo, chặn, log trận và replay phục vụ điều tra; hành vi team-kill lặp lại và gian lận phải có quy trình xem xét riêng.

FR91: Hình phạt rời trận không được áp dụng sau khi đội đã bị loại.

FR92: Màn hình kết quả phải cung cấp thống kê và replay tóm tắt nhưng không trao sức mạnh cho trận tiếp theo.

FR93: Mọi nội dung hậu phát hành phải chỉ rõ trụ cột P1–P4 và chỉ số kiểm chứng, không tạo sức mạnh/thông tin/ngụy trang/tiện ích bằng chi tiêu hoặc tiến trình ngoài trận, không chèn nhịp thương mại vào Standard và phải bị loại hoặc tách khỏi Standard nếu làm giảm tension, fairness hoặc readability.

**Tổng FR: 93**

### Non-Functional Requirements

NFR1: Baseline phải là Godot 4.x và v1.0 phải hỗ trợ Windows 10/11 x64, Linux x64, macOS 13+ Intel x64/Apple Silicon, Android 10+ ARM64 và iOS 16+ ARM64.

NFR2: Input family v1.0 phải là Keyboard/Mouse và Touch; controller và console nằm ngoài phạm vi.

NFR3: Desktop phải ưu tiên 1920×1080, hỗ trợ từ 1280×720 đến 3840×2160 và các tỷ lệ ultrawide phổ biến; mobile phải chạy landscape trên điện thoại và tablet có safe area/notch.

NFR4: Máy desktop tối thiểu mục tiêu phải tương đương CPU 4 nhân đời 2017, RAM 8 GB, GTX 1060/RX 580 và SSD; máy đề nghị tương đương CPU 6 nhân đời 2020, RAM 16 GB và RTX 2060/RX 6600.

NFR5: Mobile tối thiểu phải tương đương Snapdragon 778G/Dimensity 920 với RAM 6 GB hoặc iPhone 11/A13; mobile đề nghị tương đương Snapdragon 8 Gen 1/Dimensity 8100 với RAM 8 GB hoặc iPhone 13/A15.

NFR6: Một core gameplay, dữ liệu vũ khí/loot/bo, authoritative simulation và network protocol phải phục vụ cả năm nền tảng.

NFR7: Khác biệt nền tảng chỉ được nằm sau input adapter, presentation/quality profile, lifecycle, secure storage, platform identity/invite/permission và release pipeline.

NFR8: Mobile lifecycle phải hỗ trợ `Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended`; resume không được bảo đảm giữ slot vô hạn hoặc tạo miễn nhiễm.

NFR9: Desktop phải dùng profile renderer desktop, Android/iOS dùng profile mobile; collision và gameplay visibility không được thay đổi theo quality profile.

NFR10: Máy desktop tối thiểu phải đạt 60 FPS trung vị và p95 frame time ≤25 ms ở 1080p/Low trong replay 30 phút gồm thành phố, xe, khói và bo cuối.

NFR11: Máy desktop đề nghị phải đạt 90 FPS trung vị và p95 frame time ≤16,7 ms ở 1080p/High với cùng replay chuẩn.

NFR12: Bộ nhớ desktop client phải ≤6 GB RAM sau trận 45 phút có đổi ba vùng bản đồ.

NFR13: Thời gian vào trận desktop phải ≤45 giây p95 từ xác nhận ghép trận đến sảnh chờ trên SSD tối thiểu với cache lạnh.

NFR14: Mobile tối thiểu phải đạt 45 FPS trung vị và p95 frame time ≤33,3 ms ở Low qua replay chuẩn và thermal soak.

NFR15: Mobile đề nghị phải đạt 60 FPS trung vị và p95 frame time ≤25 ms ở Medium qua replay chuẩn và thermal soak.

NFR16: Working memory mobile phải ≤3 GB và ứng dụng không được bị OS termination trong trận 45 phút gồm foreground/background.

NFR17: FPS trung vị mobile không được giảm quá 15% sau thermal soak 30 phút trên thiết bị đại diện.

NFR18: Thời gian vào trận mobile phải ≤60 giây p95 từ xác nhận ghép trận đến sảnh chờ với cache lạnh trên thiết bị tối thiểu.

NFR19: Tỷ lệ phiên không crash phải ≥99,5% trong cửa sổ 30 ngày.

NFR20: Máy chủ phải giữ mô phỏng 30 Hz ổn định cho 100 người với 10% headroom trong soak test 45 phút và tình huống bo cuối.

NFR21: Sự kiện bắn và sát thương phải được xử lý trong ≤1 tick ở p95 tại tải 100 người, RTT 80 ms và packet loss 1%.

NFR22: Băng thông trung bình không được vượt 1,5 Mbps mỗi chiều cho mỗi client trong trận 100 người 30 phút.

NFR23: Bù trễ phát bắn phải bị giới hạn tối đa 150 ms; người chơi vượt 150 ms phải nhận cảnh báo và trạng thái quá khứ không được ưu tiên vô hạn trước hiện tại.

NFR24: Mục tiêu ghép vùng phải là ping trung vị ≤80 ms và packet loss <1%; Standard không được khởi tạo nếu không có vùng đạt ngưỡng trừ khi người chơi xác nhận tiếp tục.

NFR25: Sai lệch vị trí nhìn thấy so với vị trí xác nhận phải ≤0,5 m ở p95 trong điều kiện 80 ms RTT và 1% packet loss.

NFR26: Bản cài desktop v1.0 phải ≤25 GB, bản cài mobile ≤12 GB và patch cân bằng không được yêu cầu tải lại quá 2 GB nội dung không đổi.

NFR27: Hệ thống phải duy trì tối đa 6 khói dày đồng thời trong bán kính 100 m quanh người chơi mà vẫn đạt ngưỡng FPS máy tối thiểu.

NFR28: Mobile UI phải tôn trọng safe area; touch target tối thiểu phải là 48 logical units, riêng bắn/thoát xe/đóng tối thiểu 64 khi safe area cho phép.

NFR29: Âm thanh stereo/HRTF phải cho người thử nghiệm xác định đúng cung 30° của nguồn âm ở ≥85% lần thử tại khoảng cách 20–80 m.

NFR30: Bốn bộ trang phục mặc định phải nằm trong biên 5% của nhau trong thử nghiệm phát hiện mục tiêu.

NFR31: Toàn bộ ngưỡng hiệu năng phải đạt trong ba phiên soak liên tiếp trước khi chấp nhận.

NFR32: Tỷ lệ trận được máy chủ kết thúc với kết quả hợp lệ phải ≥99,0%.

NFR33: Dưới 0,5% phát bắn hợp lệ được khiếu nại hitreg có thể bị replay xác nhận sai quá 0,5 m hoặc quá một tick.

NFR34: Ít nhất 95% người chơi phải được ghép vào vùng có ping trung vị ≤80 ms trong khu vực ra mắt.

NFR35: Mỗi input pool phải chứng minh đủ dân số tạo trận 100 người trong ngưỡng chờ được phê duyệt; không được dùng bot hoặc fallback pool ngầm để đạt chỉ số.

NFR36: Mọi mobile profile phải đạt gate FPS, memory, thermal, load và lifecycle trên device matrix trước release candidate.

NFR37: Thời lượng trận phải có trung vị 28–32 phút và p90 không vượt 35 phút.

NFR38: Survival curve phải nằm trong dải mục tiêu của bảng vòng bo trong ít nhất 80% trận beta.

NFR39: Từ 60–75% người chơi phải có vũ khí chính trong 90 giây và dưới 5% không tìm thấy súng sau khi loot trọn một cụm nhà trung bình.

NFR40: Ít nhất 80% người thử nghiệm phải giải thích được quyết định chính dẫn đến cái chết; ít nhất 70% phải chấm nhận định “vị trí và thông tin quan trọng hơn độ hiếm trang bị” ở mức 4/5 trở lên.

NFR41: Không archetype loot thường nào được vượt 22% số hạ gục trong mẫu cân bằng đủ lớn.

NFR42: 100% nội dung ảnh hưởng gameplay phải tiếp cận được chỉ bằng hành động trong trận, không bằng tiền hoặc tiến trình tài khoản.

NFR43: Cổng R1 phải chứng minh môi trường 8 client, build smoke trên năm nền tảng và command/network path desktop + mobile; phải dừng nếu gunplay/hitreg hoặc mobile input/performance tối thiểu không đạt.

NFR44: Cổng R2 phải có staffing đa nền tảng đã re-estimate, 24 mixed clients, Touch HUD và lifecycle; phải dừng nếu loop 24 người, mobile memory/thermal hoặc information parity không đạt.

NFR45: Cổng R3 phải có 100-client protocol mix, benchmark máy chủ ≤8 vCPU/16 GB, device lab và population test từng pool; phải dừng nếu 30 Hz, băng thông, streaming hoặc population viability không đạt.

NFR46: Cổng R4 phải có QA/security/backend, signing/certification, vận hành vùng và beta 100 người thật; phải dừng nếu thiếu release candidate family trên bất kỳ nền tảng nào hoặc chưa đạt technical/gameplay gate.

NFR47: v1.0 chỉ được coi là sẵn sàng khi vòng lặp 100 người hoạt động trọn vẹn, tải kỹ thuật đạt mục tiêu, playtest xác nhận bốn trụ cột và release candidate family đạt trên Windows, Linux, macOS, Android và iOS.

NFR48: Tên vũ khí, hình dáng, âm thanh và mọi tài sản tham chiếu thực tế phải qua kiểm chứng pháp lý.

**Tổng NFR: 48**

### Additional Requirements

#### Ràng buộc phạm vi

- Standard vĩnh viễn loại trừ pay-to-win, vũ khí/chỉ số trả phí, loot box, gacha, battle pass hết hạn, hero/class/ultimate, kỹ năng siêu nhiên, pet chiến đấu, loadout ngoài trận, hồi sinh, tự cứu, mua lại đồng đội, trạm triệu hồi, quảng cáo thương hiệu, sân khấu sự kiện và mỹ phẩm phát sáng.
- v1.0 loại trừ console/controller, bản đồ thứ hai, PvE/zombie/boss/cốt truyện, ranked, esports tools, public custom server, modding/UGC, phá hủy hoặc xây dựng, survival-crafting, replay người dùng đầy đủ, kill-cam cạnh tranh, spectator nâng cao, thời tiết động, ngày/đêm, thiên tai ngẫu nhiên và toàn bộ lớp storefront/live-service.
- FPP-only, ranked, custom server, replay đầy đủ, bản đồ thứ hai, console và controller chỉ là ứng viên hậu v1.0 sau các kiểm chứng dân số, hiệu năng, cân bằng và aim-assist/cross-play tương ứng.
- Các target 25 vũ khí, 6 phương tiện, 18 POI và 420 công trình là provisional, chỉ được khóa sau khi mobile viability và server scale gate cùng đạt.

#### Giả định

- A-001: Đảo Vọng và bối cảnh Đông Nam Á là đề xuất tạo bản sắc; chủ đề có thể đổi mà không thay đổi vòng lặp cốt lõi.
- A-002: Nếu phát hành thương mại, mô hình ưu tiên là mua game một lần; giá và chi phí máy chủ cần business validation riêng.
- A-003: Quy mô nhóm và ngân sách chưa xác định; các mốc là cổng học hỏi, không phải lịch phát hành hoặc cam kết sản xuất.
- A-004 đã bị thay thế: envelope PC-first cũ không còn dùng để phê duyệt production; phạm vi năm nền tảng phải được Architecture và production planning ước lượng lại trước R2.
- A-005: 100 người và 8 × 8 km vẫn là north-star v1.0; content breadth chỉ được khóa sau mobile viability và server scale gate.

#### Phụ thuộc

- Cần hạ tầng máy chủ theo vùng đủ để duy trì ping mục tiêu và thử tải 100 client.
- Cần nguồn người thử nghiệm đủ lớn cho các mốc 24 và 100 người.
- Kiến trúc Godot phải chứng minh streaming bản đồ, mô phỏng 100 người và mô hình mạng trước khi sản xuất toàn bộ nội dung.
- macOS/iOS build-sign-test cần máy macOS, Xcode, provisioning và thiết bị thật; Android cần ARM64 AAB/Gradle/signing cùng device lab đại diện.
- Production planning phải khóa ngân sách trước R2 và R3.

#### Câu hỏi chưa chặn

- Mức giá mua một lần và chính sách máy chủ dài hạn.
- Tên/chủ đề cuối của Đảo Vọng.
- Thứ tự ra mắt khu vực sau beta kín.

### GDD Completeness Assessment

GDD 1.1.0 có độ phủ rất cao: core loop, luật trận, combat, loot, map, multiplayer, input parity, UX, accessibility, hiệu năng và cổng sản xuất đều có thông số hoặc ngưỡng kiểm chứng. Decision log cho thấy phạm vi năm nền tảng và hai input family đã được phê duyệt, đồng thời các target content lớn được giữ ở trạng thái provisional.

Các điểm cần theo dõi trong đánh giá readiness:

- GDD không có mã FR/NFR nguyên bản; 141 mã truy vết trong báo cáo này là mã đánh giá, không phải ID nguồn ổn định.
- Trạng thái GDD là `ready-for-architecture`, không tự động đồng nghĩa với production-ready.
- Quy mô nhóm, ngân sách và staffing đa nền tảng chưa được xác định; đây là điều kiện bắt buộc trước R2/R3.
- Mô hình thương mại, chi phí máy chủ và chính sách vận hành dài hạn chưa được business validation.
- Liên kết `./epics.md` trong GDD trỏ tới bản Epics cũ nằm cùng thư mục; assessment đã chọn bản root-level mới hơn làm nguồn chuẩn.
- Target 100 người/8 × 8 km là north-star bắt buộc, nhưng breadth 25 vũ khí/6 xe/18 POI/420 công trình vẫn có điều kiện và không nên được chuyển thành cam kết production trước khi vượt gate.

## Epic Coverage Validation

Epics dùng hệ mã riêng gồm 110 FR và 55 NFR. Ma trận dưới đây đối chiếu theo ngữ nghĩa từ 93 FR được trích trực tiếp trong bước GDD Analysis; “Epics FR” trong cột coverage là ID của tài liệu Epics, không phải ID đánh giá ở cột đầu.

### Coverage Matrix

| GDD FR | Yêu cầu GDD | Epic/Story coverage | Trạng thái |
|---|---|---|---|
| FR1 | Standard 100 người, 8×8 km, tay trắng, sống cuối | Epic 4, Stories 4.2/4.13; Epics FR1 | ✓ Đã phủ |
| FR2 | Chọn Solo/Duo/Squad, sảnh 60 giây, không loadout | Epic 4, Stories 4.2–4.3; Epics FR2/FR4/FR39 | ✓ Đã phủ |
| FR3 | Chuỗi phase hoàn chỉnh từ đường bay đến Results | Epic 4, Stories 4.1/4.3–4.5/4.13; Epics FR3–FR4 | ✓ Đã phủ |
| FR4 | Điều kiện thắng Solo và đội | Epic 4, Stories 4.2/4.7; Epics FR5–FR6 | ✓ Đã phủ |
| FR5 | Điều kiện elimination Solo/DBNO/toàn đội | Epic 4, Stories 4.2/4.6–4.7; Epics FR5 | ✓ Đã phủ |
| FR6 | Leave sau máy bay là thất bại; spectate đến team elimination | Epic 4, Stories 4.9–4.10; Epics FR7–FR8 | ✓ Đã phủ |
| FR7 | Không hồi sinh/mua lại/tự cứu/trạm triệu hồi | Epic 4, Stories 4.2/4.7; Epics FR9 | ✓ Đã phủ |
| FR8 | Toàn bộ movement/stance và thông số | Epic 1, Stories 1.4–1.6/1.12–1.13; Epics FR14–FR18 | ✓ Đã phủ |
| FR9 | Không stamina; fall damage | Epic 1, Stories 1.4/1.6; Epics FR19/FR21 | ✓ Đã phủ |
| FR10 | Nước sâu, bơi/lặn, weapon lock, breath | Epic 1, Story 1.7; Epics FR20 | ✓ Đã phủ |
| FR11 | 100 HP và hit-region multipliers | Epic 2, Story 2.6; Epics FR25–FR26 | ✓ Đã phủ |
| FR12 | Armor/helmet reduction, durability và break ordering | Epic 2, Story 2.6; Epics FR27–FR29 | ✓ Đã phủ |
| FR13 | Năm healing/boost item với timing/effect/limit | Epic 3, Story 3.6; Epics FR30 | ✓ Đã phủ |
| FR14 | Interruption và boost cap | Epic 3, Stories 3.3/3.6; Epics FR30/FR37 | ✓ Đã phủ |
| FR15 | DBNO bleed progression | Epic 4, Story 4.6; Epics FR31 | ✓ Đã phủ |
| FR16 | Revive timing/interruption và DBNO restrictions | Epic 4, Stories 4.6–4.7; Epics FR32–FR33 | ✓ Đã phủ |
| FR17 | Body/backpack capacity 50/120/180/250 | Epic 3, Story 3.2; Epics FR35 | ✓ Đã phủ |
| FR18 | Equipment slots và capacity-cost rules | Epic 3, Stories 3.1–3.2; Epics FR34/FR36 | ✓ Đã phủ |
| FR19 | Quick pickup, drag/drop và ammo auto-pick | Epic 3, Stories 3.3–3.5; Epics FR40/FR42–FR43 | ✓ Đã phủ |
| FR20 | Weighted loot spawn theo geography | Epic 3, Story 3.7; Epics FR38 | ✓ Đã phủ |
| FR21 | Loot targets sau 90 giây | Epic 3, Story 3.8; Epics FR44 | ✓ Đã phủ |
| FR22 | Geography tier của loot | Epic 3, Story 3.7; Epics FR45 | ✓ Đã phủ |
| FR23 | Airdrop phase, visibility, contents, no essential exclusivity | Epic 3, Story 3.9; Epics FR46–FR47 | ✓ Đã phủ |
| FR24 | Bốn throwable archetype và thông số | Epic 3, Story 3.11; Epics FR49 | ✓ Đã phủ |
| FR25 | Throwable capacity và preview 1,5 giây | Epic 3, Stories 3.10–3.11; Epics FR48/FR50 | ✓ Đã phủ |
| FR26 | Sáu vehicle archetype và số chỗ | Epic 5, Stories 5.8/5.10; Epics FR51 | ✓ Đã phủ |
| FR27 | Vehicle speed/fuel/tires/HP/audio/explosion countdown | Epic 5, Stories 5.9/5.12; Epics FR52–FR53 | ✓ Đã phủ |
| FR28 | Vehicle collision damage và no paid armored vehicle | Epic 5, Story 5.11; Epics FR54–FR55; product-integrity gate | ✓ Đã phủ |
| FR29 | Semantic input shared across device adapters | Epic 1, Story 1.3; Epics FR22 | ✓ Đã phủ |
| FR30 | Keyboard/Mouse bindings | Epic 1, Story 1.10; Epics FR23 | ✓ Đã phủ |
| FR31 | Touch layout và persistence | Epic 1 Story 1.11; Epic 8 Story 8.11; Epics FR24/FR58 | ✓ Đã phủ |
| FR32 | Gyro optional; no Touch assistance/extra cues | Epic 1 Stories 1.11/1.13; Epic 2 Story 2.7; Epics NFR33 | ✓ Đã phủ |
| FR33 | TPP/shoulder swap/first-person ADS | Epic 1, Story 1.8; Epics FR56 | ✓ Đã phủ |
| FR34 | Camera collision và head-line-of-sight anti-peek | Epic 1, Story 1.8; Epics FR57 | ✓ Đã phủ |
| FR35 | Full remap/layout/sensitivity/hold-toggle | Epic 1 Stories 1.10–1.11; Epic 8 Stories 8.9/8.11; Epics FR58 | ✓ Đã phủ |
| FR36 | Provisional 25-weapon roster | Epic 2, Story 2.3; Epics FR59 | ✓ Đã phủ |
| FR37 | Five calibers và attachment roster | Epic 2, Story 2.3; Epics FR60–FR61 | ✓ Đã phủ |
| FR38 | No weapon leveling/carry-over/skin v1 | Epic 2 Story 2.3; Epic 9 Stories 9.3/9.7; Epics FR93/FR96 | ✓ Đã phủ |
| FR39 | Full archetype combat baseline và falloff | Epic 2, Stories 2.3/2.7/2.15; Epics FR62 | ✓ Đã phủ |
| FR40 | AR TTK ranges | Epic 2, Stories 2.3/2.15; Epics NFR23 | ✓ Đã phủ |
| FR41 | Projectile flight/drop, no primary hitscan | Epic 2, Story 2.5; Epics FR63 | ✓ Đã phủ |
| FR42 | Recoil progression/recovery và movement spread | Epic 2, Story 2.7; Epics FR64 | ✓ Đã phủ |
| FR43 | Shot feedback; no floating damage | Epic 2, Story 2.10; Epics FR68–FR69 | ✓ Đã phủ |
| FR44 | Hit feedback và server-confirmed elimination | Epic 2, Stories 2.10/2.12; Epics FR69–FR70 | ✓ Đã phủ |
| FR45 | Damage-direction cue 30°, no shooter range/location | Epic 8, Story 8.6; UX-DR17 | ✓ Đã phủ |
| FR46 | TPP hip-fire/shoulder/ADS states | Epic 1 Story 1.8; Epic 2 weapon actions; Epics FR56 | ✓ Đã phủ |
| FR47 | Breath-hold, exhausted sway và zeroing | Epic 2, Story 2.8; Epics FR65 | ✓ Đã phủ |
| FR48 | Aim punch; no mouse aim assist/magnetism | Epic 2 Stories 2.7–2.8; Epic 1 parity gate; Epics FR66/NFR33 | ✓ Đã phủ |
| FR49 | Melee range/wind-up/damage | Epic 2, Story 2.9; Epics FR67 | ✓ Đã phủ |
| FR50 | Server authority over gameplay outcomes | Epics 2/6/10, Stories 2.1–2.15/6.15/10.8; Epics FR71 | ✓ Đã phủ |
| FR51 | Hit-trade ordering and replay evidence | Epic 2, Story 2.12; Epics FR70 | ✓ Đã phủ |
| FR52 | Human opponents, bot disclosure, Training targets | Epic 6 Story 6.7; Epic 8 Story 8.15; Epics FR78–FR79/FR94 | ✓ Đã phủ |
| FR53 | 8×8 map và production content targets | Epic 7, Stories 7.1/7.3/7.5–7.6; Epics FR83 | ✓ Đã phủ |
| FR54 | Open spans, bypasses và final-circle rules | Epic 5 Stories 5.4–5.6; Epic 7 Story 7.7; Epics FR84–FR86 | ✓ Đã phủ |
| FR55 | Exact combat-distance envelopes by environment | Không có Epics FR hoặc Story AC mang các dải 0–25/40–150/150–400/400–800 m | ❌ Thiếu |
| FR56 | Open-space alternatives và choke bypass | Epic 5 Story 5.6; Epic 7 Story 7.7; Epics FR84–FR85 | ✓ Đã phủ |
| FR57 | Final-circle land rule và static/non-destructible cover | Final-circle có ở Epic 5/7; không có Story/AC khóa “cover tĩnh, không phá nhà/đào đất/xây công sự” | ❌ Thiếu |
| FR58 | Weather weights và no mid-match transition | Epic 5 Story 5.7; Epic 7 Story 7.9; Epics FR88 | ✓ Đã phủ |
| FR59 | Rain/fog modifier, no full night, clothing detectability parity | Rain/fog có ở Epic 5/7; không thấy no-full-night hoặc biên phát hiện trang phục 5% | △ Một phần |
| FR60 | 100-player Solo/Duo/Squad counts | Epic 4, Story 4.2; Epics FR1–FR2 | ✓ Đã phủ |
| FR61 | Region/wait priority và newcomer soft MMR | Epic 6, Story 6.5; Epics FR75 | ✓ Đã phủ |
| FR62 | K/M, Touch và Mixed pool disclosure | Epic 6, Story 6.6; Epics FR76 | ✓ Đã phủ |
| FR63 | Input-family match lock/requeue/no silent relaxation | Epic 6, Stories 6.6–6.7; Epics FR77–FR79 | ✓ Đã phủ |
| FR64 | Shared account/backend/balance/protocol; no extra mobile info | Epic 1 foundation; Epic 6 Stories 6.1–6.9; Epics FR13/NFR31–NFR34 | ✓ Đã phủ |
| FR65 | Standard primary; ranked/custom/tournament/FPP-only deferred | Không có Requirement Inventory, Story AC hoặc Source Requirement ghi boundary này | ❌ Thiếu |
| FR66 | Team voice, position + eight contextual pings | Epic 6, Stories 6.10–6.11; Epics FR81 | ✓ Đã phủ |
| FR67 | 100% friendly fire and report flow | Epic 6, Story 6.12; Epics FR82 | ✓ Đã phủ |
| FR68 | Nine zone phases and timing/survival curve | Epic 4, Story 4.8; Epics FR90 | ✓ Đã phủ |
| FR69 | Next-zone reveal and no forecast/bombing zone | Epic 4, Story 4.8; Epics FR91 | ✓ Đã phủ |
| FR70 | Explicit 0–3/3–10/10–22/22+ minute progression curve | Không có requirement/story truy vết trực tiếp bốn mốc này | ❌ Thiếu |
| FR71 | No power progression | Epic 9, Stories 9.2–9.3/9.7; Epics FR92–FR93/FR96 | ✓ Đã phủ |
| FR72 | Profile statistics, mastery limits, non-expiring rewards | Epic 9, Stories 9.2–9.3; Epics FR92–FR93 | ✓ Đã phủ |
| FR73 | No commerce/live-service v1 and one gameplay entitlement | Epic 9, Story 9.7; Epics FR96/NFR54 | ✓ Đã phủ |
| FR74 | Weapon/supply-drop kill-share limits | Epic 2 balance/gate; Epics NFR24 | ✓ Đã phủ |
| FR75 | Drop-point win-rate and archetype strength/weakness | Drop win-rate có ở NFR25; không có AC riêng cho mỗi archetype có một tình huống mạnh và một tình huống bất lợi | △ Một phần |
| FR76 | POI spacing 800–1.500 m and non-vehicle escape ≤70% slower | Epic 5/7 có road graph nhưng không có các ngưỡng này trong Requirement Inventory/AC | ❌ Thiếu |
| FR77 | Roof access/blind spot; 80% window standard; penetration language | Không có Requirement Inventory hoặc Story AC tương ứng | ❌ Thiếu |
| FR78 | Environmental navigation without minimap dependence | Map/place-name UI có ở Epic 8; không có Story/AC cho signage/material/landmark navigation trong world | ❌ Thiếu |
| FR79 | Restrained-realism art, ordinary survivor silhouette, fictional weapon identity | Asset stories có provenance/parity nhưng không truy vết art-direction constraints này | ❌ Thiếu |
| FR80 | Blood reduction/color option with equivalent clarity | Epic 8, Story 8.10; UX-DR51 | ✓ Đã phủ |
| FR81 | Minimal non-commercial HUD groups | Epic 8, Story 8.5; Epics FR97 | ✓ Đã phủ |
| FR82 | Desktop/mobile inventory world-risk dimensions | Epic 8, Story 8.7; Epics FR99/UX-DR22–23; desktop target được siết từ ≤70% xuống ≤68% | ✓ Đã phủ |
| FR83 | Full-map information and exclusions | Epic 8, Story 8.8; Epics FR98 | ✓ Đã phủ |
| FR84 | No music while alive | Epic 8, Story 8.12; Epics FR105 | ✓ Đã phủ |
| FR85 | Footstep/gunshot audible distances, surface spectra, masking rule | Audio Epic 8 phủ output/mix/HRTF nhưng không có 20/45/70 m, 400–600/1.000 m hoặc masking AC | ❌ Thiếu |
| FR86 | Remap/toggle/FOV/sensitivity/Gyro/haptic/shake/flash settings | Epic 8, Stories 8.9–8.11; Epics FR100 | ✓ Đã phủ |
| FR87 | Three color-blind presets and redundant encoding | Epic 8, Story 8.10; Epics FR101 | ✓ Đã phủ |
| FR88 | System/team-ping subtitles and no visual footstep cue | Epic 8, Story 8.14; Epics FR102 | ✓ Đã phủ |
| FR89 | Contextual voice permission and route/focus safety | Epic 8 Story 8.13; Epic 6 Stories 6.10/6.14; Epics FR103/FR109 | ✓ Đã phủ |
| FR90 | Report/block/match log/evidence replay and misconduct review | Epic 9, Stories 9.5–9.8; Epic 6 evidence; Epics FR107–FR108 | ✓ Đã phủ |
| FR91 | No leave penalty after team elimination | Epic 4 Story 4.10; Epic 8 Story 8.17; Epics FR7 | ✓ Đã phủ |
| FR92 | Results statistics and replay summary without next-match power | Epic 9, Stories 9.1/9.4; Epics FR10/FR106/NFR54 | ✓ Đã phủ |
| FR93 | Post-release P1–P4 evidence and anti-drift approval gate | Epic 9 Story 9.7 phủ no-commerce/no-FOMO nhưng không yêu cầu pillar/metric declaration hoặc reject/tách khỏi Standard theo playtest | ❌ Thiếu |

### Missing Requirements

#### Critical Missing FRs

**FR55: Cự ly giao tranh theo loại không gian**

GDD yêu cầu 0–25 m trong nhà, 40–150 m tại làng/rừng, 150–400 m ở ruộng/sườn đồi/đường và 400–800 m chỉ tại sightline có đánh đổi rõ.

- Tác động: Map validators không có envelope để phát hiện sightline hoặc density sai với weapon roster.
- Khuyến nghị: Bổ sung vào Epic 5 Story 5.6 và Epic 7 Story 7.7 với histogram sightline/collision test theo từng loại không gian.

**FR57: Cover tĩnh và phạm vi không phá hủy**

GDD yêu cầu cover v1.0 là tĩnh; không phá nhà, đào đất hoặc xây công sự.

- Tác động: Thiếu boundary này có thể dẫn đến model dữ liệu, replication và asset pipeline hỗ trợ destructibility ngoài phạm vi.
- Khuyến nghị: Bổ sung AC vào Epic 5 Story 5.5/5.6 và Epic 7 Story 7.4, kèm validator chặn component/destruction state ngoài Standard.

**FR59: No-full-night và fairness của trang phục**

GDD yêu cầu không có đêm tối hoàn toàn và bốn bộ trang phục mặc định nằm trong biên 5% của nhau trong thử nghiệm phát hiện mục tiêu.

- Tác động: Trực tiếp ảnh hưởng information parity và competitive fairness.
- Khuyến nghị: Mở rộng Epic 5 Story 5.7 và Epic 7 Story 7.9; thêm detection study làm gate cho Epic 8/10.

**FR76: POI spacing và đường rút không cần xe**

GDD yêu cầu POI loot cao cách nhau 800–1.500 m, nối bằng ít nhất hai tuyến mặt đất; mỗi POI lớn có đường rút không cần xe chậm hơn đường chính tối đa 70%.

- Tác động: Thiếu tiêu chí route khiến road-graph validator có thể pass nhưng nhịp di chuyển và khả năng thoát POI sai thiết kế.
- Khuyến nghị: Bổ sung AC định lượng vào Epic 5 Story 5.4 và Epic 7 Story 7.3/7.7.

**FR77: Roof/window/material combat language**

GDD yêu cầu mái lợi thế có hai cách tiếp cận hoặc điểm mù, 80% cửa sổ chiến đấu dùng kích thước/silhouette thống nhất và vật liệu xuyên/không xuyên đạn có ngôn ngữ hình ảnh nhất quán.

- Tác động: Ảnh hưởng trực tiếp counter-play, hit expectation và art/gameplay parity.
- Khuyến nghị: Bổ sung vào Epic 5 Story 5.5 và Epic 7 Story 7.4–7.5 với building-kit validator.

**FR85: Khoảng nghe và phổ âm cạnh tranh**

GDD yêu cầu bước chân chạy/đi thường/đi bộ nghe tới 70/45/20 m; súng không giảm thanh tới 1.000 m, súng giảm thanh 400–600 m; vật liệu có phổ âm riêng và máy bay/thùng tiếp tế không che hoàn toàn tiếng súng gần.

- Tác động: Audio là nguồn thông tin gameplay cốt lõi; HRTF localization pass không chứng minh được range/masking.
- Khuyến nghị: Thêm Story hoặc AC vào Epic 8 Story 8.12, đồng thời kiểm chứng trên map ở Epic 7 Story 7.8.

#### High Priority Missing or Partial FRs

**FR65:** Ghi rõ Standard là luật chính và ranked/custom/tournament/FPP-only bị deferred; bổ sung product-scope acceptance gate vào Epic 9 Story 9.7.

**FR70:** Bổ sung telemetry/gate cho progression curve 0–3, 3–10, 10–22 và 22+ phút vào Epic 4 Story 4.13 hoặc Epic 7/10 playtest gate.

**FR75:** Mở rộng weapon-manifest/balance AC để mỗi archetype có ít nhất một tình huống mạnh và một tình huống bất lợi rõ.

**FR78:** Bổ sung environmental-navigation acceptance cho biển báo, vật liệu và địa danh, không phụ thuộc hoàn toàn vào minimap.

**FR79:** Bổ sung art-direction/content contract cho restrained realism, ordinary-survivor silhouette và fictional weapon identity.

**FR93:** Mở rộng integrity gate để mọi nội dung hậu phát hành phải khai báo P1–P4, metric kiểm chứng và bị loại hoặc tách khỏi Standard nếu playtest làm giảm tension/fairness/readability.

### Epic-only or Expanded Requirements

Epics có các yêu cầu không tồn tại như FR độc lập trong GDD nhưng được bổ sung hợp lý từ UX/Architecture: server-confirmed hold progress, atomic inventory rejection, post-exit vehicle countdown state, prediction/reconciliation, party Ready invalidation, deterministic map seed, Field Orientation onboarding, non-pausing surfaces, localization/audio-output contracts, Pending/Unavailable Results, chi tiết Report/Block, reconnect token/state và provider-degraded behavior. Các bổ sung này không mâu thuẫn GDD.

### Coverage Statistics

- Tổng GDD FR được đánh giá: **93**
- Đã phủ đầy đủ: **81**
- Phủ một phần: **2**
- Chưa có đường triển khai đủ rõ: **10**
- Tỷ lệ phủ nghiêm ngặt: **87,1%**
- Tổng FR nội bộ được tài liệu Epics khai báo: **110**, và FR Coverage Map nội bộ gán cả 110 vào Epic; con số này không thay thế đối chiếu ngữ nghĩa với GDD.

## UX Alignment Assessment

### UX Document Status

**Đã tìm thấy và ở trạng thái `final`.**

Nguồn UX chính:

- `DESIGN.md` — visual system, 30 component contracts, token, responsive layout, motion/flash và mobile primitives.
- `EXPERIENCE.md` — IA, state, input routing, HUD, Inventory/Map/Party, audio/accessibility và bốn player journey.
- `final-ux-verification.md` báo cáo **20 Closed · 5 Accepted dependency · 0 Open**.
- Bộ UX không có `index.md`; `DESIGN.md` và `EXPERIENCE.md` phải tiếp tục được coi là hai peer contract chuẩn.

### UX ↔ GDD Alignment

Các phần liên kết tốt:

- Cùng luật Standard 100 người, TPP + first-person ADS, tay trắng, Solo/Duo/Squad, DBNO, không hồi sinh và Results do máy chủ xác nhận.
- HUD giữ đúng bảy nhóm dữ liệu GDD qua sáu module, không thêm damage number, enemy outline, loot radar hoặc visual footstep cue.
- Inventory desktop siết yêu cầu GDD từ tối đa 70% xuống tối đa 68%, giữ world strip tối thiểu 32%; mobile giữ đúng giới hạn 62%/38%.
- Map chỉ lộ next zone sau server-confirmed wait phase, không loot/enemy/prediction; damage cue giữ screen-relative và không tự đóng Map.
- Touch, Gyro, safe area, input-pool disclosure và mobile interruption giữ gameplay/information parity.
- Accessibility giữ remap, hold/toggle, color-blind presets, subtitle, blood/hit-color, motion/flash control mà không tạo tactical assistance.
- Không store/news/reward rail/FOMO/live-event; không nhạc khi người chơi còn sống.

Các mở rộng UX không có FR độc lập trong GDD nhưng không mâu thuẫn:

- Field Orientation tùy chọn, không thưởng, tách khỏi Training Grounds.
- Central 16:9 live-world viewport trên ultrawide.
- Chi tiết party Ready/leader, ping TTL/cooldown, Report receipt/retry, Pending/Unavailable Results và input focus lifecycle.
- Việt/Anh localization cùng Noto font pipeline.

### UX ↔ Architecture Alignment

Architecture hỗ trợ trực tiếp phần lớn contract UX:

- ADR-14 khóa Godot `Control`/`Container`/`Theme`, presenter và immutable `ViewState`; widget không đọc packet/entity/backend trực tiếp.
- Desktop/mobile dùng chung presenter/state nhưng khác layout composition.
- Semantic input adapters, signed input-family claim, platform adapters và guarded lifecycle state machine phù hợp input/lifecycle UX.
- `game/src/client/ui/{presenters,view_states,navigation,components}`, UI scenes, settings, lifecycle, audio và voice đều có ownership rõ.
- Central 16:9, anti-peek visibility, mobile renderer parity, safe area, Touch/Gyro, performance budgets và device-lab gate đều được kiến trúc mang theo.
- Audio/voice có Godot audio baseline, HRTF metric, `VoiceProvider`, permission/route/background behavior và provider spike.
- Local settings, secure token, backend report/block, evidence replay và privacy boundary hỗ trợ state/error paths UX.

### Alignment Issues

#### UX-A1 — Reconnect/AFK outcome chưa được khóa

Architecture thừa nhận avatar protection, timeout và authoritative outcome khi disconnect chưa được GDD khóa, nhưng phần validation lại tuyên bố không còn quyết định kiến trúc mở.

- Tác động: UX-029/UX-043 chỉ được hiển thị state từ owner; Story reconnect không thể triển khai an toàn nếu chưa có grace/AFK/avatar policy.
- Yêu cầu: hoàn tất ADR/policy ở Epic 6 Story 6.13 trước Story 6.14; khóa owner API, grace theo phase, neutral input, vulnerability/outcome và token rotation.

#### UX-A2 — Quyền voice/ping sau elimination chưa được khóa

UX mặc định spectator không tạo marker chiến thuật mới và chỉ nhận information parity, nhưng quyền voice/ping hậu elimination vẫn được giao cho Gameplay quyết định. Architecture chỉ nói voice team-only và spectator parity.

- Tác động: implementation có thể vô tình cấp kênh thông tin ngoài contract cho người đã chết.
- Yêu cầu: bổ sung quyết định rõ vào spectator/voice contract trước Epic 8 Story 8.18 và Epic 6 voice gate.

#### UX-A3 — Audio bus nội bộ và control-facing không cùng contract

Architecture liệt kê các bus tối thiểu `Master, UI, Ambience, Footsteps, Weapons, Vehicles, Voice`; UX chỉ cho player chỉnh `Master, World, Team Voice, UI, Music`, trong đó World giữ tỷ lệ cố định và cấm footstep boost/EQ/night mode.

- Tác động: nếu expose trực tiếp bus Architecture, người chơi có thể tạo lợi thế tactical trái UX.
- Yêu cầu: Architecture phải nói rõ Ambience/Footsteps/Weapons/Vehicles là internal child buses của player-facing World; thêm Music ownership và cấm expose tactical sub-bus/EQ.

#### UX-A4 — Localization chưa có boundary kiến trúc rõ

Architecture chỉ có thư mục font chung; không định nghĩa locale/catalog/schema/fallback ownership. Epic 8 Story 8.3 có Module/File Ownership và AC đầy đủ, nên đã có đường triển khai nhưng Architecture chưa phản ánh boundary này.

- Tác động: các Story UI sớm có thể hard-code chuỗi trước khi localization pipeline tồn tại.
- Yêu cầu: thêm localization port/catalog ownership và dependency rule; Story 8.3 phải precede production UI strings hoặc cung cấp scaffold sớm hơn.

#### UX-A5 — Các quyết định input/map còn gate trước implementation

- Raw-mouse choice, physical-vs-logical key policy, localized OS key labels và non-QWERTY/Linux display names chưa khóa.
- Map orientation mặc định và zoom limits chưa khóa.

Epics đã ghi rõ các gate này, nhưng Architecture chưa sở hữu policy. Story 1.10 và Story 8.8 không được bắt đầu implementation chi tiết trước khi các quyết định được ghi nhận.

#### UX-A6 — Architecture tham chiếu bản Epics cũ

Frontmatter Architecture vẫn trỏ tới `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/epics.md`, trong khi assessment đã chọn `_bmad-output/planning-artifacts/epics.md` mới hơn.

- Tác động: traceability và validation summary “9/9 Epic” đã lỗi thời so với tài liệu hiện tại gồm 10 Epic.
- Yêu cầu: cập nhật source reference và chạy lại Architecture validation/mapping theo bản Epics mới.

### Warnings

- Trạng thái UX `final` nghĩa là contract tài liệu đã đóng, không có nghĩa năm dependency UX-027–UX-031 đã được triển khai hoặc kiểm chứng.
- Static HTML/mockup và PNG validation không thay Godot snapshot, device-hand playtest, notch/system-gesture test, Gyro fatigue, haptic, thermal hoặc real-device accessibility testing.
- Screen-reader/menu narration, extended subtitle controls, motor/hearing playtest và professional photosensitivity scope vẫn cần quyết định v1/deferred cùng owner trước release-readiness.
- Invite provider, deep report taxonomy/evidence attachment/moderation SLA và deep replay payload không chặn Combat Sandbox nhưng phải có API/schema/security/retention contract trước Story sở hữu.

### UX Alignment Verdict

**Phù hợp có điều kiện.** UX, GDD và Architecture nhất quán về trải nghiệm cốt lõi và fairness. Có đường triển khai cho hầu hết UX contract, nhưng các Story liên quan reconnect, spectator voice/ping, localization, audio controls, input naming và Map policy phải giữ trạng thái chưa Ready cho đến khi các decision gate tương ứng được khóa. Architecture cần được revalidate theo bản Epics mới.

## Epic Quality Review

### Review Scope and Structural Results

Đã kiểm tra toàn bộ **10 Epic và 135 Story** theo tiêu chuẩn `create-epics-and-stories`, gồm player value, tính độc lập, kích thước, dependency, thời điểm tạo data/entity, acceptance criteria và traceability.

Kết quả kiểm tra máy:

- 135/135 Story có `As a / I want / So that`.
- 135/135 Story có Source Requirements, Depends on, Blocks, Acceptance Criteria, Error/Recovery Path, Test Boundary và Definition of Done.
- 135/135 Story có ít nhất một bộ Given/When/Then.
- Không tìm thấy dependency đi tới Story hoặc Epic tương lai.
- Không tìm thấy vòng dependency; graph hiện tại là DAG theo thứ tự Epic.
- Story 1.1 tồn tại và đáp ứng yêu cầu khởi tạo clean Godot Standard project của Architecture.

Chất lượng acceptance criteria nhìn chung cao: có authority, error/recovery, parity, evidence và test boundary cụ thể. Vấn đề chính không phải thiếu format mà là cách đóng gói giá trị, kích thước và thời điểm thực hiện một số enabler.

### Epic Compliance Matrix

| Epic | Player/User Value | Independence | Story Sizing / Timing | Kết luận |
|---|---|---|---|---|
| 1 — Người sống sót đầu tiên | Có outcome chơi được rõ | Đứng độc lập | Story 1.1 và 1.2 quá rộng | Đạt có điều kiện |
| 2 — Đấu súng tin cậy | Rõ, kiểm thử được | Chỉ dùng Epic 1 | Cấu trúc và AC tốt | Đạt |
| 3 — Loot/tài nguyên | Rõ | Chỉ dùng Epic 1–2 | Story 3.1 và 3.11 gom quá nhiều | Đạt có điều kiện |
| 4 — Trận BR hoàn chỉnh | Rõ | Chỉ dùng Epic trước | Gate rộng nhưng outcome nhất quán | Đạt |
| 5 — World/Vehicle Slice 2×2 km | Có playable outcome, nhưng tên/phạm vi mang dạng technical milestone | Chỉ dùng Epic trước | Story 5.1 tạo schema/pipeline quá rộng; world và vehicle bị gom | Không đạt cấu trúc hiện tại |
| 6 — Online cạnh tranh | Rõ | Chỉ dùng Epic trước | Dependency cấp Epic quá thô, giảm parallelism | Đạt có điều kiện |
| 7 — Đảo Vọng production scale | Rõ | Chỉ dùng Epic trước | Hợp lý như content scale sau gate | Đạt |
| 8 — UX/accessibility đa thiết bị | Rõ | Không có forward dependency | Bị đặt sau toàn bộ Epic 1–7; 19 Story tạo big-bang integration | Không đạt sequencing hiện tại |
| 9 — Profile/product integrity | Rõ | Chỉ dùng Epic trước | Hợp lý, traceability tốt | Đạt |
| 10 — Release năm nền tảng | Outcome cuối có giá trị, nhưng phần lớn nội dung là release/infrastructure program | Chỉ dùng Epic trước | CI, dependency lock, SBOM và observability bị làm quá muộn | Không đạt cấu trúc hiện tại |

### 🔴 Critical Violations

#### EQ-C1 — Epic 10 là technical release program được trình bày như product Epic

Epic 10 gom dependency lock/SBOM, reproducible CI/signing, platform packaging, server container, observability và rollout/rollback. Story 10.1 còn phụ thuộc **Epic 1–9**, rồi Story 10.2 mới tạo artifact family/CI contract.

Đây là vi phạm tiêu chuẩn Epic phải cung cấp một increment player/user value. Việc thêm câu “As a người chơi” không biến dependency management, container hardening hoặc telemetry thành player story. Nó cũng đặt các control kỹ thuật nền tảng sau khi gần như toàn bộ sản phẩm đã được xây xong.

**Tác động:**

- Reproducibility, signing boundary, SBOM và upgrade policy được phát hiện quá muộn.
- Platform incompatibility có thể tạo rework xuyên chín Epic.
- Observability/rollback không đồng hành với backend/server increments trước đó.
- Epic release trở thành kho gom NFR thay vì mỗi owner chứng minh NFR khi capability được tạo.

**Yêu cầu sửa:**

1. Chuyển dependency lock, upgrade ADR, CI artifact family và signing boundary vào Story 1.1 hoặc các enabler nhỏ ngay sau Story 1.1.
2. Đưa server container/observability vào Epic 6 tại thời điểm dedicated server và matchmaking được đưa lên môi trường.
3. Gắn performance, reliability, security và platform qualification AC vào Story/Epic sở hữu capability.
4. Giữ một release-readiness checklist/gate riêng; nếu vẫn giữ Epic 10, chỉ giữ các outcome có thể diễn đạt theo người dùng từng platform và không dùng nó để trì hoãn engineering controls nền tảng.

### 🟠 Major Issues

#### EQ-M1 — Epic 5 dùng technical milestone và gom hai value stream

Tên “World/Vehicle Slice 2×2 km” mô tả lát cắt sản xuất hơn là một capability của người chơi. Goal có player value thực — đi bộ, bơi và lái qua một khu vực ổn định — nhưng phạm vi đồng thời chứa world schema, terrain bake, streaming, POI/road/building/coast/weather, vehicle, fuel, exit safety và water behavior.

**Yêu cầu sửa:** Đổi Epic thành outcome chơi được, ví dụ “Khám phá và thoát hiểm trong vùng thử nghiệm”, rồi cân nhắc tách world traversal/streaming khỏi vehicle mobility. Mỗi Epic sau tách phải có vertical slice người chơi tự kiểm chứng được.

#### EQ-M2 — Story 1.1 quá lớn và nằm trên critical path của toàn bộ backlog

Story 1.1 đồng thời tạo clean Godot project, monorepo boundaries, bootstrap, build smoke cho năm client + server, toolchain fail-closed, quarantine asset và CI. Đây là nhiều outcome có thể hoàn thành/kiểm chứng độc lập.

**Yêu cầu sửa:** Tách tối thiểu thành:

- clean Godot project + local bootstrap;
- repository/module boundary;
- một build smoke chuẩn;
- mở rộng build smoke theo platform;
- CI/toolchain/quarantine validation.

Story đầu tiên vẫn phải tạo project có thể chạy, đúng yêu cầu greenfield của Architecture.

#### EQ-M3 — Story 1.2 là một feature set thay vì một Story

Story 1.2 gom provenance và license asset, humanoid rig/import, nhiều clip chuyển động, authoring clip thiếu, AnimationTree, upper-body layer, root-motion validation, client/server parity và headless packaging.

**Yêu cầu sửa:** Tách asset intake/rig, locomotion state graph, upper-body aim layer và parity/package validation. Chỉ tạo animation/data contract cần cho capability hiện tại; không reserve toàn bộ layer cho Epic tương lai trong cùng Story.

#### EQ-M4 — Story 3.1 tạo inventory/item domain quá rộng ở đầu Epic

Story 3.1 sở hữu item definitions và immutable inventory manifest, đồng thời mở đường cho phần lớn FR30 và FR34–FR43/FR48–FR49. Nó trở thành data-model gateway cho cả Epic thay vì giới thiệu entity theo use case đầu tiên.

**Yêu cầu sửa:** Giữ một stable-ID/catalog kernel tối thiểu, sau đó đưa weapon/ammo, armor/healing, capacity và throwable definition vào Story đầu tiên thực sự tiêu thụ từng loại.

#### EQ-M5 — Story 3.11 trộn feature implementation với Epic gate

“Four authoritative throwable archetypes và Epic 3 gate” vừa triển khai bốn archetype, vừa kiểm tra toàn bộ Epic. Đây là hai outcome khác nhau, có failure mode và sizing khác nhau.

**Yêu cầu sửa:** Tách throwable capability thành một hoặc nhiều Story; giữ gate thành verification task/checklist hoặc Story riêng chỉ khi nó tạo evidence có owner rõ.

#### EQ-M6 — Story 5.1 là “setup all models/pipeline” cho world domain

Story 5.1 tạo `MapDefinition`, `TerrainTileData` và deterministic bake pipeline trước mọi terrain/streaming/route capability. Cách đóng gói này có nguy cơ thiết kế schema theo giả định của toàn Epic thay vì phát triển vừa đủ theo consumer.

**Yêu cầu sửa:** Tạo schema và bake contract nhỏ nhất cho terrain slice đầu tiên; bổ sung field/validator khi Story streaming, road, building, coast hoặc weather cần chúng.

#### EQ-M7 — UX được tích hợp quá muộn và bị over-serialized

Story 8.1 phụ thuộc **Epic 1–7**, sau đó gần như toàn bộ Story UX phụ thuộc 8.1. Theme, localization scaffold, presenter/view-state base, input labeling và accessibility primitives vì vậy chỉ xuất hiện sau khi gameplay/world/online đã hoàn thành.

Không có forward dependency, nhưng sequence này tạo big-bang UX integration và làm tăng rủi ro hard-coded UI/string/input contract.

**Yêu cầu sửa:**

- Khởi tạo Theme/component/localization/presenter foundation ngay sau scaffold Epic 1.
- Giao HUD với combat, Inventory với loot, Map với match/world, Party/voice với online.
- Giữ Epic 8 cho cross-device hardening, accessibility consolidation, onboarding và final UX evidence.
- Thay dependency `Epic 1–7` bằng dependency Story/contract cụ thể.

#### EQ-M8 — Dependency cấp Epic quá thô làm mất khả năng triển khai song song

Các ví dụ gồm Story 5.1 phụ thuộc Epic 1–4, Story 6.1 phụ thuộc Epic 1–5, Story 8.1 phụ thuộc Epic 1–7 và Story 10.1 phụ thuộc Epic 1–9. Không phải mọi output của các Epic trước đều cần cho các Story này.

**Yêu cầu sửa:** Thay dependency toàn Epic bằng Story/contract cụ thể. Platform gateway, Theme, localization, CI và dependency lock có thể bắt đầu sau scaffold/protocol cần thiết, không phải sau toàn bộ content.

#### EQ-M9 — Gate Story đang gom integration evidence quá rộng

Backlog dùng nhiều Story gate ở cuối Epic: 1.13, 2.15, 3.11, 4.13, 5.13, 6.16–6.18, 7.10, 8.19, 9.8 và 10.15. Gate là hợp lý khi tạo evidence hoặc quyết định promotion, nhưng không được che feature work chưa có Story riêng hoặc lặp lại DoD của mọi Story.

**Yêu cầu sửa:** Với mỗi gate, phân biệt:

- feature/capability chưa triển khai — phải có Story riêng;
- automated evidence/benchmark — có thể là Story nếu tạo artifact có owner;
- promotion decision — nên là checklist/milestone dùng evidence đã sinh, không phải catch-all implementation Story.

### 🟡 Minor Concerns

#### EQ-m1 — “As a player” đôi lúc che actor thực

Một số Story thực chất phục vụ development, test, world, release hoặc operations team. Ví dụ Story 1.12, 2.14, 3.8, 5.1, 7.1, 10.1, 10.2, 10.8 và 10.14. Dùng actor thực là tốt hơn việc ép technical enabler thành player story.

**Khuyến nghị:** Gắn nhãn `Enabler`, nói rõ consumer/outcome và liên kết tới player-facing Story mà nó mở khóa.

#### EQ-m2 — “Blocks” và dependency đôi khi dùng tên gate hoặc phạm vi chung

Các cụm như “Epic X gate”, “production content Epic 7–9” hoặc “gameplay presenters Epic 1–7” không xác định artifact/contract cụ thể.

**Khuyến nghị:** Thay bằng Story ID + output/contract được tiêu thụ để dependency có thể kiểm chứng.

#### EQ-m3 — Một số Story có rất nhiều AC nhưng chưa có sizing signal

Story 1.1 có 7 nhóm Given và Story 1.2 có 9 nhóm Given; các Story gate cũng bao phủ nhiều platform/evidence. Backlog chưa ghi estimate, split threshold hoặc rule giới hạn số capability.

**Khuyến nghị:** Trong sprint planning, mọi Story có nhiều hơn một capability hoặc không thể hoàn tất trong một sprint phải được split trước khi chuyển `ready-for-dev`.

### Positive Findings

- Không có forward dependency hoặc circular dependency.
- Thứ tự dependency trong từng Epic nhất quán với Story numbering.
- Epic 1 có initial project setup đúng clean-project decision của Architecture.
- Epic 2, 4, 7 và 9 có player outcome rõ, cấu trúc tương đối tốt.
- Acceptance criteria có BDD, error handling, test boundary và DoD nhất quán trên toàn bộ 135 Story.
- Traceability tới FR/NFR/UX/Architecture được duy trì ở từng Story.

### Epic Quality Verdict

**Không đạt để triển khai nguyên trạng.** Backlog có chất lượng AC và traceability rất cao, không có forward dependency, nhưng vẫn vi phạm chuẩn ở Epic 10 dạng technical program, Epic 5 dạng technical slice, UX/CI/enabler bị đặt quá muộn và một số Story nền tảng có kích thước vượt ngưỡng triển khai độc lập. Các vấn đề EQ-C1 và EQ-M1–EQ-M8 cần được xử lý hoặc có kế hoạch split/resequence được phê duyệt trước khi sprint đầu tiên được coi là implementation-ready.

## Summary and Recommendations

### Overall Readiness Status

**NOT READY**

Outsurvive **chưa sẵn sàng để bắt đầu implementation theo backlog hiện tại**.

Các tài liệu có độ chi tiết, traceability và chất lượng acceptance criteria cao. Tuy nhiên, readiness bị chặn bởi ba nhóm vấn đề: GDD chưa được phủ đầy đủ trong Epics, các contract kiến trúc/UX quan trọng chưa khóa hoặc đang tham chiếu artifact cũ, và cấu trúc Epic/Story đặt một số engineering control nền tảng quá muộn.

Assessment ghi nhận **31 finding cụ thể trong 3 nhóm**:

- 12 requirement-coverage finding: 10 thiếu và 2 phủ một phần.
- 6 UX/Architecture alignment finding.
- 13 Epic-quality finding: 1 critical, 9 major và 3 minor.

### Critical Issues Requiring Immediate Action

1. **Bổ sung sáu FR cạnh tranh/map/audio đang thiếu ở mức critical:** FR55, FR57, FR59, FR76, FR77 và FR85. Mỗi FR cần Story/AC định lượng, owner và test evidence cụ thể.
2. **Loại bỏ cấu trúc technical program của Epic 10:** dependency lock, CI/signing, SBOM, server container và observability phải được đưa về Epic/Story sở hữu và thực hiện sớm hơn.
3. **Revalidate Architecture theo bản Epics hiện hành:** Architecture đang tham chiếu bản 9-Epic cũ trong khi backlog chuẩn có 10 Epic.
4. **Khóa các decision gate trước Story liên quan:** reconnect/AFK outcome, spectator voice/ping, player-facing audio bus, localization boundary, raw-mouse/key identity và Map orientation/zoom.
5. **Resequence UX và engineering foundations:** Theme, presenter, localization, CI, dependency lock và observability không được đợi toàn bộ gameplay/content hoàn thành.
6. **Split các Story quá lớn trên critical path:** ưu tiên Story 1.1, 1.2, 3.1, 3.11 và 5.1.

### Recommended Next Steps

1. **Correct course trên artifact chuẩn.** Dùng `_bmad-output/planning-artifacts/epics.md` làm nguồn duy nhất; archive hoặc đánh dấu rõ bản Epics cũ đã superseded.
2. **Tạo một remediation matrix.** Với từng ID FR55/57/59/65/70/75/76/77/78/79/85/93 và UX-A1–A6, ghi artifact cần sửa, owner, Story/AC đích, evidence và trạng thái.
3. **Cập nhật Architecture.** Sửa source reference, re-run mapping 10 Epic, thêm localization/audio control ownership và ghi ADR cho reconnect, spectator, input/map policy.
4. **Refactor backlog.** Reframe/split Epic 5; phân rã Epic 10; chuyển CI/SBOM/observability và UX foundation về sớm; thay dependency toàn Epic bằng dependency Story/contract.
5. **Split critical-path Stories.** Đảm bảo mỗi Story tạo một capability có thể hoàn tất độc lập trong một sprint và chỉ tạo data/entity vừa đủ cho consumer hiện tại.
6. **Chạy lại coverage và quality checks.** Mục tiêu tối thiểu trước sprint planning: 93/93 GDD FR có đường triển khai rõ, 0 open decision gate cho Story `ready-for-dev`, 0 technical Epic, 0 oversized critical-path Story.
7. **Chỉ sau đó thực hiện sprint planning.** Có thể cho phép một preparation sprint giới hạn ở artifact correction, ADR, spike có timebox và scaffold; không coi đây là bắt đầu production implementation.

### Readiness Exit Criteria

Assessment được chuyển từ `NOT READY` sang `READY` khi:

- Coverage nghiêm ngặt đạt 100% hoặc mọi deferred FR có quyết định scope chính thức.
- Architecture tham chiếu đúng backlog 10 Epic và không còn contradiction với UX controls.
- UX-A1–A5 có owner decision/ADR trước Story tiêu thụ.
- Epic 5/10 được reframe hoặc split theo player/user value.
- Story 1.1, 1.2, 3.1, 3.11 và 5.1 được split hoặc có sizing/evidence chứng minh hoàn tất độc lập trong một sprint.
- CI/reproducibility/security/observability controls xuất hiện tại thời điểm capability đầu tiên cần chúng.

### Final Note

Kết luận `NOT READY` không phản ánh tài liệu yếu; ngược lại, các artifact đủ chi tiết để lộ rõ rủi ro trước khi code được viết. Sửa các blocker trên sẽ bảo toàn phần tốt nhất của bộ tài liệu — authority, parity, BDD và traceability — đồng thời tránh big-bang integration và rework đa nền tảng.

**Assessment date:** 2026-07-26

**Assessor:** Codex — GDS Implementation Readiness workflow
