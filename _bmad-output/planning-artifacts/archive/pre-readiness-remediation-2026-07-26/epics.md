---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - "_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md"
  - "_bmad-output/game-architecture.md"
  - "_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/DESIGN.md"
  - "_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md"
  - "_bmad-output/project-context.md"
  - "_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-23.md"
  - "_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/decision-log.md"
  - "_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/.decision-log.md"
---

# outsurvive - Epic Breakdown

## Overview

Tài liệu này cung cấp phân rã Epic và Story đầy đủ cho outsurvive, chuyển các yêu cầu từ GDD, UX Design và Game Architecture thành các hạng mục triển khai có thể kiểm chứng.

## Requirements Inventory

### Functional Requirements

FR1: Hệ thống phải cung cấp luật chơi Standard battle royale TPP cho tối đa 100 người, trong đó mọi người xuất phát tay trắng và chiến đấu tới người hoặc đội sống cuối cùng.

FR2: Người chơi phải có thể chọn Solo, Duo hoặc Squad bốn người trước khi vào hàng chờ; Duo hỗ trợ tối đa 50 đội và Squad tối đa 25 đội.

FR3: Trận đấu phải đi qua các giai đoạn chuẩn bị, sảnh chờ, máy bay, đổ bộ, loot đầu trận, di chuyển/giao tranh, bo cuối và kết quả.

FR4: Sảnh chờ phải có 60 giây chuẩn bị; máy bay và đổ bộ phải cho phép người chơi đọc đường bay, chọn điểm rơi, điều khiển tốc độ/khoảng bay và quan sát dù đối thủ.

FR5: Solo phải loại người chơi khi HP về 0; Duo/Squad phải hỗ trợ DBNO và chỉ loại đội khi không còn thành viên có thể chiến đấu.

FR6: Duo/Squad phải công nhận chiến thắng khi ít nhất một thành viên còn sống sau khi mọi đội khác bị loại.

FR7: Rời trận sau khi máy bay khởi hành phải được tính là thất bại; sau khi đội bị loại, việc rời trận không được áp dụng hình phạt thất bại sai.

FR8: Người chơi bị loại trong Duo/Squad phải có thể spectate một đồng đội còn sống cho tới khi đội bị loại hoặc người chơi chủ động rời.

FR9: Standard không được cung cấp hồi sinh, mua lại, tự hồi sinh hoặc trạm triệu hồi.

FR10: Trận phải tạo kết quả do máy chủ xác nhận gồm placement, thời gian sống, kills/assists và thống kê combat/survival tối thiểu.

FR11: Results phải cho phép Play Again, trở về Sảnh chính và mở Report/Block đối với đối tượng hợp lệ.

FR12: Hệ thống phải hỗ trợ phiên mục tiêu 28–35 phút và có thể kết thúc sớm khi chỉ còn một người hoặc một đội.

FR13: Hệ thống phải duy trì một luật gameplay, dữ liệu cân bằng và content manifest chung cho Windows, Linux, macOS, Android và iOS.

FR14: Người chơi phải có thể đi bộ, chạy thường, chạy nước rút, ngồi, nằm, nhảy, leo/vượt và nghiêng người theo các tốc độ, thời gian hồi và đánh đổi đã nêu trong GDD.

FR15: Chạy nước rút phải khóa bắn và tạo độ trễ 0,35 giây trước khi súng sẵn sàng sau khi dừng.

FR16: Nhảy phải đạt tối đa 0,9 m, có hồi 0,45 giây và khóa ADS khi đang ở trên không.

FR17: Leo/vượt phải hỗ trợ vật cản cao 0,6–1,4 m, kéo dài 0,45–0,90 giây, khóa bắn và phát âm thanh rõ.

FR18: Nghiêng người phải đạt tối đa 18°, vào tư thế trong 0,15 giây và giảm tốc di chuyển còn 65%.

FR19: Hệ thống phải áp dụng sát thương rơi từ độ cao trên 3 m và cho phép tử vong khi rơi từ 8 m nếu người chơi không đầy máu.

FR20: Nước sâu phải giảm tốc còn 2,0 m/s, khóa vũ khí và cho phép lặn tối đa 20 giây trước khi mất HP.

FR21: Hệ thống không được dùng thanh stamina; tốc độ và tiếng động phải là đánh đổi chính của di chuyển.

FR22: Gameplay phải nhận `GameplayCommand` ngữ nghĩa chung từ Keyboard/Mouse, Touch hoặc Gyro thay vì đọc thiết bị thô trong luật gameplay.

FR23: Keyboard/Mouse phải hỗ trợ đầy đủ các binding di chuyển, tư thế, tương tác, nạp đạn, vật ném và Inventory đã nêu trong GDD.

FR24: Touch landscape phải cung cấp cần di chuyển trái, vùng nhìn phải, nút bắn phải, nút bắn trái tùy chọn và các nút ngữ cảnh cho tư thế, ADS, tương tác, nạp đạn, vật ném, map, inventory và phương tiện.

FR25: Mỗi người chơi phải có 100 HP và HP không được tự hồi theo thời gian.

FR26: Sát thương phải dùng hệ số vùng cơ thể: đầu ×2,20; ngực ×1,00; bụng ×0,90; tay/chân ×0,75.

FR27: Áo giáp cấp 1/2/3 phải giảm sát thương thân 15%/30%/45% với độ bền 160/220/280.

FR28: Mũ cấp 1/2/3 phải giảm sát thương đầu 30%/45%/55% với độ bền 80/150/230.

FR29: Viên đạn làm độ bền giáp về 0 vẫn phải nhận giảm sát thương của giáp; giáp chỉ bị phá sau viên đạn đó.

FR30: Băng cá nhân, túi cứu thương, bộ cứu thương lớn, nước tăng lực và thuốc giảm đau phải dùng đúng thời gian, hiệu quả, giới hạn HP và quy tắc ngắt đã nêu trong GDD.

FR31: Trong Duo/Squad, người chơi về 0 HP phải vào trạng thái Gục với 100 HP chảy máu, tốc độ mất máu khởi điểm 2 HP/giây và tăng gấp đôi sau mỗi lần gục tiếp theo.

FR32: Hồi đồng đội phải mất 10 giây và bị ngắt khi người cứu di chuyển hoặc chịu sát thương.

FR33: Người gục chỉ được bò 0,7 m/s, đánh dấu và nói chuyện; không được dùng súng, hồi máu hoặc tự cứu.

FR34: Hệ thống phải cung cấp hai ô vũ khí chính, một ô súng ngắn, một ô cận chiến và một ô vật ném đang chọn.

FR35: Cơ thể phải có 50 đơn vị sức chứa; ba cấp ba lô phải nâng tổng sức chứa lên 120/180/250.

FR36: Đạn, hồi máu và vật ném phải dùng sức chứa; phụ kiện đã gắn trên súng không dùng sức chứa.

FR37: Người chơi phải có thể điều trị, hồi đồng đội, nạp đạn và thực hiện hành động giữ theo progress xác nhận từ máy chủ, với lý do ngắt rõ ràng.

FR38: Hệ thống loot phải tạo vật phẩm theo nhóm spawn logic và chọn vật phẩm cụ thể bằng ngẫu nhiên có trọng số theo từng trận.

FR39: Mọi người phải bắt đầu tay trắng và không được chọn loadout, vũ khí hoặc kỹ năng trước trận.

FR40: Nhặt nhanh phải mất 0,20 giây mỗi món; Inventory phải hỗ trợ nhặt, trang bị, di chuyển, tách chồng và thả vật phẩm.

FR41: Inventory phải từ chối slot sai loại, quá sức chứa hoặc mutation không hợp lệ mà không di chuyển item khỏi nguồn.

FR42: Hệ thống không được tự nhặt vũ khí, giáp hoặc phụ kiện.

FR43: Người chơi phải có thể bật tự nhặt đạn đúng cỡ tới ngưỡng riêng do họ cấu hình; giá trị 0 phải tắt tự nhặt cho cỡ đạn đó.

FR44: Sau 90 giây loot một cụm nhà trung bình, phân phối loot phải hướng tới 95% có súng, 70% có vũ khí chính, 50% có giáp hoặc mũ và 35% có hồi máu.

FR45: Khu dân cư nhỏ phải ưu tiên đồ cơ bản; cơ sở quân sự, cảng và công nghiệp phải có loot tốt hơn cùng rủi ro tiếp cận/tranh chấp cao hơn.

FR46: Một thùng tiếp tế phải xuất hiện trong mỗi pha bo 1–5 tại vị trí có thể tiếp cận, phát khói thấy được ở 800 m và chứa một vũ khí đặc biệt cùng giáp/hồi máu cấp cao.

FR47: Không vật phẩm thiết yếu nào được chỉ có trong thùng tiếp tế.

FR48: Người chơi phải có thể mang tối đa sáu vật ném trong giới hạn sức chứa.

FR49: Hệ thống phải hỗ trợ lựu đạn mảnh, lựu đạn khói, lựu choáng và chai cháy với ngòi nổ, bán kính, thời lượng và tác dụng đã nêu trong GDD.

FR50: Quỹ đạo dự kiến của vật ném chỉ được hiển thị trong 1,5 giây đầu khi ngắm.

FR51: Hệ thống phải hỗ trợ sáu archetype phương tiện: sedan, jeep, bán tải, xe máy, thuyền và xe tải với số chỗ tương ứng.

FR52: Phương tiện phải có tốc độ tối đa 80–125 km/h, nhiên liệu, HP, bốn trạng thái lốp và âm thanh nghe được trong 250–450 m tùy xe.

FR53: Phương tiện về 0 HP phải phát cảnh báo cháy 3 giây trước khi nổ; trạng thái đếm ngược phải tiếp tục hiển thị sau khi người chơi rời ghế cho tới khi máy chủ xác nhận nổ hoặc hủy.

FR54: Va chạm xe trên 35 km/h phải gây sát thương và trên 70 km/h có thể hạ gục người không được vật cản che.

FR55: Xe không được tự báo va chạm gây sát thương; máy chủ phải xác nhận collision, damage và explosion.

FR56: Camera chuẩn phải hỗ trợ TPP hip-fire, TPP ngắm qua vai, đổi vai và ADS thứ nhất.

FR57: Camera phải bị đẩy về phía trước khi sát tường và không render đối thủ/vật thể bị che hoàn toàn khỏi đường nhìn từ đầu nhân vật chỉ vì camera TPP nhìn thấy.

FR58: Người chơi phải có thể remap toàn bộ action gameplay, chỉnh layout Touch, độ nhạy hip-fire/ADS/từng độ phóng và chọn hold/toggle cho ADS, nghiêng, ngồi và chạy.

FR59: Danh mục v1.0 phải hướng tới 25 vũ khí gồm 3 súng ngắn, 3 SMG, 3 shotgun, 5 AR, 3 DMR, 3 sniper, 2 LMG và 3 cận chiến.

FR60: Hệ thống phải hỗ trợ năm cỡ đạn 9 mm, .45, 5,56 mm, 7,62 mm và 12 gauge với màu, hình hộp và biểu tượng phân biệt.

FR61: Hệ thống phải hỗ trợ 4 đầu nòng, 4 tay cầm, 3 băng đạn, 2 báng và 7 loại ngắm; phụ kiện chỉ gắn vào slot hợp lệ.

FR62: Mỗi archetype vũ khí phải áp dụng damage, RPM, băng đạn, vận tốc, thời gian nạp, falloff, ADS, spread và recoil theo baseline GDD hoặc dữ liệu cân bằng đã được phê duyệt.

FR63: Tất cả vũ khí chính phải dùng projectile có thời gian bay và độ rơi; không được dùng hitscan.

FR64: Recoil phải tăng qua tám viên đầu, ổn định sau viên 12 và bắt đầu hồi khi ngừng bắn 0,25 giây; tư thế và chuyển động phải sửa đổi spread theo hệ số GDD.

FR65: Scope từ 4× phải hỗ trợ giữ hơi tối đa 8 giây, trạng thái hụt hơi 4 giây và zero 100–800 m theo bước 100 m khi scope hỗ trợ.

FR66: Aim punch phải phụ thuộc năng lượng viên đạn/giáp, không vượt 1,5° mỗi hit và có ngưỡng 0,12 giây chống khóa ngắm liên tục.

FR67: Cận chiến phải có tầm 1,8 m, wind-up 0,35–0,55 giây và damage 35–60 tùy vũ khí.

FR68: Mỗi phát bắn phải có tiếng nổ, tiếng cơ khí, lóe nòng, vỏ đạn và phản lực camera có thể phân biệt.

FR69: Trúng mục tiêu phải tạo máu/bụi theo setting, âm thanh nhẹ và phản ứng cơ thể; không được hiển thị số damage nổi.

FR70: Hit marker, impact cạnh tranh, DBNO và elimination chỉ được xác nhận sau trạng thái máy chủ; hit trade hợp lệ phải được chấp nhận nếu cả hai viên đã rời nòng trước elimination.

FR71: Máy chủ trận đấu phải xác nhận movement validity, shot, projectile, damage, ammo, inventory, loot, vehicle, zone và result.

FR72: Client phải dự đoán và hòa giải chỉ các trạng thái được phép, không optimistic-commit inventory, loot, damage hoặc kết quả.

FR73: Bù trễ phải rewind bounded hitbox history tối đa 150 ms và không được rewind toàn world.

FR74: Người chơi vượt 150 ms phải nhận cảnh báo kết nối; nếu không vùng nào đạt ngưỡng, họ phải xác nhận rõ trước khi tiếp tục.

FR75: Matchmaking phải ưu tiên vùng mạng, thời gian chờ và soft MMR chỉ cho 10 trận đầu để tránh nhóm kỹ năng cao nhất.

FR76: Keyboard/Mouse, Touch và Mixed/Keyboard-Mouse phải là các input pool riêng; party trộn phải được công bố và xác nhận trước Ready.

FR77: Input family phải được khóa khi vào trận; kết nối Keyboard/Mouse ngoài trên mobile không được đổi pool giữa trận và phải yêu cầu requeue sau trận.

FR78: Hệ thống không được âm thầm dùng bot để lấp Standard, đổi pool hoặc nới quy tắc công bằng.

FR79: Hàng chờ thử nghiệm dùng bot phải công bố số bot dự kiến trước khi người chơi xác nhận.

FR80: Hệ thống party phải hỗ trợ tối đa bốn người, leader, Ready, invite, reconnect và clear Ready khi roster, mode, region hoặc input-pool disclosure thay đổi.

FR81: Giao tiếp đội phải hỗ trợ voice team-only, PTT mặc định, open-mic tùy chọn, mute/volume từng người và tám ping ngữ cảnh đã khóa trong UX.

FR82: Friendly fire phải bật ở 100% damage sau khi lên máy bay, hiển thị nguồn trung tính và cung cấp luồng Report/Block.

FR83: Bản đồ Đảo Vọng phải hướng tới 8×8 km, 18 POI, 55 cụm nhà, ít nhất 420 công trình có thể vào, 180 vị trí xe có trọng số và 12 bến thuyền sau khi vượt các cổng scale/mobile.

FR84: Mỗi khoảng trống dài trên 120 m phải cung cấp ít nhất hai lựa chọn từ cover cứng, địa hình lõm, smoke, xe hoặc tuyến vòng.

FR85: Cầu và đèo phải có tuyến vòng chậm hơn; không được tồn tại một choke bắt buộc duy nhất từ vùng đất lớn vào bo.

FR86: Vòng cuối không được đặt quá 50% diện tích trên nước, vách không thể đứng hoặc mái không thể tiếp cận.

FR87: Seed trận chỉ được chọn loot, phương tiện, đường bay, thời tiết và bo; không được tái sinh hình học map runtime.

FR88: Thời tiết phải được chọn khi bắt đầu trận theo trọng số quang 70%, mưa 15%, sương 15% và không đổi đột ngột giữa trận.

FR89: Mưa phải giảm khoảng nghe bước chân 15%; sương phải giới hạn độ tương phản mục tiêu sau 180–250 m.

FR90: Hệ thống bo phải chạy chín pha với thời gian chờ, thời gian thu, bán kính, damage ngoài bo và survival target theo bảng GDD.

FR91: Bo tiếp theo chỉ được lộ khi pha chờ bắt đầu; không được có vật phẩm dự báo bo hoặc vùng ném bom ngẫu nhiên gây chết tức thời.

FR92: Hồ sơ phải ghi số trận, top 10, chiến thắng, cự ly hạ gục, độ chính xác và lịch sử mùa mà không tăng sức mạnh.

FR93: Weapon Mastery chỉ được mở số liệu chuyên sâu và huy hiệu hồ sơ không hết hạn; không được mở skin hoặc sức mạnh.

FR94: Training Grounds phải có bia tĩnh, bia di động 2–8 m/s và bot luyện ba hành vi; kết quả training không được ảnh hưởng thống kê cạnh tranh.

FR95: Field Orientation phải là onboarding tùy chọn, có thể bỏ qua/chơi lại, gồm bốn checkpoint movement-camera, loot-inventory, fire-ADS và zone-cover, không trao reward/mastery/stats.

FR96: v1.0 không được cung cấp storefront, premium currency, microtransaction, loot box, gacha, battle pass, daily streak, quảng cáo hoặc live-event.

FR97: HUD trận phải hiển thị đúng các nhóm HP/boost, ammo, stance, direction, minimap, squad state và zone phase mà không chứa nội dung thương mại.

FR98: Map toàn màn hình phải hiển thị flight path, current/next zone hợp lệ, marker đội và địa danh; không được hiển thị loot hoặc đối thủ.

FR99: Inventory và Map không được pause trận; Inventory desktop phải giữ dải nhìn thế giới tối thiểu 32%, còn mobile tối thiểu 38%.

FR100: Hệ thống phải cung cấp settings cho graphics, audio, accessibility, language, input, Touch layout, Gyro, haptic, FOV, sensitivity, camera shake và flash intensity.

FR101: Hệ thống phải cung cấp ba preset mù màu cho bo, marker, hit effect và reticle; thông tin quan trọng phải dùng thêm shape, icon hoặc label.

FR102: Hệ thống phải cung cấp subtitle cho thông báo hệ thống và ping đồng đội; không được biến âm thanh bước chân thành chỉ báo trực quan trong competitive queue.

FR103: Permission voice chỉ được hỏi khi người chơi bật voice/PTT; denial không được lặp prompt và audio-route/lifecycle change không được làm kẹt input hoặc phát voice ngoài ý muốn.

FR104: Audio phải hỗ trợ Stereo Headphones với HRTF On/Off, Stereo Speakers và Mono accessibility downmix; Team Voice, UI và Music phải có control riêng trong giới hạn công bằng đã khóa.

FR105: Khi người chơi còn sống, không được phát nhạc nền; nhạc chỉ được dùng ở menu, Results và sau khi máy chủ xác nhận chiến thắng.

FR106: Results/Replay Summary phải dùng event/stat máy chủ xác nhận; khi payload chưa đến phải hiển thị Pending, khi không có phải hiển thị Unavailable và không dựng kill-cam giả.

FR107: Report MVP phải hỗ trợ target hợp lệ, category Cheating, Team-kill/Friendly-fire abuse, Harassment/Voice, Teaming, Exploit hoặc Other, ghi chú tùy chọn, receipt và retry.

FR108: Block phải là hành động local tách khỏi Report và có thể áp dụng ngay cả khi Report đang chờ gửi.

FR109: Lifecycle mobile phải xử lý `Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended`, trung hòa held input/PTT và dùng cùng match identity/token.

FR110: Platform adapter failure hoặc provider degraded phải hiển thị capability/state rõ mà không âm thầm đổi luật gameplay, input pool hoặc nguồn thông tin.

### NonFunctional Requirements

NFR1: Ít nhất 80% người thử nghiệm phải mô tả nguyên nhân thắng/thua bằng quyết định và kỹ năng thay vì vật phẩm ngoài trận hoặc may rủi không thể ứng phó.

NFR2: Ít nhất 90% tình huống tử vong phải được người xem độc lập giải thích đúng từ replay nội bộ.

NFR3: Chênh lệch win rate giữa giáp cấp 2 và cấp 3 phải dưới 8 điểm phần trăm sau khi kiểm soát kỹ năng.

NFR4: Desktop minimum phải đạt 60 FPS median và p95 frame time ≤25 ms ở 1080p/Low trên replay chuẩn.

NFR5: Desktop recommended phải đạt 90 FPS median và p95 frame time ≤16,7 ms ở 1080p/High trên cùng replay chuẩn.

NFR6: Desktop client phải dùng ≤6 GB RAM sau trận 45 phút.

NFR7: Thời gian từ xác nhận ghép trận tới pre-match phải ≤45 giây p95 trên desktop minimum với cache lạnh.

NFR8: Mobile minimum phải đạt 45 FPS median và p95 frame time ≤33,3 ms ở Low trên thiết bị minimum.

NFR9: Mobile recommended phải đạt 60 FPS median và p95 frame time ≤25 ms ở Medium trên thiết bị recommended.

NFR10: Mobile working memory phải ≤3 GB và không bị OS terminate trong trận 45 phút.

NFR11: Mobile median FPS không được giảm quá 15% sau 30 phút thermal soak.

NFR12: Thời gian vào pre-match trên mobile minimum phải ≤60 giây p95 với cache lạnh.

NFR13: Dedicated server phải duy trì simulation 30 Hz cho 100 người với tối thiểu 10% headroom trong soak 45 phút.

NFR14: Damage event phải được xử lý trong ≤1 tick ở p95 dưới tải 100 người, 80 ms RTT và 1% packet loss.

NFR15: Sai lệch vị trí nhìn thấy so với vị trí máy chủ xác nhận phải ≤0,5 m ở p95 trong điều kiện 80 ms RTT/1% packet loss.

NFR16: Băng thông trung bình không được vượt 1,5 Mbps mỗi chiều trên mỗi client trong trận 100 người.

NFR17: Match server Alpha phải hướng tới envelope ≤8 vCPU/16 GB cho mỗi trận và được xác minh bằng benchmark.

NFR18: Tối đa sáu smoke dày đồng thời trong bán kính 100 m quanh người chơi vẫn phải giữ performance budget minimum.

NFR19: Crash-free sessions phải đạt ≥99,5% trong cửa sổ 30 ngày.

NFR20: Ít nhất 99,0% trận phải kết thúc với kết quả máy chủ hợp lệ.

NFR21: Ít nhất 95% người chơi trong khu vực ra mắt phải được ghép vào vùng có ping median ≤80 ms và packet loss mục tiêu <1%.

NFR22: Khiếu nại hit registration được replay xác nhận sai quá 0,5 m hoặc quá một tick phải dưới 0,5% phát bắn hợp lệ.

NFR23: TTK AR ở 20 m phải nằm trong 0,17–0,25 giây không giáp và 0,25–0,40 giây qua giáp cấp 2 sau mọi thay đổi balance.

NFR24: Không vũ khí loot thường nào được vượt 22% tổng kills trong mẫu ít nhất 10.000 kills; vũ khí supply drop không vượt 8%.

NFR25: Win rate theo drop point không được lệch quá ±20% quanh trung bình sau khi kiểm soát kỹ năng và team size.

NFR26: Tất cả packet không tin cậy phải được kiểm tra type, length, range, cadence, sequence, ownership và state transition trước khi mutate.

NFR27: Client không được có authority đối với movement validity, hit, damage, ammo, inventory, loot, vehicle collision, zone hoặc match result.

NFR28: Session/join/reconnect token phải có expiry, nonce và replay protection; secret không được xuất hiện trong source, artifact log, prompt hoặc MCP.

NFR29: Gameplay time phải dùng `ServerTick`, local timeout dùng monotonic clock và simulation randomness dùng purpose-specific seeded streams.

NFR30: Platform identity, PII và combat telemetry phải được tách boundary; không được log raw voice, token, signing secret hoặc PII không cần thiết.

NFR31: Tất cả năm client target phải dùng cùng collision, cover, silhouette, openings, visibility semantics, gameplay data và protocol.

NFR32: Ultrawide Standard phải giữ live-world viewport cạnh tranh 16:9 ở giữa; phần ngoài không được chứa world entity hoặc gameplay cue.

NFR33: Touch không được nhận target snap, auto-fire, enemy detection, visual footstep cue, magnetism hoặc thông tin chiến đấu bổ sung.

NFR34: Không bot, silent pool fallback hoặc desktop-only attestation được phép tạo tiêu chuẩn công bằng mà mobile không thể đáp ứng.

NFR35: Mọi mỹ phẩm hoặc platform visual variant không được thay hitbox, collision, silhouette chiến đấu, âm thanh hoặc khả năng ngụy trang vượt giới hạn parity.

NFR36: Text thường phải đạt contrast ≥4,5:1; text lớn, icon cần thiết và focus ring phải đạt ≥3:1 sau compositing thực tế.

NFR37: UI phải hỗ trợ scale 80–140% mà không làm text thấp hơn 12 px, label critical thấp hơn 14 px hoặc số critical thấp hơn 18 px.

NFR38: Desktop UI phải không crop/overlap critical content tại 1280×720, 1920×1080, 2560×1440, 3840×2160, 3440×1440 và 5120×1440 ở scale 80/100/140%.

NFR39: Mobile UI phải vượt acceptance trên phone 20:9, phone 16:9 và tablet 4:3 với notch trái/phải, gesture bar, UI scale 100/120/140% và left-handed layout.

NFR40: Touch target thường phải ≥48 logical units; fire, exit và close phải ≥64 khi safe area cho phép.

NFR41: UI phải hỗ trợ đầy đủ keyboard focus, traversal theo thứ tự đọc, không keyboard trap và không bắt drag chuột làm đường thao tác duy nhất.

NFR42: Motion HUD phải kéo dài 120–180 ms, contextual fade-out ≤120 ms, translation ≤12 px; không overshoot, bounce, strobe hoặc parallax.

NFR43: Critical flash chỉ được chiếm ≤10% central frame và không vượt 3 lần/giây; Reduce Motion/Flash phải giữ nguyên timing và thông tin gameplay.

NFR44: Âm thanh Stereo/HRTF phải cho người thử nghiệm xác định đúng cung 30° ở ≥85% lần thử tại 20–80 m trên từng output cạnh tranh hỗ trợ.

NFR45: Inventory, Map và Pause không được mute/duck footsteps, gunshots, vehicles, zone hoặc team voice khi người chơi còn sống.

NFR46: World streaming không được tạo gameplay-breaking hitch hoặc làm sai projectile, door, vehicle, collision, water hay audio state khi qua cell boundary.

NFR47: Cell không được unload khi còn projectile, vehicle, door transition, gameplay reference hoặc async commit chưa hoàn tất.

NFR48: Critical combat assets phải preload trước trận; world-cell loading phải có bounded cache và main-thread instantiation budget.

NFR49: Build v1.0 phải hỗ trợ Windows 10/11 x64, Linux x64, macOS 13+ Intel/Apple Silicon, Android 10+ ARM64, iOS 16+ ARM64 và Linux x86-64 headless server.

NFR50: Bản cài desktop phải ≤25 GB, mobile ≤12 GB và balance patch không được yêu cầu tải lại quá 2 GB nội dung không đổi.

NFR51: V1.0 chỉ sẵn sàng khi vòng lặp 100 người, bốn trụ cột gameplay, server/load gate và release-candidate family trên cả năm nền tảng đều đạt.

NFR52: Scale phải được chứng minh tuần tự qua 8 → 24 → 50 → 100 protocol-mixed clients; không được khóa full map/content trước các gate tương ứng.

NFR53: Nếu 100 người hoặc 8×8 km không đạt budget, sản phẩm phải giữ quy mô đã chứng minh thay vì trao authority cho client, dùng bot ẩn hoặc giảm gameplay parity.

NFR54: Toàn bộ nội dung ảnh hưởng gameplay phải có thể tiếp cận bằng hành động trong trận, không bằng tiền hoặc progression ngoài trận.

NFR55: Mọi engine, plugin, database, orchestrator hoặc native SDK upgrade phải có ADR, version/checksum manifest và compatibility/parity gate.

### Additional Requirements

