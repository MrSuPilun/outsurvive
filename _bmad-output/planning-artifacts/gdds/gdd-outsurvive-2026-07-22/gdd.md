---
title: "OutSurvive - Game Design Document"
game_type: "shooter"
secondary_genres:
  - "battle-royale"
  - "survival"
platforms:
  - "PC - Windows"
  - "PC - Linux"
  - "macOS"
  - "Mobile - Android"
  - "Mobile - iOS"
input_families:
  - "Keyboard and Mouse"
  - "Touch"
engine: "Godot"
created: "2026-07-22"
updated: "2026-07-22"
version: "1.1.0"
status: "ready-for-architecture"
---

# OutSurvive - Game Design Document

**Tác giả:** Nhà sáng lập OutSurvive  
**Thể loại chính:** Shooter  
**Cấu trúc trận:** Battle royale sinh tồn  
**Nền tảng:** Windows, Linux, macOS, Android và iOS; Keyboard/Mouse và Touch  
**Engine mục tiêu:** Godot

---

## Tóm tắt điều hành

### Khái niệm cốt lõi

OutSurvive là game bắn súng battle royale nhiều người chơi lấy lối chơi PUBG cổ điển làm nền: 100 người đổ bộ tay trắng xuống một bản đồ lớn, tự chọn nơi tiếp đất, nhặt trang bị tại chỗ, di chuyển theo vùng an toàn thu hẹp và chiến đấu cho đến khi chỉ còn một người hoặc một đội sống sót.

OutSurvive giữ lại cảm giác dễ tổn thương, sự im lặng giữa các cuộc đấu súng và giá trị của từng quyết định. Trò chơi loại bỏ kỹ năng siêu nhiên, hồi sinh tiện lợi, loadout trả trước và các hệ thống thương mại chen vào vòng lặp trận đấu. Mỗi chiến thắng phải đến từ thông tin, vị trí, quản trị rủi ro và kỹ năng sử dụng vũ khí.

### Fantasy cốt lõi

> Bị thả vào một vùng đất thù địch với hai bàn tay trắng, đọc tình hình tốt hơn đối thủ, thích nghi bằng những gì tìm được và sống sót nhờ chính quyết định của mình.

### Định nghĩa “sinh tồn đúng nghĩa”

Trong OutSurvive, **sinh tồn** nghĩa là khan hiếm tài nguyên, thông tin không hoàn hảo, vị trí có giá trị, tử vong loại người chơi khỏi trận và sai lầm không thể xóa bằng tiền hoặc tiện ích hồi sinh. Đây là sinh tồn chiến thuật theo trận kiểu PUBG cổ điển, không phải survival-crafting; đói, khát, xây căn cứ và chế tạo không thuộc vòng lặp cốt lõi.

### Đối tượng người chơi

- Người chơi từ 18 tuổi, thích battle royale chiến thuật và chấp nhận hậu quả cao khi thất bại.
- Cựu người chơi PUBG/Free Fire muốn quay lại nhịp độ sinh tồn ban đầu, trước khi game bị chi phối bởi kỹ năng nhân vật, sự kiện và vật phẩm phô trương.
- Người chơi desktop hoặc mobile thích đấu súng có độ giật, đường đạn và âm thanh định hướng; không tìm kiếm nhịp độ arcade liên tục.
- Phiên chơi mục tiêu 28–35 phút; người chơi phải chấp nhận có trận kết thúc trong vài phút đầu.

### Điểm khác biệt cốt lõi

1. **Sinh tồn là hệ thống, không phải nhãn thể loại:** khan hiếm tài nguyên, thông tin không hoàn hảo, tiếng động và vòng bo buộc người chơi lựa chọn giữa an toàn với cơ hội.
2. **Không có sức mạnh được mua hoặc cày ngoài trận:** mọi người bắt đầu tay trắng; tiến trình tài khoản chỉ ghi nhận thành tích và mở khóa biểu đạt thẩm mỹ có tiết chế.
3. **Bản đồ Đông Nam Á hư cấu, thực dụng và dễ đọc:** địa hình nhiệt đới, ruộng, làng, cảng và cao nguyên tạo bản sắc riêng mà không thay đổi vòng lặp battle royale cổ điển.
4. **Sản phẩm tôn trọng người chơi:** không loot box, không battle pass gây FOMO, không quảng cáo trong trận và không sự kiện thương hiệu làm thay đổi không khí sinh tồn.

---

## Mục tiêu và bối cảnh

### Mục tiêu dự án

- Tạo một trận battle royale mà 80% người thử nghiệm mô tả nguyên nhân thắng/thua bằng quyết định và kỹ năng, không bằng vật phẩm ngoài trận hoặc may rủi không thể ứng phó.
- Duy trì ba nhịp rõ ràng: chuẩn bị căng thẳng, di chuyển có tính toán và giao tranh ngắn nhưng nguy hiểm.
- Cho phép chiến thắng bằng nhiều phong cách hợp lệ: ẩn mình, kiểm soát địa hình, phục kích, di chuyển chủ động hoặc bắn chính xác.
- Đưa một luật chơi duy nhất đến mức ổn định trước khi thêm bản đồ, chế độ hoặc nội dung live-service.
- Xây phạm vi có thể kiểm chứng theo tầng: sandbox đấu súng → vertical slice 24 người → thử tải 100 người → bản phát hành 100 người.

### Bối cảnh và động lực

PUBG và Free Fire chứng minh sức hấp dẫn của fantasy “người sống cuối cùng”. Tuy nhiên, tầm nhìn OutSurvive phản đối việc để skin, hợp tác thương hiệu, sự kiện liên tục hoặc tiện ích hồi sinh làm loãng hậu quả của sinh tồn. Thiết kế dùng PUBG cổ điển làm chuẩn tham chiếu cho cấu trúc trận, không sao chép bản đồ, tên vật phẩm, mỹ thuật hoặc thông số cân bằng của PUBG.

### Nguyên tắc ra quyết định

Khi hai tính năng xung đột, áp dụng thứ tự ưu tiên:

1. Công bằng và tính toàn vẹn của trận đấu.
2. Căng thẳng sinh tồn và hậu quả của quyết định.
3. Độ rõ của thông tin và khả năng phản ứng.
4. Chiều sâu kỹ năng đấu súng và di chuyển.
5. Khả năng vận hành, mở rộng nội dung và thương mại.

### Phạm vi của chuẩn tham chiếu “PUBG cổ điển”

Chuẩn tham chiếu là vòng lặp PC battle royale đời đầu, không phải tái tạo nguyên trạng một patch PUBG cụ thể. Khi Early Access, PUBG 1.0 và Erangel Classic khác nhau, OutSurvive giữ yếu tố củng cố bốn trụ cột và loại yếu tố tạo tử vong thiếu counter-play hoặc làm loãng Standard.

| Yếu tố tham chiếu | Quyết định OutSurvive | Lý do |
|---|---|---|
| Máy bay, nhảy dù, xuất phát tay trắng | Giữ | tạo quyết định điểm rơi và công bằng đầu trận |
| 100 người, bản đồ 8×8 km | Giữ làm north-star | tạo khoảng lặng, route và mật độ giảm dần |
| TPP/FPP | Điều chỉnh | Standard dùng TPP với ADS thứ nhất; FPP-only chỉ mở khi không làm vỡ hàng chờ |
| Loot khan hiếm | Giữ, thêm ngưỡng chống “không có súng” | duy trì thích nghi mà không để cả cụm nhà vô dụng |
| Đạn có vận tốc, độ rơi và giật súng | Giữ, dùng roster/thông số riêng | cốt lõi của kỹ năng shooter |
| DBNO trong đội | Giữ | tạo quyết định cứu–bỏ và phối hợp; không chuyển thành hồi sinh |
| Phương tiện có nhiên liệu/tiếng động | Giữ | đánh đổi tốc độ lấy việc bộc lộ vị trí |
| Vùng bo thu hẹp | Giữ, chỉnh bằng survival curve | điều khiển nhịp và mật độ có thể đo |
| Mưa và sương | Giữ có trọng số | thay đổi thông tin nghe/nhìn nhưng vẫn báo từ đầu trận |
| Red zone gây chết ngẫu nhiên | Loại bỏ | xung đột P2/P4 vì counter-play yếu |
| Cửa hàng skin, premium currency, battle pass, collab/live-event | Loại khỏi v1.0 | không cho lớp thương mại trở thành một vòng lặp cạnh tranh với sinh tồn |

