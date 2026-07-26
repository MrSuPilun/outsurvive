# OutSurvive — UX/UI Research Synthesis

**Ngày:** 2026-07-22  
**Phạm vi:** UI/HUD cho PC battle royale sinh tồn; nghiên cứu dùng để ra quyết định, không sao chép giao diện hoặc tài sản của game tham chiếu.

## Câu hỏi nghiên cứu

1. Điều gì làm UI PUBG cổ điển gợi cảm giác sinh tồn?
2. Những cải tiến nào tăng độ rõ mà không biến HUD thành radar trợ chiến?
3. UI Godot phải thích ứng 720p–4K và ultrawide như thế nào?
4. Mức contrast/accessibility tối thiểu nào không phá công bằng âm thanh–thông tin?

## Phát hiện

### 1. Giữ cấu trúc quen thuộc, không sao chép vẻ ngoài

- PUBG chính thức mô tả Erangel Classic bằng world map/minimap, match-start timer và kiểu chữ/đồ họa “vintage”. Giá trị cần giữ là cảm giác bản đồ dã chiến và thông tin chức năng; không dùng font, icon hoặc bố cục PUBG nguyên bản.
- Hướng phù hợp với OutSurvive là **Field Instrument**: bảng số liệu như dụng cụ hiện trường, bề mặt mờ tối, đường chia mảnh, typography có tính công nghiệp nhưng thân bài vẫn đọc nhanh.
- Không dùng “military cosplay UI”: quá nhiều ốc vít, giấy rách, texture nhiễu hoặc stencil khó đọc sẽ làm giảm độ rõ và tăng chi phí asset.

Nguồn: [PUBG — Erangel Classic Returns](https://pubg.com/en/news/7282).

### 2. Progressive disclosure tốt hơn HUD cố định dày đặc

- PUBG Update 40.1 thêm throwable list chỉ xuất hiện ngắn khi rút/đổi vật ném và thêm trạng thái hành động của squad. Điều này hỗ trợ nguyên tắc: thông tin chiến đấu xuất hiện khi có quyết định cần đưa ra, rồi thu lại.
- OutSurvive áp dụng cùng nguyên lý cho vật ném, healing/revive, trạng thái xe và cảnh báo mạng. Thông tin không liên quan bị ẩn; không thêm enemy detection, footstep radar hoặc loot recommendation.
- Inventory improvement của PUBG cho thấy giảm số bước đổi vũ khí/phụ kiện và đặt attachment gần weapon slot làm thao tác ít ma sát hơn. OutSurvive giữ thao tác nhanh nhưng không tự chọn “đồ tốt nhất”, vì tự động hóa đó làm yếu P1/P3.

Nguồn: [PUBG Update 40.1](https://www.pubg.com/en/news/9690), [PUBG Console Inventory Improvement](https://www.pubg.com/en/news/1672), [PUBG Update 30.2 — Inventory UX](https://pubg.com/en/news/7494).

### 3. Accessibility là độ rõ, không phải thêm thông tin chiến thuật

- WCAG 2.2 yêu cầu thành phần UI/đồ họa cần thiết có contrast nhận diện được; W3C giải thích non-text UI cần phân biệt với màu kề cận.
- Đặt floor: text thường ≥4,5:1; text lớn/icon/state ≥3:1; focus ≥3:1. Màu trạng thái luôn đi cùng icon, shape hoặc label.
- Không chuyển âm thanh bước chân thành radar hình ảnh. Accessibility tập trung vào subtitle hệ thống/ping, mixer, HRTF test, màu–shape redundancy và khả năng giảm motion/flash.

Nguồn: [WCAG 2.2](https://www.w3.org/TR/WCAG22/), [Understanding Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [Understanding Text Contrast](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html).

### 4. Responsive phải bảo vệ cạnh tranh

- Godot khuyến nghị anchors/containers cho nhiều aspect ratio và cho phép tách resolution scale của 3D với UI. UI cần crisp kể cả khi world render bị scale xuống.
- Base design 1920×1080; các control chiến thuật nằm trong competitive safe frame 16:9. Ultrawide mở rộng background/world-facing chrome nhưng không đẩy minimap/compass quá xa tâm nhìn hoặc cấp thêm dữ liệu.
- UI scale 80–140%; font/icon vector hoặc distance-field; panel layout dùng anchors/containers thay vì tọa độ tuyệt đối.

Nguồn: [Godot — Multiple resolutions](https://docs.godotengine.org/en/4.6/tutorials/rendering/multiple_resolutions.html), [Godot — Using Containers](https://docs.godotengine.org/en/4.6/tutorials/ui/gui_containers.html).

## Direction được chọn: Field Instrument

### Thuộc tính

- **Grounded:** giống công cụ dùng ngoài hiện trường, không giống màn hình cửa hàng.
- **Sparse:** chỉ báo thường trực giới hạn; context card tự thu lại.
- **Measured:** số, tick, vạch và icon hình học; animation ngắn, không celebration loop.
- **Weathered, not dirty:** texture hạt rất nhẹ ở menu/map; HUD chiến đấu sạch.
- **Human under pressure:** nguy hiểm dùng động tác/nhịp rõ, không dùng hiệu ứng giật/flash quá mức.

### Palette kiểm chứng trên `#161B18`

| Token ứng viên | Giá trị | Contrast | Vai trò |
|---|---|---:|---|
| text.primary | `#E7E3D5` | 13,58:1 | nội dung chính |
| text.secondary | `#B9C0B7` | 9,37:1 | nhãn/phụ trợ |
| text.muted | `#8F9A91` | 5,98:1 | metadata |
| signal.attention | `#D6A84B` | 7,94:1 | focus, cảnh báo không chí mạng |
| signal.zone | `#73AFC7` | 7,21:1 | bo/đội/định vị |
| signal.danger | `#DC6652` | >4,5:1 | sát thương, lỗi nguy hiểm |
| signal.success | `#8FB06C` | 7,14:1 | xác nhận, sống sót |

## Anti-pattern bị loại

- Dashboard nhiều tab, tin tức hoặc carousel ở màn hình chính.
- Neon gradient, glassmorphism sáng, rounded card lớn hoặc animation “mobile live-service”.
- Kill-feed toàn cục dày đặc; số damage nổi; footstep radar; loot auto-score.
- Full-screen inventory che hoàn toàn thế giới hoặc render nhân vật trang trí ở giữa.
- Màu rarity là tín hiệu duy nhất; màu danger dùng cho hành động không nguy hiểm.
- Badge đỏ, streak, countdown reward và CTA thúc ép quay lại.