- **BẮT BUỘC CHO EPIC 1 STORY 1:** Khởi tạo dự án Godot Standard sạch; không kế thừa starter kit hoặc framework gameplay bên thứ ba. Official TPS demo và `godot-demo-projects` chỉ được dùng làm nguồn tham khảo có kiểm soát.
- Pin Godot Engine Standard và export templates ở phiên bản `4.7.1-stable`; dùng typed GDScript. Mọi nâng cấp engine phải qua compatibility branch và five-platform smoke test.
- Scaffold domain-driven monorepo theo project tree kiến trúc, tách rõ `game`, `native`, `backend`, `infrastructure`, `content-source`, `prepare-asset`, `test-harness` và `docs`.
- Duy trì dependency direction vào shared ports/contracts/simulation; `shared` không được import client, server, platform SDK, UI, renderer hoặc backend implementation.
- Chỉ `AppKernel`, `BuildInfo`, `PlatformGateway` và service thực sự sống toàn ứng dụng được làm Autoload; Autoload mới cần ADR.
- Dùng modular authoritative simulation; SceneTree/Node chỉ sở hữu composition, lifecycle cục bộ và presentation.
- Application lifecycle và match lifecycle phải là guarded state machine với transition table/guard, không dùng nhóm boolean chồng chéo.
- Gameplay authoritative phải chạy trong fixed 30 Hz phase scheduler với thứ tự ingest input → movement → physics query → combat → inventory → zone → commit events → build snapshots.
- Phase order là protocol contract; thay đổi phải có deterministic regression test và ADR.
- Người chơi phải dùng custom kinematic `CharacterMotor`; Jolt chỉ làm collision/query và server-authoritative vehicle physics, không giả định deterministic tuyệt đối.
- Projectile phải dùng ballistic integration với swept collision segment; không tạo một `RigidBody3D` cho mỗi viên.
- Transport realtime phải dùng ENet/UDP dưới custom binary replication protocol; không dùng SceneTree replication, RPC name, `NodePath` hoặc instance ID làm protocol identity.
- Mỗi message phải có numeric type ID, protocol version, sequence, tick, payload length và validation rule.
- Reliable ordered channel phải dành cho session, phase, inventory và interaction; input/snapshot dùng các unreliable-sequenced channel riêng.
- Protocol xử lý packet theo `decode → validate → apply`; cấm `Variant`, Dictionary hoặc object deserialization cho untrusted transport.
- Replication phải có snapshot delta, relevance graph và update tier theo loại entity để đáp ứng budget 100 người.
- Prediction/reconciliation phải theo Authority Mirror Pattern, có input sequence, ack, restore/replay và presentation smoothing tách khỏi correction.
- Handshake phải khớp `build_id`, `protocol_version`, `gameplay_schema_version` và `content_manifest_hash`.
- Server phải giữ bounded hitbox history cho lag compensation và clamp shot timestamp theo session clock/latency envelope.
- Dùng stable content/gameplay ID như `weapon.ar_556_01`; không dùng file path, `res://`, NodePath hoặc display name làm identity.
- Typed Custom Resources chỉ là authoring source và phải được validate/bake thành immutable gameplay manifest cùng platform asset packs.
- Client và server phải tải cùng gameplay manifest; server artifact không chứa texture, mesh, shader hoặc audio presentation không cần thiết.
- Terrain3D `1.0.2` chỉ được dùng trong editor; bake thành versioned `TerrainTileData` gồm height, collision, material mask, mesh LOD và dependency manifest.
- World 8×8 km phải dùng hierarchical multi-grid; terrain, entity streaming, building HLOD, navigation, audio và server spatial query có grid/cadence độc lập.
- `WorldCellId` phải là identity logic ổn định; cell baseline 250×250 m chỉ là giả thuyết benchmark, không phải quyết định cứng.
- World streaming phải dùng threaded load, prefetch corridor, high/low-water cache, generation/cancellation ID và cell lease.
- Gameplay readiness của cell phải hoàn tất trước presentation readiness; entity qua cell không được destroy/recreate.
- `MapDefinition` phải chứa terrain tile index, water/coastline, POI/compound, road graph, building placement, cover, loot/vehicle/dock, navigation/connectivity và validation rules.
- Map bake CI phải chạy route, connectivity, sightline, terrain seam, water, collision, visibility và cell-budget validators trước khi ký manifest.
- `WaterVolume` phải cung cấp gameplay surface, depth, swimming và buoyancy giản lược; visual wave desktop/mobile không được thay gameplay surface.
- Building phải tách gameplay shell/collision/opening khỏi desktop/mobile visual variant và có automated parity test.
- Asset từ `prepare-asset/` là quarantine, không được Godot import hoặc đưa vào manifest trước provenance/license/naming/scale/topology/LOD/collision review.
- Prototype Survivor trong Epic 1 dùng nhân vật `Regular` của Quaternius Universal Base Characters cùng Universal Animation Library/Universal Animation Library 2 (CC0) làm placeholder có kiểm soát; phải pin URL tải, ngày lấy, file gốc, license và checksum trước khi promote. Nhân vật production về sau phải giữ humanoid skeleton/animation contract tương thích hoặc đi qua migration story riêng.
- Animation nhân vật chỉ là presentation: custom authoritative `CharacterMotor` và gameplay state chạy ở fixed 30 Hz; không dùng root motion cho walk/run/sprint/swim. `AnimationTree` phải có locomotion BlendSpace, state machine stand/crouch/prone/air/vault/swim/dive, upper-body bone-filter layer cho ADS/weapon/reload và procedural lean/aim pitch. Vault/dive clip thiếu được author trong Blender trên cùng skeleton nhưng không sở hữu trajectory gameplay.
- Asset intake ngày 2026-07-26 ghi nhận `prepare-asset/audio/` có 2.072 file (~105 MB: 1.926 OGG, 85 MP3, 61 WAV), snapshot fingerprint `29983680d0cfb1c4bdebad0fd9ce1624fea23efe60264ba4f1d7727455e3cd23`; chưa tìm thấy license/provenance/manifest nên toàn bộ vẫn ở quarantine.
- Âm thanh mới phải được phân loại và chỉ promote theo allowlist: movement/footstep/swim/UI cho Epic 1, weapon/impact/shell/explosion cho Epic 2, vehicle/ambience cho Epic 5 và final mix/music/control cho Epic 8. Monster/zombie, character VO, cutscene, event-specific music và file không rõ nghĩa bị loại khỏi Standard baseline trừ khi có quyết định content cùng provenance riêng.
- Asset intake ngày 2026-07-26 ghi nhận `prepare-asset/textures/` có 36 PNG (~16 MB, 256–1024 px; một ảnh 256×512), snapshot fingerprint `fd4a9ee367dde43271579bd0fbba8ec92d8f5735447b90a9b956be670c5b12ff`; tên hiện là opaque, tất cả có alpha và chưa có license/provenance/PBR metadata.
- Texture mới chỉ là ứng viên bề mặt đất/đá/bê tông. Trước khi dùng trong Combat Sandbox hoặc Terrain3D slice phải xác minh quyền sử dụng, mục đích alpha, seamless tiling, color space, scale texel, mobile compression, stable content ID và quan hệ albedo/normal/roughness/mask; thiếu map phải dùng material mặc định có kiểm soát thay vì suy đoán channel.
- Mỗi asset được promote phải có per-file checksum, source/author/license/retrieval date, derived-edit chain, stable content ID và owner trong asset manifest; snapshot fingerprint chỉ nhận diện đợt intake, không thay thế per-file manifest.
- Generated terrain, world, manifest và protocol file là read-only, có `generated_do_not_edit`; phải sửa source rồi regenerate.
- Authoritative và presentation entity phải được tạo qua factory riêng; không instantiate replicated entity ngoài factory.
- Chỉ pool VFX, casing, impact và UI marker khi có `reset_for_reuse()`; không pool object giữ authoritative identity khi chưa chứng minh reset.
- UI phải dùng Godot `Control`/`Container`/`Theme`, presenter và immutable `ViewState`; widget không đọc packet, authoritative entity hoặc backend SDK trực tiếp.
- Desktop và mobile dùng chung presenter/state nhưng layout composition khác; safe area, Touch editor và interruption state thuộc presentation/platform layer.
- Platform service phải nằm sau typed ports cho identity, entitlement, invite, voice permission, app lifecycle, secure storage và build info.
- Platform token phải đổi thành internal `AccountId`; gameplay không được dùng Apple/Google/store ID trực tiếp.
- Input-family claim phải do control plane ký, match server xác minh, khóa suốt trận và ghi mixed disclosure vào ready/evidence state.
- EOS Voice là provider ưu tiên nhưng chỉ được promote sau five-platform spike, pin version/checksum/license provenance và contract qua `VoiceProvider`; trước đó dùng `UnsupportedVoiceAdapter` hoặc test double.
- Voice không được đi qua game transport; provider không được truy cập gameplay state hoặc signing secret.
- Nakama `3.40.0` và Nakama Common `1.47.0` phải làm control plane cho account, party, queue, profile/statistics và report/block; Nakama realtime socket không mang combat snapshot.
- Nakama Godot SDK `3.4.0` phải được bọc adapter và contract test trước khi sử dụng.
- CockroachDB `26.2.3` phải lưu account link, profile, statistics, audit và idempotent match result; live match state nằm trong RAM match server.
- `MatchAllocator` riêng phải cấp một Linux headless process/pod cho mỗi trận qua Agones `1.59.0` trên Kubernetes `1.35.6`.
- Server chỉ nhận allocation secret ngắn hạn, không nhận database credential; local/CI và production phải dùng cùng server artifact.
- Match result persistence phải dùng idempotency key, payload hash và precondition/version; cùng command ID với payload khác là security error.
- Local `ConfigFile` chỉ lưu graphics, audio, accessibility và input preference; session/reconnect token dùng secure storage; local file không có authority với profile/result.
- Evidence Event Spine phải ghi committed domain events có tick, sequence, stable type ID và schema version, cộng checkpoint định kỳ.
- Evidence replay tối thiểu phải bao phủ shot, damage, loot, zone và result; presentation/speculative event không được đi vào evidence.
- Report phải liên kết match ID, player ID và evidence window; block không thay đổi kết quả trận.
- Structured logging phải đi qua `GameLog` dưới dạng JSON có build/trace/match/tick/region/account hash; cấm `print()`/`printerr()` trong production code ngoài bootstrap logger.
- Hot path dùng counter/histogram thay vì per-frame/per-entity log; DEBUG/TRACE phải gated và có bounded duration.
- Error handling phải dùng typed result: Rejected, Recoverable, Match-critical hoặc Process-fatal; authority/protocol/content failure phải fail-closed.
- Config phải chia build identity, gameplay data, platform profile, player settings và operations config, mỗi lớp có schema/version/range/default.
- Remote operations config chỉ được tắt queue, region hoặc provider lỗi với trạng thái rõ; không được đổi damage, recoil, loot, bo, pool policy hoặc bot count.
- Communication chỉ dùng direct typed call, Godot signal local/presentation và deterministic domain-event queue; không dùng global string event bus.
- Gameplay dùng `ServerTick`, timeout local dùng monotonic clock, UTC chỉ dùng cho log/certificate/retention/operations.
- Loot, vehicle, zone và weather phải dùng random stream riêng theo purpose ID.
- Main thread sở hữu SceneTree, Node lifecycle và Jolt; worker chỉ xử lý immutable/ownership-transfer DTO, IO, decompress, decode hoặc validation và không giữ Node reference.
- Mỗi subsystem phải có typed public interface, owner/lifecycle, error contract, structured logs, metrics, config validation, test seam/failure injection, cleanup, security/privacy classification, debug path và authority declaration.
- Bắt buộc cung cấp debug registry có permission cùng overlay/inspector cho network, tick, bandwidth, relevance, streaming, terrain, TPP visibility, projectile/lag compensation, vehicle, water, audio, input family và evidence.
- Development tools chỉ hoạt động trong debug build với `--dev-tools`; production client không được gửi cheat command, server operator command phải có auth/permission/audit.
- Test phải nằm trong `game/tests/{unit,integration,deterministic,fixtures,golden}` và các harness tương ứng cho replay, impairment, server load, map và device.
- Shared simulation unit test không được cần renderer, UI, platform SDK, socket thật hoặc backend live.
- Protocol codec phải có golden byte fixtures, round-trip test và fuzz malformed/untrusted packet.
- Bug hit registration, desync hoặc match result phải có evidence/replay fixture tái hiện trước khi sửa.
- Static checks phải chặn direct `print()`, platform SDK ngoài adapter, arbitrary asset path, generated edits, spawn ngoài factory và client authority.
- CI phải build Windows, Linux, macOS Universal 2, Android ARM64 AAB, iOS archive và Linux headless server bằng version/checksum đã pin.
- Apple signing/notarization/TestFlight phải chạy trên isolated macOS runner; signing asset và production secret nằm ngoài repository, artifact log, prompt và MCP.
- Dependency phải có version, license, checksum, wrapper và owner; build phải tạo SBOM.
- Plugin/GDExtension/native module mới chỉ được promote sau profiling hoặc spike, ADR và desktop/Android/iOS/macOS build-parity gate.
- Production rollout có thể hỗ trợ backend N/N-1 nhưng không được trộn client có protocol/content không tương thích trong cùng trận.
- Observability phải liên kết `trace_id`, `match_id`, `account_id_hash`, `build_id` và region, đồng thời thu tick time, relevance count, snapshot bytes, correction, hit validation, streaming hitch, memory và thermal metrics.
- Retention baseline: operational logs 30 ngày, crash 90 ngày, raw telemetry 90 ngày, aggregated non-PII 13 tháng, unreported evidence 30 ngày và reported evidence 180 ngày hoặc tới khi case đóng; raw voice không được ghi/lưu.
- Luồng xóa account mục tiêu phải hoàn tất trong 30 ngày trừ legal/security hold được ghi nhận; optional analytics phải tách khỏi essential operations.
- Bốn spike bắt buộc trước production content lock là Network Arena, World Streaming Slice, Mobile Device Slice và Water & Boat Slice.
- Chuỗi world/content gate bắt buộc là 0,5 km² Combat Sandbox → 2×2 km slice → 8×8 km greybox → 100-client/mobile gate → khóa 18 POI/420 building.
- Backlog phải có một story khởi tạo đầu tiên sở hữu `game/project.godot`, domain structure, test/import baseline, export presets và five-platform smoke; full signing/release pipeline vẫn thuộc giai đoạn release.
- FR20 về swimming/diving phải có story sở hữu ground↔swim↔dive state, tốc độ 2,0 m/s, weapon lock, breath/HP, camera/input, `WaterVolume` và authoritative replication trước slice 2×2 km.
- Các capability quá lớn phải được tách thành story độc lập: protocol foundation, match host, headless-client harness, authority theo domain, lag compensation, terrain/coast/hydrology, POI/road graph, modular building/validator, scale gates 24/50/100, platform build/sign/certification và device-test families.
- Story không được chứa deliverable phụ thuộc future Epic. Epic world ban đầu chỉ giao modular kit, hai POI đại diện và validator; full 18 POI/420 building expansion chỉ bắt đầu sau scale/mobile gate.
- Product/business decision về giá phát hành và chi phí máy chủ phải nằm trong product/operations decision backlog, không được tính là player story hoặc story velocity.
- Mỗi story chi tiết phải có `Source Requirements` truy vết FR/NFR/UX/ADR, actor/outcome, `Depends on`, `Blocks`, module/file ownership, Given/When/Then AC, error/recovery path, test boundary, platform applicability và Definition of Done.
- Story reconnect chưa được Ready cho tới khi ADR/policy khóa owner API, reconnect grace theo match phase, AFK neutral input, avatar vulnerability/outcome, token expiry/rotation và các destination `Restored/Timed out/Team eliminated/Match ended`.
- Story input/remap phải khóa raw-mouse choice, physical-vs-logical key policy, localized OS key labels, non-QWERTY/Linux display-name behavior, required escape bindings và atomic Apply/Cancel persistence.
- Story Map phải khóa orientation mặc định và zoom limits trước implementation; các lựa chọn không được đổi damage cue world-camera-relative hoặc information range giữa platform.
- Story spectator phải khóa quyền voice/ping sau elimination; mặc định spectator không được tạo marker chiến thuật mới và mọi voice còn lại chỉ được hoạt động trong team-information parity.
- Trước E7 refinement phải ghi quyết định v1/deferred cùng risk/owner cho screen reader/menu narration, extended subtitle controls, motor/hearing playtest và professional photosensitivity scope.
- Localization/font phải là story có owner trước production UI, bao phủ locale Việt/Anh, catalog, plural/date/number policy, Noto license/provenance, SDF/raster/fallback metrics và five-platform text snapshot.
- Invite provider, deep report taxonomy/evidence attachment/moderation SLA và deep replay payload không chặn Combat Sandbox nhưng phải có API/schema/retention/security contract trước story sở hữu tương ứng.

### UX Design Requirements

UX-DR1: Xây Godot Theme dùng đầy đủ token màu, typography, spacing, radius và component constants trong `DESIGN.md`; không hard-code style phân tán trong scene.

UX-DR2: Triển khai palette Field Instrument charcoal–olive–bone với amber cho attention/focus, cyan cho zone/team, rust-red cho danger và green-muted cho success; không dùng neon, glassmorphism, gradient bóng hoặc chrome trang trí dày.

UX-DR3: Mọi text-bearing backplate phải dùng `surface-overlay` tối thiểu 92% opacity hoặc local solid backplate nếu compositing không đạt contrast.

UX-DR4: Mọi trạng thái gameplay quan trọng phải dùng color + icon/shape/label; `signal-danger` và `signal-success` không được là tín hiệu duy nhất.

UX-DR5: Triển khai ba preset Protanopia, Deuteranopia và Tritanopia bằng token swap cho zone, teammate marker, hit effect và reticle, giữ nguyên geometry, timing, identity number và line style.

UX-DR6: Ship Noto Sans, Noto Sans Condensed và Noto Sans Mono cùng Unicode fallback có x-height tương thích; xác minh dấu tiếng Việt, tiếng Anh dài và missing-glyph trên cả năm nền tảng.

UX-DR7: Typography phải giữ text tối thiểu 12 px, gameplay label tối thiểu 14 px và số critical tối thiểu 18 px ở mọi UI scale 80–140%; keycap phải co giãn 32–96 px mà không thu nhỏ font dưới minimum.

UX-DR8: Chuẩn hóa central competitive frame 16:9 lớn nhất vừa viewport; HUD và live-world Standard nằm trong frame, ultrawide side area chỉ chứa matte/chrome không tương tác.

UX-DR9: Triển khai Compact 1280–1599 px, Base 1600–2559 px và Large ≥2560 px bằng anchors/containers; co spacing trước, không giảm text dưới token minimum.

UX-DR10: Thực hiện acceptance responsive desktop tại sáu resolution và UI scale 80/100/140%, bảo đảm không crop critical module, focus ring, subtitle, reticle hoặc close binding.

UX-DR11: Lobby phải có navigation dọc trái, world scene trung tâm, `party-panel` và Deploy bên phải; không có news, store, reward rail hoặc event carousel.

UX-DR12: `match-hud` phải giữ sáu module neo ổn định: `compass`, `squad-panel`, `health-boost-bar`, `minimap-zone-panel`, `weapon-ammo-panel` và `reticle`; đúng bảy nhóm dữ liệu persistent, không thêm feed thương mại.

UX-DR13: Triển khai overlay lane/collision và priority P0–P3: lethal/immediate, active commitment, match/system và contextual; sáu module persistent không được bị overlay che.

UX-DR14: Áp dụng z-order world 0 → HUD 10 → Inventory/Map 20 → contextual 30 → critical 40 → Pause/confirm 50 → blocking modal 60; không xếp quá một modal.

UX-DR15: `compass`, teammate world marker, `squad-panel`, `party-panel` và `map-marker-layer` phải dùng identity cố định Circle/1, Square/2, Triangle/3, Diamond/4.

UX-DR16: `reticle` phải có bốn arm 8 px, center gap 6 px, stroke 2 px và outline 1 px ở 100% scale; ADS sight/scope tiếp quản, hit confirm chỉ sau server confirmation và không có lock/lead/range/damage cue.

UX-DR17: `damage-direction-indicator` phải dùng cung 30° ngắn; trên Map vẫn screen-relative theo world camera tại thời điểm hit, xếp nhiều hit theo recency và không tạo radar lịch sử.

UX-DR18: `status-banner` và `network-warning` phải có icon + label + severity, giới hạn một critical banner cùng lúc; network warning xuất hiện khi ping >150 ms hoặc cần xác nhận và không che combat.

UX-DR19: `context-prompt` phải lấy binding hiện hành, dùng động từ trước đối tượng và chỉ hiện khi action hợp lệ; context arbitration phải ưu tiên DBNO assist → vehicle safety/exit → traversal/vehicle enter → pickup và luôn cho truy cập action phụ.

UX-DR20: `context-action-card` phải dùng anatomy chung cho heal, revive, throwable, scope/breath, armor break và vehicle; vehicle card hiển thị fuel, HP, bốn lốp và fire countdown 3 giây.

UX-DR21: `progress-timer` phải bám server state, không chạy tới 100% giả; interruption phải có icon, label và lý do ngắn.

UX-DR22: Desktop `inventory-panel` phải dùng bố cục 34% Nearby/Backpack — 32% world strip — 34% Weapons/Equipment tại 1920×1080 và luôn giữ tổng panel ≤68%.

UX-DR23: Mobile Inventory phải là panel tabbed Nearby/Backpack/Equipment rộng ≤62%, giữ world strip ≥38%, tap/action menu là đường chính và drag chỉ là shortcut.

UX-DR24: `item-row` phải hiển thị icon/hình hộp, tên, số lượng và khối lượng; ammo/rarity không chỉ dùng màu; lỗi sức chứa giữ item tại nguồn và focus.

UX-DR25: `equipment-slot` phải hiển thị slot silhouette, tier label, durability current/max, bar và broken icon; >50% neutral, 1–50% attention + notch, 0 danger + BROKEN/crosshatch.

UX-DR26: Map/Phase phải có header trên trái, phase/timer trên phải, legend dưới trái và binding dưới phải; current zone nét liền, next zone nét đứt chỉ sau server reveal.

UX-DR27: `map-marker-layer` phải hỗ trợ pan, zoom, đặt/xóa marker, place name, flight path và team marker; không loot, enemy, sound-source marker hoặc zone prediction.

UX-DR28: Mobile Map phải hỗ trợ one-finger pan, pinch zoom, tap marker và long-press radial; nút close 64 units luôn trong safe area, damage không tự đóng Map.

UX-DR29: `party-panel` phải hiển thị 1–4 người, leader, Ready, reconnect, network, voice và input family; thay roster/mode/region/pool phải clear Ready và mixed disclosure cần acknowledgement.

UX-DR30: `voice-ping-indicator` phải hỗ trợ team voice và tám intent `Đi tới`, `Nguy hiểm`, `Địch nhìn thấy`, `Loot ở đây`, `Cần vật tư`, `Giữ vị trí`, `Tập hợp`, `Phương tiện` với TTL/cooldown đã khóa và không auto-track địch.

UX-DR31: `results-table` phải ưu tiên placement, survival time, kills/assists và dữ liệu tự cải thiện; Pending/Unavailable phải là state rõ, không dùng celebration/reward loop.

UX-DR32: Xây `action-button`, `navigation-item` và `focus-ring` với keyboard/pointer parity, active route duy nhất, disabled reason và focus ring 2 px không bị crop.

UX-DR33: `settings-control` phải stage thay đổi, phát hiện conflict theo active context, Apply atomically, Cancel rollback, persist qua restart và xác nhận Reset category/Reset All.

UX-DR34: Remap phải hỗ trợ primary + secondary cho toàn bộ action gameplay tối thiểu trong UX-027, giữ đường keyboard/mouse cho `ui_accept`, `ui_cancel`, Pause, Inventory-close và Map-close.

UX-DR35: Input routing khi Inventory, Map hoặc Pause mở phải chặn click-through, trung hòa action bị chặn và yêu cầu key/pointer release trước re-arm đúng matrix UX-026.

UX-DR36: Focus lifecycle phải đặt focus xác định khi mở từng surface/modal, chuyển tới sibling gần nhất khi item biến mất, trả focus cho caller khi đóng và bảo đảm `ui_cancel` thoát một cấp.

UX-DR37: `subtitle-line` phải hỗ trợ speaker/identity, tối đa hai dòng, nền ≥92%, max width 60%, queue/preemption/no-drop và coalesce message lặp; không che reticle, prompt, progress, HP hoặc ammo.

UX-DR38: `safe-area-root` phải đọc OS inset tại launch, rotate/resume/display change, giữ critical controls trong boundary và fallback preset an toàn khi layout lưu không hợp lệ.

UX-DR39: `touch-stick` phải có base 96 px, thumb 48 px, pointer ownership, dead zone và cancel khi finger-up hoặc OS interruption.

UX-DR40: `touch-look-zone` phải chiếm tối thiểu 40% chiều ngang phải, trong suốt ở production, tách pointer ID và không cướp fire/action hoặc tự bắn/ADS khi tap.

UX-DR41: `touch-action-button` phải có target thường ≥48, fire/exit/close ≥64 khi safe area cho phép, phát semantic press/release, hỗ trợ hold/toggle và không để stuck action khi interruption.

UX-DR42: `control-layout-editor` phải có grid 8 px, handle ≥48 px, preview phone/tablet + safe area, chỉnh vị trí/kích thước/opacity, Apply/Cancel/Reset và chặn overlap làm mất fire/exit/close/Pause.

UX-DR43: Mobile HUD phải giữ reticle ở tâm live world trên phone 20:9, phone 16:9 và tablet 4:3, hỗ trợ notch/gesture/left-handed layout mà không che central aim corridor.

UX-DR44: IA phải giữ launch → Deploy tối đa ba hành động và mỗi surface chỉ sâu một cấp từ bề mặt mẹ; modal xác nhận không được xếp chồng.

UX-DR45: Reconnect UI phải phản ánh đúng owner party/ticket/seat/live match, trung hòa held command/PTT, giữ cùng identity/token và chỉ chuyển tới state do server/backend trả về.

UX-DR46: Spectator phải chỉ follow teammate còn sống, không free camera; HUD, map, damage cue và audio chỉ phản ánh thông tin hợp lệ của target, không cho inventory riêng hoặc marker bí mật.

UX-DR47: Report/Block phải có draft retention khi offline, receipt/retry và block local tách biệt; microcopy phải trung tính, ngắn, có số liệu và không kết tội trước evidence.

UX-DR48: Field Orientation phải cho Start/Skip/Continue/Restart, lưu checkpoint gần nhất cục bộ, hoàn tất hoặc bỏ qua đều về Lobby và không tạo reward funnel.

UX-DR49: Audio UI phải giữ World bus theo tỷ lệ cố định, không có footstep boost/EQ chiến thuật; HRTF theo world camera trên HUD/Inventory/Map/Pause và spectator theo target.

UX-DR50: Motion phải dùng fade/slide 120–180 ms, contextual fade-out ≤120 ms, translation ≤12 px; Reduce Motion chuyển sang opacity/state swap ≤100 ms và Reduce Flash dùng icon/backplate tĩnh.

UX-DR51: UI phải hỗ trợ color contrast, full keyboard navigation, Touch tap fallback, UI scale, hold/toggle, FOV, Gyro, haptic, camera shake, flash, blood/hit-color và system/ping subtitles theo Accessibility Floor.

UX-DR52: Voice permission chỉ được hỏi theo ngữ cảnh; denial không lặp prompt, audio-route change không bật PTT và interruption không làm mất world-state cue bắt buộc.

UX-DR53: Mọi chuỗi UI phải qua localization Việt/Anh; gameplay-critical label không ellipsis, label dài reflow/alias có tooltip hoặc accessible label thay vì giảm font.

UX-DR54: Pause phải không pause server/world audio, focus Resume, xác nhận Leave với hậu quả đúng trạng thái và không gắn cảnh báo thất bại sau khi đội đã bị loại.

UX-DR55: Offline Lobby phải disable Deploy nhưng giữ Training/Settings; queue timeout/error phải về Lobby với nguyên nhân, không tự đổi region/mode/pool/trận.

UX-DR56: Không surface nào được thêm store/news/reward rail, red badge, countdown FOMO, kill-feed dày, damage number, footstep radar, loot score, enemy outline hoặc live-service celebration.

### FR Coverage Map

FR1: Epic 4 — Luật Standard battle royale 100 người và điều kiện sống cuối.
FR2: Epic 4 — Chọn Solo/Duo/Squad trước hàng chờ.
FR3: Epic 4 — Vòng đời đầy đủ từ chuẩn bị tới kết quả.
FR4: Epic 4 — Sảnh chờ, máy bay và đổ bộ.
FR5: Epic 4 — Elimination Solo và DBNO theo đội.
FR6: Epic 4 — Điều kiện thắng Duo/Squad.
FR7: Epic 4 — Hậu quả rời trận theo trạng thái đội.
FR8: Epic 4 — Spectate đồng đội còn sống.
FR9: Epic 4 — Không hồi sinh/mua lại/tự cứu trong Standard.
FR10: Epic 4 — Kết quả trận do máy chủ xác nhận.
FR11: Epic 4 — Play Again, Lobby và lối vào Report/Block từ Results.
FR12: Epic 4 — Thời lượng và kết thúc sớm của trận.
FR13: Epic 1 — Gameplay/data/content manifest chung trên năm nền tảng.
FR14: Epic 1 — Các trạng thái di chuyển và tư thế cơ bản.
FR15: Epic 1 — Sprint weapon-lock và ready delay.
FR16: Epic 1 — Jump limit, recovery và airborne ADS lock.
FR17: Epic 1 — Vault range, timing, weapon-lock và audio.
FR18: Epic 1 — Lean angle, transition và movement modifier.
FR19: Epic 1 — Fall damage.
FR20: Epic 1 — Swimming/diving, weapon-lock và breath/HP.
FR21: Epic 1 — Movement trade-off không stamina.
FR22: Epic 1 — Semantic `GameplayCommand`.
FR23: Epic 1 — Keyboard/Mouse bindings.
FR24: Epic 1 — Touch landscape controls.
FR25: Epic 2 — Health baseline.
FR26: Epic 2 — Hit-region damage modifiers.
FR27: Epic 2 — Body armor reduction/durability.
FR28: Epic 2 — Helmet reduction/durability.
FR29: Epic 2 — Armor-break damage ordering.
FR30: Epic 3 — Healing và boost actions.
FR31: Epic 4 — DBNO bleed state.
FR32: Epic 4 — Revive timing và interruption.
FR33: Epic 4 — DBNO movement/action restrictions.
FR34: Epic 3 — Equipment slots.
FR35: Epic 3 — Body/backpack capacity.
FR36: Epic 3 — Capacity cost và attached-item rule.
FR37: Epic 3 — Server-confirmed hold actions và interruption reason.
FR38: Epic 3 — Weighted loot generation.
FR39: Epic 3 — Empty start/no loadout.
FR40: Epic 3 — Quick pickup và inventory mutations.
FR41: Epic 3 — Invalid inventory mutation rejection.
FR42: Epic 3 — Không auto-pick weapon/armor/attachment.
FR43: Epic 3 — Bounded ammo auto-pickup.
FR44: Epic 3 — 90-second loot-availability targets.
FR45: Epic 3 — Loot geography.
FR46: Epic 3 — Airdrop schedule, visibility và contents.
FR47: Epic 3 — Không essential item độc quyền airdrop.
FR48: Epic 3 — Throwable capacity.
FR49: Epic 3 — Bốn throwable archetype.
FR50: Epic 3 — Throwable trajectory-preview limit.
FR51: Epic 5 — Sáu vehicle archetype.
FR52: Epic 5 — Vehicle speed/fuel/HP/tire/audio states.
FR53: Epic 5 — Vehicle fire countdown và post-exit cue.
FR54: Epic 5 — Vehicle collision damage.
FR55: Epic 5 — Server-authoritative vehicle damage/explosion.
FR56: Epic 1 — TPP hip-fire/over-shoulder/shoulder-swap/ADS camera.
FR57: Epic 1 — Camera collision và head-line-of-sight anti-peek.
FR58: Epic 1 — Full remap, Touch layout, sensitivity và hold/toggle.
FR59: Epic 2 — Weapon roster.
FR60: Epic 2 — Ammo caliber identities.
FR61: Epic 2 — Attachment roster và slot validity.
FR62: Epic 2 — Weapon-archetype balance baselines.
FR63: Epic 2 — Projectile ballistics/no primary hitscan.
FR64: Epic 2 — Recoil progression/recovery và spread modifiers.
FR65: Epic 2 — Breath-hold và zeroing.
FR66: Epic 2 — Aim punch.
FR67: Epic 2 — Melee baseline.
FR68: Epic 2 — Shot presentation feedback.
FR69: Epic 2 — Hit feedback/no floating damage.
FR70: Epic 2 — Server-confirmed combat feedback và hit trade.
FR71: Epic 2 — Authoritative movement/combat/inventory/loot/vehicle/zone/result contract, khởi đầu ở Combat Sandbox và được harden ở Epic 6/10.
FR72: Epic 2 — Prediction/reconciliation boundary.
FR73: Epic 2 — Bounded lag compensation.
FR74: Epic 6 — High-latency warning và region confirmation.
FR75: Epic 6 — Region/wait-time/newcomer matchmaking.
FR76: Epic 6 — Touch/Keyboard-Mouse/Mixed pools và disclosure.
FR77: Epic 6 — Match-locked input family và requeue.
FR78: Epic 6 — Không silent bots/pool switch/fairness relaxation.
FR79: Epic 6 — Experimental bot disclosure.
FR80: Epic 6 — Party, leader, Ready, invite và reconnect.
FR81: Epic 6 — Team voice và tám contextual pings.
FR82: Epic 6 — Friendly fire và Report/Block entry.
FR83: Epic 7 — Đảo Vọng 8×8 km và production content targets sau gate.
FR84: Epic 5 — Open-space traversal alternatives, được mở rộng toàn map ở Epic 7.
FR85: Epic 5 — Choke và bypass rules, được mở rộng toàn map ở Epic 7.
FR86: Epic 5 — Final-circle land-playability, được mở rộng toàn map ở Epic 7.
FR87: Epic 5 — Match seed không sinh runtime geometry.
FR88: Epic 5 — Weather selection.
FR89: Epic 5 — Rain/fog gameplay behavior.
FR90: Epic 4 — Nine-phase safe-zone schedule.
FR91: Epic 4 — Next-zone reveal và no forecast/bombing zone.
FR92: Epic 9 — Non-power profile statistics.
FR93: Epic 9 — Weapon Mastery không power/skin.
FR94: Epic 8 — Training Grounds.
FR95: Epic 8 — Optional Field Orientation.
FR96: Epic 9 — Không storefront/FOMO/live-event trong v1.
FR97: Epic 8 — Minimal commercial-free match HUD.
FR98: Epic 8 — Map information contract.
FR99: Epic 8 — Non-pausing desktop/mobile Inventory và world-risk strip.
FR100: Epic 8 — Graphics/audio/accessibility/language/input settings.
FR101: Epic 8 — Color-blind presets và redundant encoding.
FR102: Epic 8 — System/ping subtitles và no visual footstep radar.
FR103: Epic 8 — Contextual voice permission và interruption safety.
FR104: Epic 8 — Audio output/control contract.
FR105: Epic 8 — Music timing.
FR106: Epic 9 — Server-confirmed Results/Replay Summary states.
FR107: Epic 9 — Report MVP.
FR108: Epic 9 — Local Block tách khỏi Report.
FR109: Epic 6 — Mobile interruption/reconnect state machine, được harden ở Epic 10.
FR110: Epic 6 — Explicit platform/provider degraded state, được harden ở Epic 10.

## Epic List

### Epic 1: Người sống sót đầu tiên trên năm nền tảng

Người chơi có thể khởi động bản build sạch, điều khiển nhân vật bằng Keyboard/Mouse hoặc Touch, di chuyển, đổi tư thế, bơi/lặn, tương tác và sử dụng camera TPP/ADS công bằng.

**FRs covered:** FR13–FR24, FR56–FR58  
**Natural dependencies:** Không.

### Epic 2: Đấu súng có thể tin cậy

Người chơi có thể bắn, nhận sát thương và hiểu kết quả giao tranh trong Combat Sandbox tối đa 8 client, với projectile, recoil, giáp, authority, prediction và lag compensation đúng contract.

**FRs covered:** FR25–FR29, FR59–FR73  
**Natural dependencies:** Epic 1.

### Epic 3: Loot và quản trị tài nguyên sinh tồn

Người chơi có thể bắt đầu tay trắng, nhặt và quản lý vũ khí, đạn, giáp, hồi máu, sức chứa và vật ném với mọi mutation được máy chủ xác nhận.

**FRs covered:** FR30, FR34–FR50  
**Natural dependencies:** Epic 1–2.

### Epic 4: Một trận battle royale hoàn chỉnh

Người chơi có thể trải qua vòng lặp từ lobby thử nghiệm, máy bay, đổ bộ, loot, DBNO, chín pha bo, spectate đến kết quả trong một match host hoàn chỉnh.

**FRs covered:** FR1–FR12, FR31–FR33, FR90–FR91  
**Natural dependencies:** Epic 1–3.

### Epic 5: World/Vehicle Slice 2×2 km

Người chơi có thể đi bộ, bơi và lái phương tiện qua một lát cắt gồm POI dày, compound thưa, đường, cầu, bờ biển và thời tiết mà không gặp lỗi streaming hoặc gameplay parity.

**FRs covered:** FR51–FR55, FR84–FR89  
**Natural dependencies:** Epic 1, Epic 3–4.

### Epic 6: Trận đấu online cạnh tranh đa nền tảng

Người chơi có thể lập party, chọn vùng/input pool, vào trận qua matchmaking, voice/ping, reconnect và chơi ở các cổng 24→50→100 client với authority, evidence và fairness đầy đủ.

**FRs covered:** FR74–FR82, FR109–FR110; harden FR71–FR73.  
**Natural dependencies:** Epic 1–5.

### Epic 7: Đảo Vọng ở quy mô sản xuất

Sau khi scale/mobile gate đạt, người chơi có thể khám phá bản đồ 8×8 km hoàn chỉnh với 18 POI, 55 compound, mục tiêu 420 công trình, route và content parity được kiểm định.

**FRs covered:** FR83; mở rộng và chứng minh FR84–FR89 ở quy mô đầy đủ.  
**Natural dependencies:** Epic 5–6.

### Epic 8: Trải nghiệm rõ ràng và tiếp cận trên mọi thiết bị

Người chơi có HUD, Inventory, Map, audio, localization, accessibility, Touch layout, Training Grounds và Field Orientation nhất quán trên desktop/mobile.

**FRs covered:** FR94–FR105.  
**Natural dependencies:** Các hệ thống gameplay liên quan trong Epic 1–7.

### Epic 9: Hồ sơ và tính toàn vẹn sản phẩm

Người chơi có hồ sơ, mastery không tăng sức mạnh, Results/Replay Summary, Report/Block và một sản phẩm không storefront, FOMO hoặc pay-to-win.

**FRs covered:** FR92–FR93, FR96, FR106–FR108.  
**Natural dependencies:** Epic 4, Epic 6 và Epic 8.

### Epic 10: Bản phát hành ổn định trên năm nền tảng

Người chơi nhận được các bản build tương thích, an toàn và đạt performance/reliability trên Windows, Linux, macOS, Android và iOS; Linux headless server có thể vận hành và rollback.

**FRs hardened:** FR13, FR71, FR109–FR110.  
**NFR focus:** NFR4–NFR55.  
**Natural dependencies:** Epic 1–9.

## Epic 1: Người sống sót đầu tiên trên năm nền tảng

Người chơi có thể khởi động bản build sạch, điều khiển nhân vật bằng Keyboard/Mouse hoặc Touch, di chuyển, đổi tư thế, bơi/lặn, tương tác và sử dụng camera TPP/ADS công bằng.

### Story 1.1: Khởi tạo Godot Standard và build smoke trên năm nền tảng

As a người chơi,
I want OutSurvive khởi động ổn định trên nền tảng được hỗ trợ,
So that tôi có thể bước vào cùng một gameplay baseline bất kể thiết bị.

**Source Requirements:** FR13; NFR31, NFR49, NFR55; Architecture scaffold và asset-quarantine contract.

**Depends on:** Không.

**Blocks:** Story 1.2–1.13 và mọi Epic sau.

**Module/File Ownership:** `game/project.godot`, `game/export_presets.cfg`, bootstrap/kernel, test baseline và cấu trúc monorepo.

**Platform Applicability:** Windows, Linux, macOS, Android, iOS và Linux headless server.

**Acceptance Criteria:**

**Given** repository chưa có dự án gameplay  
**When** scaffold được tạo  
**Then** phải dùng Godot Standard `4.7.1-stable`, typed GDScript và export template có checksum đã pin  
**And** không dùng starter kit hoặc framework gameplay bên thứ ba.

**Given** scaffold hoàn tất  
**When** kiểm tra cấu trúc repository  
**Then** phải có boundary cho `game`, `native`, `backend`, `infrastructure`, `content-source`, `prepare-asset`, `test-harness` và `docs`  
**And** `shared` không được phụ thuộc client, server, UI, renderer, platform SDK hoặc backend implementation.

**Given** một client build được khởi động  
**When** bootstrap chạy  
**Then** smoke scene phải hiển thị `build_id`, engine version, platform family và lifecycle state  
**And** khởi động, đóng ứng dụng sạch mà không cần backend hoặc network live.

**Given** export toolchain hợp lệ  
**When** chạy build matrix  
**Then** phải tạo được Windows x64, Linux x64, macOS Universal 2, Android ARM64, iOS ARM64 và Linux headless artifacts  
**And** desktop/mobile development builds phải có launch-smoke evidence; full release signing vẫn thuộc Epic 10.

**Given** version, SDK hoặc export template sai  
**When** build/import được chạy  
**Then** pipeline phải fail-closed với mã lỗi rõ ràng  
**And** không đánh dấu artifact dở dang là hợp lệ.

**Given** asset đang nằm trong `prepare-asset/`  
**When** Godot headless import chạy  
**Then** character, audio, texture, model và weapon quarantine không được tự động import hoặc xuất hiện trong content manifest  
**And** chỉ asset qua promotion manifest mới được dùng từ Story 1.2 trở đi.

**Given** clean workspace  
**When** chạy headless import, unit smoke, boundary checks và build smoke  
**Then** tất cả phải thành công không cần MCP, không chứa secret và không dùng `print()` trong production code  
**And** kết quả lưu kèm build ID, platform và checksum artifact.

**Error/Recovery Path:** Toolchain, SDK hoặc checksum mismatch phải trả typed failure, xóa/không publish artifact chưa hoàn chỉnh và giữ log không chứa secret để có thể sửa cấu hình rồi chạy lại.

**Test Boundary:** Headless import smoke, bootstrap unit/integration test, dependency-boundary static check, export-preset validation và launch-smoke evidence cho từng platform family.

**Definition of Done:** Clean checkout tái tạo được scaffold; các test/gate trên đạt; version/checksum và artifact evidence được lưu; không có quarantine asset, generated cache hoặc secret lọt vào runtime/source control.

### Story 1.2: Prototype Survivor, humanoid rig và animation contract

As a người chơi,
I want nhân vật phản ánh rõ tư thế và trạng thái vận động,
So that tôi có thể đọc chính xác hành động của mình và đối thủ trên mọi nền tảng.

**Source Requirements:** FR13; presentation slice của FR14, FR17–FR18, FR20; NFR31, NFR35, NFR49, NFR55.

**Depends on:** Story 1.1.

**Blocks:** Story 1.3–1.8 và Epic 2.

**Module/File Ownership:** `content-source/characters`, `content-source/licenses`, `game/assets/characters`, `game/src/client/presentation/characters`, `game/scenes/entities/characters`, asset validator và animation tests.

**Platform Applicability:** Cả năm client; Linux headless chỉ nhận contract/manifest, không chứa mesh hoặc animation.

**Acceptance Criteria:**

**Given** nguồn Quaternius được tải  
**When** asset được đưa qua promotion pipeline  
**Then** chỉ model `Regular` và các animation cần thiết từ Universal Animation Library/UAL2 được promote  
**And** phải lưu URL, CC0 license copy, ngày tải, archive checksum, per-file checksum và stable content ID.