---

## Lối chơi cốt lõi

### Trụ cột thiết kế

#### P1 — Mỗi quyết định đều có giá sinh tồn

Loot, đạn, hồi máu, thời gian, vị trí và tiếng động là tài nguyên hữu hạn. Người chơi không thể thu thập mọi thứ hoặc sửa mọi sai lầm; mỗi lựa chọn phải tạo ra một thứ bị bỏ lại.

#### P2 — Đấu súng sát thương cao nhưng có thể đọc được

Vũ khí có đường đạn, độ giật và vai trò khác nhau. Tử vong nhanh, nhưng âm thanh, lóe nòng, vệt va chạm, hướng nhận sát thương và địa hình phải cho người chơi cơ hội hiểu mối đe dọa.

#### P3 — Thông tin và địa hình mạnh hơn đồ hiếm

Đỉnh đồi, đường rút, tiếng bước chân, đường bay, vòng bo và hành vi đối thủ tạo lợi thế lớn hơn chênh lệch một cấp trang bị. Không vật phẩm nào xóa bỏ nhu cầu đọc trận đấu.

#### P4 — Một sân chơi nghiêm túc và bình đẳng

Không lớp nhân vật, kỹ năng chủ động, chỉ số trả phí hoặc loadout ngoài trận. Mỹ phẩm không thay đổi silhouette chiến đấu, âm thanh, hitbox hoặc khả năng ngụy trang vượt giới hạn cho phép.

### Chuỗi truy vết trụ cột

| Trụ cột | Cơ chế củng cố | Chỉ số kiểm chứng |
|---|---|---|
| P1 | loot ngẫu nhiên có trọng số, túi giới hạn, hồi máu bị ngắt, không hồi sinh | ≥60% người thử nghiệm nêu được ít nhất một đánh đổi tài nguyên quyết định kết quả |
| P2 | đạn vật lý, giật súng, giáp có độ bền, feedback hướng sát thương | ≥90% tình huống tử vong được người xem độc lập giải thích đúng từ replay nội bộ |
| P3 | bản đồ lớn, âm thanh định hướng, vùng an toàn, địa hình và phương tiện | chênh lệch tỉ lệ thắng giữa giáp cấp 2 và 3 dưới 8 điểm phần trăm khi kiểm soát kỹ năng |
| P4 | xuất phát tay trắng, không tăng sức mạnh ngoài trận, không storefront/live-event ở v1.0 | 100% trang bị ảnh hưởng gameplay chỉ xuất hiện hoặc được tìm thấy trong trận |

### Vòng lặp trận đấu

1. **Chuẩn bị (60 giây):** chọn Solo, Duo hoặc Squad; vào sảnh chờ; không chọn vũ khí hay kỹ năng.
2. **Quan sát đường bay (30–45 giây):** đọc hướng máy bay, chọn điểm rơi, cân bằng mật độ đối thủ với chất lượng loot.
3. **Đổ bộ (20–90 giây):** điều khiển tốc độ và khoảng bay; quan sát dù của đối thủ để cập nhật kế hoạch.
4. **Trang bị ban đầu (2–5 phút):** tìm vũ khí, đạn, giáp, túi và hồi máu; quyết định giao tranh sớm hoặc rút lui.
5. **Đọc vùng an toàn:** so đường đi, thời gian, địa hình, phương tiện và tiếng súng; chọn di chuyển sớm an toàn hoặc ở lại loot với rủi ro cao.
6. **Di chuyển và giao tranh:** thu thập thông tin → chiếm vị trí → khai hỏa hoặc né tránh → dùng tài nguyên → đánh giá lại.
7. **Kết thúc (5–10 người cuối):** không gian nhỏ, ít đường rút, thông tin âm thanh quan trọng; quyết định khai hỏa có thể lộ vị trí cho bên thứ ba.
8. **Kết quả:** nhận thống kê và replay tóm tắt; không nhận sức mạnh cho trận sau; động lực lặp lại là cải thiện quyết định và kỹ năng.

### Vòng lặp từng phút

> Quan sát → hình thành giả thuyết về nguy cơ → chọn đường/vị trí → hành động → tạo tiếng động và tiêu hao tài nguyên → đọc phản ứng của thế giới → cập nhật kế hoạch.

### Điều kiện thắng và thua

- **Solo:** người chơi sống cuối cùng thắng.
- **Duo/Squad:** đội có ít nhất một thành viên còn sống khi mọi đội khác bị loại thắng.
- Người chơi bị loại khi HP về 0 ở Solo, khi bị kết liễu trong trạng thái gục, hoặc khi toàn đội không còn thành viên có thể chiến đấu.
- Rời trận sau khi máy bay khởi hành được tính là thất bại; người chơi có thể xem đồng đội cho đến khi đội bị loại.
- Không có hồi sinh, mua lại, tự hồi sinh hoặc trạm triệu hồi trong luật chơi chuẩn.

---

## Cơ chế trò chơi

### Di chuyển và tư thế

| Hành động | Thông số mục tiêu | Đánh đổi |
|---|---:|---|
| Đi bộ | 2,3 m/s | tiếng nhỏ, súng sẵn sàng |
| Chạy thường | 4,5 m/s | tiếng nghe được xa hơn, độ chính xác giảm |
| Chạy nước rút | 6,3 m/s | không bắn; 0,35 giây đưa súng lên sau khi dừng |
| Ngồi | 1,8 m/s | silhouette thấp; độ giật dọc ×0,80 |
| Nằm | 0,8 m/s | silhouette rất thấp; độ giật dọc ×0,60; đổi hướng chậm |
| Nhảy | cao tối đa 0,9 m; hồi 0,45 giây | không ADS trong không trung |
| Leo/vượt | vật cản 0,6–1,4 m; 0,45–0,90 giây | khóa bắn; có âm thanh rõ |
| Nghiêng người | tối đa 18°; vào tư thế 0,15 giây | di chuyển ×0,65 |

- Không có thanh stamina; tốc độ và tiếng động tự tạo đánh đổi.
- Rơi từ trên 3 m bắt đầu gây sát thương; từ 8 m có thể tử vong khi không đầy máu.
- Nước sâu giảm tốc còn 2,0 m/s và khóa vũ khí; lặn tối đa 20 giây trước khi mất HP.

### Sức khỏe, giáp và trạng thái gục

- Mỗi người có 100 HP; HP không tự hồi.
- Sát thương theo vùng: đầu ×2,20; ngực ×1,00; bụng ×0,90; tay/chân ×0,75.
- Áo giáp giảm sát thương thân: cấp 1 giảm 15%, cấp 2 giảm 30%, cấp 3 giảm 45%; độ bền lần lượt 160/220/280.
- Mũ giảm sát thương đầu: cấp 1 giảm 30%, cấp 2 giảm 45%, cấp 3 giảm 55%; độ bền lần lượt 80/150/230.
- Giáp vẫn giảm sát thương của viên đạn làm độ bền về 0; sau đó bị phá hủy.

