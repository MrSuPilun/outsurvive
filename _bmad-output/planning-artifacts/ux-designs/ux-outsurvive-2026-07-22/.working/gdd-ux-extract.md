# Trích xuất ràng buộc UX từ GDD — OutSurvive

**Nguồn duy nhất:** `/Users/hiddengem/Projects/godot/outsurvive/_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md`  
**Phiên bản nguồn:** 1.0.0, trạng thái `ready-for-architecture`, cập nhật 2026-07-22  
**Phạm vi:** Chỉ ghi lại quyết định và ràng buộc có tác động trực tiếp tới UX. Tài liệu này không bổ sung màu sắc, bố cục, luồng hay hành vi chưa có trong GDD.

## Vision / pillars

- Trải nghiệm nền là battle royale sinh tồn kiểu PUBG cổ điển trên PC: 100 người xuất phát tay trắng, tự chọn điểm rơi, loot tại chỗ, di chuyển theo vùng an toàn thu hẹp và chiến đấu cho tới khi còn một người hoặc một đội.
- Fantasy cốt lõi là dễ tổn thương, thông tin không hoàn hảo và thích nghi bằng những gì tìm được; chiến thắng phải đến từ thông tin, vị trí, quản trị rủi ro và kỹ năng vũ khí.
- Sinh tồn ở đây là sinh tồn chiến thuật theo trận, không phải survival-crafting. Đói, khát, xây căn cứ và chế tạo không thuộc vòng lặp cốt lõi.
- Nhịp trải nghiệm phải giữ được khoảng lặng giữa giao tranh, chuẩn bị căng thẳng, di chuyển có tính toán và giao tranh ngắn nhưng nguy hiểm; không hướng tới nhịp arcade liên tục.
- Khi các yêu cầu xung đột, thứ tự ưu tiên đã khóa là: (1) công bằng và toàn vẹn trận đấu; (2) căng thẳng sinh tồn và hậu quả quyết định; (3) độ rõ thông tin và khả năng phản ứng; (4) chiều sâu đấu súng/di chuyển; (5) vận hành, mở rộng nội dung và thương mại.
- P1: loot, đạn, hồi máu, thời gian, vị trí và tiếng động là tài nguyên hữu hạn; UX không được làm mất cảm giác đánh đổi.
- P2: sát thương cao nhưng mối đe dọa phải đọc được qua âm thanh, lóe nòng, va chạm, hướng nhận sát thương và địa hình.
- P3: thông tin và địa hình phải tạo lợi thế lớn hơn độ hiếm trang bị; UI không được biến đồ hiếm thành câu trả lời thay thế cho đọc trận.
- P4: sân chơi nghiêm túc và bình đẳng; không lớp nhân vật, kỹ năng chủ động, chỉ số trả phí hoặc loadout ngoài trận. Mỹ phẩm không được thay đổi silhouette chiến đấu, âm thanh, hitbox hay khả năng ngụy trang vượt giới hạn.
- Đối tượng là người chơi từ 18 tuổi thích battle royale chiến thuật, chấp nhận hậu quả cao và khả năng bị loại chỉ sau vài phút. Phiên chơi mục tiêu là 28–35 phút.

## Platform / form-factor / input

- Nền tảng v1.0: PC Windows 10/11 và Linux 64-bit; Godot 4.x; chuột và bàn phím.
- Độ phân giải chuẩn: 1920×1080. Phải hỗ trợ từ 1280×720 tới 3840×2160 và các tỷ lệ ultrawide phổ biến.
- Mobile, console, controller, controller aim assist và cross-play không thuộc v1.0.
- Góc nhìn Standard là TPP; có chuyển vai camera. ADS chuyển sang góc nhìn thứ nhất qua thước ngắm/ống ngắm.
- Khi sát tường, camera bị đẩy về phía trước. Vật thể hoặc đối thủ không được hiển thị nếu đường nhìn từ đầu nhân vật bị che hoàn toàn, nhằm hạn chế lợi thế nhìn xuyên góc của TPP.
- Sơ đồ phím đã nêu trong GDD: WASD di chuyển; chuột camera/ngắm; Shift chạy nhanh; Ctrl đi bộ; C ngồi; Z nằm; Space nhảy/vượt; Q/E nghiêng; F tương tác; R nạp đạn; G chọn vật ném; Tab mở kho đồ.
- Phải cho phép gán lại toàn bộ phím.
- Phải cho phép chọn giữ/nhấn cho ADS, nghiêng, ngồi và chạy; phần khả năng tiếp cận cũng yêu cầu tùy chọn toggle/hold.
- Độ nhạy phải chỉnh riêng cho hip-fire, ADS và từng độ phóng. FOV, rung camera và cường độ flash cũng phải điều chỉnh được.
- Chuột không có aim assist, magnetism hoặc đạn bẻ hướng.