**Given** Prototype Survivor được import  
**When** asset validator kiểm tra  
**Then** skeleton phải có orientation, scale, bone map, rest pose và humanoid contract ổn định  
**And** mọi clip phải retarget vào cùng skeleton mà không tạo skeleton riêng ngoài manifest.

**Given** animation library được bake  
**When** kiểm tra danh mục clip  
**Then** phải có baseline cho idle, walk, jog, sprint, crouch, prone/crawl, jump, fall, land, vault, swim và dive  
**And** clip vault/dive còn thiếu được author trong Blender trên cùng skeleton, kèm source và derived-edit record.

**Given** character presentation scene chạy  
**When** mock visual state thay đổi  
**Then** `AnimationTree` phải cung cấp locomotion 2D BlendSpace và state machine cho stand, crouch, prone, air, vault, swim và dive  
**And** transition không pop pose, kẹt state hoặc phụ thuộc gameplay story tương lai.

**Given** nhân vật aim hoặc nghiêng người  
**When** `aim_pitch` hoặc `lean_amount` thay đổi  
**Then** upper-body bone-filter/procedural layer phải cập nhật pose mà không phá locomotion chân  
**And** contract phải dành sẵn layer cho ADS, weapon action và reload của Epic 2.

**Given** animation locomotion được phát  
**When** validator đo transform của character root  
**Then** root displacement phải nằm trong tolerance tối đa 0,01 m  
**And** animation không được điều khiển vị trí authoritative, capsule, vault trajectory hoặc swimming trajectory.

**Given** cùng một presentation state và tick sequence  
**When** chạy desktop và mobile visual variants  
**Then** skeleton, clip timing, silhouette chiến đấu và attachment sockets phải tương đương  
**And** chỉ LOD, material hoặc shader quality được phép khác.

**Given** Linux headless artifact được build  
**When** kiểm tra manifest và package contents  
**Then** server chỉ chứa stable character/skeleton contract cần cho gameplay  
**And** không chứa texture, mesh, animation hoặc presentation archive.

**Given** license, checksum, skeleton hoặc animation contract không hợp lệ  
**When** promotion/import được chạy  
**Then** asset phải bị từ chối với typed validation error  
**And** placeholder cũ vẫn hoạt động thay vì xuất hiện asset hỏng hoặc mất hình.

**Error/Recovery Path:** Asset lỗi quay lại quarantine; manifest đã ký không bị sửa một phần; validator nêu chính xác file, bone, clip hoặc provenance field cần sửa.

**Test Boundary:** Provenance test, checksum test, skeleton/bone-map validation, root-motion tolerance, animation-state traversal, attachment-socket parity, headless package-content test và desktop/mobile visual smoke.

**Definition of Done:** Prototype Survivor chạy được trong animation validation scene; toàn bộ clip và license có manifest; root motion bị loại khỏi authority; desktop/mobile parity đạt; headless server không mang presentation asset.

### Story 1.3: GameplayCommand ngữ nghĩa và fixed-tick input pipeline

As a người chơi,
I want mọi thiết bị điều khiển tạo cùng một ý định gameplay,
So that luật chơi và phản hồi không thay đổi theo nền tảng.

**Source Requirements:** FR13, FR22; NFR27, NFR29, NFR31, NFR33.

**Depends on:** Story 1.1.

**Blocks:** Story 1.4–1.11 và mọi prediction/authority story.

**Module/File Ownership:** `game/src/shared/contracts`, `game/src/shared/kernel`, `game/src/client/input/semantic`, input fixtures và deterministic scheduler tests.

**Platform Applicability:** Cả năm client và Linux headless simulation.

**Acceptance Criteria:**

**Given** Keyboard/Mouse, Touch hoặc test adapter phát input  
**When** input được lấy mẫu  
**Then** adapter phải tạo typed `GameplayCommand` có player ID, sequence, target tick, semantic actions và normalized axes  
**And** shared gameplay không được đọc `Input`, keycode, pointer ID hoặc platform API trực tiếp.

**Given** command đến sớm, trễ, trùng hoặc ngoài range  
**When** fixed 30 Hz scheduler ingest  
**Then** command phải được validate, order/deduplicate và clamp/reject theo contract trước mutation  
**And** phase ingest phải có deterministic fixture chứng minh cùng command stream cho cùng kết quả.

**Given** focus mất, OS interruption hoặc adapter disconnect  
**When** input stream bị ngắt  
**Then** mọi held action và PTT phải được trung hòa bằng semantic release an toàn  
**And** action chỉ được re-arm sau một chu kỳ release hợp lệ.

**Error/Recovery Path:** Command malformed hoặc cadence bất thường bị reject có reason/metric; last safe command không được giữ vô hạn và không tạo stuck movement/fire.

**Test Boundary:** Codec/validation unit tests, device-adapter contract tests, 30 Hz deterministic fixtures, interruption/re-arm integration test và static check cấm raw device read ngoài adapter.

**Definition of Done:** Ba adapter mẫu tạo cùng command contract; scheduler ingest deterministic; invalid input fail-closed; shared simulation hoàn toàn độc lập thiết bị.

### Story 1.4: Ground locomotion và sprint trade-off

As a người chơi,
I want đi, chạy và chạy nước rút có nhịp độ rõ ràng,
So that tôi có thể đổi tốc độ lấy tiếng động và khả năng sẵn sàng chiến đấu.

**Source Requirements:** FR14–FR15, FR21–FR22; NFR15, NFR27, NFR31.

**Depends on:** Story 1.2–1.3.

**Blocks:** Story 1.5–1.7, Story 1.12 và movement authority trong Epic 2.

**Module/File Ownership:** `game/src/shared/simulation/movement`, `game/src/server/authority/movement`, character factory/scene adapter và locomotion tests.

**Platform Applicability:** Cả năm client và Linux headless server.

**Acceptance Criteria:**

**Given** movement command hợp lệ trên mặt đất  
**When** custom kinematic `CharacterMotor` chạy ở 30 Hz  
**Then** walk, run và sprint phải dùng speed/acceleration/turning từ gameplay manifest cùng slope/step rules đã khóa  
**And** Jolt chỉ cung cấp collision/query, không sở hữu movement authority.

**Given** người chơi bắt đầu sprint  
**When** sprint còn active hoặc vừa dừng  
**Then** fire phải bị khóa trong sprint và weapon-ready chỉ trở lại sau 0,35 giây  
**And** không có stamina bar, stamina drain hoặc platform-specific speed.

**Given** client dự đoán movement khác server  
**When** authoritative state được áp dụng  
**Then** canonical position/velocity/state phải đến từ server-compatible motor  
**And** presentation animation chỉ đọc visual state, không kéo physics root.

**Error/Recovery Path:** Surface/collision query bất hợp lệ giữ nhân vật ở last valid pose, ghi typed rejection và không teleport xuyên geometry.

**Test Boundary:** Speed/acceleration golden tests, slope/step fixtures, sprint lock timing, 30 Hz replay determinism và desktop/mobile command parity.

**Definition of Done:** Walk/run/sprint hoạt động trong test scene với custom motor, đúng manifest/timing, không stamina, không root-motion authority và có deterministic evidence.

### Story 1.5: Crouch, prone và lean có collision guard

As a người chơi,
I want đổi tư thế và nghiêng người quanh cover,
So that tôi có thể giảm silhouette và quan sát góc bắn với đánh đổi công bằng.

**Source Requirements:** FR14, FR18, FR22; NFR27, NFR31, NFR35.

**Depends on:** Story 1.4.

**Blocks:** Story 1.8, Story 1.12 và hitbox authority trong Epic 2.

**Module/File Ownership:** Movement stance domain, capsule/profile definitions, character presentation adapter và stance fixtures.

**Platform Applicability:** Cả năm client và Linux headless server.

**Acceptance Criteria:**

**Given** stance command hợp lệ  
**When** chuyển stand/crouch/prone  
**Then** motor phải áp dụng collider, eye height, speed và transition timing từ manifest  
**And** đứng dậy dưới trần thấp phải bị guard từ chối mà không xuyên collision.

**Given** lean trái/phải  
**When** command đạt full input  
**Then** lean tối đa 18°, vào pose trong 0,15 giây và movement còn 65%  
**And** camera, muzzle/hitbox reference và presentation phải dùng cùng authoritative lean state.

**Given** client gửi stance/lean transition không hợp lệ  
**When** server validate  
**Then** transition bị reject/correct theo sequence  
**And** animation phải blend về canonical state không pop hoặc đổi silhouette ngoài contract.

**Error/Recovery Path:** Clearance query lỗi hoặc state không tồn tại giữ stance hiện hành, trả reason và cho phép thử lại khi geometry/state hợp lệ.

**Test Boundary:** Capsule clearance fixtures, exact lean/timing tests, speed modifier, rapid-toggle fuzz và five-platform silhouette snapshot.

**Definition of Done:** Ba stance và lean chạy đúng guard/timing; collider, camera reference và animation đồng bộ; invalid transition không xuyên cover.

### Story 1.6: Jump, vault và fall damage authoritative

As a người chơi,
I want vượt vật cản và chịu hậu quả rơi nhất quán,
So that traversal có thể dự đoán và không bị animation hoặc latency gian lận.

**Source Requirements:** FR16–FR17, FR19, FR22; NFR27, NFR29, NFR31.

**Depends on:** Story 1.4–1.5.

**Blocks:** Story 1.12 và combat movement validation.

**Module/File Ownership:** Movement traversal/fall domains, traversal queries, presentation events và deterministic fixtures.

**Platform Applicability:** Cả năm client và Linux headless server.

**Acceptance Criteria:**

**Given** jump command trên ground hợp lệ  
**When** motor thực thi  
**Then** đỉnh nhảy không vượt 0,9 m, cooldown là 0,45 giây và ADS bị khóa khi airborne  
**And** client không thể thay gravity, impulse hoặc grounded flag.

**Given** vật cản cao 0,6–1,4 m có landing clearance  
**When** traversal được xác nhận  
**Then** vault kéo dài 0,45–0,90 giây theo profile, khóa fire và phát semantic audible event  
**And** trajectory do gameplay tính, animation chỉ khớp trajectory đó.

**Given** nhân vật rơi  
**When** server xác nhận landing height/velocity  
**Then** damage bắt đầu trên 3 m và profile 8 m có thể gây tử vong khi HP không đầy theo bảng GDD  
**And** damage event commit trong authoritative order trước presentation.

**Error/Recovery Path:** Mép/landing bị chặn hoặc query thay đổi giữa dự đoán và commit phải hủy vault về last safe pose với reason, không snap xuyên vật cản.

**Test Boundary:** Jump apex/cooldown golden, vault height/duration matrix, blocked-landing cases, fall-damage boundary tests và replay determinism.

**Definition of Done:** Jump/vault/fall chạy đúng giới hạn, weapon/ADS locks đúng tick, traversal không dùng root motion và toàn bộ boundary có fixtures.

### Story 1.7: Swimming, diving và WaterVolume

As a người chơi,
I want bơi và lặn qua vùng nước sâu,
So that bờ biển là một tuyến di chuyển có rủi ro và luật rõ ràng.

**Source Requirements:** FR20, FR22; NFR27, NFR31, NFR46–NFR47.

**Depends on:** Story 1.3–1.6.

**Blocks:** Story 1.12, Epic 5 Water & Boat Slice.

**Module/File Ownership:** `game/src/shared/simulation/water`, movement water states, `game/scenes/world/water`, camera/input adapters và water tests.

**Platform Applicability:** Cả năm client và Linux headless server.

**Acceptance Criteria:**

**Given** nhân vật đi qua surface/depth threshold của `WaterVolume`  
**When** server tick chuyển state  
**Then** ground↔swim↔dive phải dùng guarded transition và tốc độ nước sâu 2,0 m/s  
**And** visual waves không được thay gameplay surface/depth.

**Given** swim/dive active  
**When** người chơi điều khiển camera và movement  
**Then** vũ khí bị khóa, input/camera dùng semantic contract và breath tối đa 20 giây  
**And** hết breath phải tạo HP loss authoritative cho tới khi nổi lên hợp lệ.

**Given** water cell/presentation chưa sẵn sàng hoặc replication correction đến  
**When** state được áp dụng  
**Then** gameplay readiness phải thắng presentation readiness và giữ entity identity  
**And** client không được tự khai báo ra khỏi nước hoặc reset breath.

**Error/Recovery Path:** Water metadata thiếu/invalid làm volume fail-closed khỏi signed map; runtime query lỗi giữ last valid water state và phát metric thay vì teleport.

**Test Boundary:** Surface/depth boundary, transition graph, speed/weapon lock, 20-second breath/HP, replication correction và headless water fixtures.

**Definition of Done:** Ground/swim/dive đầy đủ authority, camera/input/presentation nối đúng contract và WaterVolume tái dùng được cho Epic 5.

### Story 1.8: Camera TPP, shoulder swap, ADS và anti-peek

As a người chơi,
I want camera chiến đấu linh hoạt nhưng không nhìn xuyên cover,
So that TPP hữu ích mà vẫn giữ information fairness.

**Source Requirements:** FR56–FR57; NFR31–NFR32, NFR35; UX-DR8, UX-DR16–UX-DR17.

**Depends on:** Story 1.2, Story 1.4–1.7.

**Blocks:** Epic 2 aiming/combat presentation và spectator camera.

**Module/File Ownership:** `game/src/client/presentation/camera`, character camera anchors, visibility query adapter và camera tests.

**Platform Applicability:** Cả năm client; server chỉ nhận aim intent/reference, không nhận camera authority.

**Acceptance Criteria:**

**Given** người chơi ở gameplay state cho phép  
**When** chọn hip-fire TPP, over-shoulder, shoulder swap hoặc ADS  
**Then** camera chuyển đúng anchor/FOV/sensitivity profile và ADS dùng góc nhìn thứ nhất  
**And** airborne/weapon/state locks từ gameplay phải được tôn trọng.

**Given** camera gần tường hoặc vật cản  
**When** collision probe phát hiện obstruction  
**Then** camera phải đẩy tới trước không xuyên geometry  
**And** smoothing không tạo extra information hoặc làm reticle lệch aim contract.

**Given** camera thấy entity nhưng line-of-sight từ head/approved origin bị che hoàn toàn  
**When** visibility resolver chạy  
**Then** entity presentation phải bị occlude theo anti-peek contract  
**And** desktop/mobile/ultrawide không được có information range khác nhau.

**Error/Recovery Path:** Anchor/query thiếu dùng safe hip camera, disable mode lỗi có status rõ và không gửi camera transform như bằng chứng hit.

**Test Boundary:** Mode/FOV transitions, wall probes, shoulder swap, head-LOS occlusion fixtures, ultrawide 16:9 frame và mobile parity screenshots.

**Definition of Done:** Bốn camera mode hoạt động, collision/anti-peek đạt fixtures và server authority không phụ thuộc camera client.

### Story 1.9: Context interaction và arbitration

As a người chơi,
I want nút tương tác luôn chọn hành động hợp lệ và dễ hiểu,
So that tôi không thực hiện nhầm hành động trong tình huống căng thẳng.

**Source Requirements:** UX-DR19–UX-DR21, UX-DR35; architecture authority/interaction contract.

**Depends on:** Story 1.3–1.8.

**Blocks:** Pickup, revive, vehicle và contextual HUD stories.

**Module/File Ownership:** Shared interaction contracts, server interaction authority, client interaction presenter và arbitration fixtures.

**Platform Applicability:** Cả năm client và Linux headless server.

**Acceptance Criteria:**

**Given** nhiều interaction candidate cùng hợp lệ  
**When** arbitration chạy  
**Then** ưu tiên DBNO assist → vehicle safety/exit → traversal/vehicle enter → pickup  
**And** action phụ vẫn truy cập được mà không thay đổi priority theo platform.

**Given** người chơi bắt đầu hold action  
**When** server xác nhận progress hoặc interruption  
**Then** client hiển thị committed progress, action/target stable ID và reason ngắt  
**And** progress không tự chạy tới 100% hoặc optimistic-commit.

**Given** target biến mất, ra range hoặc ownership thay đổi  
**When** action được validate  
**Then** server reject idempotently và focus/prompt chuyển sang candidate hợp lệ kế tiếp  
**And** không mutate target cũ.

**Error/Recovery Path:** Candidate/query lỗi loại riêng candidate, giữ input hoạt động và phát typed rejection thay vì kẹt interaction state.

**Test Boundary:** Priority table, target churn, hold interruption, duplicate command/idempotency và Keyboard/Touch parity.

**Definition of Done:** Arbitration deterministic, prompt/progress bám server state và contract tái dùng được cho loot/revive/vehicle.

### Story 1.10: Keyboard/Mouse bindings, remap và sensitivity contract

As a người chơi desktop,
I want remap đầy đủ và chỉnh cách ngắm/giữ nút,
So that điều khiển phù hợp phần cứng và thói quen của tôi.

**Source Requirements:** FR23, FR58; UX-DR33–UX-DR36, UX-DR53.

**Depends on:** Story 1.3, Story 1.8–1.9.

**Blocks:** Epic 8 Settings polish và five-platform input gate.

**Module/File Ownership:** Keyboard/mouse adapter, input settings schema, binding-label provider, local settings persistence và tests.

**Platform Applicability:** Windows, Linux, macOS; shared settings contract dùng cho mobile.

**Acceptance Criteria:**

**Given** danh mục action gameplay  
**When** người chơi remap primary/secondary, sensitivity hip/ADS/scope hoặc hold/toggle  
**Then** thay đổi phải stage, phát hiện conflict theo context, Apply atomically và Cancel rollback  
**And** `ui_accept`, `ui_cancel`, Pause, Inventory-close và Map-close luôn còn escape path.

**Given** keyboard layout không phải QWERTY hoặc OS khác nhau  
**When** binding được hiển thị  
**Then** policy physical-vs-logical key và raw-mouse choice đã khóa phải được áp dụng  
**And** label OS/localized không được dùng display text làm gameplay identity.

**Given** settings hợp lệ đã Apply  
**When** restart ứng dụng  
**Then** binding/sensitivity/hold-toggle được restore từ versioned local config  
**And** config cũ/hỏng fallback về default có migration status rõ.

**Error/Recovery Path:** Conflict không giải được hoặc persistence failure giữ cấu hình active cũ, báo reason và không ghi file một phần.

**Test Boundary:** Complete-action coverage, conflict matrix, Apply/Cancel atomicity, non-QWERTY/Linux labels, raw mouse và restart migration.

**Definition of Done:** Keyboard/Mouse đầy đủ binding/remap/sensitivity, có escape bindings và semantic output không thay đổi theo label/layout.

### Story 1.11: Touch landscape, multitouch và interruption safety

As a người chơi mobile,
I want điều khiển Touch phản hồi đồng thời và không kẹt nút,
So that tôi có thể di chuyển, nhìn, bắn và tương tác công bằng.

**Source Requirements:** FR24, FR58; NFR33, NFR39–NFR40; UX-DR38–UX-DR43.

**Depends on:** Story 1.3, Story 1.8–1.10.

**Blocks:** Epic 8 Touch layout editor và mobile device gates.

**Module/File Ownership:** Touch adapter, safe-area root, touch stick/look/action controls, layout schema và mobile tests.

**Platform Applicability:** Android và iOS; desktop debug emulation không thay device evidence.

**Acceptance Criteria:**

**Given** landscape Touch layout  
**When** nhiều ngón điều khiển stick trái, look zone phải, fire và contextual actions  
**Then** mỗi control sở hữu pointer ID riêng và phát semantic press/release/axis  
**And** look tap không tự bắn/ADS, Touch không có snap, magnetism, auto-fire hoặc extra enemy cue.

**Given** Touch baseline control surface  
**When** gameplay state cho phép action tương ứng  
**Then** layout phải có left movement stick, right look zone, right fire, optional left fire, stance, ADS, interact, reload, throwable, Map, Inventory và vehicle actions  
**And** contextual button chỉ hiện/phát command khi action hợp lệ.

**Given** người chơi điều chỉnh Touch baseline  
**When** thay vị trí, kích thước, opacity hoặc left-handed preset rồi Apply/Cancel/Reset  
**Then** thay đổi phải atomic, persist versioned và không làm mất fire/exit/close/Pause  
**And** Epic 8 chỉ production-harden editor/preview, không phải story đầu tiên cung cấp khả năng chỉnh layout của FR58.

**Given** phone/tablet safe area hoặc left-handed preset  
**When** layout load/rotate/resume  
**Then** reticle giữ giữa live world, critical control nằm trong inset và target thường ≥48, fire/exit/close ≥64 khi cho phép  
**And** layout invalid fallback preset an toàn.

**Given** finger-up, focus loss, OS interruption hoặc audio-route modal  
**When** adapter bị cancel  
**Then** mọi held action được release và cần touch mới để re-arm  
**And** không có stuck movement, fire, ADS hoặc PTT.

**Error/Recovery Path:** Pointer collision/layout corruption hủy owner bị ảnh hưởng, restore safe preset và giữ Pause/exit truy cập được.

**Test Boundary:** Multitouch ownership, gesture conflict, interruption fuzz, phone 20:9/16:9/tablet 4:3, notch/gesture/left-handed và semantic parity.

**Definition of Done:** Touch controller hoạt động trên Android/iOS representative devices, không stuck action và không thêm assistance bị cấm.

### Story 1.12: Movement Validation Course và promotion asset bề mặt/âm thanh

As a đội phát triển gameplay,
I want một course tái lập cùng asset đã kiểm duyệt,
So that movement, animation, âm thanh và surface response được đánh giá nhất quán.

**Source Requirements:** FR13–FR24, FR56–FR58; NFR31, NFR35, NFR46, NFR55; asset intake 2026-07-26.

**Depends on:** Story 1.2–1.11.

**Blocks:** Story 1.13 và các movement/combat regression gate.

**Module/File Ownership:** `game/scenes/training/movement_validation`, `game/tools/asset_validation`, `game/assets/audio/footsteps`, approved surface assets, `content-source/licenses` và validation reports.

**Platform Applicability:** Cả năm client; Linux headless chạy course fixtures không render/audio.

**Acceptance Criteria:**

**Given** 2.072 audio và 36 texture đang ở quarantine  
**When** intake validator phân loại  
**Then** mỗi candidate phải có source/author/license/date/checksum/stable ID và technical metadata  
**And** file thiếu provenance, monster/zombie/VO/event content hoặc role không rõ phải bị loại riêng, không promote theo thư mục hàng loạt.

**Given** texture đất/đá/bê tông đủ quyền sử dụng  
**When** chọn subset cho course  
**Then** phải xác minh alpha purpose, color space, tiling/seam, texel scale và mobile compression  
**And** không suy đoán normal/roughness/mask; map thiếu dùng material default đã khai báo.

**Given** movement/footstep/vault/swim audio đủ quyền sử dụng  
**When** promote  
**Then** clip phải được normalize loudness, phân surface/action, kiểm tra loop/channel và gắn semantic audible-event ID  
**And** server chỉ phát event, không chứa audio file.

**Given** course được chạy  
**When** replay bộ command chuẩn  
**Then** phải bao phủ flat/slope/step, stance clearance, lean cover, jump, vault 0,6–1,4 m, fall thresholds, water transition và camera anti-peek  
**And** report so sánh authoritative state, animation state, surface ID và audible event theo tick.

**Error/Recovery Path:** Asset không đạt giữ nguyên quarantine và course dùng neutral licensed primitive/test tone; failure không được vô hiệu gameplay test.

**Test Boundary:** Per-file provenance/checksum, texture seam/import, audio loudness/loop, deterministic movement replay, animation-state coverage và surface/event mapping.

**Definition of Done:** Course tái lập hoàn chỉnh; subset audio/texture hợp lệ được dùng thật với manifest; asset bị loại có reason; không file quarantine nào bị import trực tiếp.

### Story 1.13: Epic 1 five-platform parity gate

As a người chơi trên bất kỳ nền tảng hỗ trợ,
I want movement và camera có cùng luật và thông tin,
So that thiết bị không quyết định lợi thế gameplay.

**Source Requirements:** FR13–FR24, FR56–FR58; NFR15, NFR31–NFR35, NFR49.

**Depends on:** Story 1.1–1.12.

**Blocks:** Epic 2 và mọi production-content expansion.

**Module/File Ownership:** Device-lab harness, Epic 1 evidence pack, parity reports và release-smoke configuration.

**Platform Applicability:** Windows, Linux, macOS, Android và iOS; Linux headless authoritative reference.

**Acceptance Criteria:**

**Given** cùng gameplay manifest, seed và command fixtures  
**When** chạy Movement Validation Course trên năm client và headless reference  
**Then** authoritative position/state/timing phải khớp deterministic tolerance và collision/silhouette/information semantics tương đương  
**And** khác biệt chỉ được nằm ở presentation LOD/material/profile đã cho phép.

**Given** Keyboard/Mouse và Touch thực hiện cùng semantic sequence  
**When** so sánh output  
**Then** không platform nào có extra speed, aim assistance, visibility hoặc action shortcut  
**And** input labels/layout không thay gameplay command identity.

**Given** một platform thiếu evidence hoặc vượt parity tolerance  
**When** gate tổng hợp  
**Then** Epic 1 phải fail với owner, fixture và reproduction rõ  
**And** không waive bằng client authority, silent feature removal hoặc platform-specific gameplay data.

**Error/Recovery Path:** Gate failure giữ Epic 2 blocked; fix chạy lại fixture bị ảnh hưởng và regression suite đầy đủ trước khi đóng.

**Test Boundary:** Five-platform launch/device smoke, deterministic course replay, visual/LOS snapshots, input parity, mobile interruption và headless manifest/package checks.

**Definition of Done:** Epic 1 evidence pack đạt trên năm nền tảng; mọi FR được trace tới fixture; asset manifest hợp lệ; Epic 2 được mở khóa.

## Epic 2: Đấu súng có thể tin cậy

Người chơi có thể bắn, nhận sát thương và hiểu kết quả giao tranh trong Combat Sandbox tối đa 8 client, với projectile, recoil, giáp, authority, prediction và lag compensation đúng contract.

### Story 2.1: Binary gameplay protocol và compatibility handshake

As a người chơi online,
I want client chỉ vào trận tương thích và packet được kiểm tra,
So that giao tranh không hỏng vì build, content hoặc dữ liệu mạng sai.

**Source Requirements:** FR71–FR73; NFR26–NFR31, NFR55.

**Depends on:** Story 1.13.

**Blocks:** Story 2.2, Story 2.11–2.15 và Epic 6.

**Module/File Ownership:** `game/src/shared/protocol/{codec,messages,validation,versions}`, golden fixtures và protocol fuzz harness.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** một gameplay packet  
**When** codec encode/decode  
**Then** header phải có numeric type ID, protocol version, sequence, tick và payload length  
**And** payload không dùng `Variant`, `Dictionary`, object, `NodePath`, RPC name hoặc instance ID.

**Given** packet không tin cậy  
**When** pipeline xử lý  
**Then** phải chạy `decode → validate type/length/range/cadence/sequence/ownership/state → apply`  
**And** malformed packet không được mutate simulation hoặc làm process crash.

**Given** client join Combat Sandbox  
**When** handshake  
**Then** `build_id`, `protocol_version`, `gameplay_schema_version` và `content_manifest_hash` phải khớp  
**And** mismatch trả destination/reason rõ trước khi cấp gameplay identity.

**Error/Recovery Path:** Packet sai bị drop có bounded metric/rate-limit; compatibility mismatch giữ client ngoài match và không downgrade protocol âm thầm.

**Test Boundary:** Golden bytes, round-trip, endian/boundary cases, fuzz malformed input, handshake matrix và static prohibited-type scan.

**Definition of Done:** Codec versioned, fuzz/golden đạt, handshake fail-closed và không protocol identity nào phụ thuộc SceneTree.

### Story 2.2: Fixed-30-Hz Combat Sandbox match host

As a người chơi,
I want một đấu trường nhỏ có máy chủ sở hữu trạng thái,
So that mọi cơ chế bắn được thử trong điều kiện online thật.

**Source Requirements:** FR71–FR72; NFR13–NFR17, NFR27, NFR29.

**Depends on:** Story 2.1.

**Blocks:** Story 2.3–2.15.

**Module/File Ownership:** `game/src/server/{bootstrap,match_host,connections,authority,shutdown}`, match-server scene và sandbox configuration.

**Platform Applicability:** Linux headless server và năm client.

**Acceptance Criteria:**

**Given** sandbox process khởi động với seed/config hợp lệ  
**When** tối đa 8 client join  
**Then** host chạy phase order cố định ingest → movement → physics query → combat → inventory → zone → commit → snapshot ở 30 Hz  
**And** mỗi player/entity có stable runtime identity do server factory cấp.

**Given** connection join/leave hoặc process shutdown  
**When** lifecycle transition  
**Then** guarded match state machine phải cleanup connection/entity/channel deterministically  
**And** không giữ Node/socket/timer mồ côi.

**Given** config/manifest/phase invariant lỗi  
**When** host phát hiện  
**Then** match fail-closed với typed Match-critical outcome và evidence tối thiểu  
**And** client nhận state rõ thay vì tiếp tục sandbox sai authority.

**Error/Recovery Path:** Lỗi một connection bị cô lập; invariant authority/content lỗi kết thúc sandbox có reason; process-fatal chỉ dùng khi không thể bảo toàn match.

**Test Boundary:** Headless boot/shutdown, 1–8 join/leave, phase-order deterministic test, factory enforcement và failure injection.

**Definition of Done:** Sandbox 8 slot chạy 30 Hz, lifecycle sạch, phase order được khóa bằng test và không có client authority.

### Story 2.3: Weapon, ammunition và attachment gameplay manifest

As a người chơi,
I want danh mục súng, đạn và phụ kiện có quy tắc nhất quán,
So that mỗi món có identity và chỉ số có thể học được.

**Source Requirements:** FR59–FR62; NFR23–NFR24, NFR31, NFR55.

**Depends on:** Story 2.2.

**Blocks:** Story 2.4–2.10 và Epic 3.

**Module/File Ownership:** `game/content/definitions/{weapons,ammunition,attachments}`, typed authoring resources, validators và generated gameplay manifest.

**Platform Applicability:** Năm client và Linux headless server dùng cùng gameplay manifest.

**Acceptance Criteria:**

**Given** authoring definitions  
**When** bake manifest  
**Then** phải có mục tiêu 25 vũ khí đúng nhóm, năm cỡ đạn, 4 muzzle, 4 grip, 3 magazine, 2 stock và 7 optic  
**And** mỗi item có stable ID, slot compatibility và approved damage/RPM/magazine/velocity/reload/falloff/ADS/spread/recoil data.

**Given** năm cỡ đạn 9 mm, .45, 5,56 mm, 7,62 mm và 12 gauge  
**When** author identity/presentation metadata  
**Then** mỗi cỡ phải có tổ hợp màu, hình hộp và biểu tượng phân biệt  
**And** màu không được là tín hiệu duy nhất và gameplay identity không phụ thuộc visual label.

**Given** definition thiếu, trùng ID, ngoài range hoặc attachment sai slot  
**When** validator chạy  
**Then** bake phải fail trước khi ký manifest  
**And** client/server không được fallback sang display name hoặc file path.

**Given** năm platform build  
**When** so sánh gameplay hash  
**Then** hash phải giống server và mọi client  
**And** visual asset variant không được thay balance/collision/silhouette.

**Error/Recovery Path:** Manifest lỗi giữ bản signed trước; author sửa source rồi regenerate, không chỉnh generated file trực tiếp.

**Test Boundary:** Schema/range/uniqueness, roster counts, compatibility matrix, golden manifest/hash và platform package parity.

**Definition of Done:** Catalog/data baseline bake được, cùng hash trên mọi target và đủ contract cho weapon/inventory stories.

### Story 2.4: Authoritative weapon action, ammo và reload state

As a người chơi,
I want bắn và nạp đạn phản hồi đúng trạng thái súng,
So that ammo và timing không thể bị client gian lận.

**Source Requirements:** FR62, FR68, FR70–FR72; NFR14, NFR26–NFR29.

**Depends on:** Story 2.3.

**Blocks:** Story 2.5, Story 2.7–2.12.

**Module/File Ownership:** Shared weapon state machine, server combat authority, weapon command/messages và unit fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** fire/reload/switch command hợp lệ  
**When** server tick xử lý  
**Then** cadence, fire mode, magazine/reserve ammo, reload duration và action locks phải theo manifest  
**And** shot ID/ammo mutation chỉ commit một lần tại authoritative tick.

**Given** command đến khi sprint, vault, swim, airborne ADS-lock, reload hoặc ammo rỗng  
**When** validate  
**Then** action bị reject với stable reason  
**And** client presentation hòa giải về canonical weapon state.

**Given** packet lặp/trễ hoặc client khai ammo khác  
**When** server apply  
**Then** sequence/idempotency ngăn bắn hoặc trừ đạn hai lần  
**And** ammo client không bao giờ là authority.

**Error/Recovery Path:** State invariant lỗi dừng weapon instance bị ảnh hưởng, emit evidence và không làm hỏng inventory/player khác.

**Test Boundary:** Cadence/reload/ammo boundaries, action-lock matrix, duplicate/reordered commands và deterministic weapon replay.

**Definition of Done:** Weapon state authoritative, ammo/reload đúng data, invalid commands fail-closed và presentation có canonical state.

### Story 2.5: Projectile ballistics và swept collision

As a người chơi,
I want đạn có thời gian bay và độ rơi đáng tin,
So that lead, khoảng cách và cover quyết định phát bắn.

**Source Requirements:** FR62–FR63, FR70–FR73; NFR14–NFR16, NFR22, NFR27.

**Depends on:** Story 2.4.

**Blocks:** Story 2.6, Story 2.10–2.13.

**Module/File Ownership:** `game/src/shared/simulation/ballistics`, server physics-query adapter, projectile messages và ballistic fixtures.

**Platform Applicability:** Linux headless authority; năm client nhận presentation snapshots/events.

**Acceptance Criteria:**

**Given** shot đã commit  
**When** projectile simulation chạy ở fixed tick  
**Then** mọi primary weapon dùng ballistic integration với velocity/gravity/falloff từ manifest và swept segment collision  
**And** không tạo `RigidBody3D` per bullet hoặc dùng hitscan thay thế.

**Given** projectile qua nhiều candidate trong một tick  
**When** query trả kết quả  
**Then** hit gần nhất hợp lệ phải được chọn theo stable ordering và ownership/filter rules  
**And** shot/projectile/hit event giữ causal IDs.

**Given** projectile hết range/lifetime hoặc cell/query lỗi  
**When** cleanup  
**Then** identity được retire deterministic, không double-hit hoặc leak  
**And** lỗi không chuyển hit authority sang client.

**Error/Recovery Path:** Query không hợp lệ hủy projectile có typed reason/evidence; không đoán hit hoặc giữ projectile vô hạn.

**Test Boundary:** Trajectory/drop/falloff golden, swept tunneling, ordering, cleanup, cover fixtures và bandwidth/entity-count profiling.

**Definition of Done:** Projectile server-authoritative có travel/drop, không tunneling trong fixtures và không dùng per-bullet rigid body.

### Story 2.6: Health, hit regions và armor durability

As a người chơi,
I want sát thương và giáp tuân theo công thức công khai,
So that kết quả trúng đạn có thể giải thích.

**Source Requirements:** FR25–FR29, FR62–FR63, FR70–FR71; NFR1–NFR3, NFR14, NFR22.

**Depends on:** Story 2.5.

**Blocks:** Story 2.9–2.13 và DBNO trong Epic 4.

**Module/File Ownership:** `game/src/shared/simulation/health`, hitbox definitions, armor/equipment state và damage fixtures.

**Platform Applicability:** Linux headless authority; năm client presentation.

**Acceptance Criteria:**

**Given** validated projectile hit  
**When** damage resolve  
**Then** player bắt đầu 100 HP, không tự hồi và dùng head ×2,20, chest ×1,00, abdomen ×0,90, limb ×0,75  
**And** hit region đến từ authoritative hitbox history/collision.

**Given** body armor hoặc helmet tier 1–3  
**When** damage áp dụng  
**Then** reduction/durability đúng FR27–FR28 và viên làm durability về 0 vẫn nhận reduction trước khi armor break commit  
**And** event order là hit → mitigation → HP/durability → break/elimination candidate.

**Given** invalid region/tier/damage value  
**When** resolver validate  
**Then** damage bị reject và evidence ghi source/projectile/target IDs  
**And** client không được tự báo HP, armor break hoặc elimination.