| Vật phẩm | Thời gian dùng | Hiệu quả | Giới hạn |
|---|---:|---:|---|
| Băng cá nhân | 3,5 giây | +10 HP trong 4 giây | không vượt 75 HP |
| Túi cứu thương | 6,0 giây | đưa HP lên 75 | bị ngắt khi di chuyển/chịu sát thương |
| Bộ cứu thương lớn | 9,0 giây | đưa HP lên 100 | hiếm, chiếm nhiều sức chứa |
| Nước tăng lực | 4,0 giây | +40 hồi phục theo thời gian | tối đa 100 điểm tăng lực |
| Thuốc giảm đau | 6,0 giây | +60 hồi phục theo thời gian | hiếm hơn nước tăng lực |

- Trong Duo/Squad, HP về 0 gây **Gục** với 100 HP chảy máu; mất 2 HP/giây ở lần đầu, nhân đôi tốc độ sau mỗi lần gục tiếp theo.
- Hồi đồng đội mất 10 giây và bị ngắt khi người cứu di chuyển hoặc chịu sát thương.
- Người gục chỉ bò 0,7 m/s, đánh dấu và nói chuyện; không dùng súng, hồi máu hoặc tự cứu.

### Kho đồ và sức chứa

- Cơ thể có 50 đơn vị sức chứa; ba cấp ba lô tăng tổng lên 120/180/250.
- Hai ô vũ khí chính, một ô súng ngắn, một ô cận chiến và một ô vật ném đang chọn.
- Đạn, hồi máu và vật ném dùng sức chứa; phụ kiện gắn trên súng không dùng sức chứa.
- Nhặt vật phẩm mất 0,20 giây mỗi món qua tương tác nhanh; kéo thả trong giao diện không làm chậm thời gian trận.
- Không tự động nhặt vũ khí, giáp hoặc phụ kiện. Có thể bật tự nhặt đạn đúng cỡ tới ngưỡng do người chơi đặt.

### Hệ thống loot

- Mọi người bắt đầu tay trắng; không có loadout.
- Vị trí spawn thuộc nhóm logic theo loại không gian, nhưng vật phẩm cụ thể được chọn ngẫu nhiên có trọng số mỗi trận.
- Mục tiêu sau khi loot 90 giây tại một cụm nhà trung bình: 95% người chơi có ít nhất một súng; 70% có vũ khí chính; 50% có giáp hoặc mũ; 35% có hồi máu.
- Khu dân cư nhỏ ưu tiên đồ cơ bản; cơ sở quân sự/cảng/công nghiệp có loot tốt hơn nhưng nhiều đường tiếp cận và tỷ lệ tranh chấp cao hơn.
- Thùng tiếp tế xuất hiện một lần trong các pha bo 1–5, rơi ở vị trí có thể tiếp cận, phát khói nhìn thấy ở 800 m và chứa một vũ khí đặc biệt cùng giáp/hồi máu cấp cao.
- Không vật phẩm thiết yếu nào chỉ có trong thùng tiếp tế.

### Vật ném và công cụ

| Vật phẩm | Thời gian kích hoạt | Bán kính/hiệu quả | Vai trò |
|---|---:|---:|---|
| Lựu đạn mảnh | ngòi 5 giây | chí mạng 3 m; sát thương tới 8 m | đẩy đối thủ khỏi cover |
| Lựu đạn khói | phát sau 1,5 giây; tồn tại 25 giây | màn khói đường kính 12 m | cắt tầm nhìn, cứu đồng đội, di chuyển |
| Lựu choáng | ngòi 2,5 giây | tối đa 5 giây trong 5 m có đường nhìn | đột kích phòng |
| Chai cháy | vỡ khi va chạm; cháy 12 giây | vùng 4 m; 10 sát thương/giây | khóa đường và cầu thang |

- Người chơi mang tối đa 6 vật ném nhờ sức chứa; không có túi riêng vô hạn.
- Quỹ đạo dự kiến chỉ hiện trong 1,5 giây đầu khi ngắm để không biến ném xa thành hành động không cần kỹ năng.

### Phương tiện

- Sáu archetype: sedan 4 chỗ, jeep 4 chỗ, bán tải 4 chỗ, xe máy 2 chỗ, thuyền 4 chỗ, xe tải 6 chỗ.
- Tốc độ tối đa 80–125 km/h; tiếng động nghe được 250–450 m tùy xe.
- Phương tiện cần nhiên liệu, có lốp bị phá và phát nổ sau khi HP về 0 với cảnh báo cháy 3 giây.
- Va chạm trên 35 km/h gây sát thương; trên 70 km/h có thể hạ gục người không có vật cản che.
- Xe là công cụ di chuyển nhanh nhưng bộc lộ vị trí; không có xe bọc thép mua ngoài trận.

### Điều khiển và đầu vào

- Gameplay chỉ tiêu thụ lệnh ngữ nghĩa dùng chung; Keyboard/Mouse, Touch và Gyro tùy chọn là các adapter đầu vào, không tạo luật gameplay riêng theo nền tảng.
- Keyboard/Mouse: WASD di chuyển; chuột điều khiển camera/ngắm; Shift chạy nhanh; Ctrl đi bộ; C ngồi; Z nằm; Space nhảy/vượt; Q/E nghiêng; F tương tác; R nạp đạn; G chọn vật ném; Tab kho đồ.
- Touch landscape: cần di chuyển bên trái, vùng nhìn bên phải, nút bắn phải và nút bắn trái tùy chọn, cùng các nút ngữ cảnh cho tư thế, tương tác, nạp đạn, ADS, vật ném và phương tiện. Bố cục, kích thước và độ trong suốt được lưu theo lớp thiết bị.
- Gyro là tùy chọn ngắm bổ trợ. Touch không có target snap, auto-fire, enemy detection hay chỉ báo bước chân trực quan; aim slowdown/friction chỉ được cân nhắc sau prototype công bằng trong Touch pool và không bật mặc định.
- TPP là góc nhìn chuẩn; người chơi có thể chuyển vai camera. ADS chuyển sang góc nhìn qua thước ngắm/ống ngắm thứ nhất.
- Camera bị đẩy vào phía trước khi sát tường; vật thể/đối thủ không được hiển thị nếu đường nhìn từ đầu nhân vật bị che hoàn toàn, hạn chế lợi thế “nhìn xuyên góc” của TPP.
- Cho phép gán lại toàn bộ phím hoặc bố cục Touch; chỉnh riêng độ nhạy theo hip-fire/ADS/từng độ phóng và giữ/nhấn cho ADS, nghiêng, ngồi, chạy.

---

## Thiết kế chuyên biệt: Shooter

### Hệ thống vũ khí

#### Danh mục v1.0

- 3 súng ngắn, 3 SMG, 3 shotgun, 5 assault rifle, 3 DMR, 3 sniper rifle, 2 LMG và 3 vũ khí cận chiến: tổng 25 vũ khí.
- 5 cỡ đạn: 9 mm, .45, 5,56 mm, 7,62 mm và 12 gauge. Mỗi cỡ có màu, hình hộp và biểu tượng riêng.
- Phụ kiện: 4 đầu nòng, 4 tay cầm, 3 băng đạn, 2 báng và 7 loại ngắm (red dot, holo, 2×, 3×, 4×, 6×, 8×).
- Vũ khí không lên cấp, không mang qua trận và không có skin trong v1.0.

#### Bảng cảm giác vũ khí mục tiêu

Sát thương là hit ngực trước giáp trong vùng chưa falloff. Falloff nội suy tuyến tính từ mốc đầu đến mốc cuối; sau mốc cuối, sát thương giữ ở 55% giá trị gốc.