## HUD / information hierarchy

- Danh sách thông tin HUD trận được GDD giới hạn ở: HP/tăng lực, đạn, tư thế, hướng, minimap, trạng thái đội và pha bo.
- HUD trận không được chứa banner cửa hàng, nhiệm vụ, quảng cáo hoặc tiến trình battle pass.
- Không hiển thị số sát thương nổi trong trận Standard.
- Người bị bắn nhận chỉ báo hướng theo cung 30°; chỉ báo không được tiết lộ vị trí hoặc khoảng cách của người bắn.
- Hit feedback có thể xác nhận đã trúng bằng hiệu ứng máu/bụi, âm thanh nhẹ và phản ứng cơ thể; xác nhận hạ gục chỉ xuất hiện sau khi máy chủ xác nhận trạng thái.
- Tâm pha bo kế tiếp được lộ khi pha chờ bắt đầu. Không có vật phẩm dự báo bo.
- Nếu độ trễ vượt 150 ms, người chơi phải nhận cảnh báo kết nối.
- Nếu hàng chờ thử nghiệm dùng bot, UI phải ghi rõ số bot dự kiến trước khi người chơi vào trận; bot không được dùng âm thầm để lấp đầy Standard.
- Friendly fire bật ở 100% sau khi lên máy bay; UI phải ghi rõ nguồn sát thương và cung cấp luồng báo cáo.
- Không có chỉ báo bước chân trực quan trong hàng chờ cạnh tranh vì nó làm thay đổi cân bằng thông tin.
- Biển báo, màu vật liệu và địa danh trong thế giới phải hỗ trợ định hướng mà không bắt người chơi phụ thuộc hoàn toàn vào minimap.

## Inventory / map / loot

- Kho đồ chiếm tối đa 70% màn hình và vẫn phải để lộ vùng trung tâm/xung quanh để duy trì rủi ro khi loot.
- Bản đồ toàn màn hình hiển thị đường bay, bo hiện tại, bo tiếp theo, marker đội và địa danh; không hiển thị loot hoặc đối thủ.
- Nhặt nhanh một vật phẩm mất 0,20 giây. Kéo thả trong giao diện kho đồ không làm chậm thời gian trận.
- Không tự động nhặt vũ khí, giáp hoặc phụ kiện. Người chơi có thể bật tự nhặt đúng cỡ đạn tới một ngưỡng do họ đặt.
- Sức chứa cơ thể là 50; ba cấp ba lô nâng tổng sức chứa lên 120/180/250.
- Các slot đã khóa: hai vũ khí chính, một súng ngắn, một cận chiến và một vật ném đang chọn.
- Đạn, hồi máu và vật ném tiêu tốn sức chứa; phụ kiện đã gắn trên súng không tiêu tốn sức chứa.
- Năm cỡ đạn phải có màu, hình hộp và biểu tượng riêng.
- Cấp vật phẩm không được truyền đạt chỉ bằng màu.
- Quỹ đạo dự kiến của vật ném chỉ hiện trong 1,5 giây đầu khi ngắm.
- Thùng tiếp tế dùng khói có thể thấy từ 800 m; không vật phẩm thiết yếu nào chỉ có trong thùng tiếp tế.
- Loot phải giữ tính ngẫu nhiên có trọng số theo loại không gian, đồng thời đáp ứng ngưỡng chống “không có súng” đã định lượng trong GDD.

## Party / voice / ping / spectator