**Error/Recovery Path:** Invariant âm/NaN/unknown ID cô lập damage command, giữ canonical health và phát Match-critical nếu manifest mismatch.

**Test Boundary:** Công thức từng region/tier, exact break-shot ordering, boundary HP/durability, deterministic combat replay và statistical armor sanity.

**Definition of Done:** Health/armor formula đạt golden tests, mọi mutation authoritative và damage chain có thể replay/giải thích.

### Story 2.7: Recoil, spread và movement modifiers

As a người chơi,
I want độ giật và độ tản phản ánh súng, tư thế và chuyển động,
So that kiểm soát chuột/Touch và lựa chọn tư thế tạo khác biệt kỹ năng.

**Source Requirements:** FR62, FR64; NFR1, NFR23–NFR24, NFR31, NFR33.

**Depends on:** Story 2.4, Story 2.6.

**Blocks:** Story 2.10–2.12 và balance gates.

**Module/File Ownership:** Weapon spread/recoil simulation, client aim presentation và recoil golden fixtures.

**Platform Applicability:** Năm client với cùng gameplay parameters; server xác nhận shot cone.

**Acceptance Criteria:**

**Given** chuỗi fire liên tục  
**When** recoil index tăng  
**Then** recoil tăng qua 8 viên đầu, ổn định sau viên 12 và bắt đầu hồi sau 0,25 giây ngừng bắn  
**And** seeded shot direction có thể tái hiện từ evidence.

**Given** stance/movement/ADS state  
**When** shot resolve  
**Then** spread modifier dùng đúng hệ số GDD từ authoritative state  
**And** Touch không nhận magnetism, target snap hoặc cone có lợi hơn.

**Given** frame rate hoặc presentation smoothing khác  
**When** cùng tick/seed/commands chạy  
**Then** shot cone/recoil gameplay outcome phải giống nhau  
**And** camera recoil không sửa authoritative direction sau commit.

**Error/Recovery Path:** Recoil profile thiếu/invalid chặn weapon definition khi bake; runtime không fallback sang zero recoil.

**Test Boundary:** Bullet-index curves, 0,25-second recovery, stance/movement matrix, seed determinism và input-family parity.

**Definition of Done:** Recoil/spread đúng baseline, deterministic, không platform assistance và presentation tách khỏi shot authority.

### Story 2.8: Scope breath-hold, zeroing và aim punch

As a người chơi,
I want scope tầm xa có breath, zeroing và phản ứng khi bị bắn,
So that đấu súng xa có quyết định và counterplay rõ.

**Source Requirements:** FR65–FR66; NFR1, NFR22–NFR23, NFR31.

**Depends on:** Story 2.6–2.7.

**Blocks:** Story 2.10–2.12.

**Module/File Ownership:** Aiming state domain, optic definitions, scope presentation và aim-effect fixtures.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** optic từ 4× hỗ trợ tính năng  
**When** người chơi giữ hơi hoặc đổi zero  
**Then** breath tối đa 8 giây, exhausted state 4 giây và zero 100–800 m theo bước 100 m  
**And** unsupported optic từ chối zero/breath action rõ ràng.

**Given** validated hit gây aim punch  
**When** energy/armor resolver tạo effect  
**Then** punch không vượt 1,5° mỗi hit và có ngưỡng 0,12 giây chống chain-lock  
**And** effect source/timing do server event xác nhận, client chỉ trình bày.

**Given** ADS bị khóa bởi movement/action state  
**When** scope input đến  
**Then** state machine từ chối transition và giữ camera/reticle canonical  
**And** không giữ breath timer khi đã rời scope.

**Error/Recovery Path:** Optic/effect data lỗi chặn manifest; route camera lỗi fallback hip mode nhưng không bỏ gameplay penalty.

**Test Boundary:** Breath/exhaust timers, zero steps/ballistic alignment, punch cap/debounce, ADS-lock matrix và platform visual parity.

**Definition of Done:** Scope mechanics có authority/data/test đầy đủ, aim punch bounded và không phát sinh information/aim advantage theo platform.

### Story 2.9: Melee combat baseline

As a người chơi,
I want cận chiến hoạt động khi không có đạn,
So that giao tranh gần vẫn có lựa chọn rủi ro rõ.

**Source Requirements:** FR59, FR67, FR70–FR72; NFR14, NFR27, NFR31.

**Depends on:** Story 2.4, Story 2.6.

**Blocks:** Story 2.10, Story 2.12 và inventory equipment.

**Module/File Ownership:** Melee definitions/state, server melee query, presentation events và fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** một trong ba melee weapon và attack command hợp lệ  
**When** wind-up hoàn tất  
**Then** query authoritative có tầm 1,8 m, wind-up 0,35–0,55 giây và damage 35–60 theo manifest  
**And** hit chỉ commit một lần theo attack ID.

**Given** target ngoài range, bị cover hoặc attacker bị interrupt  
**When** resolve  
**Then** không có damage/hit confirm  
**And** animation swing không được tạo hit riêng.

**Given** latency/reordered commands  
**When** server validate  
**Then** ownership/state/tick window phải được kiểm tra  
**And** không rewind toàn world hoặc cho client chọn target.

**Error/Recovery Path:** Query/weapon ID lỗi reject attack, cleanup attack state và không trừ durability/ammo không liên quan.

**Test Boundary:** Range/wind-up/damage boundaries, cover, interruption, duplicate attack và deterministic ordering.

**Definition of Done:** Ba melee archetype dùng chung contract, hit authoritative và presentation không sở hữu damage.

### Story 2.10: Combat presentation và promotion audio/vũ khí

As a người chơi,
I want phát bắn và va chạm có hình/tiếng dễ phân biệt,
So that tôi hiểu điều gì vừa xảy ra mà không cần damage number.

**Source Requirements:** FR68–FR70; NFR31, NFR35, NFR44, NFR48, NFR55; UX-DR16–UX-DR18.

**Depends on:** Story 2.3–2.9.

**Blocks:** Story 2.12, Epic 8 audio mix.

**Module/File Ownership:** `game/src/client/presentation/{weapons,effects}`, `game/assets/audio/weapons`, weapon visual assets, promotion manifests và presentation tests.

**Platform Applicability:** Năm client; Linux headless chỉ phát semantic events.

**Acceptance Criteria:**

**Given** audio/weapon assets ở quarantine  
**When** promotion review  
**Then** chỉ gunshot/mechanical/impact/shell/melee/explosion và weapon visual đủ provenance/license/checksum/technical review được promote  
**And** unknown/monster/event content bị loại, server artifact không chứa presentation assets.

**Given** shot event local/remote hợp lệ  
**When** trình bày  
**Then** có tiếng nổ, cơ khí, muzzle flash, casing và camera reaction phân biệt theo archetype/range  
**And** VFX/audio không thay shot direction, timing hoặc visibility semantics.

**Given** validated hit event  
**When** impact trình bày  
**Then** tạo máu/bụi theo setting, âm thanh nhẹ và body reaction  
**And** không floating damage, enemy outline, hit cue chưa server-confirm hoặc platform-only cue.

**Error/Recovery Path:** Asset thiếu dùng neutral approved fallback theo semantic ID; event/VFX lỗi không làm mất combat state hoặc crash.

**Test Boundary:** Provenance/loudness/pooling reset, event-to-cue mapping, no-premature-confirm tests, distance/output snapshots và package parity.

**Definition of Done:** Combat cues dùng subset asset hợp lệ, phân biệt được, không lộ extra information và không mang presentation asset lên server.

### Story 2.11: Authority Mirror prediction và reconciliation

As a người chơi online,
I want điều khiển phản hồi nhanh nhưng tự sửa theo máy chủ,
So that latency không làm mất cảm giác điều khiển hoặc phá fairness.

**Source Requirements:** FR71–FR72; NFR14–NFR16, NFR26–NFR29.

**Depends on:** Story 2.1–2.7.

**Blocks:** Story 2.12–2.15 và Epic 6 scale.

**Module/File Ownership:** `game/src/client/{prediction,replication}`, server snapshots/acks, shared state serialization và impairment tests.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** local movement/allowed weapon presentation input  
**When** client predict  
**Then** state buffer lưu command sequence/tick và chỉ dự đoán domain được phép  
**And** inventory, loot, damage, HP, ammo commit và result không optimistic-commit.

**Given** snapshot có ack/correction  
**When** reconcile  
**Then** client restore authoritative state, replay unacked commands và tách presentation smoothing khỏi simulation correction  
**And** correction có metric magnitude/frequency.

**Given** snapshot stale/out-of-order hoặc buffer quá giới hạn  
**When** apply  
**Then** sequence rule drop/rebase an toàn  
**And** không dùng client state để lấp authoritative gap.

**Error/Recovery Path:** Buffer invariant lỗi hard-resync player local có reason/metric; repeated failure chuyển degraded/disconnect state rõ.

**Test Boundary:** Restore/replay golden, loss/jitter/reorder impairment, forbidden optimistic domains, correction metrics và long-session buffer bounds.

**Definition of Done:** Prediction responsive, reconciliation deterministic, authority boundaries có static/runtime tests và impairment suite đạt.

### Story 2.12: Server-confirmed feedback và hit-trade resolution

As a người chơi,
I want hit marker, armor break và elimination chỉ xuất hiện khi chắc chắn,
So that phản hồi combat không nói sai kết quả.

**Source Requirements:** FR69–FR72; NFR2, NFR14, NFR22; UX-DR16–UX-DR18.

**Depends on:** Story 2.6, Story 2.9–2.11.

**Blocks:** Story 2.15 và results/evidence stories.

**Module/File Ownership:** Combat committed events, client feedback presenter, trade resolver và replay fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** speculative shot/hit presentation  
**When** chưa có committed server event  
**Then** không hiển thị hit marker, armor break, DBNO hoặc elimination  
**And** local muzzle/weapon feedback phải phân biệt rõ với confirmation.

**Given** hai projectile đã rời nòng trước elimination commit  
**When** cả hai hit hợp lệ theo timeline  
**Then** hit trade được chấp nhận và damage events commit theo stable order  
**And** elimination không xóa projectile hợp lệ hồi tố.

**Given** duplicate/late confirmation  
**When** presenter consume  
**Then** causal event ID đảm bảo cue đúng một lần  
**And** replay cho ra cùng combat explanation.

**Error/Recovery Path:** Missing presentation mapping log bounded warning và dùng neutral cue; không suy đoán outcome từ local VFX.

**Test Boundary:** Speculative-vs-confirmed timing, hit-trade timelines, duplicate events, armor/DBNO/elimination ordering và replay explanation.

**Definition of Done:** Mọi competitive confirmation bám committed event, hit trades đúng timeline và không có false-positive cue.

### Story 2.13: Bounded hitbox history và lag compensation

As a người chơi có latency hợp lệ,
I want máy chủ đánh giá phát bắn theo thời điểm hợp lý,
So that hit registration công bằng mà không cho phép bắn quá khứ vô hạn.

**Source Requirements:** FR70–FR73; NFR14–NFR16, NFR22, NFR26–NFR29.

**Depends on:** Story 2.5–2.6, Story 2.11–2.12.

**Blocks:** Story 2.15 và Epic 6 network scale.

**Module/File Ownership:** `game/src/server/lag_compensation`, session clock, hitbox snapshots và lag fixtures.

**Platform Applicability:** Linux headless server; client chỉ gửi bounded shot timing evidence.

**Acceptance Criteria:**

**Given** shot timestamp đã đồng bộ session clock  
**When** server validate  
**Then** timestamp clamp theo latency envelope và rewind hitbox history tối đa 150 ms  
**And** chỉ hitbox cần thiết được rewind, không rewind world/door/projectile/vehicle.

**Given** timestamp quá cũ, tương lai, replayed hoặc cadence bất thường  
**When** validate  
**Then** shot bị clamp/reject theo policy có reason/evidence  
**And** ownership, ammo và weapon state vẫn được xét ở authoritative timeline.

**Given** history buffer chạy lâu  
**When** soak  
**Then** memory/copy cost bounded và snapshot retirement deterministic  
**And** hit accuracy giữ tolerance đã khóa.

**Error/Recovery Path:** Thiếu history dùng current authoritative hitboxes với degraded metric hoặc reject theo policy; không tin client transform.

**Test Boundary:** 0–150 ms boundaries, future/old/replayed timestamps, moving target/cover fixtures, memory soak và ≤0,5 m/one-tick accuracy evidence.

**Definition of Done:** Lag compensation bounded, có clock/clamp/history tests, không rewind toàn world và có metrics phục vụ khiếu nại hit.

### Story 2.14: Reusable headless-client harness

As a đội kiểm thử,
I want client headless có thể chạy kịch bản deterministic,
So that combat và network được tái hiện tự động mà không cần người điều khiển.

**Source Requirements:** FR71–FR73; NFR13–NFR17, NFR52; architecture test-harness contract.

**Depends on:** Story 2.1–2.13.

**Blocks:** Story 2.15 và Epic 6 scale gates.

**Module/File Ownership:** `test-harness/headless_clients`, scenario DSL, artifact/report schema và CI integration.

**Platform Applicability:** Linux CI/load workers kết nối cùng Linux match server.

**Acceptance Criteria:**

**Given** scenario seed, manifest hash và command script  
**When** harness khởi tạo 1–8 clients  
**Then** mỗi client handshake/join/act/disconnect như protocol thật và xuất trace theo tick/sequence  
**And** không gọi server implementation nội bộ để bỏ qua transport.

**Given** loss/latency/jitter/reorder profile  
**When** scenario chạy  
**Then** impairment áp độc lập theo channel/client và có thể tái lập bằng seed  
**And** report thu tick, bytes, corrections, hit validation và outcome.

**Given** client/process timeout hoặc assertion fail  
**When** harness cleanup  
**Then** process/socket/artifact được đóng bounded, failure giữ reproduction bundle  
**And** CI không báo pass một phần.

**Error/Recovery Path:** Worker/client lỗi được đánh dấu riêng; scenario tổng fail có seed/log/checksum, cho phép rerun đúng case.

**Test Boundary:** Harness self-tests, protocol conformance, deterministic seed, impairment calibration và process-leak checks.

**Definition of Done:** Harness 1–8 client tái dùng được, dùng transport thật, tạo reproduction/report chuẩn và cleanup sạch.

### Story 2.15: Network Arena 8-client combat gate

As a người chơi,
I want Combat Sandbox ổn định dưới latency và packet loss mục tiêu,
So that hit, movement và phản hồi đáng tin trước khi mở rộng game.

**Source Requirements:** FR25–FR29, FR59–FR73; NFR13–NFR17, NFR22–NFR24, NFR31.

**Depends on:** Story 2.1–2.14.

**Blocks:** Epic 3–4 và scale expansion Epic 6.

**Module/File Ownership:** Network Arena scenario pack, balance/combat evidence, performance reports và gate configuration.

**Platform Applicability:** Linux headless reference và representative clients của năm platform family.

**Acceptance Criteria:**

**Given** 8 protocol-mixed clients, 80 ms RTT và 1% loss  
**When** combat scenarios chạy  
**Then** server giữ 30 Hz/headroom target, damage xử lý ≤1 tick p95 và visible/server position error ≤0,5 m p95  
**And** bandwidth/correction/hit metrics nằm trong budget hoặc có blocking failure.

**Given** weapon/armor/projectile scenarios  
**When** replay evidence được phân tích  
**Then** formula, recoil, hit trade, confirmation và lag compensation phải tái hiện đúng  
**And** không có client authority hoặc platform-specific outcome.

**Given** bất kỳ critical metric/fixture fail  
**When** gate tổng hợp  
**Then** Epic 2 không hoàn tất và report chỉ rõ build/manifest/seed/client/tick  
**And** không waive bằng hitscan, client hit authority hoặc giảm parity.

**Error/Recovery Path:** Gate failure giữ reproduction bundle và rerun subset sau fix; baseline chỉ cập nhật qua reviewed data change.

**Test Boundary:** Full 8-client impairment matrix, weapon/armor golden, profiling, replay explainability và five-platform presentation parity.

**Definition of Done:** Network Arena gate đạt, mọi FR Epic 2 có evidence, harness tái dùng được và Epic 3–4 được mở khóa.

## Epic 3: Loot và quản trị tài nguyên sinh tồn

Người chơi có thể bắt đầu tay trắng, nhặt và quản lý vũ khí, đạn, giáp, hồi máu, sức chứa và vật ném với mọi mutation được máy chủ xác nhận.

### Story 3.1: Item definitions và immutable inventory manifest

As a người chơi,
I want mọi vật phẩm có identity và thuộc tính ổn định,
So that inventory không thay đổi ý nghĩa giữa client và server.

**Source Requirements:** FR30, FR34–FR43, FR48–FR49; NFR27, NFR31, NFR55.

**Depends on:** Story 2.3, Story 2.15.

**Blocks:** Story 3.2–3.11.

**Module/File Ownership:** `game/content/definitions/{equipment,consumables,throwables}`, shared item identifiers/schema, validators và generated manifest.

**Platform Applicability:** Năm client và Linux headless server dùng cùng gameplay hash.

**Acceptance Criteria:**

**Given** item authoring resources  
**When** bake  
**Then** weapon, ammo, attachment, equipment, healing, boost và throwable phải có stable content ID, type, slot, stack/capacity cost và gameplay fields  
**And** display name/file path không được làm protocol identity.

**Given** duplicate ID, invalid range/reference hoặc platform data khác  
**When** validator chạy  
**Then** bake/signing fail trước runtime  
**And** generated manifest read-only và hash khớp mọi target.

**Error/Recovery Path:** Giữ signed manifest trước khi source lỗi; không load partial/fallback item có gameplay khác.

**Test Boundary:** Schema/range/reference/uniqueness, golden manifest/hash và five-platform package parity.

**Definition of Done:** Item manifest immutable, versioned, cùng hash client/server và đủ dữ liệu cho inventory/loot/action stories.

### Story 3.2: Equipment slots, backpack capacity và load constraints

As a người chơi,
I want trang bị và sức chứa có giới hạn rõ,
So that lựa chọn mang gì tạo đánh đổi sinh tồn.

**Source Requirements:** FR34–FR36, FR48; NFR27, NFR31.

**Depends on:** Story 3.1.

**Blocks:** Story 3.3–3.6, Story 3.10.

**Module/File Ownership:** Shared inventory/equipment aggregate, capacity calculator và inventory fixtures.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** inventory mới  
**When** trang bị item  
**Then** có hai primary, một pistol, một melee và một selected throwable slot đúng type  
**And** slot không hợp lệ bị từ chối không mất item.

**Given** body capacity 50 và backpack tier 1/2/3  
**When** tính capacity  
**Then** tổng capacity lần lượt 120/180/250 khi mang backpack và ammo/heal/throwable dùng capacity  
**And** attachment đã gắn không dùng capacity.

**Given** item removal làm capacity giảm dưới current load  
**When** mutation validate  
**Then** action bị từ chối hoặc dùng explicit overflow policy đã khóa  
**And** server không tự xóa/drop item.

**Error/Recovery Path:** Arithmetic/definition lỗi reject transaction nguyên tử, giữ aggregate trước đó và emit invariant evidence.

**Test Boundary:** Slot matrix, exact capacity tiers/costs, attachment exception, overflow và integer boundary/fuzz.

**Definition of Done:** Equipment/capacity authoritative, mọi invariant có test và client chỉ trình bày canonical aggregate.

### Story 3.3: Atomic inventory mutations và server-confirmed hold actions

As a người chơi,
I want nhặt, chuyển, tách và thả item không làm mất đồ,
So that inventory đáng tin ngay cả khi latency hoặc thao tác lỗi.

**Source Requirements:** FR37, FR40–FR41; NFR14, NFR26–NFR29; UX-DR21, UX-DR24.

**Depends on:** Story 3.2.

**Blocks:** Story 3.4–3.6, Story 3.9–3.11 và Epic 8 Inventory.

**Module/File Ownership:** Inventory command/transaction service, protocol messages, server interaction authority và mutation fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** pickup/equip/move/split/drop command có expected version  
**When** server validate  
**Then** mutation áp nguyên tử, increment aggregate version và trả committed delta/rejection  
**And** slot sai, quá capacity, ownership/range/state sai giữ item tại nguồn.

**Given** hold action cho heal/revive/reload/interaction  
**When** progress hoặc interruption xảy ra  
**Then** progress đến từ server tick và reason ngắt stable  
**And** client không tự hoàn tất hay optimistic-commit.

**Given** duplicate/reordered/retried command  
**When** command ID đã thấy  
**Then** cùng payload trả cùng result, payload khác là security error  
**And** không double-mutate.

**Error/Recovery Path:** Version conflict trả fresh canonical snapshot/delta; transaction invariant lỗi rollback toàn bộ và giữ evidence.

**Test Boundary:** Mọi mutation success/failure, atomic rollback, idempotency/payload mismatch, interruption và network impairment.

**Definition of Done:** Inventory transaction an toàn, không mất/nhân đôi item, có typed reasons và tái lập được từ command/event log.

### Story 3.4: Empty start, world loot và manual pickup policy

As a người chơi,
I want bắt đầu tay trắng và tự quyết định món cần nhặt,
So that hành trình trang bị bắt đầu từ lựa chọn trong trận.

**Source Requirements:** FR38–FR42; NFR27, NFR31, NFR54.

**Depends on:** Story 3.3.

**Blocks:** Story 3.5, Story 3.7–3.9.

**Module/File Ownership:** World-loot entities/factory, pickup interaction, match-start inventory policy và loot fixtures.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** Standard player spawn  
**When** match inventory tạo  
**Then** không có loadout, weapon, armor, item hoặc skill đã chọn trước trận  
**And** mọi gameplay item phải đến từ hành động trong match.

**Given** world item trong range và pickup hợp lệ  
**When** quick pickup commit  
**Then** mỗi món mất 0,20 giây, dùng stable entity/item IDs và factory retire entity sau transaction  
**And** weapon, armor, attachment không bao giờ auto-pickup.

**Given** hai player tranh cùng item hoặc item unload/despawn  
**When** server order commands  
**Then** chỉ transaction đầu hợp lệ thắng, bên còn lại nhận reason  
**And** không clone/mất item.

**Error/Recovery Path:** Entity/reference lỗi reject pickup; world item giữ/retire theo canonical state, client ghost được reconcile.

**Test Boundary:** Empty start, 0,20-second timing, contested pickup, range/ownership, no-auto-pick prohibited types và factory identity.

**Definition of Done:** Standard luôn tay trắng, world pickup authoritative và policy manual rõ trên mọi input family.

### Story 3.5: Configurable bounded ammo auto-pickup

As a người chơi,
I want tự nhặt đúng cỡ đạn tới ngưỡng đã chọn,
So that giảm thao tác lặp mà không tự động quyết định trang bị.

**Source Requirements:** FR42–FR43; NFR27, NFR31; UX-DR33.

**Depends on:** Story 3.4.

**Blocks:** Epic 8 Settings/Inventory polish.

**Module/File Ownership:** Ammo pickup policy, local preference schema, server pickup validation và tests.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** ammo caliber threshold đã Apply  
**When** matching ammo trong valid pickup range  
**Then** client có thể đề nghị auto-pick tới threshold nhưng server vẫn kiểm tra capacity/ownership/state  
**And** threshold 0 tắt hoàn toàn caliber đó.

**Given** weapon/equipment/attachment hoặc ammo sai caliber  
**When** scanner chạy  
**Then** không tạo auto-pick command  
**And** không dùng màu/display name để xác định caliber.

**Error/Recovery Path:** Preference hỏng fallback threshold mặc định an toàn; server rejection dừng retry loop cho entity/version đó.

**Test Boundary:** Per-caliber thresholds, value 0, capacity boundary, item-type exclusion, restart persistence và race conditions.

**Definition of Done:** Ammo auto-pick bounded/configurable, không mở rộng sang item bị cấm và mọi mutation vẫn authoritative.

### Story 3.6: Healing và boost commitment actions

As a người chơi,
I want hồi máu và dùng boost theo timing/ngắt rõ,
So that tôi cân nhắc vị trí và rủi ro trước khi sử dụng.

**Source Requirements:** FR30, FR37; NFR27, NFR29, NFR31; UX-DR20–UX-DR21.

**Depends on:** Story 3.3.

**Blocks:** Epic 4 revive action và Epic 8 contextual UI.

**Module/File Ownership:** Consumable action domain, health integration, inventory transaction và action fixtures.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** bandage, first-aid kit, med kit, energy drink hoặc painkiller  
**When** use action hợp lệ  
**Then** duration/effect/HP cap/boost theo GDD manifest và item chỉ consumed khi commit  
**And** HP không tự hồi ngoài explicit effect.

**Given** movement, damage, state change hoặc target/item invalid theo rule  
**When** interruption tick đến  
**Then** action dừng với reason, progress không tới 100% giả và item giữ/consume theo commit policy  
**And** duplicate completion không double-heal.

**Error/Recovery Path:** Manifest/action invariant lỗi rollback health/item transaction và emit evidence; client reconcile progress/state.

**Test Boundary:** Mỗi consumable golden, HP caps, all interruption reasons, exact commit tick và duplicate/reorder.

**Definition of Done:** Năm consumable đúng timing/effect, action server-confirmed và inventory/health atomic.

### Story 3.7: Weighted loot generation và geography tiers

As a người chơi,
I want khu vực rủi ro cao có loot tốt hơn nhưng vẫn ngẫu nhiên công bằng,
So that lựa chọn điểm rơi có ý nghĩa chiến thuật.

**Source Requirements:** FR38, FR45; NFR25, NFR29, NFR31.

**Depends on:** Story 3.1, Story 3.4.

**Blocks:** Story 3.8–3.9 và map loot placement.

**Module/File Ownership:** Loot tables/groups, purpose-specific RNG, spawn service và statistical fixtures.

**Platform Applicability:** Linux headless authority; client nhận spawned entities.

**Acceptance Criteria:**

**Given** signed spawn groups và match seed  
**When** loot generation chạy  
**Then** group logic chọn item cụ thể bằng weighted RNG stream riêng cho loot  
**And** same seed/manifest/map placements cho same result, không phụ thuộc render order.

**Given** residential nhỏ hoặc military/port/industrial location  
**When** tier resolve  
**Then** residential ưu tiên basic; high-risk locations có quality tốt hơn theo approved table  
**And** không tạo essential item chỉ ở một premium/risky source.

**Error/Recovery Path:** Empty/invalid group làm map bake fail; runtime không fallback sang arbitrary item hoặc shared RNG stream.

**Test Boundary:** Seed determinism, weight distributions, geography tier comparisons, no-empty-group và random-stream isolation.

**Definition of Done:** Loot weighted theo geography, deterministic theo seed và có simulator-compatible output.

### Story 3.8: Loot distribution simulator và 90-second targets

As a nhà thiết kế,
I want đo khả năng trang bị sau đầu trận,
So that người chơi có cơ hội cạnh tranh hợp lý mà không bảo đảm loot.

**Source Requirements:** FR44–FR45; NFR24–NFR25, NFR29.

**Depends on:** Story 3.7.

**Blocks:** Story 3.9 và production map loot lock.

**Module/File Ownership:** `test-harness/map_analysis` loot simulator, scenarios, reports và CI gates.

**Platform Applicability:** Headless analysis; kết quả áp cùng manifest cho mọi client.

**Acceptance Criteria:**

**Given** representative medium compound và approved traversal model  
**When** chạy đủ seeded simulations cho 90 giây loot  
**Then** hướng tới ≥95% có gun, ≥70% primary, ≥50% armor/helmet và ≥35% healing  
**And** report có confidence/sample size, location tier và manifest hash.

**Given** target fail hoặc một item/spot thống trị  
**When** gate phân tích  
**Then** report chỉ ra group/placement contribution và block data promotion  
**And** không sửa bằng client-side spawn hoặc guaranteed hidden loadout.

**Error/Recovery Path:** Scenario/map input invalid fail report, giữ approved loot manifest trước và không công bố số liệu thiếu mẫu.

**Test Boundary:** Statistical reproducibility, target thresholds, tier stratification, seed independence và regression baseline review.

**Definition of Done:** Simulator CI tái lập được, baseline đạt/ghi exception có owner và loot data sẵn sàng cho airdrop/full match.

### Story 3.9: Airdrop schedule, visibility và contents

As a người chơi,
I want airdrop tạo điểm tranh chấp có giá trị nhưng không bắt buộc,
So that tôi có thể chọn rủi ro thay vì bị khóa khỏi item thiết yếu.

**Source Requirements:** FR46–FR47; NFR24, NFR27, NFR31.

**Depends on:** Story 3.7–3.8.

**Blocks:** Epic 4 zone integration và Epic 7 placement expansion.

**Module/File Ownership:** Airdrop scheduler/content definitions, accessible-placement query, smoke presentation và tests.

**Platform Applicability:** Linux headless authority và năm client presentation.

**Acceptance Criteria:**

**Given** zone phase 1–5 bắt đầu theo schedule  
**When** airdrop spawn  
**Then** đúng một crate mỗi phase tại vị trí map-validated có thể tiếp cận  
**And** chứa một special weapon cùng high-tier armor/healing từ signed table.

**Given** crate active  
**When** presentation render  
**Then** smoke phải nhận biết ở 800 m trong parity profile  
**And** mobile/desktop visibility không đổi gameplay information range.

**Given** item catalog  
**When** exclusivity validator chạy  
**Then** không essential item nào chỉ tồn tại trong airdrop  
**And** placement/content lỗi chặn spawn có evidence thay vì đặt vào vùng không tới được.

**Error/Recovery Path:** Không có placement hợp lệ dùng deterministic retry/fallback node đã bake; hết fallback skip có Match-critical metric, không spawn tùy ý.

**Test Boundary:** Phase counts, accessibility, content/exclusivity, 800 m visual parity và deterministic placement retries.

**Definition of Done:** Airdrop phase 1–5 đúng lịch/content, có accessible placement và không độc quyền essential item.

### Story 3.10: Throwable capacity và bounded trajectory preview

As a người chơi,
I want mang và ngắm vật ném với giới hạn rõ,
So that chuẩn bị ném hữu ích nhưng không biến thành đường ngắm vĩnh viễn.

**Source Requirements:** FR48, FR50; NFR27, NFR31.

**Depends on:** Story 3.2–3.3.

**Blocks:** Story 3.11 và Epic 8 throwable context card.

**Module/File Ownership:** Throwable inventory slot/state, aim preview presenter và trajectory fixtures.

**Platform Applicability:** Năm client và Linux headless authority cho throw state.

**Acceptance Criteria:**

**Given** inventory/capacity hợp lệ  
**When** thêm throwable  
**Then** tổng mang không vượt sáu và vẫn chịu capacity cost  
**And** selected throwable slot tham chiếu item instance hợp lệ.

**Given** aim throwable bắt đầu  
**When** elapsed vượt 1,5 giây  
**Then** predicted trajectory không còn hiển thị  
**And** preview không xuyên geometry, reveal enemy hoặc quyết định authoritative hit.

**Given** throw bị cancel/interrupted  
**When** state kết thúc  
**Then** preview/held action cleanup và item chỉ consumed khi server commit throw  
**And** Touch/Keyboard tạo cùng semantic action.

**Error/Recovery Path:** Preview query lỗi ẩn preview nhưng giữ cancel/throw contract; invalid inventory state reject không consume item.

**Test Boundary:** Six-item/capacity boundaries, 1,5-second cutoff, cancel/commit, obstruction và input parity.

**Definition of Done:** Carry/selection/preview đúng giới hạn, không leak information và consumption authoritative.

### Story 3.11: Four authoritative throwable archetypes và Epic 3 gate

As a người chơi,
I want frag, smoke, stun và molotov có tác dụng phân biệt,
So that vật ném mở ra nhiều cách xử lý cover và giao tranh.

**Source Requirements:** FR48–FR50; NFR14, NFR18, NFR27, NFR31.

**Depends on:** Story 3.10 và Story 2.5–2.12.

**Blocks:** Epic 4 và performance hardening Epic 10.

**Module/File Ownership:** Throwable simulation/effects, server area queries, presentation pooling và Epic 3 scenarios.

**Platform Applicability:** Linux headless authority và năm client presentation.

**Acceptance Criteria:**

**Given** committed throw  
**When** fuse/impact resolve  
**Then** frag, smoke, stun và molotov dùng đúng fuse/radius/duration/effect từ GDD manifest  
**And** damage/status/area ownership do server xác nhận.

**Given** smoke/fire/stun presentation  
**When** platform variant render  
**Then** geometry/timing/visibility/gameplay area tương đương, chỉ quality khác  
**And** tối đa sáu smoke dày gần player vẫn có profiling marker cho NFR18.

**Given** Epic 3 scenario pack  
**When** chạy inventory→pickup→heal→loot→airdrop→throwable flows dưới impairment  
**Then** không item duplication/loss, false progress hoặc client commit  
**And** mọi FR30/34–50 có evidence trace.

**Error/Recovery Path:** Effect definition/query lỗi reject/terminate entity deterministic; presentation fallback không thay authoritative area.

**Test Boundary:** Mỗi archetype golden, fuse/radius/duration, stacked effects, pooling reset, impairment transactions và full Epic 3 traceability.

**Definition of Done:** Bốn throwable hoạt động authoritative; inventory/loot flow đạt gate; Epic 4 được mở khóa.

## Epic 4: Một trận battle royale hoàn chỉnh

Người chơi có thể trải qua vòng lặp từ lobby thử nghiệm, máy bay, đổ bộ, loot, DBNO, chín pha bo, spectate đến kết quả trong một match host hoàn chỉnh.

### Story 4.1: Guarded application và Standard match lifecycle

As a người chơi,
I want trận chuyển qua các giai đoạn hợp lệ,
So that tôi không bị kẹt hoặc nhận trạng thái mâu thuẫn.

**Source Requirements:** FR1, FR3, FR7, FR12; NFR19–NFR20, NFR27, NFR29.

**Depends on:** Epic 1–3.

**Blocks:** Story 4.2–4.13.

**Module/File Ownership:** Shared match state machine, client application lifecycle, server match host transitions và lifecycle fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** Standard match được tạo  
**When** lifecycle chạy  
**Then** transitions phải theo bảng guard từ Preparing/Lobby/Aircraft/Drop/Active/Finalizing/Results/Closed  
**And** không dùng nhóm boolean chồng chéo làm phase authority.

**Given** command/event không hợp lệ cho phase hiện tại  
**When** validate  
**Then** transition/mutation bị reject với current state và allowed destinations  
**And** phase change chỉ commit một lần có tick/sequence.

**Given** process/client lifecycle change  
**When** cleanup/finalize  
**Then** owner/timer/entity/subscription đóng theo thứ tự deterministic  
**And** không bỏ qua authoritative result nếu match đã đủ điều kiện kết thúc.

**Error/Recovery Path:** Invalid invariant chuyển match sang Match-critical finalization có evidence; client nhận explicit terminal state.

**Test Boundary:** Transition-table exhaustive tests, duplicate/out-of-order events, failure injection và full lifecycle deterministic replay.

**Definition of Done:** Application/match lifecycle guarded, không state mâu thuẫn và là nền cho toàn bộ phase story.

### Story 4.2: Solo, Duo, Squad roster và Standard ruleset

As a người chơi,
I want chọn Solo, Duo hoặc Squad trước trận,
So that luật đội và điều kiện thắng phù hợp lựa chọn.

**Source Requirements:** FR1–FR2, FR5–FR6, FR9; NFR27, NFR31, NFR54.

**Depends on:** Story 4.1.

**Blocks:** Story 4.3–4.7, Story 4.9–4.13.

**Module/File Ownership:** Mode definitions, team/roster aggregate, Standard rule validator và tests.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** mode selection  
**When** roster validate  
**Then** Solo có player đơn, Duo tối đa 50 team ×2 và Squad tối đa 25 team ×4 cho target 100  
**And** team/player IDs stable suốt trận.

**Given** Standard ruleset  
**When** content/capability validate  
**Then** không respawn, buyback, self-revive hoặc recall station  
**And** mọi player bắt đầu tay trắng theo Epic 3.

**Given** roster/mode mismatch hoặc duplicate membership  
**When** match start guard chạy  
**Then** start bị từ chối có reason  
**And** không tự đổi mode, team size hoặc thêm bot.