| Archetype | Sát thương | RPM | Băng | Vận tốc | Nạp chiến thuật | Falloff đầu→cuối | Cự ly chủ đạo |
|---|---:|---:|---:|---:|---:|---:|---:|
| Súng ngắn | 35 | 450 | 15 | 350 m/s | 1,8 giây | 40→150 m | 0–40 m |
| SMG | 31 | 800 | 30 | 400 m/s | 2,3 giây | 50→200 m | 0–80 m |
| Shotgun | 9 × 18 viên | 75 | 5 | 350 m/s | 0,65 giây/viên | 25→80 m | 0–35 m |
| AR 5,56 | 41 | 700 | 30 | 820 m/s | 2,6 giây | 100→500 m | 30–250 m |
| AR 7,62 | 47 | 600 | 30 | 715 m/s | 2,9 giây | 80→450 m | 20–200 m |
| DMR | 55 | 300 tối đa | 10 | 780 m/s | 2,7 giây | 180→800 m | 100–500 m |
| Sniper bolt-action | 85 | 45 | 5 | 850 m/s | 3,5 giây | 300→1.000 m | 200–800 m |
| LMG | 43 | 650 | 60 | 750 m/s | 5,5 giây | 120→600 m | 50–300 m |

Giá trị spread là góc nón toàn phần khi đứng yên; recoil là độ lệch camera trung bình mỗi viên trước phụ kiện. Shotgun dùng spread để mô tả nón pellet, không dùng spread ADS chuẩn.

| Archetype | ADS | Hip spread | ADS spread | Recoil dọc/viên | Recoil ngang/viên |
|---|---:|---:|---:|---:|---:|
| Súng ngắn | 0,18 giây | 2,4° | 0,10° | 1,0° | ±0,40° |
| SMG | 0,22 giây | 2,0° | 0,09° | 0,7° | ±0,35° |
| Shotgun | 0,24 giây | 5,0° | 3,5° pellet cone | 4,0° | ±1,50° |
| AR 5,56 | 0,28 giây | 2,6° | 0,06° | 0,9° | ±0,45° |
| AR 7,62 | 0,30 giây | 2,8° | 0,07° | 1,2° | ±0,60° |
| DMR | 0,33 giây | 3,0° | 0,04° | 2,0° | ±0,80° |
| Sniper bolt-action | 0,42 giây | 3,2° | 0,02° | 5,5° | ±1,00° |
| LMG | 0,32 giây | 3,2° | 0,10° | 1,0° | ±0,55° |

TTK được đo từ hit đầu tiên đến hit chí mạng cuối cùng, bắn trúng ngực liên tục ở 20 m, không headshot, không falloff và không tính thời gian ADS.

| Vũ khí chuẩn | Hit không giáp | TTK không giáp | Hit qua giáp cấp 2 | TTK qua giáp cấp 2 |
|---|---:|---:|---:|---:|
| AR 5,56 (41 damage, 700 RPM) | 3 | 0,171 giây | 4 | 0,257 giây |
| AR 7,62 (47 damage, 600 RPM) | 3 | 0,200 giây | 4 | 0,300 giây |

- Dải TTK AR mục tiêu ở 20 m là 0,17–0,25 giây không giáp và 0,25–0,40 giây qua giáp cấp 2; vũ khí cụ thể phải nằm trong dải sau khi thay đổi damage/RPM.
- Viên đạn có thời gian bay và độ rơi; không có vũ khí chính hitscan.
- Loạt bắn đầu dễ kiểm soát hơn bắn kéo dài: độ giật tăng trong 8 viên đầu, ổn định sau viên 12; ngừng bắn 0,25 giây bắt đầu hồi giật.
- Đứng yên là độ tản chuẩn; ngồi ×0,75; nằm ×0,55; đi bộ ×1,30; chạy ×2,20; nhảy ×4,00.

#### Feedback chiến đấu

- Mỗi phát bắn phải phân biệt được bằng tiếng nổ, tiếng cơ khí, lóe nòng, vỏ đạn và phản lực camera.
- Không dùng số sát thương nổi trong trận chuẩn.
- Trúng mục tiêu cho phản hồi máu/bụi theo cài đặt nội dung, âm thanh nhẹ và phản ứng cơ thể; không xác nhận hạ gục cho tới khi trạng thái được máy chủ xác nhận.
- Người bị bắn nhận chỉ báo hướng theo cung 30°, không hiển thị vị trí hoặc khoảng cách kẻ bắn.

### Ngắm bắn và chiến đấu

- TPP hip-fire, ngắm qua vai và ADS qua sight là ba trạng thái; chuyển trạng thái theo thời gian ADS trong bảng vũ khí.
- Giữ hơi khi dùng scope 4× trở lên tối đa 8 giây; hết hơi tăng dao động ×2 trong 4 giây.
- Scope zero mặc định 100 m; người chơi chỉnh 100–800 m theo bước 100 m với scope phù hợp.
- Aim punch phụ thuộc năng lượng viên đạn và giáp; tối đa 1,5° mỗi hit, có ngưỡng 0,12 giây để tránh khóa ngắm liên tục.
- Không aim assist cho chuột; không magnetism và không đạn bẻ hướng.
- Cận chiến là phương án cuối: tầm 1,8 m, wind-up 0,35–0,55 giây, 35–60 sát thương.

### Mô hình hit registration và mạng cạnh tranh

- Kết quả vị trí, phát bắn, sát thương, loot và thắng/thua do máy chủ trận đấu xác nhận.
- Nhịp mô phỏng mục tiêu 30 Hz cho trận 100 người; các sự kiện bắn và sát thương không được xử lý chậm hơn một tick ở tải chuẩn.
- Bù trễ cho phát bắn có giới hạn tối đa 150 ms. Người chơi vượt 150 ms nhận cảnh báo kết nối; trạng thái quá khứ không được ưu tiên vô hạn trước trạng thái hiện tại.
- Mục tiêu ghép vùng là ping trung vị ≤80 ms và packet loss <1%; không khởi tạo trận chuẩn nếu người chơi không có vùng đáp ứng ngưỡng, trừ khi họ xác nhận tiếp tục.
- Sai lệch vị trí nhìn thấy so với vị trí xác nhận không vượt 0,5 m ở p95 trong điều kiện 80 ms/1% loss.
- Hit trade được chấp nhận nếu hai phát bắn hợp lệ đã rời nòng trước khi một bên bị loại; replay phải thể hiện thứ tự xác nhận.

### Đối thủ và AI

- Đối thủ trong trận chuẩn là người thật; không có quái, boss hoặc NPC chiến đấu.
- Bot không được âm thầm dùng để lấp đầy trận chuẩn. Nếu một hàng chờ thử nghiệm dùng bot, UI phải ghi rõ số bot dự kiến trước khi người chơi vào trận.
- Training Grounds có bia tĩnh, bia di động 2–8 m/s và bot luyện tập với ba hành vi: lao qua khoảng trống, đổi cover, peak/bắn trả. Kết quả training không ảnh hưởng thống kê cạnh tranh.

### Thiết kế bản đồ và không gian giao tranh

#### Bản đồ đầu tiên: Đảo Vọng

[ASSUMPTION: Đảo Vọng và bối cảnh Đông Nam Á là đề xuất tạo bản sắc; chủ đề có thể đổi mà không thay đổi vòng lặp cốt lõi.]