- Chế độ Standard hỗ trợ Solo 100 người, Duo tối đa 50 đội và Squad 25 đội bốn người.
- Bước chuẩn bị cho phép chọn Solo, Duo hoặc Squad; không cho chọn vũ khí hay kỹ năng.
- Giao tiếp đội gồm voice, ping vị trí và 8 ping ngữ cảnh.
- Ping không được tự nhận dạng kẻ địch xuyên vật cản.
- Người gục có thể bò, đánh dấu và nói chuyện; không thể dùng súng, hồi máu hoặc tự cứu.
- Cứu đồng đội mất 10 giây và bị ngắt khi người cứu di chuyển hoặc chịu sát thương.
- Người bị loại có thể xem đồng đội cho tới khi đội bị loại.
- Spectator nâng cao, replay người dùng đầy đủ và kill-cam cạnh tranh không thuộc v1.0.
- Báo cáo, chặn, log trận và replay phục vụ điều tra phải được hỗ trợ từ bản phát hành.
- Kết quả Training Grounds không ảnh hưởng thống kê cạnh tranh.

## State flows

- Vòng đời trận đã khóa: chọn Solo/Duo/Squad và sảnh chờ → quan sát đường bay → đổ bộ → trang bị ban đầu → đọc vùng an toàn → di chuyển/giao tranh → kết thúc với 5–10 người cuối → kết quả.
- Các khoảng thời gian mục tiêu có ảnh hưởng UX: chuẩn bị 60 giây; quan sát đường bay 30–45 giây; đổ bộ 20–90 giây; loot ban đầu 2–5 phút.
- Kết quả sau trận cung cấp thống kê và replay tóm tắt; không trao sức mạnh cho trận sau.
- Solo bị loại khi HP về 0. Duo/Squad dùng trạng thái Gục; người chơi bị loại khi bị kết liễu hoặc khi toàn đội không còn thành viên có thể chiến đấu.
- Rời trận sau khi máy bay khởi hành được tính là thất bại. Không áp dụng hình phạt rời trận sau khi đội đã bị loại.
- Không có hồi sinh, mua lại, tự hồi sinh hoặc trạm triệu hồi trong Standard.
- Hồi máu có thời gian dùng và giới hạn cụ thể; túi cứu thương/bộ cứu thương lớn bị ngắt khi di chuyển hoặc chịu sát thương. HP không tự hồi.
- Chiến đấu có ba trạng thái ngắm: TPP hip-fire, ngắm qua vai và ADS qua sight; chuyển trạng thái theo thời gian ADS của vũ khí.
- Scope phù hợp cho phép chỉnh zero 100–800 m theo bước 100 m; scope 4× trở lên cho phép giữ hơi tối đa 8 giây, sau đó dao động tăng gấp đôi trong 4 giây.
- Phương tiện phát nổ sau khi HP về 0 với cảnh báo cháy 3 giây.
- Vùng an toàn có chín pha với chờ, thu, bán kính, sát thương và số người sống mục tiêu đã định lượng. Pha 1–3 cho phép chữa/di chuyển ngoài bo có chủ đích; từ pha 6, ngoài bo không còn là chiến thuật bền vững.
- Nếu không có vùng mạng đáp ứng ngưỡng, trận Standard không được khởi tạo trừ khi người chơi xác nhận tiếp tục.
- Thời tiết được chọn lúc bắt đầu trận và không đổi đột ngột giữa trận.

## Accessibility

- Gán lại toàn bộ phím; hỗ trợ toggle/hold.
- Cho phép chỉnh FOV, độ nhạy, rung camera và cường độ flash.
- Có ba preset mù màu áp dụng cho bo, marker, hit effect và reticle.
- Không chỉ dùng màu để truyền đạt cấp vật phẩm.
- Máu có tùy chọn giảm hoặc đổi màu, nhưng độ rõ của hit feedback phải tương đương.
- Có phụ đề cho thông báo hệ thống và ping đồng đội.
- Không cung cấp chỉ báo bước chân trực quan trong hàng chờ cạnh tranh do ràng buộc công bằng thông tin.

## Feedback / game feel