**Error/Recovery Path:** Invalid roster trả về pre-match owner với correction; signed ruleset mismatch hủy match trước aircraft.

**Test Boundary:** Solo/Duo/Squad capacity, team identity, prohibited capability scan và invalid roster cases.

**Definition of Done:** Ba mode có roster/rules rõ, Standard không có revive ngoài DBNO teammate và không silent fallback.

### Story 4.3: 60-second pre-match waiting room

As a người chơi,
I want một khoảng chuẩn bị có đếm giờ rõ,
So that client tải xong và tôi biết khi nào trận bắt đầu.

**Source Requirements:** FR3–FR4; NFR7, NFR12, NFR19, NFR31.

**Depends on:** Story 4.1–4.2.

**Blocks:** Story 4.4–4.5.

**Module/File Ownership:** Pre-match phase controller, readiness/load reports, minimal lobby HUD và tests.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** match roster đủ điều kiện và clients load critical assets  
**When** pre-match bắt đầu  
**Then** server chạy countdown 60 giây bằng `ServerTick` và replicate remaining time  
**And** client timer không tự quyết định aircraft transition.

**Given** client chưa ready, disconnect hoặc content hash sai  
**When** start guard đánh giá  
**Then** áp policy explicit trước deadline hoặc từ chối client/match  
**And** không kéo dài vô hạn hay âm thầm đổi roster bằng bot.

**Error/Recovery Path:** Timer/state desync reconcile từ phase snapshot; match-critical readiness lỗi kết thúc với destination rõ.

**Test Boundary:** Exact 60-second ticks, join/load readiness, disconnect boundaries, timer reconciliation và five-platform critical-asset smoke.

**Definition of Done:** Waiting room 60 giây authoritative, readiness có guard và transition aircraft deterministic.

### Story 4.4: Flight path, aircraft, drop và parachute

As a người chơi,
I want đọc đường bay và điều khiển điểm rơi,
So that chiến lược trận bắt đầu trước khi chạm đất.

**Source Requirements:** FR3–FR4; NFR27, NFR29, NFR31, NFR35.

**Depends on:** Story 4.3 và Epic 1 movement/camera.

**Blocks:** Story 4.5, Story 4.13 và full Map UI.

**Module/File Ownership:** Aircraft/drop simulation, flight-path seed stream, parachute controller, camera presentation và fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** match seed/map bounds  
**When** flight path tạo  
**Then** server chọn path hợp lệ bằng purpose RNG và replicate stable path/aircraft timing  
**And** runtime không sinh/đổi geometry map.

**Given** player trên aircraft  
**When** jump/freefall/parachute commands  
**Then** player điều khiển tốc độ/khoảng bay theo GDD và server xác nhận position/state  
**And** camera cho phép đọc địa hình, path và parachute đối thủ trong information contract.

**Given** late/invalid jump hoặc landing query lỗi  
**When** validate  
**Then** server dùng deterministic boundary/fallback landing policy  
**And** không cho client teleport/chọn position tùy ý.

**Error/Recovery Path:** Aircraft/path config lỗi chặn match trước departure; player-state lỗi đưa về safe authoritative drop state có evidence.

**Test Boundary:** Path bounds/seed, jump timing, parachute motion/landing, visual parity và network correction.

**Definition of Done:** Aircraft→drop→landing hoàn chỉnh, authoritative và tái lập theo seed.

### Story 4.5: Standard phase orchestration và match duration

As a người chơi,
I want trận tiến triển tới kết thúc trong nhịp độ dự kiến,
So that mỗi phase có mục tiêu và không kéo dài vô hạn.

**Source Requirements:** FR3, FR6, FR12; NFR19–NFR20, NFR27, NFR29.

**Depends on:** Story 4.1–4.4.

**Blocks:** Story 4.6–4.13.

**Module/File Ownership:** Match phase orchestrator, alive/team counters, terminal guards và timing fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** Standard match active  
**When** phase/time/alive state thay đổi  
**Then** orchestrator hướng tới phiên 28–35 phút theo approved schedule  
**And** có thể kết thúc sớm khi chỉ còn một player/team hợp lệ.

**Given** concurrent elimination/zone/leave events  
**When** terminal guard chạy  
**Then** winner/placement được xác định một lần theo committed event order  
**And** không client nào tự công nhận thắng.

**Error/Recovery Path:** Counter/invariant mismatch rebuild từ authoritative roster/entity state; không chọn winner bằng client report.

**Test Boundary:** Duration schedule, early-end, simultaneous terminal events, Solo/team counters và deterministic placements.

**Definition of Done:** Match không kéo dài vô hạn, kết thúc đúng alive/team condition và tạo terminal event duy nhất.

### Story 4.6: DBNO bleed state và restrictions

As a người chơi Duo/Squad,
I want được gục trước khi bị loại,
So that đồng đội có cơ hội cứu trong rủi ro.

**Source Requirements:** FR5, FR31, FR33; NFR27, NFR29, NFR31.

**Depends on:** Story 2.6, Story 4.2, Story 4.5.

**Blocks:** Story 4.7, Story 4.9–4.13.

**Module/File Ownership:** Health DBNO domain, team-state integration, movement/action restrictions và fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** Duo/Squad player về 0 HP và team còn khả năng chiến đấu  
**When** damage commit  
**Then** player vào DBNO với 100 bleed HP, drain đầu 2 HP/s và mỗi lần gục sau tăng gấp đôi  
**And** Solo đi thẳng elimination.

**Given** DBNO active  
**When** command đến  
**Then** chỉ crawl 0,7 m/s, mark và voice hợp lệ; weapon/heal/self-revive bị khóa  
**And** bleed/state dùng server tick.

**Given** bleed HP về 0 hoặc damage kết liễu hợp lệ  
**When** resolve  
**Then** elimination commit một lần  
**And** không có Standard self-save/respawn.

**Error/Recovery Path:** DBNO counter/state invariant lỗi fail-closed sang canonical health/team resolution có evidence.

**Test Boundary:** Solo bypass, bleed rates qua repeated downs, action matrix, crawl speed và finish/elimination ordering.

**Definition of Done:** DBNO đúng mode/rate/restriction, authoritative và nối được revive/team elimination.

### Story 4.7: Revive, team elimination và victory rules

As a thành viên đội,
I want cứu đồng đội và nhận kết quả thắng/thua đúng,
So that teamwork và người sống cuối cùng được công nhận.

**Source Requirements:** FR5–FR6, FR9, FR32; NFR20, NFR27, NFR31.

**Depends on:** Story 3.3, Story 4.6.

**Blocks:** Story 4.9–4.13.

**Module/File Ownership:** Revive interaction, team outcome resolver, committed result events và tests.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** reviver/DBNO teammate hợp lệ trong range  
**When** revive giữ đủ 10 giây  
**Then** server commit revive theo approved post-revive health state  
**And** movement hoặc damage của reviver ngắt với reason.

**Given** không thành viên team nào còn có thể chiến đấu  
**When** elimination resolve  
**Then** team bị loại và placement khóa  
**And** Duo/Squad thắng nếu ít nhất một thành viên còn sống sau khi mọi team khác bị loại.

**Given** duplicate revive/elimination hoặc target state đổi  
**When** validate  
**Then** idempotency/state guard ngăn double mutation  
**And** không mở self-revive/respawn.

**Error/Recovery Path:** Revive conflict trả canonical DBNO/team state; result invariant mismatch chuyển match finalization critical.

**Test Boundary:** Exact 10-second timer, all interruptions, simultaneous revive/damage, team wipe/win và duplicate events.

**Definition of Done:** Revive/team outcome đúng timing/mode, không self-revive và victory event duy nhất.

### Story 4.8: Nine-phase safe zone và reveal contract

As a người chơi,
I want bo thu theo lịch rõ và vùng kế tiếp chỉ lộ đúng lúc,
So that di chuyển là quyết định có thể lập kế hoạch nhưng không bị dự báo quá mức.

**Source Requirements:** FR90–FR91; NFR27, NFR29, NFR31.

**Depends on:** Story 4.5.

**Blocks:** Story 4.13, Epic 5 zone validators và Map UI.

**Module/File Ownership:** Zone simulation/scheduler, zone RNG stream, damage integration, replication và fixtures.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** signed nine-phase table và match seed  
**When** zone scheduler chạy  
**Then** wait/shrink/radius/outside damage/survival target từng phase theo GDD  
**And** zone RNG tách khỏi loot/vehicle/weather.

**Given** phase wait bắt đầu  
**When** next zone được commit  
**Then** client mới nhận/hiển thị next zone  
**And** không có forecast item hoặc random instant-kill bombing zone.

**Given** player ngoài zone  
**When** damage ticks  
**Then** server xác nhận damage theo current phase/tick  
**And** pause/map/inventory không dừng zone.

**Error/Recovery Path:** Zone geometry/table invalid chặn match/map manifest; runtime invariant lỗi finalizes Match-critical thay vì dùng vùng client.

**Test Boundary:** Nine-phase golden timeline, reveal timing, outside damage, RNG isolation và reconnect/snapshot phase restoration.

**Definition of Done:** Chín phase chạy deterministic, reveal đúng thời điểm và damage hoàn toàn authoritative.

### Story 4.9: Teammate-only spectator với information parity

As a người chơi đã bị loại,
I want theo dõi đồng đội còn sống,
So that tôi vẫn đồng hành mà không cung cấp thông tin bất hợp lệ.

**Source Requirements:** FR8; NFR31–NFR35; UX-DR45–UX-DR46.

**Depends on:** Story 4.6–4.7.

**Blocks:** Story 4.13 và Epic 8 spectator UI.

**Module/File Ownership:** Spectator state/target resolver, camera/information filters và spectator tests.

**Platform Applicability:** Năm client; server xác nhận target/permissions.

**Acceptance Criteria:**

**Given** player bị loại nhưng team còn sống  
**When** vào spectator  
**Then** chỉ follow teammate sống, không free camera, cho tới team eliminated hoặc player leave  
**And** target switch chỉ tới candidate server xác nhận.

**Given** spectator nhận HUD/map/audio/damage state  
**When** presentation lọc  
**Then** chỉ thông tin hợp lệ của target được hiển thị  
**And** spectator không có inventory riêng, marker bí mật hoặc tạo ping chiến thuật mới; voice chỉ theo parity policy.

**Error/Recovery Path:** Target mất/invalid chọn teammate hợp lệ kế tiếp hoặc team-eliminated destination; không rơi vào free camera.

**Test Boundary:** Target lifecycle, information-field allowlist, voice/ping permissions, team wipe và platform camera parity.

**Definition of Done:** Spectator teammate-only, không extra information và có terminal transitions rõ.

### Story 4.10: Leave consequences theo aircraft/team state

As a người chơi,
I want hậu quả rời trận được nói và áp dụng đúng,
So that tôi không bị tính thất bại sai sau khi đội đã kết thúc.

**Source Requirements:** FR7–FR8; NFR20, NFR27; UX-DR54.

**Depends on:** Story 4.1–4.7, Story 4.9.

**Blocks:** Story 4.11–4.13 và reconnect policy Epic 6.

**Module/File Ownership:** Leave command/policy, outcome resolver, confirmation-state contract và tests.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** aircraft đã departure và player/team chưa eliminated  
**When** leave commit  
**Then** player nhận failure consequence theo mode/team state  
**And** confirmation microcopy phản ánh chính xác hậu quả trước action.

**Given** team đã eliminated  
**When** player leave từ spectator/results transition  
**Then** không áp failure penalty mới/sai  
**And** placement/result đã khóa không bị sửa.

**Given** disconnect chưa phân loại voluntary/recoverable  
**When** baseline policy xử lý  
**Then** giữ seat/avatar state explicit cho reconnect contract sau  
**And** không tự coi là safe leave.

**Error/Recovery Path:** Outcome state thiếu từ chối leave finalization cho tới canonical snapshot hoặc match-ended fallback có evidence.

**Test Boundary:** Pre/post aircraft, Solo/team alive/eliminated, spectator leave, duplicate command và disconnect distinction.

**Definition of Done:** Leave consequence đúng phase/team state, không false failure sau elimination và có seam cho reconnect.

### Story 4.11: Server-confirmed match results và statistics

As a người chơi,
I want kết quả phản ánh chính xác trận vừa chơi,
So that placement và thống kê có thể tin cậy.

**Source Requirements:** FR10, FR12; NFR2, NFR20, NFR27, NFR30.

**Depends on:** Story 4.5–4.10.

**Blocks:** Story 4.12–4.13, Epic 9 persistence/summary.

**Module/File Ownership:** Result aggregate, combat/survival stat reducers, committed result payload và evidence fixtures.

**Platform Applicability:** Linux headless authority; năm client consume payload.

**Acceptance Criteria:**

**Given** match terminal event  
**When** result reducer finalize  
**Then** payload có placement, survival time, kills/assists và minimum combat/survival stats từ committed events  
**And** result ID/match ID/schema version/hash ổn định.

**Given** duplicate finalization hoặc late combat event  
**When** result đã khóa  
**Then** same command/payload idempotent, payload khác là security/invariant error  
**And** client/local config không sửa result.

**Error/Recovery Path:** Reducer/evidence gap đánh dấu result Unavailable/critical theo policy, không dựng stats giả; match vẫn có terminal state.

**Test Boundary:** Solo/team placements, simultaneous eliminations, kill/assist reducers, idempotency và replay-to-result equivalence.

**Definition of Done:** Result payload authoritative/versioned, tái tạo được từ events và sẵn sàng persistence/UI.

### Story 4.12: Results actions và Report/Block intent entry

As a người chơi sau trận,
I want chơi lại, về Lobby hoặc mở Report/Block đúng đối tượng,
So that tôi có bước tiếp theo rõ ràng.

**Source Requirements:** FR11; UX-DR31, UX-DR47, UX-DR54.

**Depends on:** Story 4.11.

**Blocks:** Story 4.13, Epic 9 deep Results/Report/Block.

**Module/File Ownership:** Minimal Results presenter/view state, replay/lobby transitions, moderation-intent port và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** result payload hợp lệ  
**When** Results mở  
**Then** placement/survival/kills/assists được hiển thị và Play Again/local test queue, Lobby đều hoạt động  
**And** không reward loop, store hoặc fabricated kill-cam.

**Given** eligible participant target  
**When** chọn Report hoặc Block  
**Then** route tạo typed intent với match/target IDs và mở minimal draft/local-block adapter chức năng  
**And** invalid/self/nonparticipant target bị từ chối rõ.

**Given** payload chưa có/không thể có  
**When** presenter load  
**Then** hiển thị Pending/Unavailable  
**And** actions không phụ thuộc stats tự dựng.

**Error/Recovery Path:** Navigation/adapter unavailable giữ Results và hiển thị capability state; draft intent không mất khi retry trong phiên.

**Test Boundary:** Results states, three actions, target eligibility, navigation failure và no-commercial-elements scan.

**Definition of Done:** Results có actions hoạt động trong current environment và moderation entry dùng typed contract, không chờ UI/backend tương lai để test.

### Story 4.13: Full Standard match loop và replay gate

As a người chơi,
I want chơi trọn một trận từ waiting room tới Results,
So that vòng battle royale cốt lõi được chứng minh trước khi thêm world/network scale.

**Source Requirements:** FR1–FR12, FR31–FR33, FR90–FR91; NFR1–NFR3, NFR19–NFR20, NFR27.

**Depends on:** Story 4.1–4.12 và Epic 1–3 gates.

**Blocks:** Epic 5–6.

**Module/File Ownership:** Full-loop scenario pack, evidence replay fixtures, match reports và gate configuration.

**Platform Applicability:** Linux headless reference và representative clients của năm platform family.

**Acceptance Criteria:**

**Given** scripted Solo/Duo/Squad scenarios  
**When** chạy waiting→aircraft→drop→loot/combat→DBNO/zone→spectate→Results  
**Then** mọi phase/transition/outcome đúng ruleset và result tái tạo từ committed events  
**And** không capability Standard bị cấm xuất hiện.

**Given** disconnect/leave/simultaneous damage/zone edge cases  
**When** impairment/replay chạy  
**Then** placement/winner/result không phân kỳ  
**And** ít nhất 90% death scenarios trong internal replay set có causal explanation đúng.

**Given** gate fail  
**When** report tổng hợp  
**Then** giữ build/manifest/seed/match/tick reproduction và block Epic 5–6  
**And** không waive bằng client authority hoặc bỏ phase.

**Error/Recovery Path:** Failed scenario được rerun từ fixture/checkpoint; baseline chỉ đổi qua reviewed rule/data decision.

**Test Boundary:** Full-loop deterministic matrix, Solo/Duo/Squad, phase/leave/DBNO/zone/results edges và evidence explainability.

**Definition of Done:** Core battle royale loop hoàn chỉnh, trace đủ FR, result/replay tin cậy và sẵn sàng world/network expansion.

## Epic 5: World/Vehicle Slice 2×2 km

Người chơi có thể đi bộ, bơi và lái phương tiện qua một lát cắt gồm POI dày, compound thưa, đường, cầu, bờ biển và thời tiết mà không gặp lỗi streaming hoặc gameplay parity.

### Story 5.1: MapDefinition, TerrainTileData và deterministic bake pipeline

As a đội xây world,
I want map được author bằng schema và bake có kiểm định,
So that runtime chỉ tải content đã version hóa và có thể tái tạo.

**Source Requirements:** FR83–FR87; NFR29, NFR31, NFR46–NFR48, NFR55.

**Depends on:** Epic 1–4.

**Blocks:** Story 5.2–5.7, Story 5.13 và Epic 7.

**Module/File Ownership:** Shared map schema, `game/tools/{terrain_bake,map_validation,manifest_builder}`, generated tile/cell manifests và tests.

**Platform Applicability:** Editor/bake pipeline, năm client và Linux headless server.

**Acceptance Criteria:**

**Given** map authoring source  
**When** bake  
**Then** `MapDefinition` chứa terrain index, water/coast, POI/compound, road, buildings, cover, loot/vehicle/dock, navigation/connectivity và validation rules  
**And** Terrain3D `1.0.2` chỉ chạy editor rồi bake versioned `TerrainTileData`.

**Given** generated world artifacts  
**When** CI kiểm tra  
**Then** file có `generated_do_not_edit`, source/dependency/checksum manifest và client/server gameplay hash tương thích  
**And** sửa generated file trực tiếp bị static gate chặn.

**Given** match seed  
**When** runtime tạo trận  
**Then** seed chỉ chọn loot, vehicle, flight path, weather và zone  
**And** không tái sinh geometry map runtime.

**Error/Recovery Path:** Schema/dependency/validator lỗi dừng bake, giữ signed map manifest trước và chỉ sửa source rồi regenerate.

**Test Boundary:** Schema round-trip, deterministic bake/hash, generated-edit guard, seed isolation và server package-content tests.

**Definition of Done:** Pipeline bake map/tile/cell versioned, deterministic, không runtime geometry generation và đủ seam cho 2×2 slice.

### Story 5.2: Terrain, coastline và hydrology slice dùng texture đã duyệt

As a người chơi,
I want địa hình, bờ biển và nước có collision rõ,
So that đi bộ/bơi không gặp seam hoặc bề mặt giả.

**Source Requirements:** FR84–FR87; NFR31, NFR35, NFR46–NFR48, NFR55.

**Depends on:** Story 5.1 và Story 1.7, Story 1.12.

**Blocks:** Story 5.3–5.7, Story 5.13.

**Module/File Ownership:** `content-source/terrain`, approved `game/assets/environment`, terrain/coast/water authoring, bake/validator reports.

**Platform Applicability:** Năm client và Linux headless collision/water data.

**Acceptance Criteria:**

**Given** 36 texture candidate và subset đã duyệt ở Story 1.12  
**When** author terrain material set  
**Then** đất/đá/bê tông hợp lệ phải có stable surface ID, texel scale, alpha/channel semantics, compression profile và provenance  
**And** không suy đoán PBR map còn thiếu hoặc import quarantine path trực tiếp.

**Given** 2×2 km height/coast/water source  
**When** bake tile data  
**Then** terrain visual, collision, material mask, mesh LOD, gameplay water surface/depth và coastline seam cùng version  
**And** desktop/mobile visual wave không thay gameplay surface.

**Given** tile seam, hole, invalid slope hoặc water mismatch  
**When** validator chạy  
**Then** manifest signing bị chặn với tọa độ/cell/material reason  
**And** server/client không load partial slice.

**Error/Recovery Path:** Texture/material không đạt dùng approved neutral material; geometry/hydrology lỗi giữ map manifest trước.

**Test Boundary:** Terrain seam/height/collision/material tests, water-depth transitions, visual-vs-gameplay surface parity, mobile memory/compression và provenance.

**Definition of Done:** 2×2 terrain/coast/water bake sạch, dùng thật subset texture hợp lệ và có collision/surface parity.

### Story 5.3: Hierarchical world streaming và cell leases

As a người chơi,
I want di chuyển qua world không bị giật hoặc mất vật thể gameplay,
So that traversal và combat không hỏng ở cell boundary.

**Source Requirements:** FR83–FR87; NFR46–NFR48.

**Depends on:** Story 5.1–5.2.

**Blocks:** Story 5.4–5.7, Story 5.13 và Epic 7 scale.

**Module/File Ownership:** Shared world cells/spatial, client streaming, server spatial queries, cache/lease system và streaming harness.

**Platform Applicability:** Năm client và Linux headless server với cadence/grid riêng.

**Acceptance Criteria:**

**Given** player/vehicle traversal corridor  
**When** streaming cập nhật  
**Then** terrain/entity/building HLOD/navigation/audio/server-query dùng hierarchical grids/cadence độc lập  
**And** `WorldCellId` là identity ổn định, 250×250 m chỉ là benchmark hypothesis.

**Given** async prefetch/load/cancel  
**When** generation thay đổi  
**Then** generation/cancellation ID, high/low-water cache và cell lease ngăn stale commit/unload  
**And** gameplay readiness hoàn tất trước presentation readiness.

**Given** projectile/vehicle/door/reference/async commit còn active  
**When** cell muốn unload  
**Then** lease giữ cell và entity không destroy/recreate khi qua boundary  
**And** main-thread instantiation nằm trong budget.

**Error/Recovery Path:** Load fail dùng bounded retry/degraded visual nhưng giữ gameplay collision/state; budget/invariant lỗi block gate.

**Test Boundary:** Rapid traversal, cancellation races, lease cases, entity identity, hitch/memory profiling và network impairment.

**Definition of Done:** Slice stream qua boundary không mất gameplay entity/collision, cache/lease bounded và có metrics/debug inspector.

### Story 5.4: Two-POI layout, compounds và road graph

As a người chơi,
I want POI dày, vùng thưa và đường nối tạo nhiều lựa chọn,
So that di chuyển trong slice không có một tuyến tối ưu duy nhất.

**Source Requirements:** FR84–FR85, FR87; NFR25, NFR31, NFR46.

**Depends on:** Story 5.1–5.3.

**Blocks:** Story 5.5–5.6, Story 5.13 và Epic 7 layout.

**Module/File Ownership:** POI/compound source, road graph, connectivity validator và map-analysis scenarios.

**Platform Applicability:** Bake/headless analysis và năm client.

**Acceptance Criteria:**

**Given** 2×2 km slice  
**When** author layout  
**Then** có hai POI đại diện, compound thưa, road/bridge/coast routes và risk/loot tags  
**And** graph dùng stable node/edge IDs trong MapDefinition.

**Given** bridge/pass/choke  
**When** connectivity validator chạy  
**Then** có bypass chậm hơn và không tồn tại choke bắt buộc duy nhất vào playable region  
**And** route vẫn hợp lệ cho foot/vehicle/boat profile tương ứng.

**Error/Recovery Path:** Disconnected/one-choke graph chặn bake với route witness; không sửa runtime path tùy seed.

**Test Boundary:** Connectivity, alternate-route cost, spawn-to-POI access, vehicle width/slope và deterministic graph bake.

**Definition of Done:** Hai POI/compound/road graph nối hợp lệ, có bypass và sẵn sàng building/cover placement.

### Story 5.5: Modular building kit và two-POI validator

As a người chơi,
I want công trình có thể vào và cover/opening giống nhau trên mọi thiết bị,
So that tôi tin tưởng góc bắn và đường đi trong nhà.

**Source Requirements:** FR84–FR85; NFR31, NFR35, NFR46–NFR48, NFR55.

**Depends on:** Story 5.4.

**Blocks:** Story 5.6, Story 5.13 và Epic 7 building expansion.

**Module/File Ownership:** `content-source/buildings`, gameplay shells, desktop/mobile variants, placement/validator tools và tests.

**Platform Applicability:** Năm client và Linux headless collision/opening data.

**Acceptance Criteria:**

**Given** modular building source đủ provenance  
**When** promote/bake  
**Then** gameplay shell/collision/openings tách khỏi desktop/mobile visual LOD  
**And** stable module/socket/building IDs không phụ thuộc scene path.

**Given** buildings đặt tại hai POI  
**When** validator chạy  
**Then** entrance, stairs, windows, cover, loot anchors, collision và navigation đều reachable/consistent  
**And** platform variants giữ silhouette/opening/visibility semantics.

**Error/Recovery Path:** Module/placement lỗi bị loại riêng hoặc block POI manifest; không tự sửa collision chỉ trên client.

**Test Boundary:** Socket/scale/topology/collision, enterability/routes, cover/LOS, HLOD swap và five-platform parity snapshots.

**Definition of Done:** Modular kit và hai POI enterable đạt validator, tách gameplay shell khỏi visuals và mở đường cho 420-building expansion.

### Story 5.6: Cover, choke và final-circle playability validators

As a người chơi,
I want khoảng trống và bo cuối luôn có counterplay,
So that địa hình không ép tôi chết vì một choke hoặc vùng không đứng được.

**Source Requirements:** FR84–FR86; NFR25, NFR31, NFR35.

**Depends on:** Story 5.2, Story 5.4–5.5 và Story 4.8.

**Blocks:** Story 5.13 và Epic 7 validation.

**Module/File Ownership:** Map-analysis cover/choke/zone validators, route witnesses và reports.

**Platform Applicability:** Headless bake/analysis; results áp cho mọi platform.

**Acceptance Criteria:**

**Given** open span dài trên 120 m  
**When** cover validator scan  
**Then** có ít nhất hai lựa chọn từ hard cover, depression, smoke route, vehicle hoặc flank  
**And** report chỉ rõ sampled paths và line-of-sight.

**Given** bridge/pass/landmass route  
**When** choke validator chạy  
**Then** có bypass chậm hơn, không mandatory single choke  
**And** bypass không dựa vào exploit collision/visual-only cover.

**Given** candidate final circle  
**When** playability validate  
**Then** ≤50% diện tích nằm trên water, unstandable cliff hoặc inaccessible roof  
**And** candidate fail bị loại khỏi signed zone set.

**Error/Recovery Path:** Insufficient nav/terrain data làm validator fail unknown, không mặc định pass.

**Test Boundary:** Synthetic known-pass/fail maps, full slice scans, platform collision parity và deterministic reports.

**Definition of Done:** Slice đạt cover/choke/final-circle rules với machine-readable evidence.

### Story 5.7: Deterministic weather và gameplay modifiers

As a người chơi,
I want thời tiết thay đổi tầm nhìn/âm thanh theo luật biết trước,
So that thích nghi có chiến thuật mà không bị đổi đột ngột.

**Source Requirements:** FR87–FR89; NFR29, NFR31, NFR35, NFR44.

**Depends on:** Story 5.1–5.3.

**Blocks:** Story 5.13 và Epic 7 weather expansion.

**Module/File Ownership:** Weather definitions/RNG, gameplay modifiers, client weather presentation và tests.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** match seed  
**When** weather chọn lúc start  
**Then** clear/rain/fog weights là 70%/15%/15% bằng weather RNG stream riêng  
**And** weather không đổi đột ngột giữa trận.

**Given** rain hoặc fog active  
**When** gameplay/presentation apply  
**Then** rain giảm footstep hearing range 15%; fog giới hạn target contrast sau 180–250 m theo profile  
**And** desktop/mobile giữ cùng information range.

**Error/Recovery Path:** Weather definition/shader/audio lỗi giữ gameplay state với approved degraded visuals và capability metric; không đổi sang clear âm thầm nếu modifier đã commit.

**Test Boundary:** Weighted distribution, RNG isolation, 15% audio range, fog contrast distance, long-session stability và platform parity.

**Definition of Done:** Ba weather states deterministic, modifiers chính xác và presentation degraded không đổi gameplay.

### Story 5.8: Six vehicle archetypes và asset contract

As a người chơi,
I want sáu loại phương tiện có vai trò/chỗ ngồi rõ,
So that chọn xe phù hợp route và đội hình.

**Source Requirements:** FR51–FR52; NFR31, NFR35, NFR55.

**Depends on:** Story 3.1, Story 5.1, Story 5.5.

**Blocks:** Story 5.9–5.13.

**Module/File Ownership:** Vehicle definitions, content-source/assets/vehicles, skeleton/socket/collision validators và manifest.

**Platform Applicability:** Năm client và Linux headless gameplay definitions.

**Acceptance Criteria:**

**Given** vehicle catalog  
**When** bake  
**Then** sedan, jeep, pickup, motorcycle, boat và truck có stable ID, seats, 80–125 km/h max-speed profile, fuel, HP, four-tire state và audio radius 250–450 m  
**And** values nằm trong approved manifest.

**Given** local `Vehicles_SciFi` hoặc asset khác  
**When** promotion review  
**Then** chỉ asset đúng license/provenance/scale/topology/LOD/collision/silhouette được dùng làm placeholder phù hợp  
**And** visual không được thay seat/collision/gameplay dimensions.

**Error/Recovery Path:** Visual asset fail dùng primitive approved; gameplay definition invalid chặn manifest.

**Test Boundary:** Catalog completeness, range/seat/tire schema, collision/scale/LOD và five-platform silhouette/package parity.

**Definition of Done:** Sáu archetype có data/asset contract hợp lệ, không phụ thuộc presentation để chạy server.

### Story 5.9: Server vehicle physics, driving, fuel, tires và audio events

As a người lái,
I want xe phản hồi theo trạng thái nhiên liệu/lốp,
So that điều khiển và hỏng hóc có thể dự đoán.

**Source Requirements:** FR52, FR55; NFR27, NFR31, NFR44, NFR46.

**Depends on:** Story 5.3, Story 5.8.

**Blocks:** Story 5.10–5.13.

**Module/File Ownership:** Server vehicle authority/Jolt adapter, vehicle input/state, fuel/tire simulation, audio events và fixtures.

**Platform Applicability:** Linux headless authority và năm client prediction/presentation.

**Acceptance Criteria:**

**Given** driver command hợp lệ  
**When** server Jolt vehicle tick chạy  
**Then** acceleration/steering/brake/max speed/fuel/tire modifiers theo manifest  
**And** client không báo position, collision, fuel hoặc tire truth.

**Given** vehicle vận hành  
**When** semantic engine/tire/surface event phát  
**Then** client trình bày audio trong radius 250–450 m theo archetype  
**And** approved vehicle audio từ intake chỉ dùng sau provenance/loudness review.

**Error/Recovery Path:** Physics invariant/NaN freeze vehicle tại safe authoritative state, reject control và emit Match-critical vehicle evidence nếu không recover.

**Test Boundary:** Speed/fuel/tire matrix, server correction, slopes/surfaces, audio radius và long-run physics stability.

**Definition of Done:** Driving authoritative, fuel/tire/audio state đúng manifest và ổn qua streaming boundary.

### Story 5.10: Vehicle seats, enter/exit và camera

As a người chơi,
I want vào, đổi ghế và rời xe an toàn,
So that cả đội sử dụng phương tiện không bị kẹt hoặc teleport.

**Source Requirements:** FR51–FR53; NFR27, NFR31; UX-DR19–UX-DR20.

**Depends on:** Story 1.8–1.9, Story 5.8–5.9.

**Blocks:** Story 5.11–5.13.

**Module/File Ownership:** Vehicle seat aggregate, enter/exit interaction, safe-exit query, camera adapter và tests.

**Platform Applicability:** Năm client và Linux headless authority.

**Acceptance Criteria:**

**Given** valid seat/range/state  
**When** enter/switch/exit commit  
**Then** occupancy mutation atomic, driver authority đúng seat và character identity không destroy/recreate  
**And** exit dùng safe position query, vehicle safety/exit có interaction priority.

**Given** exit blocked hoặc vehicle đang nguy hiểm  
**When** action request  
**Then** server từ chối với reason hoặc dùng approved alternate exit  
**And** camera/context card phản ánh canonical seat/vehicle state.

**Error/Recovery Path:** Seat conflict trả fresh occupancy; no-safe-exit giữ player trong seat và luôn còn retry/alternate path.

**Test Boundary:** Concurrent enter, seat switch, blocked exits, streaming crossing, disconnect driver và camera transitions.

**Definition of Done:** Seat lifecycle atomic, safe exit/camera hoạt động và không entity/authority leak.

### Story 5.11: Server-authoritative vehicle collision damage

As a người chơi,
I want va chạm xe gây sát thương theo tốc độ và che chắn thực,
So that đâm xe nguy hiểm nhưng không bị client khai gian.

**Source Requirements:** FR54–FR55; NFR14, NFR27, NFR31, NFR46.

**Depends on:** Story 5.9–5.10, Story 2.6.

**Blocks:** Story 5.12–5.13.

**Module/File Ownership:** Server collision evidence/resolver, damage integration và vehicle collision fixtures.

**Platform Applicability:** Linux headless authority; năm client presentation.

**Acceptance Criteria:**

**Given** server-confirmed vehicle collision trên 35 km/h  
**When** damage resolve  
**Then** gây damage theo approved curve và trên 70 km/h có thể hạ player không được vật cản che  
**And** cover/relative velocity/contact ownership do server query.

**Given** client tự báo collision/damage hoặc contact stale  
**When** validate  
**Then** report bị bỏ qua/reject  
**And** không mutate HP/vehicle.

**Error/Recovery Path:** Ambiguous contact không gây speculative damage; lưu bounded diagnostic để tái hiện.

**Test Boundary:** 35/70 km/h boundaries, cover, glancing/multiple contacts, client spoof và streaming seam collisions.

**Definition of Done:** Collision damage hoàn toàn server-authoritative, đúng thresholds và replay được.

### Story 5.12: Vehicle fire countdown, explosion và post-exit cues

As a người chơi,
I want biết xe sắp nổ ngay cả sau khi rời ghế,
So that tôi có ba giây phản ứng đáng tin.

**Source Requirements:** FR53, FR55; NFR27, NFR31; UX-DR20.

**Depends on:** Story 5.9–5.11.

**Blocks:** Story 5.13.

**Module/File Ownership:** Vehicle destruction state machine, explosion damage, presentation/audio/VFX và fixtures.

**Platform Applicability:** Linux headless authority và năm client presentation.

**Acceptance Criteria:**

**Given** vehicle HP về 0  
**When** destruction state commit  
**Then** server bắt đầu fire countdown đúng 3 giây rồi xác nhận explosion hoặc explicit cancellation policy  
**And** countdown tiếp tục replicate sau khi player rời seat.

**Given** countdown active  
**When** client trình bày  
**Then** fire/audio/context card hiển thị remaining state rõ, cùng timing/radius mọi platform  
**And** VFX không quyết định damage/explosion.

**Error/Recovery Path:** Presentation mất/rejoin rebuild countdown từ snapshot; server state invariant lỗi resolve terminal once với evidence.

**Test Boundary:** Exact 3-second timer, post-exit/reconnect, duplicate HP-zero, explosion damage/cover và audio/VFX parity.

**Definition of Done:** Countdown/explosion authoritative, cue không mất sau exit và damage/event chỉ commit một lần.

### Story 5.13: Water & Boat 2×2 slice gate

As a người chơi,
I want đi bộ, bơi và đi thuyền xuyên slice ổn định,
So that world/vehicle/water loop được chứng minh trước bản đồ 8×8 km.

**Source Requirements:** FR51–FR55, FR84–FR89; NFR31, NFR35, NFR44, NFR46–NFR48.

**Depends on:** Story 5.1–5.12 và Epic 4.

**Blocks:** Epic 6 scale và Epic 7 production map.