- Bản đồ 8 × 8 km; khoảng 58% đất liền, 12% đảo nhỏ và 30% mặt nước/biên không đi bộ.
- Bối cảnh: quần đảo Đông Nam Á hư cấu sau xung đột, với ruộng trũng, làng bê tông, rừng cao su, cao nguyên, cảng hàng hóa, sân bay bỏ hoang và đập thủy điện.
- 18 POI đặt tên, 55 cụm nhà nhỏ, tối thiểu 420 công trình có thể vào, 180 vị trí phương tiện có trọng số và 12 bến thuyền.
- Cự ly giao tranh mục tiêu: 0–25 m trong nhà; 40–150 m tại làng/rừng; 150–400 m ở ruộng, sườn đồi và đường; 400–800 m chỉ tại một số sightline có đánh đổi rõ.
- Mỗi vùng trống dài trên 120 m phải có ít nhất hai lựa chọn: cover cứng, địa hình lõm, khói, xe hoặc tuyến vòng; không bảo đảm tất cả lựa chọn đều an toàn.
- Cầu và đèo là choke point có tuyến vòng chậm hơn; không tồn tại choke bắt buộc duy nhất từ một vùng đất lớn vào bo.
- Vòng cuối không đặt quá 50% diện tích trên nước, vách không thể đứng hoặc mái không thể tiếp cận.
- Cover v1.0 là tĩnh; không phá nhà, đào đất hoặc xây công sự.

#### Thời tiết

- Trời quang 70%, mưa 15%, sương 15%; được chọn khi bắt đầu trận và không đổi đột ngột giữa trận.
- Mưa giảm khoảng nghe bước chân 15% và tăng tiếng môi trường; sương giới hạn độ tương phản mục tiêu sau 180–250 m.
- Không có đêm tối hoàn toàn; bốn bộ trang phục mặc định phải nằm trong biên 5% của nhau trong thử nghiệm phát hiện mục tiêu.

### Nhiều người chơi

- 100 người mỗi trận; Solo 100 người, Duo tối đa 50 đội, Squad 25 đội bốn người.
- Ghép trận ưu tiên vùng mạng và thời gian chờ; MMR mềm chỉ ngăn người mới gặp nhóm kỹ năng cao nhất trong 10 trận đầu.
- Keyboard/Mouse pool phục vụ Windows, Linux và macOS; Touch pool phục vụ Android và iOS. Tổ đội trộn input family vào Mixed/Keyboard-Mouse pool sau khi UI công bố rõ trước khi ready.
- Input family được khóa khi vào trận. Keyboard/Mouse ngoài trên mobile yêu cầu rời hàng chờ và requeue; không đổi input family giữa trận. Không âm thầm lấp trận bằng bot, đổi pool hoặc nới quy tắc công bằng.
- Tài khoản, progression, party và backend dùng chung. Mọi nền tảng dùng cùng dữ liệu cân bằng, protocol và quyền quyết định của máy chủ; client mobile không nhận thêm thông tin chiến đấu.
- Standard là luật chơi chính. Ranked, custom server và giải đấu được hoãn cho đến khi Standard ổn định.
- Giao tiếp đội bằng voice, ping vị trí và 8 ping ngữ cảnh; ping không tự nhận dạng kẻ địch xuyên vật cản.
- Friendly fire bật ở 100% sát thương sau khi lên máy bay; UI ghi rõ nguồn sát thương và có luồng báo cáo.
- Không đổi góc nhìn hoặc luật loot trong cùng hàng chờ. FPP-only là ứng viên sau v1.0 nếu dân số máy chủ đủ để không chia nhỏ cộng đồng.

---

## Cấu trúc vùng an toàn và nhịp trận

Vùng nguy hiểm thu hẹp để ép di chuyển, tăng mật độ và kết thúc trận; nó không được tạo tử vong ngẫu nhiên tức thời. Tâm bo có trọng số theo đất có thể chơi nhưng vẫn giữ bất định.

| Pha | Chờ | Thu | Bán kính cuối pha | Sát thương ngoài bo | Người sống mục tiêu |
|---:|---:|---:|---:|---:|---:|
| 1 | 4:00 | 4:00 | 2.500 m | 0,4 HP/s | 70–85 |
| 2 | 2:30 | 3:30 | 1.600 m | 0,7 HP/s | 50–65 |
| 3 | 2:00 | 3:00 | 1.000 m | 1,2 HP/s | 35–50 |
| 4 | 1:30 | 2:30 | 600 m | 2,0 HP/s | 22–35 |
| 5 | 1:15 | 2:00 | 360 m | 3,5 HP/s | 14–24 |
| 6 | 1:00 | 1:30 | 180 m | 6 HP/s | 8–16 |
| 7 | 0:45 | 1:00 | 90 m | 9 HP/s | 4–10 |
| 8 | 0:30 | 0:45 | 45 m | 14 HP/s | 2–6 |
| 9 | 0:15 | 0:30 | 0 m | 20 HP/s | 1 đội |

- Tổng thời gian tối đa khoảng 32 phút 30 giây sau khi bo đầu bắt đầu; trận có thể kết thúc sớm.
- Pha 1–3 cho phép chữa và di chuyển ngoài bo có chủ đích; từ pha 6, ở ngoài bo không còn là chiến thuật bền vững.
- Tâm pha tiếp theo được lộ khi pha chờ bắt đầu; không có vật phẩm dự báo bo.
- Không có vùng ném bom ngẫu nhiên gây chết tức thời; nó xung đột với P2 và P4.

---

## Tiến trình và cân bằng

### Tiến trình trong trận

Tiến trình đến từ chất lượng bộ trang bị, vị trí và thông tin. Đường cong mong muốn:

1. **0–3 phút:** từ tay trắng đến bộ trang bị có thể tự vệ.
2. **3–10 phút:** hoàn thiện hai vai trò vũ khí, túi/giáp cơ bản và đường di chuyển.
3. **10–22 phút:** thay phụ kiện, tích lũy hồi máu/vật ném, tranh vị trí hoặc thùng tiếp tế.
4. **22 phút trở đi:** loot giảm giá trị; vị trí, khói, thông tin và kỷ luật khai hỏa chi phối.

### Tiến trình ngoài trận

- Không chỉ số, perk, vũ khí, phụ kiện hoặc sức chứa được tăng ngoài trận.
- Hồ sơ ghi số trận, top 10, chiến thắng, cự ly hạ gục, độ chính xác và lịch sử mùa; dữ liệu dùng để tự cải thiện, không tăng sức mạnh.
- Weapon Mastery chỉ mở số liệu chuyên sâu và huy hiệu hồ sơ; không mở skin hoặc sức mạnh.
- Phần thưởng thành tích lâu dài, không hết hạn và không yêu cầu đăng nhập hằng ngày.

### Kinh tế và mô hình thương mại

- v1.0 không có cửa hàng trong game, premium currency, microtransaction, loot box, gacha, battle pass, daily login streak, quảng cáo hoặc live-event.
- Toàn bộ bản đồ, vũ khí và luật chơi ảnh hưởng gameplay thuộc cùng một quyền truy cập sản phẩm.
- [ASSUMPTION: Nếu phát hành thương mại, mô hình ưu tiên là mua game một lần; giá và chi phí máy chủ cần business validation riêng.]
- Mọi đề xuất thương mại hậu v1.0 phải qua cổng chống lệch tầm nhìn ở phần Chỉ số thành công trước khi được đưa vào GDD.

### Nguyên tắc cân bằng

- Không một vũ khí loot thường nào vượt 22% tổng số hạ gục trong mẫu ít nhất 10.000 mạng.
- Vũ khí thùng tiếp tế không vượt 8% tổng số hạ gục và phải mang rủi ro tiếp cận đo được.
- Tỷ lệ thắng theo điểm rơi không vượt ±20% quanh trung bình sau khi kiểm soát kỹ năng và quy mô đội.
- Mỗi archetype phải có ít nhất một cự ly hoặc tình huống mà nó là lựa chọn hợp lý và một tình huống bất lợi rõ.
- Điều chỉnh cân bằng không gắn với lịch nội dung thương mại; thay đổi lớn được thử nghiệm và công bố lý do bằng dữ liệu.