- Mỗi phát bắn phải phân biệt được bằng tiếng nổ, tiếng cơ khí, lóe nòng, vỏ đạn và phản lực camera.
- Hit feedback gồm máu/bụi theo cài đặt nội dung, âm thanh nhẹ và phản ứng cơ thể; không xác nhận hạ gục trước máy chủ.
- Recoil, spread, ADS timing, aim punch và thời gian hồi sau hành động là một phần của cảm giác vũ khí; UX không được che giấu các trạng thái này bằng phản hồi gây hiểu nhầm.
- Không có nhạc nền khi người chơi còn sống. Âm nhạc chỉ có ở menu, kết quả và khoảnh khắc chiến thắng.
- Bước chân phải phân biệt theo đất, cỏ, gỗ, bê tông, kim loại và nước; khoảng nghe thay đổi theo trạng thái di chuyển.
- Súng phải có âm gần/xa khác nhau. Âm thanh súng, xe, máy bay và thùng tiếp tế phải duy trì khả năng đọc giao tranh theo khoảng cách đã nêu trong GDD.
- Mưa làm giảm khoảng nghe bước chân 15% và tăng tiếng môi trường; sương giảm độ tương phản mục tiêu sau 180–250 m. Cả hai được báo từ đầu trận qua trạng thái thời tiết đã chọn.
- Camera shake và cường độ flash phải có tùy chỉnh; hit effect/máu phải có tùy chọn nội dung mà không làm giảm độ rõ.
- Âm thanh và chỉ báo hướng sát thương phải hỗ trợ việc hiểu nguồn nguy hiểm nhưng không tiết lộ vị trí chính xác của đối thủ.

## Anti-pattern / product integrity

- Không hero/class/ultimate, kỹ năng siêu nhiên, pet chiến đấu hoặc loadout ngoài trận.
- Không hồi sinh, tự cứu, mua lại đồng đội hoặc trạm triệu hồi trong Standard.
- Không cửa hàng trong game, premium currency, microtransaction, loot box, gacha, battle pass, daily login streak, quảng cáo hoặc live-event trong v1.0.
- Không chèn nhịp thương mại vào Standard, HUD trận hoặc bản đồ chuẩn.
- Không quảng cáo thương hiệu, sân khấu sự kiện hoặc mỹ phẩm phát sáng trong bản đồ Standard.
- Không sức mạnh, thông tin, ngụy trang hoặc tiện ích từ tiền hay tiến trình ngoài trận.
- Tiến trình tài khoản chỉ ghi thành tích và biểu đạt thẩm mỹ có tiết chế; Weapon Mastery chỉ mở số liệu chuyên sâu và huy hiệu hồ sơ.
- Phần thưởng thành tích lâu dài, không hết hạn và không yêu cầu đăng nhập hằng ngày.
- Mỹ phẩm không được thay đổi silhouette chiến đấu, âm thanh, hitbox hoặc lợi thế ngụy trang.
- Không dùng bot âm thầm trong Standard.
- Không số sát thương nổi, không chỉ báo bước chân trực quan cạnh tranh và không ping tự nhận dạng địch xuyên vật cản.
- Không red zone hoặc tử vong ngẫu nhiên tức thời thiếu counter-play.
- Thay đổi cân bằng không được gắn với lịch nội dung thương mại; thay đổi lớn phải được thử nghiệm và công bố lý do bằng dữ liệu.

## Measurable UX constraints

- Ít nhất 90% tình huống tử vong phải được người xem độc lập giải thích đúng từ replay nội bộ.
- Ít nhất 80% người thử nghiệm phải giải thích được quyết định chính dẫn tới cái chết trong khảo sát sau trận.
- Ít nhất 85% lần thử tại 20–80 m phải xác định đúng cung 30° của nguồn âm bằng stereo/HRTF.
- Kho đồ không được vượt 70% màn hình và phải giữ vùng trung tâm/xung quanh nhìn thấy được.
- Nhặt nhanh mất 0,20 giây mỗi vật phẩm; quỹ đạo vật ném chỉ hiện trong 1,5 giây đầu khi ngắm.
- Sau 90 giây loot một cụm nhà trung bình: 95% người chơi có ít nhất một súng, 70% có vũ khí chính, 50% có giáp hoặc mũ và 35% có hồi máu. Chỉ số phát hành bổ sung yêu cầu 60–75% có vũ khí chính trong 90 giây và dưới 5% không tìm thấy súng sau khi loot trọn cụm nhà trung bình.
- Bốn bộ trang phục mặc định phải nằm trong biên 5% của nhau trong thử nghiệm phát hiện mục tiêu.
- Thời lượng trận trung vị phải đạt 28–32 phút; p90 không vượt 35 phút.
- Thời gian từ xác nhận ghép trận tới sảnh chờ không vượt 45 giây ở p95 trên SSD tối thiểu/cache lạnh.
- Ghép vùng mục tiêu là ping trung vị không quá 80 ms và packet loss dưới 1%; trên 150 ms phải cảnh báo. Ít nhất 95% người chơi ở khu vực ra mắt phải được ghép vào vùng đạt ping trung vị không quá 80 ms.
- Client tối thiểu phải đạt 60 FPS trung vị ở 1080p/Low, p95 frame time không quá 25 ms; máy đề nghị đạt 90 FPS trung vị ở 1080p/High, p95 không quá 16,7 ms.
- UI phải hoạt động từ 1280×720 tới 3840×2160 và trên tỷ lệ ultrawide phổ biến.
- 100% nội dung ảnh hưởng gameplay chỉ được tiếp cận bằng hành động trong trận, không bằng tiền hoặc tiến trình tài khoản.