**Module/File Ownership:** World Streaming/Water & Boat scenario pack, device/performance reports và gate configuration.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** scripted foot→swim→boat→vehicle→building routes qua cell boundaries  
**When** slice chạy dưới network/streaming impairment  
**Then** không hitch gameplay-breaking, mất collision/water/entity/audio state hoặc identity recreation  
**And** server/client cùng map/gameplay hash.

**Given** weather, cover/choke/final-zone và vehicle-destruction scenarios  
**When** validators/replay chạy  
**Then** mọi FR Epic 5 có evidence và desktop/mobile information/collision parity  
**And** asset texture/audio/vehicle dùng trong slice đều có promotion manifest.

**Given** budget/parity/validator fail  
**When** gate tổng hợp  
**Then** full-map expansion bị block với reproduction/cell/route/build details  
**And** không waive bằng client authority hoặc giảm gameplay cover.

**Error/Recovery Path:** Failed route/fixture được rerun từ seed/cell snapshot; approved slice manifest chỉ cập nhật sau review.

**Test Boundary:** Streaming/lease soak, water/boat/vehicle routes, weather, validators, five-platform device runs và headless package/content parity.

**Definition of Done:** 2×2 slice đạt Water & Boat/streaming/vehicle gate, dùng asset hợp lệ và mở khóa network scale.

## Epic 6: Trận đấu online cạnh tranh đa nền tảng

Người chơi có thể lập party, chọn vùng/input pool, vào trận qua matchmaking, voice/ping, reconnect và chơi ở các cổng 24→50→100 client với authority, evidence và fairness đầy đủ.

### Story 6.1: PlatformGateway, account/session và degraded capability contract

As a người chơi,
I want đăng nhập và biết rõ dịch vụ nào đang khả dụng,
So that lỗi platform không âm thầm đổi luật trận.

**Source Requirements:** FR80, FR110; NFR28, NFR30, NFR49, NFR55.

**Depends on:** Epic 1–5.

**Blocks:** Story 6.2–6.14.

**Module/File Ownership:** Platform ports/adapters, `AppKernel`/`PlatformGateway`, Nakama adapter, identity/session contracts và tests.

**Platform Applicability:** Windows, Linux, macOS, Android, iOS và backend control plane.

**Acceptance Criteria:**

**Given** platform identity token hợp lệ  
**When** account exchange chạy  
**Then** token đổi thành internal `AccountId` qua typed port, expiry/nonce/replay protection được kiểm tra  
**And** gameplay không dùng Apple/Google/store ID hoặc raw token.

**Given** platform/provider capability unavailable/degraded  
**When** adapter báo state  
**Then** UI/application nhận explicit capability, reason và allowed actions  
**And** không tự đổi gameplay rule, region, input pool hoặc information source.

**Given** Nakama Godot SDK `3.4.0`/control plane versions được dùng  
**When** promote dependency  
**Then** version/checksum/license/wrapper/contract tests phải đạt  
**And** Nakama realtime socket không mang combat snapshots.

**Error/Recovery Path:** Auth/provider failure giữ user ngoài protected action, token/PII không log và retry/backoff bounded.

**Test Boundary:** Adapter contracts, token expiry/replay, degraded matrix, PII/log scan và five-platform mock/live-sandbox smoke.

**Definition of Done:** Account/session đi qua ports, degraded state explicit và không platform SDK nào xâm nhập gameplay.

### Story 6.2: Party roster, leader và Ready invalidation

As a người chơi,
I want lập party tối đa bốn người và thấy trạng thái Ready rõ,
So that cả đội chỉ vào hàng chờ với cấu hình đã xác nhận.

**Source Requirements:** FR80; UX-DR29; NFR19–NFR21, NFR30.

**Depends on:** Story 6.1.

**Blocks:** Story 6.3–6.7, Story 6.14.

**Module/File Ownership:** Backend party aggregate/API, client party presenter/state và contract tests.

**Platform Applicability:** Năm client và Nakama control plane.

**Acceptance Criteria:**

**Given** party 1–4 members  
**When** join/leave/leader/Ready mutation  
**Then** server control plane version/idempotency xác nhận roster và leader duy nhất  
**And** roster, mode, region hoặc input disclosure đổi phải clear Ready.

**Given** concurrent mutation/reconnect  
**When** expected version conflict  
**Then** client nhận canonical party snapshot và reason  
**And** không duplicate member hoặc stale Ready.

**Error/Recovery Path:** Party service degraded giữ local last-known read-only state, disable queue có status rõ và retry bounded.

**Test Boundary:** Capacity/leader transfer, Ready invalidation matrix, concurrency/idempotency và reconnect snapshot.

**Definition of Done:** Party 1–4 authoritative, Ready không stale và đủ seam cho invite/matchmaking.

### Story 6.3: Cross-platform invite provider contract

As a người chơi,
I want mời bạn vào party từ nền tảng của mình,
So that lập đội không phụ thuộc một SDK cụ thể.

**Source Requirements:** FR80, FR110; NFR28, NFR30, NFR49, NFR55.

**Depends on:** Story 6.1–6.2.

**Blocks:** Story 6.5 và party release gate.

**Module/File Ownership:** Invite port/provider adapters, deep-link payload, expiry/security schema và tests.

**Platform Applicability:** Năm client; provider availability có thể khác nhưng state phải explicit.

**Acceptance Criteria:**

**Given** eligible target/provider  
**When** invite create/accept  
**Then** payload dùng internal party/invite IDs, expiry/nonce/signature và idempotent accept  
**And** provider SDK không mutate party trực tiếp.

**Given** provider unsupported, denied hoặc deep link stale  
**When** action xảy ra  
**Then** capability/reason hiển thị rõ và party hiện tại không đổi  
**And** không fallback sang provider khác hoặc public token âm thầm.

**Error/Recovery Path:** Invalid/expired invite fail-closed; retry tạo intent mới, không reuse secret/payload cũ.

**Test Boundary:** Create/accept/decline/expiry/replay, platform degraded adapters và PII/token log scan.

**Definition of Done:** Invite contract an toàn, test được trên mọi platform adapter và failure không làm hỏng party.

### Story 6.4: Region probing và high-latency acknowledgement

As a người chơi,
I want biết vùng mạng phù hợp và được cảnh báo khi ping cao,
So that tôi chủ động chấp nhận chất lượng kết nối.

**Source Requirements:** FR74; NFR21, NFR30; UX-DR18, UX-DR55.

**Depends on:** Story 6.1.

**Blocks:** Story 6.5.

**Module/File Ownership:** Region probe service, latency summary, warning/ack state và tests.

**Platform Applicability:** Năm client và regional control-plane endpoints.

**Acceptance Criteria:**

**Given** available regions  
**When** probe chạy bounded sample  
**Then** report median latency/loss/freshness và ưu tiên region theo policy  
**And** ping >150 ms hiển thị icon+label warning.

**Given** không region nào đạt threshold  
**When** người chơi tiếp tục  
**Then** phải có explicit acknowledgement gắn selection freshness  
**And** hệ thống không tự đổi region sau xác nhận.

**Error/Recovery Path:** Probe timeout/partial results hiển thị Unknown/degraded, không giả số hoặc silently queue.

**Test Boundary:** Latency/loss sampling, >150 ms boundary, all-regions-bad acknowledgement, stale probe và offline state.

**Definition of Done:** Region selection minh bạch, high-latency cần xác nhận và có dữ liệu cho matchmaking.

### Story 6.5: Matchmaking queue, wait policy và newcomer soft MMR

As a người chơi,
I want hàng chờ ưu tiên kết nối và thời gian đợi hợp lý,
So that vào trận công bằng mà không bị khóa bởi xếp hạng cứng.

**Source Requirements:** FR74–FR75, FR78; NFR7, NFR12, NFR21, NFR34.

**Depends on:** Story 6.2–6.4.

**Blocks:** Story 6.6–6.9, Story 6.16–6.18.

**Module/File Ownership:** Nakama queue adapter, matchmaking policy, ticket lifecycle và integration tests.

**Platform Applicability:** Năm client và backend control plane.

**Acceptance Criteria:**

**Given** Ready party với mode/region/input claim  
**When** ticket tạo  
**Then** policy ưu tiên network region, wait time và soft MMR chỉ cho 10 trận đầu để tránh top skill group  
**And** ticket snapshot giữ exact roster/config/disclosures.

**Given** queue timeout/error/cancel  
**When** lifecycle kết thúc  
**Then** party trở về Lobby với reason và Ready state theo policy  
**And** không tự đổi region/mode/pool hoặc vào trận khác.

**Error/Recovery Path:** Backend degraded disable Deploy/queue có capability state; retry dùng idempotency/new ticket policy, không duplicate tickets.

**Test Boundary:** Policy ordering, first-10 boundary, ticket idempotency/cancel/timeout, party mutation và offline Lobby.

**Definition of Done:** Queue lifecycle hoạt động, policy đúng network/wait/newcomer và không silent relaxation.

### Story 6.6: Signed input-family pools và match lock

As a người chơi,
I want biết mình đang vào pool điều khiển nào,
So that fairness không thay đổi giữa trận.

**Source Requirements:** FR76–FR77; NFR31, NFR33–NFR34; UX-DR29.

**Depends on:** Story 1.3, Story 6.2, Story 6.5.

**Blocks:** Story 6.7, Story 6.9, Story 6.16–6.18.

**Module/File Ownership:** Input-family claim/signing, party disclosure/ack, match verifier và tests.

**Platform Applicability:** Năm client, control plane và match server.

**Acceptance Criteria:**

**Given** Keyboard/Mouse, Touch hoặc mixed party  
**When** Ready/ticket tạo  
**Then** control plane ký input-family claim, mixed disclosure cần acknowledgement và match server verify  
**And** claim khóa suốt match.

**Given** external Keyboard/Mouse kết nối mobile giữa trận  
**When** adapter phát hiện  
**Then** gameplay không đổi pool; capability/input restriction explicit và yêu cầu requeue sau trận  
**And** không grant Touch/Keyboard advantage chéo.

**Error/Recovery Path:** Missing/invalid claim từ chối join; device-change ambiguity dùng safe locked policy, không tự tái phân pool.

**Test Boundary:** Pool claim/signature, mixed acknowledgement, device hot-plug, tampering và party Ready invalidation.

**Definition of Done:** Input pools signed/locked/visible, mixed party có consent và device change không đổi fairness.

### Story 6.7: No-silent-bot và experimental bot disclosure

As a người chơi,
I want biết trước khi queue có bot,
So that Standard không giả người hoặc đổi tiêu chuẩn bí mật.

**Source Requirements:** FR78–FR79; NFR34, NFR53.

**Depends on:** Story 6.5–6.6.

**Blocks:** Story 6.16–6.18 và release integrity checks.

**Module/File Ownership:** Queue/ruleset capability schema, bot disclosure/ack state và static/runtime guards.

**Platform Applicability:** Năm client, control plane và match server.

**Acceptance Criteria:**

**Given** Standard queue  
**When** ticket/match compose  
**Then** bot count phải bằng 0 và không silent pool/fairness relaxation  
**And** capacity shortage trả wait/error rõ.

**Given** experimental bot queue  
**When** trước confirmation  
**Then** expected bot count/range và experimental label hiển thị, cần acknowledgement  
**And** queue/result tách khỏi Standard statistics.

**Error/Recovery Path:** Bot/ruleset metadata mismatch hủy allocation/join; không hide discrepancy ở client.

**Test Boundary:** Standard zero-bot invariant, experimental disclosure/ack, tampered metadata và queue separation.

**Definition of Done:** Không silent bot/fallback; experimental queue minh bạch và tách dữ liệu.

### Story 6.8: MatchAllocator và one-process-per-match

As a người chơi,
I want mỗi trận có server riêng đã cấp phát,
So that lỗi hoặc tải của trận khác không làm thay đổi trận của tôi.

**Source Requirements:** FR71, FR110; NFR13, NFR17, NFR19–NFR20, NFR28, NFR55.

**Depends on:** Story 2.2, Story 6.5.

**Blocks:** Story 6.9, Story 6.16–6.18.

**Module/File Ownership:** `backend/allocator`, Agones/Kubernetes adapters, Linux server image/config và allocation tests.

**Platform Applicability:** Backend, Kubernetes/Agones và Linux headless server.

**Acceptance Criteria:**

**Given** valid match ticket group  
**When** allocator request  
**Then** cấp một Linux headless process/pod cho một match bằng Agones `1.59.0`/Kubernetes `1.35.6` adapters  
**And** local/CI/production dùng cùng server artifact.

**Given** allocated server start  
**When** bootstrap  
**Then** chỉ nhận short-lived allocation secret/config, không database credential  
**And** ready/health/shutdown state trả control plane rõ.

**Error/Recovery Path:** Allocation timeout/failure trả queue destination/retry policy; orphan allocation cleanup bounded/audited.

**Test Boundary:** Allocate/ready/fail/shutdown, secret expiry, one-match isolation, image hash và local-vs-production artifact parity.

**Definition of Done:** Allocator cấp/cô lập/thu hồi match process an toàn, không trao DB credential cho server.

### Story 6.9: Secure join, seat claim và compatibility admission

As a người chơi đã được ghép,
I want vào đúng server/seat bằng token ngắn hạn,
So that người lạ hoặc build sai không chiếm trận.

**Source Requirements:** FR71, FR80, FR110; NFR26–NFR30.

**Depends on:** Story 2.1, Story 6.5–6.8.

**Blocks:** Story 6.13–6.18.

**Module/File Ownership:** Join/session token service, match admission/seat registry, client connection lifecycle và tests.

**Platform Applicability:** Năm client, control plane và Linux match server.

**Acceptance Criteria:**

**Given** allocated match/seat  
**When** client join  
**Then** token expiry/nonce/signature/replay, account/party/seat/input claim và compatibility hash được verify  
**And** token không xuất hiện trong log/artifact/prompt.

**Given** duplicate/stale/wrong-seat join  
**When** admission validate  
**Then** từ chối với typed destination/reason  
**And** không tạo entity/connection authority trước success.

**Error/Recovery Path:** Admission timeout giữ seat theo explicit grace; invalid security claim fail-closed và audit account hash.

**Test Boundary:** Valid join, expiry/replay/tamper, duplicate seat, content mismatch, logging scan và network interruption.

**Definition of Done:** Join/seat secure, compatibility enforced và là nền cho reconnect/scale.

### Story 6.10: Team voice provider spike và VoiceProvider adapter

As a thành viên đội,
I want voice team-only với mute/volume/PTT,
So that phối hợp được mà không đi qua game transport.

**Source Requirements:** FR81, FR103–FR104, FR110; NFR30–NFR31, NFR44–NFR45, NFR55; UX-DR49, UX-DR52.

**Depends on:** Story 6.1–6.2, Story 6.9.

**Blocks:** Story 6.14, Epic 8 voice/audio polish.

**Module/File Ownership:** `native/eos_voice`, `game/src/client/voice`, `VoiceProvider` port/adapters, team permissions và spike reports.

**Platform Applicability:** Năm client; EOS Voice chỉ promote sau full matrix.

**Acceptance Criteria:**

**Given** EOS Voice candidate/version/checksum/license  
**When** five-platform spike chạy  
**Then** team-only, PTT default, optional open mic, per-player mute/volume, route/interruption và permission contracts được chứng minh  
**And** provider không truy cập gameplay state/signing secret hoặc dùng game transport.

**Given** provider unsupported/degraded/denied  
**When** voice enable  
**Then** `UnsupportedVoiceAdapter`/explicit state hoạt động, gameplay/pings vẫn dùng được  
**And** không lặp permission prompt hoặc bật mic ngoài ý muốn.

**Given** EOS Voice không đạt full five-platform promote gate  
**When** đánh giá hoàn tất capability FR81  
**Then** Story 6.10 và Epic 6 phải giữ trạng thái blocked cho tới khi một provider khác đạt cùng contract hoặc FR81 được thay đổi bằng quyết định sản phẩm chính thức  
**And** `UnsupportedVoiceAdapter` chỉ là interim/runtime-degraded adapter, không được dùng làm bằng chứng rằng team voice đã hoàn tất.

**Given** provider đạt promote gate  
**When** voice session bind  
**Then** membership lấy từ signed team/seat state và raw voice không ghi/lưu  
**And** disconnect/rejoin cleanup microphone/session đúng owner.

**Error/Recovery Path:** Spike fail giữ unsupported adapter và documented blocker nhưng không đóng story; runtime failure của provider đã approved phải mute/cleanup fail-safe và hiển thị degraded state.

**Test Boundary:** Five-platform provider matrix, permissions/denial, PTT/open-mic, mute/volume, route/interruption, team isolation và privacy scan.

**Definition of Done:** Ít nhất một VoiceProvider đã đạt team-only/PTT/open-mic/mute/volume/permission/route/interruption gate trên năm platform; unsupported adapter chỉ bao phủ degraded runtime, không thay completion.

### Story 6.11: Eight contextual team pings

As a thành viên đội,
I want gửi ping ngữ cảnh ngắn gọn,
So that vẫn phối hợp được khi không dùng voice.

**Source Requirements:** FR81; UX-DR15, UX-DR30, UX-DR37; NFR31, NFR33.

**Depends on:** Story 1.9, Story 6.2, Story 6.9.

**Blocks:** Epic 8 HUD/subtitle polish.

**Module/File Ownership:** Team ping commands/authority, world/map markers, presenter/subtitles và tests.

**Platform Applicability:** Năm client và Linux match server.

**Acceptance Criteria:**

**Given** team member active  
**When** gửi một trong `Đi tới`, `Nguy hiểm`, `Địch nhìn thấy`, `Loot ở đây`, `Cần vật tư`, `Giữ vị trí`, `Tập hợp`, `Phương tiện`  
**Then** server validate ownership/range/cooldown và replicate intent/position/TTL  
**And** marker dùng fixed team identity shape/number.

**Given** enemy ping  
**When** target di chuyển  
**Then** marker không auto-track/detect enemy ngoài explicit approved snapshot  
**And** eliminated spectator không tạo marker chiến thuật mới.

**Error/Recovery Path:** Spam/invalid location bị rate-limit/reject có feedback; ping mất target hết TTL sạch.

**Test Boundary:** Eight intents, cooldown/TTL/range, no auto-track, spectator permissions và Touch/Keyboard parity.

**Definition of Done:** Tám ping authoritative, dễ phân biệt, không thêm detection và hoạt động khi voice unavailable.

### Story 6.12: Friendly fire và neutral attribution

As a người chơi đội,
I want friendly fire có luật và nguồn rõ,
So that hành vi đồng đội được xử lý nhất quán.

**Source Requirements:** FR82; NFR27, NFR31; UX-DR17, UX-DR47.

**Depends on:** Story 2.6, Story 4.4, Story 6.2, Story 6.9.

**Blocks:** Epic 9 Report và scale gates.

**Module/File Ownership:** Team-damage rules, damage attribution, moderation target intent và fixtures.

**Platform Applicability:** Năm client và Linux match server.

**Acceptance Criteria:**

**Given** aircraft đã departure  
**When** teammate gây validated damage  
**Then** friendly fire áp 100% damage và nguồn hiển thị trung tính  
**And** trước departure policy không gây Standard team damage.

**Given** team damage/elimination event  
**When** player mở Report/Block entry  
**Then** target/match/evidence window IDs được gắn đúng  
**And** block không thay result/damage.

**Error/Recovery Path:** Team identity mismatch reject damage và emit security evidence; presentation không suy đoán attribution.

**Test Boundary:** Pre/post aircraft, all damage regions/throwables/vehicles, neutral cue và moderation intent.

**Definition of Done:** Friendly fire 100% sau departure, attribution/report entry đúng và server-authoritative.

### Story 6.13: Reconnect policy ADR và secure seat contract

As a người chơi bị mất kết nối,
I want biết avatar/seat được xử lý thế nào,
So that reconnect công bằng và không mơ hồ.

**Source Requirements:** FR80, FR109–FR110; NFR20, NFR28–NFR30; UX-DR45.

**Depends on:** Story 4.10, Story 6.2, Story 6.9.

**Blocks:** Story 6.14 và scale gates.

**Module/File Ownership:** Reconnect ADR/policy, seat/token lifecycle schema, backend/match ports và policy tests.

**Platform Applicability:** Năm client, control plane và Linux match server.

**Acceptance Criteria:**

**Given** each match phase/team state  
**When** reconnect policy được khóa  
**Then** ADR xác định owner API, grace duration, AFK neutral input, avatar vulnerability/outcome và seat retention  
**And** terminal destinations chỉ gồm Restored/Timed out/Team eliminated/Match ended theo authoritative state.

**Given** reconnect token  
**When** issue/rotate/consume  
**Then** expiry/nonce/replay protection và same match/account/seat binding được quy định/test  
**And** token không lưu plaintext trong local config/log.

**Error/Recovery Path:** Chưa chốt bất kỳ policy field nào thì Story 6.14 không Ready; không dùng hidden default.

**Test Boundary:** Transition/policy table exhaustive, token lifecycle/threat cases, phase/team outcomes và ownership contracts.

**Definition of Done:** ADR được duyệt, không câu hỏi reconnect mở, schema/ports/tests khóa contract implementation.

### Story 6.14: Mobile interruption và reconnect state machine

As a người chơi mobile,
I want quay lại cùng trận sau gián đoạn hợp lệ,
So that cuộc gọi hoặc background ngắn không tạo input kẹt hay seat mới.

**Source Requirements:** FR80, FR103, FR109–FR110; NFR19–NFR21, NFR28–NFR31; UX-DR38, UX-DR45, UX-DR52.

**Depends on:** Story 6.10, Story 6.13.

**Blocks:** Story 6.16–6.18 và Epic 10 mobile release.

**Module/File Ownership:** Client lifecycle/reconnect, secure storage adapter, backend/match reconnect ports, UI state và device tests.

**Platform Applicability:** Android/iOS primary; desktop network reconnect uses same contract where applicable.

**Acceptance Criteria:**

**Given** Active client bị interruption/background  
**When** lifecycle chuyển  
**Then** state đi `Active → Interrupted → Backgrounded → Reconnecting` và neutralize held movement/fire/PTT  
**And** avatar vẫn theo vulnerability/outcome policy của ADR.

**Given** app resume với same secure token/match identity  
**When** reconnect  
**Then** chỉ chuyển `Restored`, `Timed out`, `Team eliminated` hoặc `Match ended` theo server/backend response  
**And** không tạo seat/entity/token identity mới.

**Given** audio route/permission/display thay đổi  
**When** restore presentation  
**Then** safe area/input/audio/voice rebuild mà không auto-rearm hoặc mất world-state cue bắt buộc  
**And** reconnect progress không giả.

**Error/Recovery Path:** Token expired/replayed hoặc provider unavailable đi terminal/degraded state rõ; retry bounded và không leak secret.

**Test Boundary:** Android/iOS background/call/route/rotation/kill-resume, token expiry, all destinations, avatar vulnerability và input/PTT neutralization.

**Definition of Done:** Mobile lifecycle/reconnect đúng ADR trên representative devices, không stuck input/mic và giữ same match identity.

### Story 6.15: Evidence Event Spine và authority hardening

As a vận hành viên công bằng,
I want quyết định gameplay quan trọng có evidence tái hiện,
So that desync, hit và kết quả có thể điều tra.

**Source Requirements:** FR70–FR73, FR82; NFR2, NFR14, NFR20, NFR22, NFR27, NFR30.

**Depends on:** Epic 2–5 và Story 6.9–6.14.

**Blocks:** Story 6.16–6.18, Epic 9 Report và Epic 10 reliability.

**Module/File Ownership:** `game/src/server/evidence`, committed event schema, checkpoints/replay runner và retention hooks.

**Platform Applicability:** Linux match server, replay harness và authorized tools.

**Acceptance Criteria:**

**Given** committed shot/damage/loot/zone/result/vehicle events  
**When** Evidence Spine ghi  
**Then** mỗi event có tick, sequence, stable type/schema, causal IDs và periodic checkpoint  
**And** speculative/presentation event không được ghi như truth.

**Given** replay fixture từ checkpoint/events  
**When** runner chạy  
**Then** authoritative outcome/hash tái hiện hoặc chỉ rõ divergence đầu tiên  
**And** evidence bounded, không chứa raw voice/token/PII không cần thiết.

**Given** authority static/runtime audit  
**When** scan domains  
**Then** movement/hit/damage/ammo/inventory/loot/vehicle/zone/result đều có server owner và client rejection tests  
**And** debug access permission-gated.

**Error/Recovery Path:** Evidence write pressure dùng bounded buffer/drop policy không chặn hot tick nhưng phát critical metric; result-critical gap đánh dấu điều tra.

**Test Boundary:** Event/checkpoint schema, replay equivalence, privacy scan, authority spoof suite và bounded performance.

**Definition of Done:** Evidence spine tái hiện core domains, authority audit đạt và sẵn sàng scale/report.

### Story 6.16: 24-client protocol-mixed scale gate

As a người chơi,
I want trận 24 người giữ tick và fairness,
So that hệ thống chứng minh bước scale đầu tiên.

**Source Requirements:** FR71–FR82, FR109–FR110; NFR13–NFR17, NFR21, NFR31, NFR52.

**Depends on:** Story 6.1–6.15 và Epic 5 gate.

**Blocks:** Story 6.17.

**Module/File Ownership:** 24-client scenarios, load/relevance/network reports và gate configuration.

**Platform Applicability:** Linux server/headless clients với protocol/input-family mix; representative device observers.

**Acceptance Criteria:**

**Given** 24 clients với party/pool/join/combat/world/reconnect mix  
**When** 45-minute impairment run  
**Then** server giữ 30 Hz với headroom/bytes/correction/memory metrics trong 24-client budget  
**And** authority/evidence/result invariants không fail.

**Given** gate miss  
**When** report  
**Then** block 50-client story với seed/build/manifest/profile reproduction  
**And** không dùng silent bots, client authority hoặc bỏ parity.

**Error/Recovery Path:** Worker failure tách khỏi product failure nhưng toàn gate chỉ pass khi sample/evidence đủ.

**Test Boundary:** 24-client soak, party/input mix, reconnect, world traversal, combat/loot/zone và evidence replay.

**Definition of Done:** 24-client gate đạt đầy đủ, không waiver fairness và baseline được ký.

### Story 6.17: 50-client protocol-mixed scale gate

As a người chơi,
I want trận 50 người ổn định dưới tải trung gian,
So that relevance/replication được chứng minh trước target 100.

**Source Requirements:** FR71–FR82, FR109–FR110; NFR13–NFR17, NFR21, NFR31, NFR52.

**Depends on:** Story 6.16.

**Blocks:** Story 6.18.

**Module/File Ownership:** 50-client scenarios, relevance tiers/delta-snapshot tuning reports và gate configuration.

**Platform Applicability:** Linux server/headless clients và representative five-platform observers.

**Acceptance Criteria:**

**Given** 50 mixed clients qua world/combat/zone density scenarios  
**When** soak/impairment chạy  
**Then** relevance graph/update tiers/snapshot delta giữ tick, bandwidth, correction và memory trong approved envelope  
**And** không giảm gameplay entity/information parity theo platform.

**Given** congestion/hotspot/reconnect burst  
**When** validate  
**Then** reliable/unreliable channel separation giữ inventory/session correctness và snapshot freshness  
**And** result/evidence vẫn complete.

**Error/Recovery Path:** Gate fail giữ 100 blocked và report top relevance/bytes/tick contributors; không tăng budget âm thầm.

**Test Boundary:** 50-client 45-minute soak, hotspots, channel congestion, join/reconnect bursts và replay/result equivalence.

**Definition of Done:** 50-client gate đạt, replication/relevance có evidence và target 100 được mở.

### Story 6.18: 100-client Standard online gate

As a người chơi,
I want trận Standard 100 người giữ authority và chất lượng,
So that quy mô sản phẩm được chứng minh trước khi khóa full map.

**Source Requirements:** FR71–FR82, FR109–FR110; NFR13–NFR17, NFR19–NFR22, NFR31–NFR35, NFR51–NFR53.

**Depends on:** Story 6.17.

**Blocks:** Epic 7 production content lock và Epic 10 release candidate.

**Module/File Ownership:** 100-client scenario family, server/network/device evidence, capacity decision record và signed gate.

**Platform Applicability:** Linux server/headless clients với observers Windows/Linux/macOS/Android/iOS.

**Acceptance Criteria:**

**Given** 100-player Standard mix và 45-minute target scenario  
**When** load/impairment run  
**Then** server duy trì 30 Hz với ≥10% headroom, damage ≤1 tick p95, bandwidth ≤1,5 Mbps mỗi chiều/client và correctness/evidence đạt  
**And** input pools, no-bot, party, voice/ping, friendly fire/reconnect giữ contract.

**Given** mobile/desktop observers  
**When** cùng match state trình bày  
**Then** collision/cover/silhouette/visibility/gameplay data/protocol parity  
**And** không platform-only combat information.

**Given** 100-client target không đạt  
**When** capacity decision  
**Then** sản phẩm giữ quy mô đã chứng minh và ghi owner/risk/next benchmark  
**And** không trao authority client, bot ẩn hoặc giảm parity để báo đạt.

**Error/Recovery Path:** Gate failure giữ full map/content lock blocked; reproduction và capacity decision được lưu, không falsify/average bỏ outlier.

**Test Boundary:** Full 100-client 45-minute load, combat/world/zone hotspots, party/input/reconnect, bandwidth/tick/evidence và five-platform parity.

**Definition of Done:** 100-client gate đạt hoặc scope được khóa trung thực ở mức đã chứng minh; chỉ kết quả đạt mới mở Epic 7 full-content expansion.

## Epic 7: Đảo Vọng ở quy mô sản xuất

Sau khi scale/mobile gate đạt, người chơi có thể khám phá bản đồ 8×8 km hoàn chỉnh với 18 POI, 55 compound, mục tiêu 420 công trình, route và content parity được kiểm định.

### Story 7.1: 8×8 km greybox và production-content lock

As a đội xây world,
I want khóa scope map theo gate đã chứng minh,
So that không sản xuất hàng trăm asset trên nền tảng chưa chịu được tải.

**Source Requirements:** FR83; NFR46–NFR53.

**Depends on:** Story 5.13 và Story 6.18 đạt, không chỉ có waiver.

**Blocks:** Story 7.2–7.10.

**Module/File Ownership:** 8×8 MapDefinition source, cell-budget model, content-lock ADR và greybox reports.

**Platform Applicability:** Bake/headless analysis, năm client và Linux server.

**Acceptance Criteria:**

**Given** 2×2/mobile/100-client gates đạt  
**When** production scope khóa  
**Then** MapDefinition mục tiêu 8×8 km, 18 POI, 55 compounds, ≥420 enterable buildings, 180 weighted vehicle spots và 12 boat docks  
**And** budget/owner/LOD/cell targets được ghi theo signed baseline.

**Given** 8×8 greybox bake  
**When** cell/route/load analysis chạy  
**Then** toàn map có terrain/coast/road/POI/compound placeholders và cell budget witness  
**And** không author detailed production content trước khi greybox pass.

**Error/Recovery Path:** Scale/mobile gate hoặc greybox budget fail giữ content lock đóng và cập nhật scope decision trung thực.

**Test Boundary:** Dimension/count schema, complete cell coverage, coarse connectivity, budget estimation và manifest determinism.

**Definition of Done:** 8×8 greybox đạt, scope/count/budget được khóa và mở production authoring có kiểm soát.

### Story 7.2: Full-map terrain, coastline và hydrology bake

As a người chơi,
I want toàn đảo có địa hình/nước liền mạch,
So that route ven biển và nội địa không vỡ ở tile boundary.

**Source Requirements:** FR83–FR87; NFR31, NFR35, NFR46–NFR48, NFR50.

**Depends on:** Story 7.1 và Story 5.1–5.3.

**Blocks:** Story 7.3, Story 7.6–7.10.

**Module/File Ownership:** Full terrain/coast/hydrology source, TerrainTileData, material atlas/profile và validation reports.

**Platform Applicability:** Năm client và Linux headless collision/water data.

**Acceptance Criteria:**

**Given** 8×8 source tiles  
**When** full bake  
**Then** mọi tile có height/collision/material mask/mesh LOD/water dependency và seam continuity  
**And** chỉ approved terrain textures/materials có provenance được đóng gói.

**Given** desktop/mobile profile  
**When** stream/render  
**Then** geometry/collision/water/surface IDs tương đương, texture/LOD compression nằm trong budget  
**And** visual variants không đổi concealment/standability.

**Error/Recovery Path:** Bất kỳ missing/seam/budget tile nào chặn full-map manifest; không ship partial hidden hole.

**Test Boundary:** 8×8 seam/hole/slope/water scans, platform material/LOD parity, memory/size và deterministic bake.

**Definition of Done:** Full terrain/coast/hydrology đạt seam/collision/budget và dùng asset đã kiểm duyệt.

### Story 7.3: 18 POI, 55 compounds và production road graph

As a người chơi,
I want đảo có nhịp độ địa điểm và tuyến di chuyển đa dạng,
So that điểm rơi và xoay bo tạo nhiều chiến lược.

**Source Requirements:** FR83–FR85; NFR25, NFR31, NFR46.

**Depends on:** Story 7.1–7.2 và Story 5.4.

**Blocks:** Story 7.4–7.10.

**Module/File Ownership:** POI/compound source, full road/bridge/pass graph, route tags và connectivity reports.

**Platform Applicability:** Bake/headless analysis và năm client.

**Acceptance Criteria:**

**Given** production layout  
**When** validator đếm/kiểm tra  
**Then** có đúng 18 POI và 55 compounds với stable IDs, role/density/risk/loot tags  
**And** road/bridge/pass/coast graph kết nối tới gameplay regions.

**Given** landmass/choke/POI pair  
**When** route analysis chạy  
**Then** có bypass chậm hơn và không mandatory single choke  
**And** travel-time distribution không tạo một route thống trị ngoài approved intent.

**Error/Recovery Path:** Count/connectivity/choke failure block layout sign-off với route witness; không patch runtime graph.

**Test Boundary:** Exact counts/IDs, all-pairs critical connectivity, bypass costs, spawn/flight access và deterministic graph hash.

**Definition of Done:** 18/55 layout/road graph đạt connectivity/choke rules và sẵn sàng building placement.

### Story 7.4: Production modular building library

As a người chơi,
I want nhiều loại công trình nhưng cùng luật opening/collision,
So that khám phá đa dạng mà combat vẫn đọc được.

**Source Requirements:** FR83–FR85; NFR31, NFR35, NFR46–NFR48, NFR55.

**Depends on:** Story 5.5, Story 7.3.

**Blocks:** Story 7.5, Story 7.7–7.10.

**Module/File Ownership:** Production building source/library, gameplay shells, visual variants, HLOD/collision/opening validators.

**Platform Applicability:** Năm client và Linux headless gameplay shells.

**Acceptance Criteria:**

**Given** approved modular kit  
**When** mở rộng production library  
**Then** mỗi module/building archetype có provenance, stable IDs, sockets, enterable routes, collision/openings/cover và LOD profiles  
**And** decorative variants không đổi combat silhouette/ngụy trang ngoài parity.

**Given** desktop/mobile/headless representations  
**When** parity validator chạy  
**Then** gameplay shell/openings/cover/visibility hash tương thích  
**And** HLOD swap không tạo/disappear cover.

**Error/Recovery Path:** Asset/module fail bị loại khỏi allowed kit; placement dùng approved alternative, không sửa collision theo platform.

**Test Boundary:** Provenance/topology/scale, socket composition, enterability, HLOD/opening/cover parity và package size.

**Definition of Done:** Production building library đủ đa dạng, hoàn toàn validated và tách gameplay shell khỏi visual.

### Story 7.5: 420 enterable building placements và HLOD

As a người chơi,
I want công trình trên đảo có thể vào và stream ổn định,
So that loot/combat trong nhà không phụ thuộc vị trí hoặc thiết bị.

**Source Requirements:** FR83–FR85; NFR31, NFR35, NFR46–NFR48, NFR50.

**Depends on:** Story 7.3–7.4.

**Blocks:** Story 7.6–7.10.

**Module/File Ownership:** Building placement source, world cells/HLOD dependencies, enterability/navigation reports.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** production map placements  
**When** validator chạy  
**Then** có ít nhất 420 enterable building instances với stable placement IDs và cell dependencies  
**And** entrances/interiors/stairs/windows/loot anchors/navigation reachable.