---

## Khung thiết kế bản đồ

### Loại không gian

| Loại | Mật độ loot | Cự ly | Rủi ro chính | Kỹ năng được thưởng |
|---|---|---|---|---|
| Thành phố/cảng | cao | 5–120 m | nhiều góc, bên thứ ba | clearing, âm thanh, phối hợp |
| Làng nhỏ | trung bình | 20–180 m | cover rời rạc | chọn góc và rút lui |
| Ruộng/đầm | thấp | 100–500 m | ít cover cứng | route, khói, phương tiện |
| Rừng/đồn điền | thấp–trung bình | 30–220 m | tầm nhìn đứt đoạn | nghe, flank, trigger discipline |
| Cao nguyên/đồi | thấp | 150–800 m | silhouette lộ, ít loot | quan sát và kiểm soát độ cao |
| Cầu/đèo | trung bình | 20–400 m | choke và phục kích | trinh sát, thời điểm di chuyển |

### Quy tắc bố cục

- POI loot cao cách nhau 800–1.500 m và nối bằng ít nhất hai tuyến mặt đất.
- Từ mọi POI lớn có ít nhất một đường rút không cần xe, dù chậm hơn đường chính tối đa 70%.
- Các mái có lợi thế chiến đấu phải có tối thiểu hai cách tiếp cận hoặc một điểm mù buộc người giữ mái di chuyển.
- 80% cửa sổ chiến đấu dùng chiều cao và silhouette thống nhất; vật liệu xuyên đạn/không xuyên đạn phải có ngôn ngữ hình ảnh nhất quán.
- Biển báo, màu vật liệu và địa danh giúp định hướng mà không phụ thuộc hoàn toàn vào minimap.

### Nhịp không gian

- 0–5 phút: xung đột tại điểm rơi do loot và số cửa vào.
- 5–15 phút: các tuyến rời POI tạo phục kích và giao tranh phương tiện.
- 15–24 phút: mép bo, đỉnh đồi và compound nhỏ thành điểm kiểm soát.
- 24 phút trở đi: cover cấp vi mô, khói, âm thanh và kỷ luật đội hình quyết định.

---

## Định hướng hình ảnh và âm thanh

### Mỹ thuật

- Phong cách hiện thực có tiết chế, ưu tiên silhouette và vật liệu dễ đọc hơn độ chi tiết quang học.
- Bảng màu: xanh xám nhiệt đới, đất đỏ/nâu, bê tông bạc màu và kim loại gỉ; màu bão hòa cao chỉ dành cho thông tin gameplay quan trọng.
- Nhân vật là người sống sót bình thường, không hero silhouette, hiệu ứng hào quang, cánh, thú cưng chiến đấu hoặc trang phục phát sáng.
- Vũ khí giữ tỷ lệ thực dụng nhưng dùng tên, hình dáng và âm thanh hư cấu để tạo sở hữu trí tuệ riêng.
- Máu có tùy chọn giảm/đổi màu; hit feedback vẫn giữ độ rõ tương đương.

### Giao diện

- HUD chỉ hiển thị HP/tăng lực, đạn, tư thế, hướng, minimap, trạng thái đội và pha bo.
- Không banner cửa hàng, nhiệm vụ, quảng cáo hoặc tiến trình battle pass trong HUD trận.
- Kho đồ desktop chiếm tối đa 70% màn hình. Kho đồ mobile là một panel tabbed tối đa 62% chiều ngang và giữ ít nhất 38% dải nhìn thế giới để duy trì rủi ro khi loot.
- Bản đồ toàn màn hình hiển thị đường bay, bo hiện tại/tiếp theo, marker đội và địa danh; không hiển thị loot hoặc đối thủ.
- Giao diện mobile tôn trọng safe area; touch target tối thiểu 48 logical units, riêng bắn/thoát xe/đóng tối thiểu 64 khi safe area cho phép.

### Âm thanh

- Không nhạc nền trong thời gian người chơi còn sống; âm nhạc chỉ ở menu, kết quả và khoảnh khắc chiến thắng.
- Bước chân chạy nghe được tới 70 m ngoài trời, đi thường 45 m, đi bộ 20 m; vật liệu đất, cỏ, gỗ, bê tông, kim loại và nước có phổ âm riêng.
- Súng không giảm thanh nghe tới 1.000 m và có âm xa khác âm gần; súng giảm thanh nghe tới 400–600 m tùy cỡ đạn.
- Xe nghe được 250–450 m; máy bay/thùng tiếp tế không được che hoàn toàn tiếng súng trong bán kính chiến đấu gần.
- Âm thanh stereo/HRTF phải cho người thử nghiệm xác định đúng cung 30° của nguồn âm ở ≥85% lần thử tại 20–80 m.

### Khả năng tiếp cận

- Gán lại toàn bộ phím hoặc bố cục Touch; tùy chọn toggle/hold; chỉnh FOV, độ nhạy, Gyro, haptic, rung camera và cường độ flash.
- Ba preset mù màu cho bo, marker, hit effect và reticle; không chỉ dùng màu để thể hiện cấp vật phẩm.
- Phụ đề cho thông báo hệ thống và đồng đội ping; không có chỉ báo bước chân trực quan trong hàng chờ cạnh tranh vì sẽ thay đổi cân bằng thông tin.
- Permission voice chỉ được hỏi theo ngữ cảnh; mất focus, cuộc gọi và audio-route change không được làm kẹt input hoặc phát voice ngoài ý muốn.

---

## Đặc tả kỹ thuật cấp GDD

### Mục tiêu nền tảng

- Godot 4.x; Windows 10/11 x64, Linux x64, macOS 13+ Intel x64/Apple Silicon, Android 10+ ARM64 và iOS 16+ ARM64 ở v1.0.
- Input family v1.0 là Keyboard/Mouse và Touch; controller và console ngoài phạm vi.
- Desktop chuẩn 1920×1080, hỗ trợ 1280×720 đến 3840×2160 và tỷ lệ ultrawide phổ biến. Mobile chạy landscape, gồm điện thoại và tablet với safe area/notch.
- Máy tối thiểu mục tiêu: CPU 4 nhân đời 2017, 8 GB RAM, GPU tương đương GTX 1060/RX 580, SSD.
- Máy đề nghị: CPU 6 nhân đời 2020, 16 GB RAM, GPU tương đương RTX 2060/RX 6600.
- Mobile tối thiểu: Snapdragon 778G/Dimensity 920 class với 6 GB RAM hoặc iPhone 11/A13. Mobile đề nghị: Snapdragon 8 Gen 1/Dimensity 8100 class với 8 GB RAM hoặc iPhone 13/A15.

### Hợp đồng đa nền tảng

- Một core gameplay, dữ liệu vũ khí/loot/bo, authoritative simulation và network protocol phục vụ cả năm nền tảng.
- Khác biệt nền tảng chỉ nằm sau input adapter, presentation/quality profile, lifecycle, secure storage, platform identity/invite/permission và release pipeline.
- Client lifecycle mobile là `Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended`; resume không bảo đảm giữ slot vô hạn hoặc tạo miễn nhiễm.
- Windows/Linux/macOS dùng profile renderer desktop; Android/iOS dùng profile mobile. Collision và gameplay visibility không được thay đổi theo quality profile.

### Mục tiêu hiệu năng