## Surfaces implied

Các bề mặt dưới đây chỉ là ánh xạ từ nhu cầu đã có trong GDD; tên bề mặt không xác lập bố cục hay hành vi mới.

| Bề mặt | Nhu cầu nguồn làm nó cần thiết |
|---|---|
| Chọn chế độ / ghép trận | Chọn Solo, Duo hoặc Squad; ưu tiên vùng mạng; MMR mềm cho 10 trận đầu |
| Xác nhận vùng mạng không đạt ngưỡng | Không khởi tạo Standard nếu không có vùng đạt ngưỡng, trừ khi người chơi xác nhận tiếp tục |
| Sảnh chờ trước trận | Giai đoạn chuẩn bị 60 giây; mục tiêu thời gian vào sảnh chờ |
| Trạng thái đường bay và đổ bộ | Quan sát đường bay, chọn điểm rơi, điều khiển tốc độ/khoảng bay và quan sát dù đối thủ |
| HUD sống sót trong trận | HP/tăng lực, đạn, tư thế, hướng, minimap, đội và pha bo |
| Cảnh báo kết nối | Ping vượt 150 ms phải được cảnh báo |
| Tương tác loot nhanh | Tương tác 0,20 giây/món; không tự nhặt các nhóm bị cấm |
| Kho đồ | Sức chứa, slot, kéo thả, gắn phụ kiện và ngưỡng tự nhặt đạn; tối đa 70% màn hình |
| Bản đồ toàn màn hình | Đường bay, bo hiện tại/tiếp theo, marker đội và địa danh |
| Giao tiếp voice và ping đội | Voice, ping vị trí, 8 ping ngữ cảnh; phụ đề ping |
| Trạng thái Gục / cứu đồng đội | Bò, đánh dấu, nói chuyện; cứu 10 giây và điều kiện ngắt |
| Trạng thái sử dụng vật phẩm | Thời gian hồi máu/tăng lực và điều kiện ngắt |
| Trạng thái ngắm và scope | Hip-fire, ngắm qua vai, ADS, giữ hơi và chỉnh zero |
| Trạng thái phương tiện | Nhiên liệu, HP/lốp và cảnh báo cháy 3 giây là dữ liệu/trạng thái gameplay cần được truyền đạt; cách hiển thị chưa được GDD quyết định |
| Spectator đồng đội | Xem đồng đội tới khi đội bị loại |
| Kết quả trận / replay tóm tắt | Thống kê, replay tóm tắt và âm nhạc kết quả/chiến thắng |
| Hồ sơ / lịch sử mùa / Weapon Mastery | Số trận, top 10, thắng, cự ly hạ gục, độ chính xác, lịch sử mùa, số liệu sâu và huy hiệu |
| Training Grounds | Bia tĩnh/di động và bot luyện tập; kết quả không tác động thống kê cạnh tranh |
| Cài đặt input / hình ảnh / khả năng tiếp cận | Remap, toggle/hold, sensitivity, FOV, camera shake, flash, preset mù màu, máu/hit effect và phụ đề |
| Báo cáo / chặn | Friendly-fire cần ghi nguồn và luồng báo cáo; báo cáo/chặn phải có từ bản phát hành |
| Thông báo bot dự kiến | Hàng chờ thử nghiệm phải công bố số bot trước khi vào trận |

## Unresolved UX decisions

Các mục sau chưa được GDD quyết định; đây là khoảng trống cần elicitation, không phải đề xuất giải pháp.