**Given** HLOD/cell transitions  
**When** player/projectile/vehicle tiếp cận  
**Then** gameplay shell/cover tồn tại đúng readiness/lease rules và visual swap không hitch/collision pop  
**And** server không mang visual mesh.

**Error/Recovery Path:** Invalid/unreachable placement bị loại/block count; không đánh dấu enterable nếu validator fail.

**Test Boundary:** Count/uniqueness, enterability/navigation, HLOD/cell lease, collision/LOS parity và memory/streaming soak.

**Definition of Done:** ≥420 building placements thực sự enterable, streamable và parity-safe.

### Story 7.6: Loot, 180 vehicle spots và 12 boat docks

As a người chơi,
I want loot và phương tiện phân bố theo geography/risk,
So that mỗi vùng có lựa chọn di chuyển/trang bị hợp lý.

**Source Requirements:** FR38, FR44–FR47, FR51, FR83; NFR24–NFR25, NFR29.

**Depends on:** Story 3.7–3.9, Story 5.8–5.10, Story 7.2–7.5.

**Blocks:** Story 7.7, Story 7.9–7.10.

**Module/File Ownership:** Full-map loot/vehicle/dock placements, weighted tables và statistical/accessibility reports.

**Platform Applicability:** Linux headless authority/analysis và năm client.

**Acceptance Criteria:**

**Given** full layout  
**When** placement bake  
**Then** loot anchors/tier tags, đúng 180 weighted vehicle spots và 12 accessible boat docks có stable IDs  
**And** vehicle/loot RNG streams tách biệt.

**Given** statistical simulation  
**When** chạy theo POI/compound/geography  
**Then** 90-second targets, high-risk quality và no-essential-airdrop-only giữ trong approved tolerance  
**And** spawn không vào collision/water/roof inaccessible ngoài intent.

**Error/Recovery Path:** Count/accessibility/distribution failure block manifest; không spawn runtime tùy ý để bù.

**Test Boundary:** Exact counts, accessibility/clearance, distribution targets, seed determinism và platform collision parity.

**Definition of Done:** Loot/vehicle/dock placements đủ count, accessible và đạt statistical gates.

### Story 7.7: Full-map cover, route và choke validation

As a người chơi,
I want mọi vùng đảo có ít nhất hai cách xử lý khoảng trống/choke,
So that xoay bo không trở thành cái chết bắt buộc.

**Source Requirements:** FR84–FR86; NFR25, NFR31, NFR35.

**Depends on:** Story 7.2–7.6.

**Blocks:** Story 7.9–7.10.

**Module/File Ownership:** Full-map map-analysis scenarios, cover/route/choke/final-zone reports và fix ownership.

**Platform Applicability:** Headless analysis; collision/visibility evidence từ năm platform profiles.

**Acceptance Criteria:**

**Given** toàn bộ traversable graph/open spans  
**When** validators scan  
**Then** mọi span >120 m có ≥2 counterplay options và mọi critical choke có bypass chậm hơn  
**And** không landmass/zone route nào phụ thuộc một choke duy nhất.

**Given** final-zone candidate set  
**When** land-playability scan  
**Then** mỗi candidate đạt ≤50% water/unstandable/inaccessible area  
**And** cover/route semantics khớp mobile/desktop.

**Error/Recovery Path:** Validator Unknown/Fail block affected cells/candidates và tạo route witness/owner, không mặc định pass.

**Test Boundary:** Full-map scans, synthetic validator calibration, route-cost sampling, final-zone set và platform parity.

**Definition of Done:** Full map đạt machine-verifiable cover/choke/final-zone rules.

### Story 7.8: Navigation, streaming, audio và server spatial grids

As a người chơi,
I want AI/traversal/audio/world query tiếp tục đúng khi đi khắp đảo,
So that cell boundary không làm world mất trạng thái.

**Source Requirements:** FR83–FR89; NFR46–NFR48.

**Depends on:** Story 7.2–7.7 và Story 5.3.

**Blocks:** Story 7.9–7.10.

**Module/File Ownership:** Navigation bake, streaming dependencies, audio cells, server spatial grids và soak reports.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** full-map cells  
**When** grids bake  
**Then** navigation, terrain/entity/HLOD/audio/server spatial dependencies có stable IDs/cadence và complete coverage  
**And** no dangling/missing/cyclic dependency ngoài allowed lease graph.

**Given** long traversal/teleport test corridors  
**When** streaming soak  
**Then** cache/memory/main-thread instantiation trong budget, entity identity/door/projectile/vehicle/audio state giữ đúng  
**And** cancellation không commit stale generation.

**Error/Recovery Path:** Missing dependency/cell budget failure block map manifest; runtime degraded visual không được bỏ gameplay state.

**Test Boundary:** Dependency graph, full-map traversal/prefetch/cancel, memory/hitch, lease retention và navigation continuity.

**Definition of Done:** Full-map grids/dependencies complete, bounded và ổn qua soak.

### Story 7.9: Full-map weather và zone playability parity

As a người chơi,
I want weather và bo hợp lệ trên mọi vùng đảo,
So that không trận nào bị quyết định bởi vùng không thể chơi.

**Source Requirements:** FR86–FR91; NFR25, NFR31, NFR35, NFR44.

**Depends on:** Story 4.8, Story 5.7, Story 7.2–7.8.

**Blocks:** Story 7.10.

**Module/File Ownership:** Full-map weather/zone candidates, contrast/audio profiles, validation scenarios và reports.

**Platform Applicability:** Năm client và Linux headless server.

**Acceptance Criteria:**

**Given** all zone phase/candidate/weather combinations  
**When** batch validate  
**Then** land-playability, reachability, reveal timing, rain hearing -15% và fog contrast 180–250 m giữ contract  
**And** no candidate tạo mandatory water/cliff/roof outcome.

**Given** desktop/mobile profiles  
**When** visibility/audio tests  
**Then** information distance và gameplay modifier tương đương  
**And** quality downgrade không bỏ fog/cover hoặc tăng hearing.

**Error/Recovery Path:** Candidate/profile fail bị loại/block release manifest; không chọn runtime invalid candidate.

**Test Boundary:** Full candidate×weather matrix, zone route reachability, audio/contrast measurements và five-platform parity.

**Definition of Done:** Weather/zone toàn map có signed valid set và parity evidence.

### Story 7.10: Signed production-map mobile/100-client gate

As a người chơi,
I want Đảo Vọng hoàn chỉnh chạy đúng trên target scale/device,
So that content production không phá nền kỹ thuật đã chứng minh.

**Source Requirements:** FR83–FR89; NFR13, NFR31, NFR35, NFR46–NFR53.

**Depends on:** Story 7.1–7.9.

**Blocks:** Epic 8 production UX integration và Epic 10 release candidate.

**Module/File Ownership:** Production map manifest/signing, 100-client map scenarios, mobile streaming/performance reports và gate.

**Platform Applicability:** Linux 100-client server, Windows/Linux/macOS/Android/iOS observers/devices.

**Acceptance Criteria:**

**Given** signed candidate map  
**When** 100-client/full-route/45-minute scenarios chạy  
**Then** tick/relevance/streaming/lease/collision/water/vehicle/zone/evidence correctness giữ budget  
**And** exact target counts/validators/asset provenance pass.

**Given** mobile minimum-class slice-to-full traversal  
**When** device soak  
**Then** working memory/hitch/thermal preliminary budget không phá gameplay parity  
**And** visual degradation không đổi cover/visibility/openings.

**Given** bất kỳ critical gate fail  
**When** release decision  
**Then** map manifest không ký và owner/cell/asset/route reproduction được lưu  
**And** không giảm authority/parity để giữ 8×8 claim.

**Error/Recovery Path:** Failed manifest giữ approved prior slice/map scope; retest targeted plus regression suite sau fix.

**Test Boundary:** Exact content counts, all validators, 100-client full-map load, mobile device soak, package size và manifest/hash parity.

**Definition of Done:** Production Đảo Vọng được ký chỉ khi đạt scale/mobile/content/parity gate; Epic 8–10 có stable map baseline.

## Epic 8: Trải nghiệm rõ ràng và tiếp cận trên mọi thiết bị

Người chơi có HUD, Inventory, Map, audio, localization, accessibility, Touch layout, Training Grounds và Field Orientation nhất quán trên desktop/mobile.

### Story 8.1: Field Instrument Theme và accessible base components

As a người chơi,
I want giao diện nhất quán, dễ đọc và điều khiển bằng nhiều phương thức,
So that tôi luôn nhận ra trạng thái và hành động.

**Source Requirements:** UX-DR1–UX-DR7, UX-DR32, UX-DR36; NFR36–NFR41.

**Depends on:** Epic 1–7.

**Blocks:** Story 8.2–8.19.

**Module/File Ownership:** `game/assets/ui/themes`, token resources, `action-button`, `navigation-item`, `focus-ring`, base presenters/tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** DESIGN tokens  
**When** Godot Theme build  
**Then** color/typography/spacing/radius/component constants dùng Field Instrument charcoal–olive–bone và approved signal colors  
**And** không hard-code style phân tán, neon/glass/gradient/chrome dày.

**Given** text/control states  
**When** render/focus/disable  
**Then** contrast ≥4,5:1 text thường, ≥3:1 large/icon/focus; signal dùng color+icon/shape/label  
**And** focus ring 2 px không crop, keyboard/pointer parity và disabled reason rõ.

**Error/Recovery Path:** Token/font/style thiếu làm UI validation fail; fallback theme chỉ dùng debug và không được ký production.

**Test Boundary:** Token/static scan, contrast after compositing, focus/traversal, component states và five-platform visual snapshots.

**Definition of Done:** Theme/base components reusable, accessible và là nguồn style duy nhất cho surface sau.

### Story 8.2: Responsive 16:9 competitive frame và safe areas

As a người chơi,
I want HUD/world giữ bố cục công bằng trên mọi màn hình,
So that aspect ratio không cho thêm thông tin.

**Source Requirements:** UX-DR8–UX-DR10, UX-DR38, UX-DR43; NFR32, NFR38–NFR40.

**Depends on:** Story 8.1.

**Blocks:** Story 8.4–8.19.

**Module/File Ownership:** Competitive-frame root, responsive layout profiles, safe-area root và screenshot harness.

**Platform Applicability:** Desktop resolutions/ultrawide và Android/iOS phone/tablet.

**Acceptance Criteria:**

**Given** any viewport  
**When** live Standard render  
**Then** world/HUD nằm trong central largest-fit 16:9 frame; ultrawide sides chỉ matte/chrome không tương tác  
**And** Compact/Base/Large dùng anchors/containers, co spacing trước text.

**Given** OS inset/rotate/resume/display change  
**When** safe area cập nhật  
**Then** critical controls/focus/subtitle/reticle không crop và invalid saved layout fallback safe preset  
**And** mobile aim corridor giữ rõ trên 20:9, 16:9, 4:3.

**Error/Recovery Path:** Unknown viewport/inset dùng conservative centered frame/safe preset, không mở rộng world information.

**Test Boundary:** Sáu desktop resolutions ×80/100/140%, ultrawide, three mobile ratios, notches/gesture/rotation và screenshot diff.

**Definition of Done:** Responsive frame/safe area đạt matrix, không extra world information hoặc critical crop.

### Story 8.3: Vietnamese/English localization và Noto font pipeline

As a người chơi,
I want giao diện hiển thị đúng tiếng Việt và tiếng Anh,
So that label quan trọng dễ hiểu và không mất ký tự.

**Source Requirements:** FR100; UX-DR6–UX-DR7, UX-DR53; NFR31, NFR36–NFR39, NFR55.

**Depends on:** Story 8.1–8.2.

**Blocks:** Story 8.4–8.19.

**Module/File Ownership:** Localization catalogs/schema, Noto font assets/licenses/import profiles, string linter và snapshot tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** UI strings  
**When** catalog build  
**Then** mọi string đi qua stable key cho Việt/Anh, có plural/date/number policy và fallback  
**And** gameplay-critical label không ellipsis; text dài reflow/alias+tooltip/accessible label, không giảm dưới minimum.

**Given** Noto Sans/Condensed/Mono/fallback  
**When** promote/import  
**Then** license/provenance/checksum, SDF/raster/fallback metrics và Vietnamese diacritics/missing-glyph coverage được xác minh  
**And** keycap 32–96 px không ép font dưới minimum.

**Error/Recovery Path:** Missing key/glyph hoặc malformed format fails localization gate; runtime fallback hiển thị key-safe marker trong debug, không chuỗi rỗng.

**Test Boundary:** Catalog completeness, plural/format, long English/Vietnamese, glyph coverage, font license và five-platform text snapshots.

**Definition of Done:** Việt/Anh đầy đủ, Noto hợp lệ, không missing glyph/crop critical text trên matrix.

### Story 8.4: Lobby IA, party panel và offline states

As a người chơi,
I want từ launch tới Deploy nhanh và biết khi nào online unavailable,
So that tôi không bị lạc trong menu hoặc queue sai.

**Source Requirements:** UX-DR11, UX-DR29, UX-DR44, UX-DR55–UX-DR56; FR80, FR110.

**Depends on:** Story 6.1–6.7, Story 8.1–8.3.

**Blocks:** Story 8.15–8.17.

**Module/File Ownership:** Lobby shell/navigation, party/Deploy presenters, offline/queue state và UI tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** online Lobby  
**When** render  
**Then** navigation dọc trái, world scene giữa, party panel+Deploy phải và launch→Deploy tối đa ba actions  
**And** party hiển thị 1–4 member, leader, Ready, reconnect, network, voice, input family/mixed ack.

**Given** offline/provider degraded/queue error  
**When** state đổi  
**Then** Deploy disabled có reason, Training/Settings vẫn truy cập; timeout/error trở về Lobby đúng nguyên nhân  
**And** không news/store/reward rail/event carousel/red badge/FOMO.

**Error/Recovery Path:** Presenter/backend state lỗi dùng explicit Unavailable, giữ navigation/focus và không tự queue/fallback.

**Test Boundary:** IA/action count, party state matrix, Ready invalidation, offline/degraded/timeout và prohibited-content scan.

**Definition of Done:** Lobby nhanh, rõ, commercial-free và phản ánh control-plane state chính xác.

### Story 8.5: Minimal competitive match HUD

As a người chơi,
I want thấy đúng thông tin sống còn mà không bị che màn hình,
So that quyết định combat nhanh và công bằng.

**Source Requirements:** FR97; UX-DR12, UX-DR15–UX-DR16; NFR31–NFR39.

**Depends on:** Story 8.1–8.3 và gameplay presenters Epic 1–7.

**Blocks:** Story 8.6–8.8, Story 8.18–8.19.

**Module/File Ownership:** Match HUD presenter/view state, six persistent modules, reticle/team identity components và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** player alive  
**When** HUD render  
**Then** sáu module neo `compass`, `squad-panel`, `health-boost-bar`, `minimap-zone-panel`, `weapon-ammo-panel`, `reticle` hiển thị đúng bảy nhóm persistent data  
**And** không commercial feed, damage number, footstep radar, loot score hoặc enemy outline.

**Given** reticle hip/ADS  
**When** state đổi  
**Then** hip reticle đúng 8 px arms/6 px gap/2 px stroke/1 px outline ở 100%; ADS sight/scope tiếp quản  
**And** hit confirm chỉ từ committed event, không lock/lead/range/damage cue.

**Error/Recovery Path:** Missing view-state field hiển thị explicit unknown/neutral state và metric, không đọc authoritative entity/packet trực tiếp.

**Test Boundary:** View-state/presenter contracts, module anchoring, reticle modes, team identities và responsive screenshots.

**Definition of Done:** HUD tối giản, đầy đủ persistent info, server-confirmed cues và không prohibited information.

### Story 8.6: Overlay lane, status, damage và contextual commitments

As a người chơi,
I want cảnh báo và hành động ngữ cảnh có ưu tiên rõ,
So that thông tin khẩn cấp không che hoặc mâu thuẫn HUD.

**Source Requirements:** UX-DR13–UX-DR21; FR37, FR53, FR74.

**Depends on:** Story 1.9, Story 8.5.

**Blocks:** Story 8.19.

**Module/File Ownership:** Overlay manager, status/network/damage/context/progress components và presenter tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** concurrent overlays  
**When** layout/arbitration  
**Then** dùng lane/collision P0 lethal, P1 commitment, P2 match/system, P3 contextual và z-order đã khóa  
**And** sáu HUD modules không bị che, tối đa một critical banner/modal.

**Given** damage/network/context/action state  
**When** trình bày  
**Then** damage arc 30° screen-relative theo world camera tại hit, network/status icon+label+severity, prompt binding hiện hành/verb-first và progress server-bound  
**And** vehicle card có fuel/HP/four tires/3-second fire countdown.

**Error/Recovery Path:** Overlay overflow drop/coalesce theo priority có metric; không che P0 hoặc persistent HUD.

**Test Boundary:** Priority/collision/z-order, multiple hit recency, >150 ms warning, interaction priority và interruption reasons.

**Definition of Done:** Overlay/context system rõ, bounded và không tạo radar lịch sử/false progress.

### Story 8.7: Non-pausing desktop/mobile Inventory

As a người chơi,
I want quản lý đồ mà vẫn thấy nguy hiểm xung quanh,
So that Inventory không biến thành pause hoặc vùng an toàn.

**Source Requirements:** FR99; UX-DR22–UX-DR25, UX-DR35–UX-DR36; NFR37–NFR41, NFR45.

**Depends on:** Epic 3 và Story 8.1–8.3, Story 8.5.

**Blocks:** Story 8.19.

**Module/File Ownership:** Inventory presenters/view states, desktop/mobile compositions, item/equipment components và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** desktop Inventory 1920×1080  
**When** mở  
**Then** bố cục 34% Nearby/Backpack — ≥32% world strip — 34% Weapons/Equipment và panels ≤68%  
**And** world/game/audio không pause.

**Given** mobile Inventory  
**When** mở  
**Then** tabbed panel ≤62%, world strip ≥38%, tap/action menu là primary và drag chỉ shortcut  
**And** target/safe area/focus/close path đạt contract.

**Given** item mutation bị reject  
**When** presenter cập nhật  
**Then** item giữ tại nguồn/focus, reason rõ; row có icon/shape/name/count/weight và equipment durability redundant encoding  
**And** UI không optimistic-move.

**Error/Recovery Path:** Snapshot/version conflict refresh immutable ViewState, giữ surface/focus và không duplicate item.

**Test Boundary:** Desktop/mobile layouts, mutation success/fail, focus/input blocking, world/audio continuity và accessibility snapshots.

**Definition of Done:** Inventory non-pausing, đúng world strip, mutation authoritative và usable bằng keyboard/pointer/tap.

### Story 8.8: Full Map, phase và team markers

As a người chơi,
I want xem đường bay, bo và marker đội mà không được lộ loot/địch,
So that lập kế hoạch dựa trên thông tin hợp lệ.

**Source Requirements:** FR98–FR99; UX-DR17, UX-DR26–UX-DR28, UX-DR35; NFR31–NFR33, NFR45.

**Depends on:** Story 4.4, Story 4.8, Story 6.11, Story 8.1–8.3.

**Blocks:** Story 8.18–8.19.

**Module/File Ownership:** Map presenter/layers, phase/timer/legend, marker interactions và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** Map mở  
**When** render  
**Then** có place names, flight path, current solid zone, next dashed zone chỉ sau reveal và team markers  
**And** không loot, enemy, sound-source hoặc predicted zone.

**Given** desktop/mobile interaction  
**When** pan/zoom/place/remove marker  
**Then** desktop bindings và mobile one-finger/pinch/tap/long-press radial hoạt động; close 64 units trong safe area  
**And** damage không tự đóng Map, world/audio không pause.

**Given** damage khi Map mở  
**When** cue hiển thị  
**Then** direction vẫn screen-relative theo world camera tại hit và không tạo radar history  
**And** orientation default/zoom limits đã khóa, cùng information range mọi platform.

**Error/Recovery Path:** Map data/layer unavailable hiển thị explicit state, giữ close/control; không dựng zone/marker giả.

**Test Boundary:** Reveal timing, allowed/forbidden layers, gestures/bindings, orientation/zoom, damage cue và responsive/safe-area matrix.

**Definition of Done:** Map non-pausing, chỉ có information hợp lệ, đầy đủ input và parity.

### Story 8.9: Atomic Settings architecture và input routing

As a người chơi,
I want thay đổi settings an toàn và có thể hoàn tác,
So that cấu hình lỗi không làm mất quyền điều khiển.

**Source Requirements:** FR58, FR100; UX-DR33–UX-DR36; NFR31, NFR37–NFR41.

**Depends on:** Story 1.10–1.11, Story 8.1–8.3.

**Blocks:** Story 8.10–8.14, Story 8.17, Story 8.19.

**Module/File Ownership:** Settings schemas/store/presenters, routing contexts, conflict/Apply/Cancel/Reset flows và tests.

**Platform Applicability:** Năm client với platform-specific capability fields.

**Acceptance Criteria:**

**Given** graphics/audio/accessibility/language/input/Touch/Gyro/haptic/FOV/sensitivity/shake/flash settings  
**When** edit  
**Then** changes stage, validate/conflict detect, Apply atomically, Cancel rollback, persist versioned và Reset category/all cần confirmation  
**And** unsupported capability disabled có reason.

**Given** Inventory/Map/Pause/modal open/close  
**When** input routing context đổi  
**Then** click-through/action bị chặn được neutralize, cần release trước re-arm, focus đặt/return deterministically và `ui_cancel` thoát một cấp  
**And** không keyboard trap.

**Error/Recovery Path:** Persistence/migration/Apply failure giữ active config cũ, báo reason và restore safe controls.

**Test Boundary:** Schema/range/migration, atomic Apply/Cancel/Reset, input-routing matrix, focus lifecycle và restart.

**Definition of Done:** Settings an toàn/versioned, đầy capability, không làm mất escape/control path.

### Story 8.10: Accessibility Floor, color-blind và reduced motion/flash

As a người chơi có nhu cầu tiếp cận,
I want tín hiệu quan trọng có nhiều cách nhận biết và giảm hiệu ứng khó chịu,
So that vẫn chơi được mà không nhận thêm thông tin cạnh tranh.

**Source Requirements:** FR100–FR102; UX-DR4–UX-DR5, UX-DR42, UX-DR50–UX-DR51; NFR36–NFR43.

**Depends on:** Story 8.5–8.9.

**Blocks:** Story 8.19.

**Module/File Ownership:** Accessibility profiles/tokens, motion/flash policy, settings integration và visual tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** Protanopia/Deuteranopia/Tritanopia preset  
**When** apply  
**Then** zone/team marker/hit effect/reticle đổi token nhưng giữ geometry/timing/identity/line style  
**And** critical state luôn có shape/icon/label, không color-only.

**Given** Reduce Motion/Flash  
**When** HUD/context transition/critical cue  
**Then** normal motion 120–180 ms, fade-out ≤120 ms, translation ≤12 px; reduced dùng opacity/state swap ≤100 ms và static icon/backplate  
**And** critical flash ≤10% central frame, ≤3 lần/giây, không mất information/timing.

**Given** UI scale 80–140% và accessibility controls  
**When** render/interact  
**Then** text/target/focus minimums giữ đúng và hold/toggle/FOV/Gyro/haptic/shake/blood-hit-color controls phản ánh capability  
**And** không visual footstep cue.

**Error/Recovery Path:** Invalid preset fallback default tokens + explicit status; không reset unrelated settings.

**Test Boundary:** Color/contrast simulations, motion/flash timing, scale/input/accessibility matrix và prohibited-extra-cue scan.

**Definition of Done:** Accessibility Floor đạt trên năm platform, không extra competitive information.

### Story 8.11: Production Touch layout editor

As a người chơi mobile,
I want tùy chỉnh vị trí/kích thước/opacity nút,
So that layout phù hợp tay và thiết bị của tôi.

**Source Requirements:** FR58, FR100; UX-DR38–UX-DR43; NFR39–NFR40.

**Depends on:** Story 1.11, Story 8.2, Story 8.9.

**Blocks:** Story 8.19 và Epic 10 mobile device gates.

**Module/File Ownership:** `control-layout-editor`, layout schema/store, overlap/safe-area validator và device tests.

**Platform Applicability:** Android/iOS; desktop preview tool chỉ hỗ trợ authoring.

**Acceptance Criteria:**

**Given** editor mở  
**When** move/resize/opacity control  
**Then** grid 8 px, handle ≥48 px, phone/tablet+safe-area preview và Apply/Cancel/Reset atomic  
**And** hỗ trợ left-handed layout.

**Given** proposed layout  
**When** validate  
**Then** chặn overlap/out-of-safe-area làm mất fire/exit/close/Pause, giữ target minimums/look zone ≥40%  
**And** invalid saved layout fallback safe preset.

**Error/Recovery Path:** Persistence/migration fail giữ active layout cũ; interruption cancel drag/pointer ownership và không stuck action.

**Test Boundary:** Editor gestures, validation, Apply/Cancel/Reset, device ratios/insets/left-hand và runtime multitouch regression.

**Definition of Done:** Layout editor production-ready, không thể lưu layout mất critical controls và hoạt động trên representative Android/iOS.

### Story 8.12: Competitive audio outputs, mix và music timing

As a người chơi,
I want nghe world/team/UI đúng output mà không có boost chiến thuật,
So that âm thanh rõ và công bằng trên thiết bị của tôi.

**Source Requirements:** FR104–FR105; NFR31, NFR44–NFR45, NFR55; UX-DR49.

**Depends on:** Story 2.10, Story 5.7, Story 5.9, Story 8.9.

**Blocks:** Story 8.13–8.14, Story 8.19 và audio release gate.

**Module/File Ownership:** Audio buses/output profiles, HRTF/downmix, approved audio/music assets, mix tests và settings UI.

**Platform Applicability:** Năm client và supported audio routes.

**Acceptance Criteria:**

**Given** output selection  
**When** Apply  
**Then** hỗ trợ Stereo Headphones HRTF On/Off, Stereo Speakers và Mono accessibility downmix; Team Voice/UI/Music controls riêng  
**And** World bus giữ fixed fair ratio, không footstep boost/EQ chiến thuật.

**Given** HUD/Inventory/Map/Pause/spectator  
**When** audio render  
**Then** HRTF theo world camera hoặc spectator target, critical footsteps/gunshots/vehicles/zone/team voice không bị mute/duck sai  
**And** UI surface không pause world audio.

**Given** music candidates từ intake đủ provenance/license  
**When** playback state  
**Then** music chỉ ở menu, Results hoặc sau server-confirmed victory; không phát khi player còn sống  
**And** monster/VO/event/red-zone-like tracks không tự đưa vào Standard.

**Error/Recovery Path:** Output/route/HRTF unavailable hiển thị degraded option và dùng approved safe mix, không thay gameplay audible range.

**Test Boundary:** Output/downmix/HRTF localization, bus fairness, surface continuity, alive/no-music state, asset provenance/loudness và route matrix.

**Definition of Done:** Audio output/mix/music đúng fairness/timing, dùng approved asset subset và đạt localization tests.

### Story 8.13: Contextual voice permission và route safety

As a người chơi,
I want microphone chỉ được hỏi/bật khi tôi chủ động dùng voice,
So that quyền riêng tư và PTT không bị kích hoạt ngoài ý muốn.

**Source Requirements:** FR103; UX-DR52; NFR30, NFR45.

**Depends on:** Story 6.10, Story 8.9, Story 8.12.

**Blocks:** Story 8.19.

**Module/File Ownership:** Voice settings/permission presenter, audio-route lifecycle adapter và tests.

**Platform Applicability:** Năm client, đặc biệt Android/iOS.

**Acceptance Criteria:**

**Given** voice chưa bật  
**When** app launch/Lobby  
**Then** không request microphone; chỉ hỏi khi player bật voice/PTT  
**And** denial được ghi capability state, không prompt lặp.

**Given** route change/interruption/background  
**When** voice lifecycle rebuild  
**Then** PTT/open mic neutralize theo policy, không phát ngoài ý muốn  
**And** world-state cues bắt buộc không mất.

**Error/Recovery Path:** Permission/provider failure disable voice có reason, pings vẫn dùng được và mic cleanup fail-safe.

**Test Boundary:** First enable/deny/retry settings, route/headset/call/background, PTT neutralization và privacy/log scan.

**Definition of Done:** Permission contextual, denial non-repeating, route/interruption không bật mic hoặc kẹt input.

### Story 8.14: System và team-ping subtitles

As a người chơi,
I want thông báo hệ thống/ping có subtitle dễ đọc,
So that không bỏ lỡ thông tin phi-âm-thanh mà vẫn không có footstep radar.

**Source Requirements:** FR102; UX-DR37, UX-DR51–UX-DR53; NFR36–NFR39.

**Depends on:** Story 6.11, Story 8.3, Story 8.5–8.6, Story 8.12.

**Blocks:** Story 8.19.

**Module/File Ownership:** Subtitle queue/presenter/component, localization integration và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** system/ping subtitle event  
**When** queue render  
**Then** có speaker/team identity, tối đa hai dòng, nền ≥92%, width ≤60%, queue/preemption/no-drop/coalesce rules  
**And** không che reticle/prompt/progress/HP/ammo.

**Given** competitive world audio như footstep/gunshot  
**When** subtitle resolver  
**Then** không tạo visual direction/source marker ngoài explicit system/ping contract  
**And** không biến âm thanh thành radar.

**Error/Recovery Path:** Queue overflow coalesce/drop theo documented priority có metric; P0 system state không bị mất.

**Test Boundary:** Queue/preemption/repetition, Việt/Anh long text, responsive collisions, team identities và prohibited audio visualization.

**Definition of Done:** Subtitle system rõ, localized, bounded và không tạo extra combat information.

### Story 8.15: Training Grounds

As a người chơi,
I want luyện bắn với bia và bot không ảnh hưởng thống kê,
So that học súng trước khi vào Standard.

**Source Requirements:** FR94; NFR23–NFR24, NFR31; UX-DR44, UX-DR56.

**Depends on:** Epic 1–3, Story 8.4–8.6.

**Blocks:** Story 8.16, Story 8.19.

**Module/File Ownership:** Training mode/rules, targets/bots, local/session results và tests.

**Platform Applicability:** Năm client; local/headless training host.

**Acceptance Criteria:**

**Given** Training Grounds launch  
**When** session chạy  
**Then** có static targets, moving targets 2–8 m/s và bots với ba approved behaviors  
**And** dùng cùng movement/combat/item manifest Standard.

**Given** training result  
**When** session kết thúc  
**Then** không ghi competitive profile/stats/mastery/reward  
**And** UI không tạo reward/store funnel.

**Error/Recovery Path:** Bot/target scenario lỗi cô lập/restart target, không mutate profile; offline vẫn vào Training nếu assets local hợp lệ.

**Test Boundary:** Target speeds, three behaviors, weapon parity, profile-write prohibition và five-platform smoke.

**Definition of Done:** Training đầy đủ targets/bots, offline-capable và không ảnh hưởng competitive data.

### Story 8.16: Optional Field Orientation onboarding

As a người chơi mới,
I want hướng dẫn ngắn có thể bỏ qua/chơi lại,
So that hiểu movement, loot, fire và zone trước trận thật.

**Source Requirements:** FR95; UX-DR44, UX-DR48, UX-DR56.

**Depends on:** Story 8.4, Story 8.15 và core gameplay Epic 1–4.

**Blocks:** Story 8.19.

**Module/File Ownership:** Orientation flow/checkpoints, local progress store, presenters và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** orientation start  
**When** player tiến hành  
**Then** có bốn checkpoint movement-camera, loot-inventory, fire-ADS, zone-cover với Start/Skip/Continue/Restart  
**And** local store giữ checkpoint gần nhất.

**Given** complete hoặc skip  
**When** flow kết thúc  
**Then** trở về Lobby và không reward/mastery/competitive stats  
**And** người chơi có thể replay.

**Error/Recovery Path:** Progress corrupt fallback checkpoint đầu/explicit restart; không khóa Lobby/Deploy sau lỗi.

**Test Boundary:** All checkpoint paths, skip/replay/restart, persistence migration, profile-write prohibition và input-family parity.

**Definition of Done:** Orientation optional/replayable, bốn checkpoint đủ và không reward funnel.

### Story 8.17: Non-pausing Pause, Leave và focus-safe routing

As a người chơi,
I want Pause cho settings/leave mà không dừng trận,
So that biết hậu quả và luôn quay lại được gameplay.

**Source Requirements:** FR7, FR99–FR100; UX-DR14, UX-DR35–UX-DR36, UX-DR54; NFR41, NFR45.

**Depends on:** Story 4.10, Story 8.4, Story 8.9.

**Blocks:** Story 8.19.

**Module/File Ownership:** Pause presenter/surface, leave confirmation, focus/input routing và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** Pause mở  
**When** render  
**Then** server/world/audio không pause, focus ở Resume, one-modal limit và `ui_cancel` đóng một cấp  
**And** input gameplay bị neutralize/re-arm an toàn.

**Given** Leave chọn  
**When** confirmation hiển thị  
**Then** microcopy dùng authoritative aircraft/team-eliminated consequence  
**And** không gắn false failure warning sau team elimination.

**Error/Recovery Path:** Outcome unavailable disable confirm có reason; focus/pointer failure vẫn giữ Resume/close escape.

**Test Boundary:** Pause during combat/map/inventory, focus lifecycle, input click-through, leave state matrix và audio continuity.

**Definition of Done:** Pause non-pausing, focus-safe và Leave consequence chính xác.

### Story 8.18: Spectator HUD, map, damage và audio parity

As a spectator,
I want giao diện phản ánh đúng đồng đội đang xem,
So that theo dõi hữu ích nhưng không có thông tin bí mật.

**Source Requirements:** FR8, FR97–FR99; UX-DR46, UX-DR49; NFR31–NFR35, NFR45.

**Depends on:** Story 4.9, Story 8.5–8.8, Story 8.12.

**Blocks:** Story 8.19.

**Module/File Ownership:** Spectator presenters/view states, target camera/audio binding, permission filters và tests.

**Platform Applicability:** Năm client.

**Acceptance Criteria:**

**Given** server-confirmed spectator target  
**When** HUD/Map/audio render  
**Then** chỉ target-valid health/ammo/squad/map/damage/audio state, HRTF theo target camera  
**And** không inventory riêng, free camera, marker mới hoặc off-target cue.

**Given** target eliminated/disconnects  
**When** resolver chuyển  
**Then** focus camera/UI tới next valid teammate hoặc team-eliminated state  
**And** stale target info cleanup ngay theo snapshot.

**Error/Recovery Path:** Target state unavailable ẩn field nhạy cảm và chờ canonical target, không giữ last-known enemy info.

**Test Boundary:** Target switches/elimination, field allowlist, map/damage/audio, voice/ping permissions và platform parity.

**Definition of Done:** Spectator UI/audio chỉ phản ánh target hợp lệ, không extra information.

### Story 8.19: Five-platform UX/accessibility acceptance gate

As a người chơi,
I want toàn bộ UI/audio/onboarding dùng được trên thiết bị của mình,
So that release không bỏ lại một nhóm input, màn hình hoặc nhu cầu tiếp cận.

**Source Requirements:** FR94–FR105; UX-DR1–UX-DR56; NFR31–NFR45.

**Depends on:** Story 8.1–8.18.

**Blocks:** Epic 9 production surfaces và Epic 10 release candidate.

**Module/File Ownership:** UX acceptance matrix, automated screenshots/accessibility scans, playtest protocols và decision backlog.

**Platform Applicability:** Windows, Linux, macOS, Android và iOS.

**Acceptance Criteria:**

**Given** required desktop/mobile resolution, scale, safe-area, locale, input và accessibility matrix  
**When** automated/manual acceptance chạy  
**Then** không crop/overlap/trap/contrast/glyph/critical-cue failure và information parity giữ đúng  
**And** Training/Orientation/Settings/HUD/Inventory/Map/Pause/Spectator/audio flows hoàn tất.

**Given** screen reader/menu narration, extended subtitle controls, motor/hearing playtest và professional photosensitivity scope  
**When** gate review  
**Then** mỗi item có v1/deferred decision, risk, owner và follow-up evidence  
**And** không tuyên bố hỗ trợ chưa kiểm chứng.