| Chỉ số | Mục tiêu | Cách đo |
|---|---|---|
| FPS máy tối thiểu | 60 FPS trung vị, p95 frame time ≤25 ms ở 1080p/Low | replay 30 phút gồm thành phố, xe, khói và bo cuối |
| FPS máy đề nghị | 90 FPS trung vị, p95 ≤16,7 ms ở 1080p/High | cùng replay chuẩn |
| Bộ nhớ client | ≤6 GB RAM sau 45 phút | trận đầy đủ, đổi 3 vùng bản đồ |
| Thời gian vào trận | ≤45 giây p95 từ xác nhận ghép trận đến sảnh chờ | SSD tối thiểu, cache lạnh |
| Mobile tối thiểu | 45 FPS trung vị, p95 frame time ≤33,3 ms ở Low | thiết bị tối thiểu, replay chuẩn và thermal soak |
| Mobile đề nghị | 60 FPS trung vị, p95 frame time ≤25 ms ở Medium | thiết bị đề nghị, replay chuẩn và thermal soak |
| Bộ nhớ mobile | working memory ≤3 GB; không bị OS termination trong trận 45 phút | device lab, foreground/background và trận đầy đủ |
| Nhiệt mobile | FPS trung vị giảm không quá 15% sau 30 phút | thermal soak trên thiết bị đại diện |
| Tải mobile | ≤60 giây p95 từ xác nhận ghép trận đến sảnh chờ | cache lạnh trên thiết bị tối thiểu |
| Crash-free sessions | ≥99,5% | cửa sổ 30 ngày |
| Mô phỏng máy chủ | 30 Hz ổn định với 100 người + 10% headroom tải | soak test 45 phút, tình huống bo cuối |
| Độ trễ sự kiện sát thương | ≤1 tick xử lý ở p95 | 100 người, 80 ms RTT, 1% packet loss |
| Băng thông client | trung bình ≤1,5 Mbps mỗi chiều | trận 100 người 30 phút |

### Ngân sách nội dung

- Bản cài desktop v1.0 ≤25 GB; bản cài mobile ≤12 GB; patch cân bằng không yêu cầu tải lại quá 2 GB nội dung không đổi.
- 420 công trình có thể vào từ 8 bộ module kiến trúc và 18 POI là content target tạm thời cho đến khi cả mobile viability lẫn server scale gate đạt.
- 25 vũ khí, 6 phương tiện, 4 bộ trang phục mặc định và một bản đồ là content target tạm thời; core loop/platform parity được ưu tiên nếu MVP review yêu cầu change proposal riêng để cắt breadth.
- Tối đa 6 khói dày đồng thời trong bán kính 100 m quanh một người chơi mà vẫn đạt ngưỡng FPS máy tối thiểu.

### Tính toàn vẹn cạnh tranh

- Máy chủ xác nhận mọi trạng thái ảnh hưởng gameplay; client không được tự quyết định sát thương, loot hoặc kết quả.
- Hỗ trợ báo cáo, chặn, log trận và replay phục vụ điều tra từ bản phát hành.
- Hình phạt rời trận không áp dụng sau khi đội bị loại; hành vi team-kill lặp lại và gian lận có quy trình xem xét riêng.

---

## Phạm vi sản xuất

### Các mốc kiểm chứng

[ASSUMPTION: Quy mô nhóm và ngân sách chưa xác định; các mốc dưới đây là cổng học hỏi, không phải lịch phát hành hoặc cam kết sản xuất.]

| Mốc | Quy mô | Mục tiêu học hỏi | Không phải cam kết phát hành |
|---|---|---|---|
| Combat Sandbox | 1–8 người, map 0,5 km² | desktop/mobile command path, cảm giác di chuyển, súng, hitreg, latency | mỹ thuật hoàn chỉnh, progression |
| Vertical Slice | 24 client hỗn hợp, map 2 × 2 km | drop–loot–bo–win, Touch HUD và lifecycle trong 12–15 phút | quy mô 100 người, toàn bộ content |
| Alpha tải | 100 client protocol mix, map 8 × 8 km | tải máy chủ, streaming, mobile device lab và population theo input pool | cân bằng cuối, mô hình phát hành |
| Beta kín | 100 người thật, một vùng | survival curve, fairness, retention tự nguyện | nhiều bản đồ/chế độ |
| v1.0 | 100 người, Đảo Vọng, năm nền tảng | Standard hoàn chỉnh và release candidate family đạt cổng | ranked, console, live-service lớn |

### Envelope nguồn lực và cổng tăng quy mô

[ASSUMPTION: Envelope PC-first cũ 1–3/5–8/12–20 người đã bị thay thế khi phạm vi v1.0 mở rộng lên năm nền tảng. Architecture và production planning phải ước lượng lại staffing, thiết bị, signing, QA và lịch trước khi phê duyệt R2.]

| Cổng | Envelope tối thiểu để phê duyệt bước tiếp | Điều kiện dừng |
|---|---|---|
| R1 — Combat Sandbox | môi trường 8 client; build smoke Windows/Linux/macOS/Android/iOS; command/network path desktop + mobile | gunplay/hitreg hoặc mobile input/performance tối thiểu không đạt |
| R2 — Vertical Slice | staffing đa nền tảng đã re-estimate; 24 mixed clients; Touch HUD và lifecycle | loop 24 người, mobile memory/thermal hoặc information parity không đạt |
| R3 — Alpha 100 | 100-client protocol mix; máy chủ benchmark ≤8 vCPU/16 GB; device lab và population test từng pool | 30 Hz, băng thông, streaming hoặc population viability không đạt |
| R4 — v1.0 | QA/security/backend, signing/certification và vận hành vùng; beta 100 người thật | thiếu release candidate family trên bất kỳ nền tảng nào hoặc chưa đạt technical/gameplay gate |

Mọi số nhân sự là giả thuyết lập kế hoạch, không phải lịch tuyển dụng. `gds-game-architecture` phải định lượng lại tài nguyên máy chủ; production planning phải khóa ngân sách trước R2 và R3.

### Tóm tắt Epic phát triển

| Epic | Giá trị chơi được | Trụ cột | Phụ thuộc |
|---|---|---|---|
| E1. Nền tảng người sống sót đa nền tảng | semantic input, di chuyển, camera, tư thế và tương tác có cảm giác đúng | P1, P2 | — |
| E2. Đấu súng đáng tin cậy | bắn, đạn, giật, sát thương, giáp và feedback | P2, P4 | E1 |
| E3. Loot và quản trị sinh tồn | nhặt, kho đồ, hồi máu, vật ném và scarcity | P1, P3 | E1–E2 |
| E4. Vòng đời battle royale | sảnh, máy bay, đổ bộ, bo, gục, thắng/thua | P1, P3, P4 | E1–E3 |
| E5. Đảo Vọng và phương tiện | greybox 8×8 km, route, cover và phương tiện cho vertical slice | P1, P3 | E1, E3–E4 |
| E6. Multiplayer cạnh tranh đa nền tảng | 100 người, platform identity, input pool, ghép vùng và tổ đội | P2, P4 | E1–E5 |
| E7. Độ rõ và khả năng tiếp cận đa thiết bị | art/readability, adaptive HUD, audio, Touch editor và onboarding | P2, P3, P4 | E1–E6 |
| E8. Hồ sơ và tính toàn vẹn sản phẩm | thống kê, mastery không sức mạnh và rào chắn chống FOMO/storefront | P4 | E4, E6–E7 |
| E9. Ổn định và chứng nhận đa nền tảng | hiệu năng, tải 100 người, anti-cheat, device lab, signing, QA và vận hành | P2, P4 | E1–E8 |

Chi tiết epic và high-level story nằm trong [epics.md](./epics.md).

---

## Chỉ số thành công