- IA/menu tổng thể, điểm vào và quan hệ điều hướng giữa ghép trận, Training Grounds, hồ sơ, cài đặt, kết quả và báo cáo chưa được mô tả.
- Luồng party trước trận chưa xác định: tạo/rời đội, mời/tham gia, ready state, quyền đội trưởng, thay đổi Solo/Duo/Squad và xử lý thành viên mất kết nối.
- Onboarding được nhắc trong Epic E7 nhưng chưa có mục tiêu, nội dung, thời điểm, luồng hay tiêu chí hoàn thành.
- Danh tính, từ vựng và hành vi cụ thể của 8 ping ngữ cảnh chưa được định nghĩa; cách đặt/xóa marker và quan hệ giữa ping thế giới, minimap và bản đồ toàn màn hình cũng chưa rõ.
- Voice chưa có quyết định về kênh, push-to-talk/open mic, trạng thái mute, chỉ báo người nói, volume theo thành viên hay luồng moderation.
- HUD chưa xác định quy tắc ẩn/hiện/fade, khả năng tùy biến, safe area, xử lý ultrawide và cách ưu tiên khi nhiều cảnh báo cùng xuất hiện.
- Danh sách HUD “chỉ hiển thị” bảy nhóm thông tin chưa được hòa giải rõ với các yêu cầu bắt buộc khác như cảnh báo kết nối, nguồn friendly-fire, thông báo bot và các prompt tương tác.
- Cách truyền đạt các trạng thái không nằm trong danh sách HUD — độ bền giáp/mũ, thời gian dùng vật phẩm, trạng thái giữ hơi, zero scope, nhiên liệu/HP/lốp xe và cháy 3 giây — chưa được quyết định.
- Kho đồ chưa xác định mô hình tương tác chi tiết cho kéo/thả, nhặt nhanh, gắn/tháo/đổi phụ kiện, so sánh vật phẩm, chia/xả stack, báo quá sức chứa và sắp xếp.
- Bản đồ/minimap chưa xác định pan/zoom, thao tác marker, tỷ lệ thông tin, hướng bản đồ, trạng thái khi mở trong phương tiện hay hành vi khi bị tấn công.
- Nội dung chính xác của màn kết quả và “replay tóm tắt” chưa được định nghĩa; replay đầy đủ và kill-cam cạnh tranh đã bị loại khỏi v1.0.
- Spectator đồng đội chưa xác định camera, cách chuyển thành viên, thông tin được phép xem và điều kiện kết thúc chính xác ngoài mốc đội bị loại.
- Luồng báo cáo/chặn và cách trình bày nguồn friendly-fire chưa được đặc tả; quy trình xem xét team-kill được nêu nhưng tương tác người dùng chưa rõ.
- Luồng reconnect, timeout, AFK, mất kết nối, hủy ghép trận và lỗi vào trận chưa được mô tả.
- Voice & tone/microcopy chưa được xác định cho menu, cảnh báo, kết quả, báo cáo, lỗi mạng và thông báo hệ thống.
- Accessibility chưa có mức tối thiểu cho cỡ chữ, độ tương phản, scaling UI, giảm chuyển động ngoài camera shake, cấu hình phụ đề, hỗ trợ thính giác ngoài ping hay kiểm thử motor/cognitive accessibility.
- Chưa có mục tiêu localization/i18n, ngôn ngữ phát hành hoặc quy tắc thích ứng độ dài văn bản/glyph phím.
- Chưa xác định ranh giới diegetic/non-diegetic cho prompt, marker, ping, tương tác loot, bo và trạng thái phương tiện.
- Hồ sơ, lịch sử mùa và Weapon Mastery chưa có IA, cách diễn giải số liệu hoặc ranh giới giữa tự cải thiện và tạo áp lực engagement.
- Chủ đề/tên cuối của Đảo Vọng vẫn là giả định GDD A-001; điều này để ngỏ phần nhận diện hình ảnh/ngôn ngữ địa danh nhưng không thay đổi vòng lặp UX cốt lõi.
- Mô hình mua một lần và chính sách máy chủ dài hạn vẫn là giả định GDD A-002; mọi bề mặt mua hàng hoặc quyền truy cập sản phẩm vì vậy chưa được xác lập, trong khi v1.0 đã khóa không có storefront trong game.