**Given** critical acceptance fail  
**When** report tổng hợp  
**Then** release flow bị block với surface/platform/locale/scale/reproduction  
**And** không sửa bằng giảm text dưới minimum hoặc thêm prohibited cue.

**Error/Recovery Path:** Device/sample unavailable ghi Missing Evidence và fail relevant gate, không coi là pass.

**Test Boundary:** Full responsive matrix, keyboard/pointer/Touch/Gyro, localization, accessibility/motion/audio/voice, prohibited-content/information scan và representative playtests.

**Definition of Done:** UX/accessibility gate đạt hoặc deferred scope minh bạch; mọi FR/UX-DR có evidence và production surfaces ổn định.

## Epic 9: Hồ sơ và tính toàn vẹn sản phẩm

Người chơi có hồ sơ, mastery không tăng sức mạnh, Results/Replay Summary, Report/Block và một sản phẩm không storefront, FOMO hoặc pay-to-win.

### Story 9.1: Idempotent match-result persistence

As a người chơi,
I want kết quả máy chủ được lưu đúng một lần,
So that hồ sơ không tăng/giảm sai vì retry hoặc lỗi backend.

**Source Requirements:** FR10, FR92, FR106; NFR20, NFR26–NFR30, NFR55.

**Depends on:** Story 4.11, Story 6.15, Story 8.19.

**Blocks:** Story 9.2–9.5, Story 9.8.

**Module/File Ownership:** Backend result command/API, CockroachDB migrations/repository, audit/idempotency tests.

**Platform Applicability:** Linux match server, Nakama/backend và CockroachDB.

**Acceptance Criteria:**

**Given** server-signed result command  
**When** persist  
**Then** dùng command ID, payload hash và precondition/version để ghi match/result/stat events atomic  
**And** cùng command+payload idempotent, cùng ID khác payload là security error.

**Given** transient DB/network failure  
**When** retry  
**Then** không duplicate stats/result và receipt phản ánh Pending/Committed/Rejected  
**And** match server không nhận database credentials.

**Given** CockroachDB `26.2.3` dependency  
**When** migrate/deploy  
**Then** version/checksum/license/wrapper/schema rollback contract được pin  
**And** live match state không chuyển vào DB.

**Error/Recovery Path:** Failure giữ durable retry/outbox state theo owner, result UI Pending/Unavailable; không dựng success local.

**Test Boundary:** Idempotency/payload mismatch, transaction rollback, retry/outage, migration forward/rollback và security/log scans.

**Definition of Done:** Result persistence exactly-once effect, auditable, retry-safe và đủ nền cho profile/report.

### Story 9.2: Non-power player profile statistics

As a người chơi,
I want xem lịch sử và chỉ số của mình,
So that theo dõi tiến bộ mà không nhận sức mạnh ngoài trận.

**Source Requirements:** FR92, FR96; NFR30, NFR54.

**Depends on:** Story 9.1.

**Blocks:** Story 9.3–9.4, Story 9.8.

**Module/File Ownership:** Profile/stat read model/API, client profile presenter/view state và tests.

**Platform Applicability:** Năm client và backend.

**Acceptance Criteria:**

**Given** committed results  
**When** profile reduce/query  
**Then** hiển thị matches, top 10, wins, longest kill, accuracy và season history từ authoritative data  
**And** profile không ảnh hưởng gameplay data/loadout/MMR power.

**Given** result pending/missing hoặc backend degraded  
**When** profile load  
**Then** state Pending/Unavailable/stale timestamp rõ  
**And** client không cộng số dự đoán.

**Error/Recovery Path:** Read-model rebuild từ result events/checkpoints; query failure giữ last-known read-only state có freshness.

**Test Boundary:** Reducer accuracy, season boundaries, pending/out-of-order results, privacy/authorization và five-platform UI.

**Definition of Done:** Profile stats chính xác, non-power và có degraded states minh bạch.

### Story 9.3: Weapon Mastery without power, skins or expiry

As a người chơi,
I want mastery phản ánh kinh nghiệm sử dụng súng,
So that có mục tiêu tự cải thiện không tạo pay/grind advantage.

**Source Requirements:** FR93, FR96; NFR24, NFR30, NFR54.

**Depends on:** Story 2.3, Story 9.1–9.2.

**Blocks:** Story 9.8.

**Module/File Ownership:** Mastery reducers/definitions, profile badges/deep stats presenter và prohibition tests.

**Platform Applicability:** Năm client và backend.

**Acceptance Criteria:**

**Given** committed weapon events/results  
**When** mastery reduce  
**Then** chỉ mở deep statistics và non-expiring profile badges  
**And** không unlock skin, weapon, attachment, stat bonus hoặc gameplay access.

**Given** season change/account sync  
**When** profile load  
**Then** earned mastery/badges không hết hạn theo FOMO  
**And** client/local file không author mastery.

**Error/Recovery Path:** Unknown weapon/event bị quarantine khỏi reducer có metric; không cộng vào arbitrary category.

**Test Boundary:** Reducer/event eligibility, no-power/no-skin schema scan, season persistence và tampered client data.

**Definition of Done:** Mastery chỉ deep stats/badge, server-derived, không expiry hoặc gameplay reward.

### Story 9.4: Production Results và Replay Summary states

As a người chơi,
I want Results giải thích trận bằng dữ liệu đã xác nhận,
So that biết mình đã làm gì và không bị xem kill-cam giả.

**Source Requirements:** FR10–FR11, FR106; UX-DR31; NFR2, NFR20, NFR30.

**Depends on:** Story 4.12, Story 9.1–9.3.

**Blocks:** Story 9.5–9.6, Story 9.8.

**Module/File Ownership:** Production Results/Replay Summary presenters/view states, evidence/stat query port và UI tests.

**Platform Applicability:** Năm client và backend/evidence services.

**Acceptance Criteria:**

**Given** committed payload  
**When** Results/Replay Summary render  
**Then** ưu tiên placement, survival, kills/assists và self-improvement stats từ server/evidence  
**And** Play Again/Lobby/eligible Report/Block hoạt động.

**Given** payload chưa tới hoặc không có  
**When** surface load  
**Then** hiển thị Pending hoặc Unavailable rõ  
**And** không dựng kill-cam, timeline, stats hoặc celebration giả.

**Error/Recovery Path:** Query/replay payload fail giữ Results/navigation và retry bounded; không mất report draft target context.

**Test Boundary:** Committed/Pending/Unavailable, data provenance, navigation, responsive/accessibility và no-fabrication/no-reward-loop scan.

**Definition of Done:** Results/summary production-ready, truth-bound và có mọi state lỗi rõ.

### Story 9.5: Report MVP with evidence window và retry receipt

As a người chơi,
I want gửi report đúng người/sự việc và nhận receipt,
So that hành vi gây hại có thể được xem xét dựa trên evidence.

**Source Requirements:** FR82, FR107; UX-DR47; NFR2, NFR28, NFR30.

**Depends on:** Story 6.12, Story 6.15, Story 9.1, Story 9.4.

**Blocks:** Story 9.8 và moderation operations release contract.

**Module/File Ownership:** Report schema/API/draft store, evidence-window linker, client flow/receipt/retry và tests.

**Platform Applicability:** Năm client, backend và authorized moderation tooling.

**Acceptance Criteria:**

**Given** eligible match participant  
**When** report draft tạo  
**Then** category là Cheating, Team-kill/Friendly-fire abuse, Harassment/Voice, Teaming, Exploit hoặc Other, note optional  
**And** draft gắn match/target/account-reporter hash/evidence window, không raw voice.

**Given** submit online/offline/transient failure  
**When** retry  
**Then** idempotent command trả receipt hoặc Pending/Retry state, draft giữ local an toàn  
**And** microcopy trung tính, không kết tội trước evidence.

**Given** target/self/match/category invalid  
**When** validate  
**Then** report reject có reason và không tạo case  
**And** deep taxonomy/SLA có explicit v1 contract/owner.

**Error/Recovery Path:** Offline/service outage giữ draft bounded/encrypted where available; receipt mismatch fail security, không duplicate case.

**Test Boundary:** Eligibility/categories/notes, offline retention/retry/idempotency, evidence linkage, authorization/privacy và UI accessibility.

**Definition of Done:** Report MVP chức năng, receipt/retry/evidence link đúng và không lưu raw voice.

### Story 9.6: Immediate local Block separate from Report

As a người chơi,
I want block một người ngay cả khi report chưa gửi,
So that kiểm soát tương tác của mình không phụ thuộc moderation backend.

**Source Requirements:** FR11, FR108; UX-DR47; NFR30.

**Depends on:** Story 9.4.

**Blocks:** Story 9.8.

**Module/File Ownership:** Local block store/service, platform/voice/social adapters, Results flow integration và tests.

**Platform Applicability:** Năm client; backend sync nếu có không là authority cho immediate local effect.

**Acceptance Criteria:**

**Given** eligible account target  
**When** Block  
**Then** local block áp ngay, versioned/persisted và tách command/state khỏi Report  
**And** hoạt động khi Report Pending/offline/fail.

**Given** unblock, duplicate hoặc corrupt store  
**When** mutation/load  
**Then** action idempotent, canonical local list rõ và safe migration/fallback  
**And** block không đổi match result/evidence.

**Error/Recovery Path:** Persistence fail báo chưa lưu và giữ in-session effect rõ; không báo thành công vĩnh viễn giả.

**Test Boundary:** Block/unblock/idempotency, report independence, offline/restart/migration và voice/social adapter effects.

**Definition of Done:** Block local tức thời, bền vững, độc lập Report và không ảnh hưởng gameplay truth.

### Story 9.7: No-commerce, no-FOMO product integrity gates

As a người chơi,
I want sản phẩm không bán sức mạnh hoặc tạo áp lực FOMO,
So that mọi gameplay value đến từ hành động trong trận.

**Source Requirements:** FR39, FR93, FR96–FR97; NFR1, NFR3, NFR24, NFR54; UX-DR11, UX-DR31, UX-DR56.

**Depends on:** Story 9.2–9.6 và Epic 8.

**Blocks:** Story 9.8 và release candidate.

**Module/File Ownership:** Product capability manifest, prohibited-content static/runtime scans, UI route inventory và audit reports.

**Platform Applicability:** Năm client, backend config và all release artifacts.

**Acceptance Criteria:**

**Given** v1 client/backend/content manifest  
**When** integrity audit  
**Then** không storefront, premium currency, microtransaction, loot box, gacha, battle pass, daily streak, ad hoặc live-event  
**And** không loadout/pre-match power, expiring mastery badge hoặc essential gameplay behind progression/payment.

**Given** UI/routes/config/content  
**When** prohibited pattern scan/manual review  
**Then** không store/news/reward rail/FOMO countdown/red badge/live-service celebration  
**And** remote config không thể bật hidden commercial/power capability.

**Error/Recovery Path:** Phát hiện prohibited capability block build/schema deployment; không chỉ ẩn nút UI trong khi backend route còn hoạt động.

**Test Boundary:** Static route/schema/content scans, runtime capability manifest, adversarial config và five-platform UI audit.

**Definition of Done:** Product integrity gate machine+manual đạt, không commerce/FOMO/power path trong v1.

### Story 9.8: Profile, Results, Report/Block integrity gate

As a người chơi,
I want hồ sơ và công cụ sau trận chính xác, riêng tư và ổn định,
So that tin tưởng dữ liệu và cách sản phẩm xử lý hành vi.

**Source Requirements:** FR92–FR93, FR96, FR106–FR108; NFR2, NFR19–NFR20, NFR28–NFR30, NFR54.

**Depends on:** Story 9.1–9.7.

**Blocks:** Epic 10 release candidate.

**Module/File Ownership:** End-to-end profile/result/moderation/product-integrity scenarios, privacy/security reports và gate.

**Platform Applicability:** Năm client, backend/database/evidence services.

**Acceptance Criteria:**

**Given** committed/pending/failed result, profile/mastery và report/block scenarios  
**When** E2E chạy dưới retry/offline/degraded conditions  
**Then** không duplicate/fabricate/lost mutation, receipt/state đúng và local block độc lập  
**And** no-power/no-commerce invariants giữ.

**Given** authorization/privacy audit  
**When** inspect logs/storage/API/artifacts  
**Then** không token/raw voice/unneeded PII, AccountId/hash boundaries đúng và retention hooks hiện hữu  
**And** evidence access permission-gated.

**Given** gate fail  
**When** report  
**Then** release blocked với account/match/command-safe reproduction  
**And** không sửa bằng bỏ Pending/Unavailable hoặc local truth.

**Error/Recovery Path:** Failed service scenario giữ durable recovery state; test data cleanup/audit đầy đủ.

**Test Boundary:** Full result→profile/mastery→summary→report/block flows, retry/idempotency, privacy/security và five-platform UX.

**Definition of Done:** Epic 9 E2E/integrity/privacy gates đạt và toàn bộ product non-power/non-commerce được chứng minh.

## Epic 10: Bản phát hành ổn định trên năm nền tảng

Người chơi nhận được các bản build tương thích, an toàn và đạt performance/reliability trên Windows, Linux, macOS, Android và iOS; Linux headless server có thể vận hành và rollback.

### Story 10.1: Dependency lock, upgrade ADR và SBOM

As a đội phát hành,
I want mọi dependency có nguồn và phiên bản kiểm soát,
So that build có thể tái tạo, audit và nâng cấp an toàn.

**Source Requirements:** NFR26, NFR28, NFR30, NFR49, NFR55.

**Depends on:** Epic 1–9.

**Blocks:** Story 10.2–10.15.

**Module/File Ownership:** Dependency/version/checksum/license manifest, ADRs, wrappers/owners, SBOM generator và CI policy.

**Platform Applicability:** Tất cả client/server/backend/tool artifacts.

**Acceptance Criteria:**

**Given** engine/plugin/SDK/database/orchestrator/native dependency  
**When** release manifest build  
**Then** có exact version, source, license, checksum, wrapper, owner và platform applicability  
**And** Godot Standard/export templates pin `4.7.1-stable`.

**Given** upgrade proposal  
**When** review  
**Then** phải có ADR, compatibility branch, protocol/content migration và five-platform/server parity gates  
**And** native/plugin mới cần profiling hoặc spike chứng minh.

**Given** release artifacts  
**When** SBOM generate  
**Then** dependency graph/hash gắn artifact/build ID  
**And** unknown/unapproved component block release.

**Error/Recovery Path:** Checksum/license/source mismatch fail build; giữ previous lock/artifacts, không tự fetch latest.

**Test Boundary:** Manifest completeness, checksum verification, prohibited/unwrapped dependency scan, SBOM reproducibility và upgrade-gate simulation.

**Definition of Done:** Dependency lock/SBOM đầy đủ, mọi upgrade có ADR/gate và không floating version.

### Story 10.2: Reproducible CI artifact family và signing boundaries

As a đội phát hành,
I want một commit tạo đúng family artifact có provenance,
So that mọi platform/server cùng build/content/protocol identity.

**Source Requirements:** FR13, FR71, FR110; NFR28, NFR31, NFR49–NFR50, NFR55.

**Depends on:** Story 10.1.

**Blocks:** Story 10.3–10.8, Story 10.15.

**Module/File Ownership:** CI workflows, build containers/runners, artifact manifest/checksums, signing interfaces và reports.

**Platform Applicability:** Windows, Linux, macOS, Android, iOS và Linux headless.

**Acceptance Criteria:**

**Given** immutable source/dependency/content lock  
**When** CI build  
**Then** tạo six-target artifact family với cùng build/protocol/schema/content identities và per-artifact checksum/SBOM  
**And** server package không chứa unnecessary texture/mesh/shader/audio.

**Given** signing/notarization credentials  
**When** platform stage chạy  
**Then** secrets ở isolated runners/secure stores ngoài repository/artifact/log/prompt/MCP  
**And** unsigned development artifact phân biệt rõ release-signed artifact.

**Error/Recovery Path:** Bất kỳ target/hash/provenance fail làm family incomplete/not releasable; không publish partial family như RC.

**Test Boundary:** Clean/repeat build, artifact identity/hash, secret scans, package-content rules và N/N-1 compatibility metadata.

**Definition of Done:** CI tạo artifact family tái lập, provenance đầy đủ và signing boundaries an toàn.

### Story 10.3: Windows x64 release qualification

As a người chơi Windows,
I want bản build cài/chạy ổn định trên Windows 10/11,
So that có trải nghiệm Standard đầy đủ và tương thích.

**Source Requirements:** NFR4–NFR7, NFR19, NFR31–NFR45, NFR49–NFR50.

**Depends on:** Story 10.2.

**Blocks:** Story 10.9, Story 10.15.

**Module/File Ownership:** Windows export/profile, installer/signing config, device-test scenarios và qualification report.

**Platform Applicability:** Windows 10/11 x64.

**Acceptance Criteria:**

**Given** signed Windows candidate  
**When** clean install/update/uninstall/launch/network/input/audio tests chạy  
**Then** full feature/parity matrix đạt, settings/save paths/permissions đúng và crash reporting initialized  
**And** không secret/dev-tools/unsigned native dependency.

**Given** minimum/recommended hardware  
**When** representative smoke/performance replay  
**Then** thu frame/RAM/load metrics cho Story 10.9 và installer/content size nằm desktop ≤25 GB  
**And** failure có hardware/driver/build reproduction.

**Error/Recovery Path:** Signing/installer/runtime failure block Windows RC; rollback/uninstall không xóa user settings ngoài policy.

**Test Boundary:** Win10/11 install/update/launch, KBM/audio/network, accessibility/resolutions, crash/restore và package/security scans.

**Definition of Done:** Windows build signed/qualified, feature-parity complete và sẵn sàng performance gate.

### Story 10.4: Linux x64 client release qualification

As a người chơi Linux,
I want bản native x64 có input/UI/network parity,
So that Linux không là target hạng hai.

**Source Requirements:** NFR4–NFR7, NFR19, NFR31–NFR45, NFR49–NFR50.

**Depends on:** Story 10.2.

**Blocks:** Story 10.9, Story 10.15.

**Module/File Ownership:** Linux client export/package, distro/runtime profile, input-label tests và qualification report.

**Platform Applicability:** Linux x86-64 supported baseline.

**Acceptance Criteria:**

**Given** Linux candidate  
**When** clean package/launch/update/input/audio/network tests  
**Then** full feature/protocol/content parity, filesystem permissions và runtime dependencies đúng  
**And** non-QWERTY/physical-logical key labels/Wayland-X11 policy đã chứng minh.

**Given** minimum/recommended class  
**When** performance smoke  
**Then** metrics đi vào Story 10.9, package trong desktop size budget  
**And** không desktop-only fair capability thiếu Linux.

**Error/Recovery Path:** Missing runtime/distro/input issue block Linux RC với environment reproduction; không silently disable gameplay.

**Test Boundary:** Clean launch/update, input layouts/display stacks, audio/HRTF, resolutions/accessibility, network và package scans.

**Definition of Done:** Linux client qualified ngang Windows/macOS về feature/fairness.

### Story 10.5: macOS Universal 2 signing và notarization

As a người chơi macOS,
I want build Intel/Apple Silicon được ký và notarize,
So that cài/chạy an toàn trên macOS 13+.

**Source Requirements:** NFR4–NFR7, NFR19, NFR31–NFR45, NFR49–NFR50, NFR55.

**Depends on:** Story 10.2.

**Blocks:** Story 10.9, Story 10.15.

**Module/File Ownership:** macOS Universal 2 export, entitlements/sign/notarize pipeline, native dependency validation và report.

**Platform Applicability:** macOS 13+ Intel và Apple Silicon.

**Acceptance Criteria:**

**Given** isolated macOS runner/credentials  
**When** build/sign/notarize/staple  
**Then** Universal 2 artifact pass Gatekeeper, entitlements tối thiểu và both architectures launch same identities  
**And** secrets không ra logs/artifacts.

**Given** Intel/Apple Silicon devices  
**When** feature/input/audio/network/accessibility tests  
**Then** parity đạt và metrics đi Story 10.9  
**And** native SDK/plugin có both-arch checksum/build evidence.

**Error/Recovery Path:** Signing/notarization/architecture failure block macOS RC; không distribute unsigned substitute.

**Test Boundary:** Signature/notarization/Gatekeeper, Intel/ARM launch, lifecycle/input/audio/network, accessibility và package scan.

**Definition of Done:** macOS Universal 2 signed/notarized và qualified trên cả hai architecture.

### Story 10.6: Android ARM64 AAB và device qualification

As a người chơi Android,
I want AAB chạy ổn định trên Android 10+,
So that Touch, lifecycle và network không mất trạng thái.

**Source Requirements:** FR13, FR24, FR109–FR110; NFR8–NFR12, NFR19, NFR31–NFR50.

**Depends on:** Story 10.2, Story 6.14, Story 8.11–8.19.

**Blocks:** Story 10.10, Story 10.15.

**Module/File Ownership:** Android export/AAB/signing config, manifest/permissions, device-lab scenarios và report.

**Platform Applicability:** Android 10+ ARM64 minimum/recommended devices.

**Acceptance Criteria:**

**Given** isolated signing config  
**When** AAB build/install/update  
**Then** package/ABI/permissions/audio/mic/network/secure storage/safe-area identities đúng và app launch/restore full feature  
**And** microphone permission vẫn contextual.

**Given** device matrix  
**When** Touch/Gyro/haptic/route/background/reconnect/accessibility tests  
**Then** semantic/parity contract đạt, không stuck input/PTT hoặc extra aim/information  
**And** install ≤12 GB.

**Error/Recovery Path:** Device/permission/lifecycle failure block Android RC; degraded capability explicit, không đổi input pool/rule.

**Test Boundary:** Install/update, device ratios/insets, multitouch/Gyro/haptic, call/background/reconnect, audio routes và security/package scans.

**Definition of Done:** Android AAB signed/qualified trên minimum/recommended device classes, sẵn sàng performance/thermal gate.

### Story 10.7: iOS ARM64 archive và TestFlight qualification

As a người chơi iOS,
I want build iOS 16+ an toàn và phục hồi đúng khi bị gián đoạn,
So that chơi mobile không mất seat hoặc quyền riêng tư.

**Source Requirements:** FR13, FR24, FR109–FR110; NFR8–NFR12, NFR19, NFR31–NFR50.

**Depends on:** Story 10.2, Story 6.14, Story 8.11–8.19.

**Blocks:** Story 10.10, Story 10.15.

**Module/File Ownership:** iOS export/Xcode archive, signing/provision/TestFlight pipeline, entitlements/privacy manifests và device report.

**Platform Applicability:** iOS 16+ ARM64 minimum/recommended devices.

**Acceptance Criteria:**

**Given** isolated macOS signing runner  
**When** archive/sign/upload TestFlight  
**Then** bundle/entitlements/privacy/permissions/secure storage/audio/network identities đúng và secret không lộ  
**And** installed build joins same protocol/content family.

**Given** iPhone/iPad device matrix  
**When** Touch/Gyro/haptic/safe-area/route/background/reconnect/accessibility tests  
**Then** parity đạt, no stuck input/PTT/mic và install ≤12 GB  
**And** lifecycle destinations đúng server state.

**Error/Recovery Path:** Signing/TestFlight/device failure block iOS RC; không dùng simulator-only evidence cho device behavior.

**Test Boundary:** Archive/sign/upload/install/update, phone/tablet insets, interruption/route/reconnect, permissions và package/privacy scans.

**Definition of Done:** iOS archive/TestFlight qualified trên device classes, sẵn sàng performance/thermal gate.

### Story 10.8: Linux headless server container hardening

As a vận hành viên,
I want server artifact nhỏ, an toàn và có lifecycle rõ,
So that trận có thể deploy/stop/rollback đáng tin.

**Source Requirements:** FR71, FR110; NFR13–NFR20, NFR26–NFR30, NFR49–NFR50.

**Depends on:** Story 10.2 và Epic 6.

**Blocks:** Story 10.11–10.15.

**Module/File Ownership:** Server export/container, non-root/runtime security, health/readiness/shutdown, config/secrets và tests.

**Platform Applicability:** Linux x86-64 headless server/containers.

**Acceptance Criteria:**

**Given** server container  
**When** scan/run  
**Then** non-root, minimal filesystem/capabilities, read-only where possible, no presentation assets/DB creds/dev cheat commands  
**And** build/protocol/schema/content identities/health endpoints đúng.

**Given** allocation/termination/Match-critical failure  
**When** lifecycle chạy  
**Then** readiness/drain/finalize/evidence/shutdown bounded và result retry safe  
**And** SIGTERM/timeout không tạo orphan match.

**Error/Recovery Path:** Config/secret/content mismatch fail before Ready; prior signed image còn rollback được.

**Test Boundary:** Container/security/SBOM scan, boot/readiness/health/drain/SIGTERM, secret/config failure và artifact parity.

**Definition of Done:** Server image hardened, nhỏ, lifecycle sạch và sẵn sàng load/reliability tests.

### Story 10.9: Desktop performance, memory và load-time gate

As a người chơi desktop,
I want FPS ổn định và thời gian vào trận hợp lý,
So that combat không bị quyết định bởi hitch.

**Source Requirements:** NFR4–NFR7, NFR18, NFR46–NFR50.

**Depends on:** Story 10.3–10.5 và production content Epic 7–9.

**Blocks:** Story 10.15.

**Module/File Ownership:** Desktop benchmark replay, profiling/telemetry, platform profiles và reports.

**Platform Applicability:** Windows/Linux/macOS minimum/recommended.

**Acceptance Criteria:**

**Given** standard replay/cache conditions  
**When** minimum desktop run  
**Then** 60 FPS median, p95 frame ≤25 ms at 1080p/Low, RAM ≤6 GB after 45 min và pre-match ≤45 s p95 cold cache  
**And** six nearby dense smokes vẫn nằm approved minimum envelope.

**Given** recommended desktop run  
**When** 1080p/High  
**Then** 90 FPS median, p95 frame ≤16,7 ms trên same replay  
**And** metrics gắn device/driver/build/map/manifest.

**Error/Recovery Path:** Missing sample/outlier/hitch fail relevant platform/profile gate; không average che p95.

**Test Boundary:** Minimum/recommended 45-minute replay, cold load, smoke/streaming hotspots, memory leak và three desktop OS.

**Definition of Done:** Desktop performance/memory/load budgets đạt bằng reproducible evidence.

### Story 10.10: Mobile performance, memory và thermal gate

As a người chơi mobile,
I want trận duy trì FPS mà không bị OS kill hoặc quá nhiệt giảm mạnh,
So that chơi dài vẫn cạnh tranh được.

**Source Requirements:** NFR8–NFR12, NFR18, NFR39–NFR40, NFR46–NFR50.

**Depends on:** Story 10.6–10.7 và production content Epic 7–9.

**Blocks:** Story 10.15.

**Module/File Ownership:** Android/iOS benchmark replay, thermal/memory telemetry, mobile profiles và reports.

**Platform Applicability:** Android/iOS minimum/recommended device classes.

**Acceptance Criteria:**

**Given** mobile minimum  
**When** standard replay/45-minute session  
**Then** 45 FPS median, p95 frame ≤33,3 ms Low, working memory ≤3 GB, no OS terminate và pre-match ≤60 s p95 cold cache  
**And** gameplay parity giữ.

**Given** mobile recommended  
**When** Medium/30-minute thermal soak  
**Then** 60 FPS median, p95 ≤25 ms và median FPS giảm ≤15%  
**And** six-smoke/streaming/combat hotspots có evidence.

**Error/Recovery Path:** Thermal/OS/device sample fail gate cho class/platform; không giảm collision/visibility/gameplay data để pass.

**Test Boundary:** Android/iOS min/recommended, 45-minute memory, 30-minute thermal, cold load, smoke/world hotspots và lifecycle interruptions.

**Definition of Done:** Mobile FPS/memory/thermal/load budgets đạt trên physical devices, không parity waiver.

### Story 10.11: 100-player server load và correctness soak

As a người chơi,
I want server giữ tick và kết quả đúng trong trận đầy tải,
So that quy mô 100 không làm combat/inventory/zone sai.

**Source Requirements:** NFR13–NFR17, NFR19–NFR22, NFR51–NFR53.

**Depends on:** Story 6.18, Story 7.10, Story 10.8.

**Blocks:** Story 10.14–10.15.

**Module/File Ownership:** Production 100-client load scenarios, server profiling/capacity reports và signed gate.

**Platform Applicability:** Linux headless server on target envelope.

**Acceptance Criteria:**

**Given** 100-client 45-minute production-map soak  
**When** run trên target envelope  
**Then** 30 Hz với ≥10% headroom, damage ≤1 tick p95, mean bandwidth ≤1,5 Mbps each direction/client và Alpha target ≤8 vCPU/16 GB được đo  
**And** ≥99% simulated matches tạo valid result trong reliability batch.

**Given** combat/world/zone/reconnect hotspots  
**When** evidence replay  
**Then** authority/correctness/result hashes giữ, position error ≤0,5 m p95 ở 80 ms/1% loss  
**And** không client/bot fallback.

**Error/Recovery Path:** Capacity fail khóa scope ở mức chứng minh theo NFR53, ghi decision; không làm sai số hoặc tăng envelope ngầm.

**Test Boundary:** Repeated 100-client soaks, hotspots/impairment, CPU/memory/network, result/evidence và capacity decision.

**Definition of Done:** Server load/correctness đạt production target hoặc scope giảm minh bạch; chỉ pass mở RC.

### Story 10.12: Network, streaming và patch-size hardening

As a người chơi,
I want mạng/world streaming phục hồi tốt và cập nhật không tải lại vô ích,
So that trận ổn định trên kết nối/ổ đĩa thực tế.

**Source Requirements:** NFR14–NFR16, NFR21–NFR22, NFR46–NFR50.

**Depends on:** Story 7.10, Story 10.2, Story 10.9–10.11.

**Blocks:** Story 10.15.

**Module/File Ownership:** Impairment/streaming/patch harness, relevance/cache/package delta profiles và reports.

**Platform Applicability:** Năm client, Linux server và CDN/update artifact simulation.

**Acceptance Criteria:**

**Given** latency/loss/jitter/reorder/cell traversal profiles  
**When** long scenarios chạy  
**Then** snapshot/correction/hit/streaming/lease correctness và budgets giữ, không gameplay-breaking hitch  
**And** failures tái hiện từ seed/cell/tick.

**Given** content/balance patch  
**When** delta package build  
**Then** unchanged content không tải lại >2 GB và install size desktop ≤25 GB/mobile ≤12 GB  
**And** manifest/hash/rollback integrity giữ.

**Error/Recovery Path:** Network/streaming/patch regression block RC; rollback về compatible manifest/artifact, không mix incompatible clients.

**Test Boundary:** Impairment sweeps, boundary leases, cold/warm cache, delta generation/apply/rollback và size/hash verification.

**Definition of Done:** Network/streaming robust, package/delta budgets đạt và rollback content an toàn.

### Story 10.13: Security, privacy, retention và account deletion

As a người chơi,
I want dữ liệu/tài khoản được bảo vệ và xóa theo policy,
So that chơi online không làm lộ bí mật hoặc lưu dữ liệu quá mức.

**Source Requirements:** NFR26–NFR30, NFR55; evidence/report/privacy architecture requirements.

**Depends on:** Epic 6, Epic 9, Story 10.1–10.8.

**Blocks:** Story 10.15.

**Module/File Ownership:** Threat/security tests, secrets/PII scans, retention/deletion workflows, audit/permission config và reports.

**Platform Applicability:** Năm client, server, backend/database, infrastructure và tooling.

**Acceptance Criteria:**

**Given** untrusted protocol/API/token/input  
**When** fuzz/abuse/authorization tests  
**Then** type/length/range/cadence/sequence/ownership/state/expiry/nonce/replay guards fail-closed  
**And** không secret/token/PII/raw voice trong source/log/artifact/prompt/MCP.

**Given** data lifecycle  
**When** retention jobs chạy  
**Then** operational 30d, crash 90d, raw telemetry 90d, aggregate non-PII 13m, unreported evidence 30d, reported evidence 180d/until closed theo policy  
**And** holds/audit/access permission rõ.

**Given** account deletion request  
**When** workflow execute  
**Then** mục tiêu hoàn tất ≤30 ngày trừ documented legal/security hold  
**And** essential operations tách optional analytics.

**Error/Recovery Path:** Security/privacy/deletion failure block RC/processing, alert/audit without exposed payload và có recovery owner.

**Test Boundary:** Protocol/API fuzz, auth/secret/PII scans, retention expiry, deletion E2E/hold, evidence permissions và dependency CVE review.

**Definition of Done:** Security/privacy gates đạt, retention/deletion vận hành được và không sensitive leakage.

### Story 10.14: Observability, crash reliability và rollout/rollback

As a vận hành viên,
I want phát hiện lỗi và rollback build/config an toàn,
So that sự cố không kéo dài hoặc trộn trận không tương thích.

**Source Requirements:** NFR19–NFR22, NFR28–NFR30, NFR51, NFR55.

**Depends on:** Story 10.8, Story 10.11, Story 10.13.

**Blocks:** Story 10.15.

**Module/File Ownership:** GameLog/metrics/traces, dashboards/alerts, crash pipeline, rollout/rollback runbooks và drills.

**Platform Applicability:** Năm client, Linux server, backend/infrastructure.

**Acceptance Criteria:**

**Given** production-like sessions  
**When** telemetry emit  
**Then** JSON logs/metrics liên kết trace/match/account hash/build/region/tick và thu tick/relevance/bytes/correction/hit/streaming/memory/thermal  
**And** hot path dùng counter/histogram, DEBUG/TRACE gated/bounded, không `print()`.

**Given** release rollout  
**When** canary/N/N-1/rollback  
**Then** backend có thể support compatible N/N-1 nhưng match không trộn incompatible protocol/content  
**And** remote ops config chỉ disable queue/region/provider, không đổi balance/pool/bot/rule.

**Given** crash/match/result failure drill  
**When** alert/runbook execute  
**Then** owner/detection/rollback/evidence/result recovery rõ, hướng tới crash-free ≥99,5% và valid-result ≥99,0%  
**And** signing/production secrets không vào diagnostics.

**Error/Recovery Path:** Observability outage không mở authority; rollout pause/rollback về signed compatible family với audit.

**Test Boundary:** Log/schema/privacy, metric cardinality, alerts/runbooks, crash/result drills, canary/N/N-1 compatibility và rollback.

**Definition of Done:** Observability/runbooks hoạt động, reliability targets có measurement và rollback drill thành công.

### Story 10.15: Five-platform release-candidate acceptance

As a người chơi,
I want release candidate hoàn chỉnh, công bằng và ổn định,
So that v1.0 chỉ phát hành khi toàn bộ lời hứa cốt lõi đã được chứng minh.

**Source Requirements:** FR1–FR110; NFR1–NFR55; UX-DR1–UX-DR56.

**Depends on:** Story 10.1–10.14 và mọi Epic gate.

**Blocks:** v1.0 production release.

**Module/File Ownership:** RC manifest/evidence index, cross-platform acceptance, balance/product/operations decisions, go/no-go và rollback package.

**Platform Applicability:** Windows, Linux, macOS, Android, iOS và Linux headless production server.

**Acceptance Criteria:**

**Given** one immutable RC artifact family  
**When** full functional/performance/security/UX/device/server matrix chạy  
**Then** 100-player loop, four gameplay pillars, server/load gate và five-platform RC family đạt required budgets/parity  
**And** build/protocol/schema/content/SBOM/signatures/checksums khớp.

**Given** balance/product evidence  
**When** go/no-go review  
**Then** death explainability, armor/weapon/drop-point targets, no-power/no-commerce, accessibility decisions, release price và server-cost decisions có owner/evidence  
**And** không claim unsupported/deferred capability.

**Given** một critical target không đạt  
**When** quyết định scope  
**Then** no-go hoặc giữ quy mô đã chứng minh, kèm rollback/follow-up  
**And** không dùng client authority, silent bots, parity reduction, fabricated evidence hoặc missing-device pass.

**Error/Recovery Path:** RC fail giữ previous signed family, issue reproduction/owner/risk và rerun affected plus mandatory regression gates.

**Test Boundary:** Full FR/NFR/UX traceability, five-platform certification/device tests, 100-player/8×8 scenarios, security/privacy, UX/accessibility, balance/integrity và rollout rollback drill.

**Definition of Done:** Mọi required gate đạt và go decision được ký với complete evidence/rollback; nếu không, v1.0 không phát hành.