### Chỉ số kỹ thuật

- Đạt toàn bộ ngưỡng hiệu năng trong bảng kỹ thuật ở ba phiên soak liên tiếp.
- ≥99,5% phiên không crash và ≥99,0% trận được máy chủ kết thúc với kết quả hợp lệ.
- <0,5% phát bắn hợp lệ tạo khiếu nại hitreg được replay xác nhận là sai quá 0,5 m hoặc quá một tick.
- ≥95% người chơi được ghép vào vùng có ping trung vị ≤80 ms trong khu vực ra mắt.
- Mỗi input pool phải chứng minh đủ dân số tạo trận 100 người trong ngưỡng chờ được phê duyệt; không dùng bot hoặc fallback pool ngầm để đạt chỉ số.
- Mọi profile mobile đạt FPS, memory, thermal, load và lifecycle gate trên device matrix trước release candidate.

### Chỉ số gameplay

- Thời lượng trận trung vị 28–32 phút; p90 không vượt 35 phút.
- Survival curve nằm trong dải mục tiêu của bảng vòng bo trong ≥80% trận beta.
- 60–75% người chơi có một vũ khí chính trong 90 giây; <5% không tìm thấy súng sau khi loot trọn một cụm nhà trung bình.
- ≥80% người thử nghiệm giải thích được quyết định chính dẫn tới cái chết trong khảo sát sau trận.
- ≥70% đánh giá “vị trí và thông tin quan trọng hơn độ hiếm trang bị” ở mức 4/5 trở lên.
- Không archetype loot thường nào vượt 22% số hạ gục trong mẫu cân bằng đủ lớn.
- 100% nội dung ảnh hưởng gameplay có thể tiếp cận chỉ bằng hành động trong trận, không bằng tiền hoặc tiến trình tài khoản.

### Cổng chấp nhận v1.0

v1.0 chỉ sẵn sàng khi vòng lặp 100 người hoạt động trọn vẹn, tải kỹ thuật đạt mục tiêu, playtest xác nhận cả bốn trụ cột và release candidate family đạt trên Windows, Linux, macOS, Android, iOS. Số skin, sự kiện hoặc chỉ số doanh thu không được dùng để thay thế các điều kiện này.

### Cổng chống lệch tầm nhìn hậu phát hành

Mọi tính năng hoặc nội dung mới phải:

1. Chỉ rõ trụ cột P1–P4 mà nó củng cố và chỉ số dùng để chứng minh.
2. Không tạo sức mạnh, thông tin, ngụy trang hoặc tiện ích bằng chi tiêu/tiến trình ngoài trận.
3. Không chèn nhịp thương mại vào Standard, HUD trận hoặc bản đồ chuẩn.
4. Không được phê duyệt chỉ dựa trên doanh thu, engagement hằng ngày hoặc khả năng bán skin.
5. Bị loại hoặc tách khỏi Standard nếu playtest cho thấy giảm tension, fairness hoặc readability.

---

## Ngoài phạm vi

### Loại trừ vĩnh viễn khỏi luật chơi chuẩn

- Pay-to-win, vũ khí/chỉ số trả phí, loot box, gacha và battle pass hết hạn.
- Hero, class, ultimate, kỹ năng siêu nhiên, pet chiến đấu và loadout ngoài trận.
- Hồi sinh, tự cứu, mua lại đồng đội hoặc trạm triệu hồi trong Standard.
- Quảng cáo thương hiệu, sân khấu sự kiện hoặc mỹ phẩm phát sáng chen vào bản đồ Standard.

### Không có trong v1.0

- Console, controller, controller aim assist và cross-play với console.
- Bản đồ thứ hai, chiến dịch PvE, zombie, boss, nhiệm vụ cốt truyện.
- Ranked, esports tools, custom server công khai, modding và UGC.
- Phá hủy công trình/địa hình, xây căn cứ, chế tạo, đói, khát và nhiệt độ cơ thể.
- Replay người dùng đầy đủ, kill-cam cạnh tranh và spectator nâng cao ngoài công cụ nội bộ.
- Thời tiết đổi động, chu kỳ ngày/đêm và thiên tai ngẫu nhiên.
- Cửa hàng mỹ phẩm, premium currency, battle pass, nhiệm vụ đăng nhập, collab thương hiệu và live-event.

### Ứng viên sau v1.0

- FPP-only queue, ranked, custom server và replay đầy đủ nếu dân số/hiệu năng đáp ứng.
- Bản đồ thứ hai chỉ sau khi Đảo Vọng đạt mục tiêu cân bằng.
- Console và controller sau nghiên cứu riêng về aim assist/cross-play; Keyboard/Mouse và Touch đã thuộc v1.0.

---

## Giả định, phụ thuộc và câu hỏi không chặn

### Giả định đã dùng

- **A-001:** `[ASSUMPTION: Đảo Vọng và bối cảnh Đông Nam Á là đề xuất tạo bản sắc; chủ đề có thể đổi mà không thay đổi vòng lặp cốt lõi.]`
- **A-002:** `[ASSUMPTION: Nếu phát hành thương mại, mô hình ưu tiên là mua game một lần; giá và chi phí máy chủ cần business validation riêng.]`
- **A-003:** `[ASSUMPTION: Quy mô nhóm và ngân sách chưa xác định; các mốc dưới đây là cổng học hỏi, không phải lịch phát hành hoặc cam kết sản xuất.]`
- **A-004 (đã thay thế):** `[ASSUMPTION: Envelope PC-first 1–3/5–8/12–20 người không còn dùng để phê duyệt production; phạm vi năm nền tảng phải được architecture và production planning ước lượng lại trước R2.]`
- **A-005:** `[ASSUMPTION: 100 người và 8×8 km vẫn là north-star v1.0; các target 25 vũ khí, 6 phương tiện, 18 POI và 420 công trình chỉ được khóa sau mobile viability và server scale gate.]`

### Phụ thuộc

- Hạ tầng máy chủ theo vùng đủ để duy trì ping mục tiêu và thử tải 100 client.
- Nguồn người thử nghiệm đủ lớn cho các mốc 24 và 100 người.
- Kiểm chứng pháp lý đối với tên vũ khí, hình dáng, âm thanh và mọi tài sản tham chiếu thực tế.
- Kiến trúc Godot phải chứng minh streaming bản đồ, mô phỏng 100 người và mô hình mạng trước khi sản xuất toàn bộ nội dung.
- macOS/iOS build-sign-test cần máy macOS, Xcode, provisioning và thiết bị thật; Android cần ARM64 AAB/Gradle/signing cùng device lab đại diện.

### Câu hỏi không chặn kiến trúc

- Mức giá mua một lần và chính sách máy chủ dài hạn.
- Tên/chủ đề cuối của Đảo Vọng.
- Thứ tự ra mắt khu vực sau beta kín.

---

## Nguồn tham chiếu thiết kế

- [PUBG — Erangel Classic Returns](https://www.pubg.com/en/news/7282): xác nhận các yếu tố gợi nhớ bản cổ điển như không khí u ám, mưa/sương, loot trang phục và nhịp hạ gục chậm hơn.
- [PUBG — Blue Zone Revamp](https://pubg.com/en/news/10280): mô tả vai trò của vùng bo trong việc thu hẹp không gian, thúc đẩy gặp nhau và điều khiển nhịp sống sót.
- [PUBG — Weapons](https://pubg.com/en/game-info/weapons/etc): tham chiếu phạm vi archetype vũ khí; OutSurvive dùng roster và thông số riêng.
- [PUBG — Ranked Map Service](https://pubg.com/en/news/7020): tham chiếu quy mô bản đồ 8×8 km và vai trò lâu dài của bản đồ cổ điển.
