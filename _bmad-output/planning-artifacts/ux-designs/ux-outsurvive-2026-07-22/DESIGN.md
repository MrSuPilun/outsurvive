---
name: "OutSurvive Field Instrument"
description: "Hệ thống thị giác thực dụng cho battle royale sinh tồn desktop–mobile, ưu tiên khả năng đọc, công bằng và áp lực chiến thuật."
project: "outsurvive"
document: "DESIGN.md"
status: "final"
created: "2026-07-22"
updated: "2026-07-26"
sources:
  - "../../gdds/gdd-outsurvive-2026-07-22/gdd.md"
colors:
  surface-base: '#161B18'
  surface-raised: '#202720'
  surface-overlay: '#101410'
  surface-map: '#202A25'
  surface-disabled: '#323A34'
  text-primary: '#E7E3D5'
  text-secondary: '#B9C0B7'
  text-muted: '#8F9A91'
  text-inverse: '#101410'
  border-default: '#6B786E'
  border-subtle: '#3F4942'
  signal-attention: '#D6A84B'
  signal-zone: '#73AFC7'
  signal-danger: '#DC6652'
  signal-success: '#8FB06C'
  signal-neutral: '#C9C5B8'
  scrim: '#080A09'
  cb-protanopia-zone: '#65B5D2'
  cb-protanopia-marker: '#E0B45C'
  cb-protanopia-hit: '#E3834E'
  cb-protanopia-reticle: '#F3F0E4'
  cb-deuteranopia-zone: '#73AFC7'
  cb-deuteranopia-marker: '#DDB85A'
  cb-deuteranopia-hit: '#D97852'
  cb-deuteranopia-reticle: '#F3F0E4'
  cb-tritanopia-zone: '#70B787'
  cb-tritanopia-marker: '#DDA15E'
  cb-tritanopia-hit: '#E77F95'
  cb-tritanopia-reticle: '#F3F0E4'
typography:
  display:
    fontFamily: "Noto Sans Condensed"
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.10'
    letterSpacing: 0.02em
  heading-lg:
    fontFamily: "Noto Sans Condensed"
    fontSize: 28px
    fontWeight: '700'
    lineHeight: '1.20'
    letterSpacing: 0.02em
  heading-md:
    fontFamily: "Noto Sans Condensed"
    fontSize: 22px
    fontWeight: '600'
    lineHeight: '1.25'
    letterSpacing: 0.02em
  body:
    fontFamily: "Noto Sans"
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.45'
  label:
    fontFamily: "Noto Sans"
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.30'
    letterSpacing: 0.03em
  caption:
    fontFamily: "Noto Sans"
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.35'
  key-label:
    fontFamily: "Noto Sans"
    fontSize: 13px
    fontWeight: '700'
    lineHeight: '1.20'
  minimum:
    fontFamily: "Noto Sans"
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.30'
  numeric:
    fontFamily: "Noto Sans Mono"
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.20'
    letterSpacing: 0.01em
  hud-critical:
    fontFamily: "Noto Sans Mono"
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.15'
rounded:
  sm: 2px
  DEFAULT: 4px
  md: 6px
  lg: 8px
  full: 9999px
spacing:
  '1': 4px
  '2': 8px
  '3': 12px
  '4': 16px
  '5': 24px
  '6': 32px
  '7': 48px
  '8': 64px
  safe-frame: 5%
  panel-gap: 12px
  compact-gutter: 16px
  base-gutter: 24px
  large-gutter: 32px
  overlay-lane: 360px
  subtitle-max-width: 60%
components:
  action-button:
    minHeight: 44px
    paddingX: '{spacing.4}'
    textStyle: '{typography.label}'
    background: '{colors.surface-raised}'
    foreground: '{colors.text-primary}'
    focus: '{colors.signal-attention}'
    radius: '{rounded.DEFAULT}'
  navigation-item:
    minHeight: 40px
    textStyle: '{typography.label}'
    foreground: '{colors.text-secondary}'
    active: '{colors.text-primary}'
    indicator: '{colors.signal-attention}'
  focus-ring:
    width: 2px
    color: '{colors.signal-attention}'
    radius: '{rounded.md}'
  status-banner:
    background: '{colors.surface-overlay}'
    foreground: '{colors.text-primary}'
    attention: '{colors.signal-attention}'
    danger: '{colors.signal-danger}'
    radius: '{rounded.DEFAULT}'
    backplateOpacity: '92%'
  network-warning:
    background: '{colors.surface-overlay}'
    foreground: '{colors.signal-danger}'
    textStyle: '{typography.label}'
    radius: '{rounded.DEFAULT}'
    backplateOpacity: '92%'
  match-hud:
    foreground: '{colors.text-primary}'
    secondary: '{colors.text-secondary}'
    scrim: '{colors.surface-overlay}'
    safeFrame: '{spacing.safe-frame}'
    backplateOpacity: '92%'
  compass:
    textStyle: '{typography.numeric}'
    foreground: '{colors.text-secondary}'
    active: '{colors.text-primary}'
    marker: '{colors.signal-zone}'
  squad-panel:
    background: '{colors.surface-overlay}'
    foreground: '{colors.text-primary}'
    team: '{colors.signal-zone}'
    danger: '{colors.signal-danger}'
  health-boost-bar:
    health: '{colors.text-primary}'
    boost: '{colors.signal-attention}'
    missing: '{colors.surface-disabled}'
    danger: '{colors.signal-danger}'
  weapon-ammo-panel:
    textStyle: '{typography.hud-critical}'
    foreground: '{colors.text-primary}'
    secondary: '{colors.text-secondary}'
    warning: '{colors.signal-attention}'
  minimap-zone-panel:
    background: '{colors.surface-map}'
    foreground: '{colors.text-primary}'
    zone: '{colors.signal-zone}'
    danger: '{colors.signal-danger}'
    border: '{colors.border-default}'
  context-prompt:
    background: '{colors.surface-overlay}'
    foreground: '{colors.text-primary}'
    key: '{colors.signal-attention}'
    radius: '{rounded.DEFAULT}'
  damage-direction-indicator:
    danger: '{colors.signal-danger}'
    neutral: '{colors.signal-neutral}'
    arcWidth: 30deg
  reticle:
    line: '{colors.text-primary}'
    outline: '{colors.scrim}'
    hit: '{colors.signal-danger}'
    lineWidth: 2px
    outlineWidth: 1px
    centerGap: 6px
    armLength: 8px
    protanopiaLine: '{colors.cb-protanopia-reticle}'
    protanopiaHit: '{colors.cb-protanopia-hit}'
    deuteranopiaLine: '{colors.cb-deuteranopia-reticle}'
    deuteranopiaHit: '{colors.cb-deuteranopia-hit}'
    tritanopiaLine: '{colors.cb-tritanopia-reticle}'
    tritanopiaHit: '{colors.cb-tritanopia-hit}'
  context-action-card:
    background: '{colors.surface-overlay}'
    foreground: '{colors.text-primary}'
    progress: '{colors.signal-attention}'
    danger: '{colors.signal-danger}'
    backplateOpacity: '92%'
  inventory-panel:
    background: '{colors.surface-overlay}'
    foreground: '{colors.text-primary}'
    border: '{colors.border-default}'
    radius: '{rounded.DEFAULT}'
    backplateOpacity: '92%'
  item-row:
    minHeight: 36px
    background: '{colors.surface-raised}'
    foreground: '{colors.text-primary}'
    secondary: '{colors.text-secondary}'
    focus: '{colors.signal-attention}'
  equipment-slot:
    minSize: 48px
    background: '{colors.surface-raised}'
    border: '{colors.border-default}'
    focus: '{colors.signal-attention}'
  map-marker-layer:
    background: '{colors.surface-map}'
    zone: '{colors.signal-zone}'
    danger: '{colors.signal-danger}'
    team: '{colors.signal-success}'
    text: '{colors.text-primary}'
  party-panel:
    background: '{colors.surface-raised}'
    foreground: '{colors.text-primary}'
    ready: '{colors.signal-success}'
    warning: '{colors.signal-attention}'
  voice-ping-indicator:
    foreground: '{colors.text-secondary}'
    active: '{colors.signal-zone}'
    muted: '{colors.text-muted}'
  progress-timer:
    textStyle: '{typography.numeric}'
    foreground: '{colors.text-primary}'
    progress: '{colors.signal-attention}'
    interrupted: '{colors.signal-danger}'
  results-table:
    background: '{colors.surface-raised}'
    foreground: '{colors.text-primary}'
    secondary: '{colors.text-secondary}'
    highlight: '{colors.signal-success}'
  settings-control:
    minHeight: 40px
    foreground: '{colors.text-primary}'
    secondary: '{colors.text-secondary}'
    focus: '{colors.signal-attention}'
  subtitle-line:
    background: '{colors.surface-overlay}'
    foreground: '{colors.text-primary}'
    speaker: '{colors.signal-zone}'
    textStyle: '{typography.body}'
    backplateOpacity: '92%'
    maxWidth: '{spacing.subtitle-max-width}'
  safe-area-root:
    minInset: 4px
    contentInset: 8px
    debugOutline: '{colors.signal-attention}'
  touch-stick:
    minSize: 96px
    thumbSize: 48px
    foreground: '{colors.text-primary}'
    background: '{colors.surface-overlay}'
    active: '{colors.signal-attention}'
  touch-look-zone:
    minWidth: 40%
    foreground: '{colors.text-secondary}'
    debugBorder: '{colors.border-default}'
  touch-action-button:
    minSize: 48px
    criticalMinSize: 64px
    foreground: '{colors.text-primary}'
    background: '{colors.surface-overlay}'
    active: '{colors.signal-attention}'
  control-layout-editor:
    handleSize: 48px
    gridStep: 8px
    foreground: '{colors.text-primary}'
    boundary: '{colors.signal-attention}'
    invalid: '{colors.signal-danger}'
---

# OutSurvive — Visual Design System

## Brand & Style

[ASSUMPTION: UX-005] Hướng **Field Instrument** xem UI như bộ dụng cụ hiện trường: thực dụng, thưa, đo lường được và chịu áp lực tốt. Menu và bản đồ có lớp hạt/hao mòn rất nhẹ; HUD chiến đấu sạch, không texture che chữ. Cảm giác cần đạt là một người sống sót đang đọc địa hình và tài nguyên, không phải khách hàng đang đứng trước cửa hàng.

Hình ảnh hiện thực có tiết chế của GDD được nối tiếp bằng đường chia mảnh, tick đo, icon hình học và số đơn cách. Không dùng tài sản, kiểu chữ hay bố cục nhận diện của PUBG; chỉ kế thừa nguyên tắc “thông tin chức năng trước”. Không dùng neon, gradient bóng, glassmorphism, mascot, confetti hay chrome giả quân sự dày đặc.

[ASSUMPTION: UX-004] Hệ thống này phục vụ north-star indie/commercial trên desktop và mobile, phải chứa được tiếng Việt lẫn tiếng Anh. Bộ Noto được chọn vì độ rõ và độ phủ ký tự; license, hinting trên Windows/Linux/macOS/Android/iOS và metric fallback phải được xác nhận trước production. Story 1.7–1.8 phải có snapshot acceptance trong Godot cho dấu tiếng Việt và chuỗi tiếng Anh dài ở profile compact/mobile; đây là evidence gate của story, không phải product-decision gate.

## Colors

[ASSUMPTION: UX-010] Palette charcoal–olive–bone giữ màn hình trầm; amber chỉ attention/focus, cyan cho bo và dữ liệu định vị/đội, rust-red cho nguy hiểm, green-muted cho xác nhận. Màu không bao giờ là tín hiệu duy nhất: mỗi trạng thái phải có thêm icon, nhãn, hình hoặc nhịp.

| Vai trò | Token | Dùng cho | Không dùng cho |
|---|---|---|---|
| Nền chiến đấu | `{colors.surface-base}` | nền menu và chuẩn tương phản | phủ kín thế giới khi HUD đang mở |
| Panel | `{colors.surface-raised}` / `{colors.surface-overlay}` | panel menu, HUD scrim bán trong | tạo card trang trí không có chức năng |
| Chữ | `{colors.text-primary}` / `{colors.text-secondary}` / `{colors.text-muted}` | thứ bậc đọc | biểu thị rarity một mình |
| Chú ý | `{colors.signal-attention}` | focus, đếm ngược, tài nguyên cần chú ý | CTA thương mại hoặc thưởng FOMO |
| Vùng/đội | `{colors.signal-zone}` | bo, marker định vị, trạng thái nói | tự nhận dạng địch |
| Nguy hiểm | `{colors.signal-danger}` | sát thương, gián đoạn, lỗi nguy cấp | hành động trung tính |
| Thành công | `{colors.signal-success}` | ready, sống sót, xác nhận | celebration loop |

[ASSUMPTION: UX-012/UX-022] Trên `{colors.surface-base}`, research ghi nhận `{colors.text-primary}` 13,58:1, `{colors.text-secondary}` 9,37:1, `{colors.text-muted}` 5,98:1, `{colors.signal-attention}` 7,94:1 và `{colors.signal-zone}` 7,21:1. Production phải giữ text thường ≥4,5:1, text lớn/icon/focus ≥3:1 và kiểm lại mọi tổ hợp sau opacity/compositing trong Godot. `{colors.signal-danger}` và `{colors.signal-success}` luôn đi cùng biểu tượng/hình dạng hoặc chữ.

Text-bearing backplate không được dùng alpha tùy ý: `status-banner`, `network-warning`, `match-hud`, `context-action-card`, `inventory-panel` và `subtitle-line` compositing `{colors.surface-overlay}` ở **tối thiểu 92% opacity** dưới vùng chữ. Phần đuôi/trang trí không chứa thông tin có thể giảm tới 72%. Nếu thế giới phía sau vẫn làm tổ hợp chữ dưới target, renderer phải chèn local solid backplate thay vì đổi chữ sang glow. `{colors.border-default}` đạt khoảng 3,20:1 trên `{colors.surface-map}`; `{colors.border-subtle}` chỉ dùng cho đường trang trí không cần nhận biết để thao tác.

[ASSUMPTION: UX-025] Ba preset mù màu chỉ hoán đổi token; geometry, line style, icon, identity number và timing giữ nguyên:

| Preset | Zone | Teammate marker | Hit effect | Reticle |
|---|---|---|---|---|
| Protanopia | `{colors.cb-protanopia-zone}` | `{colors.cb-protanopia-marker}` | `{colors.cb-protanopia-hit}` | `{colors.cb-protanopia-reticle}` |
| Deuteranopia | `{colors.cb-deuteranopia-zone}` | `{colors.cb-deuteranopia-marker}` | `{colors.cb-deuteranopia-hit}` | `{colors.cb-deuteranopia-reticle}` |
| Tritanopia | `{colors.cb-tritanopia-zone}` | `{colors.cb-tritanopia-marker}` | `{colors.cb-tritanopia-hit}` | `{colors.cb-tritanopia-reticle}` |

Zone luôn dùng current-line solid / next-line dashed; teammate luôn có shape + số; hit effect luôn là burst hướng tâm; `reticle` luôn dual-stroke. Preset không thêm outline địch, cường điệu muzzle/hit hay tạo footstep cue.

## Typography

`{typography.display}`, `{typography.heading-lg}` và `{typography.heading-md}` dùng Noto Sans Condensed cho tiêu đề gọn, công nghiệp nhưng không stencil. `{typography.body}` và `{typography.label}` chịu trách nhiệm đọc nhanh và localization. `{typography.numeric}` cùng `{typography.hud-critical}` dùng Noto Sans Mono để ammo, timer, khoảng cách và tọa độ không giật ngang khi số đổi.

Không dùng toàn chữ hoa cho câu dài hoặc nội dung tiếng Việt. Label ngắn có thể dùng chữ hoa khi đã kiểm tra dấu. Số chiến đấu không animate scale liên tục; thay đổi phải đọc được trong một glance. UI scale 80–140% phải scale typography bằng theme constants thay vì raster hóa.

Rendered text không bao giờ nhỏ hơn `{typography.minimum.fontSize}`; gameplay-critical label không dưới `{typography.label.fontSize}` và số critical không dưới `{typography.numeric.fontSize}`, kể cả khi UI scale là 80%. Noto Sans/Noto Sans Condensed/Noto Sans Mono phải ship cùng build với fallback Unicode có cùng x-height; missing glyph không được thay bằng ô vuông.

Key label dùng `{typography.key-label}` trong keycap rộng tự động 32–96px. Binding dài ưu tiên tên phím chuẩn hóa của OS/InputMap; quá 96px thì dùng alias đã localization và tooltip/accessible label chứa tên đầy đủ, không co font dưới minimum. Action label quan trọng được phép wrap tối đa hai dòng; Leave/Confirm/Report không được ellipsis. HUD label một dòng phải reflow module hoặc chuyển sang alias đã duyệt thay vì đè lên số.

## Layout & Spacing

[ASSUMPTION: UX-011/UX-021/UX-024] Canvas chuẩn là 1920×1080, scale từ 1280×720 đến 3840×2160. Grid cơ sở `{spacing.1}`; nhóm gần dùng `{spacing.2}`–`{spacing.3}`, panel dùng `{spacing.4}`–`{spacing.6}`. HUD chiến thuật neo trong competitive safe frame 16:9 với lề `{spacing.safe-frame}`. Trong Standard v1.0, ultrawide đặt live-world viewport 16:9 ở giữa và dùng side matte/chrome không tương tác ở hai bên; menu/Profile/Settings được dùng toàn chiều rộng. Cách này không cấp thêm world/HUD data cạnh tranh.

[ASSUMPTION: UX-008] Lobby dùng điều hướng dọc bên trái và `party-panel` + hành động Deploy bên phải; vùng giữa giữ world scene làm tiêu điểm, không chèn commerce/news rail. [Mockup Lobby](mockups/lobby.html) — minh họa left navigation, right party/action panel và world center.

[ASSUMPTION: UX-006/UX-017/UX-023] Bố cục HUD dùng sáu module neo cố định: `compass` trên giữa; `squad-panel` bên trái; `health-boost-bar` dưới giữa; `minimap-zone-panel` phải; `weapon-ammo-panel` phải dưới; `reticle` tại tâm. `context-prompt` nằm gần tâm dưới và các `context-action-card` xuất hiện theo ngữ cảnh rồi thu lại; alternate vehicle fire giữ cue P0 tại critical action lane mà không dịch sáu module. [Mockup Match HUD](mockups/match-hud.html) — minh họa sáu module anchor và alternate P0 vehicle fire.

[ASSUMPTION: UX-040/UX-041] Trên mobile landscape, toàn bộ HUD nằm trong `safe-area-root`: `touch-stick` neo trái dưới; `touch-look-zone` chiếm phần phải không có control; `touch-action-button` nhóm theo reach zone cho fire/ADS/reload/stance/interact/throwable/map/inventory/vehicle. Fire có nút phải bắt buộc và nút trái tùy chọn; các module thông tin giữ nguyên lượng dữ liệu desktop nhưng reflow để không che vùng nhìn/ngắm. [Mobile Match HUD](mockups/mobile-match-hud.html) là delta reference, không cấp enemy cue hoặc auto-play.

[ASSUMPTION: UX-007] `inventory-panel` dùng hai dải trái/phải, tổng không quá 68% chiều ngang; giữ dải thế giới trung tâm ít nhất 32%. Bố cục chuẩn tại 1920×1080 là 34% Nearby/Backpack trái — 32% world strip — 34% Weapons/Equipment phải; breakpoint khác được reflow trong contract ≤68% / ≥32%. Panel bán trong nhưng text và slot phải giữ tương phản mục tiêu. [Mockup Inventory](mockups/inventory.html) — minh họa composition chuẩn 34/32/34 và durability trong panel phải.

[ASSUMPTION: UX-042] Mobile Inventory dùng một `inventory-panel` tabbed rộng tối đa 62% viewport và giữ world-risk strip tối thiểu 38%; Nearby/Backpack/Equipment đổi bằng tap, mọi action có tap menu và drag chỉ là đường tắt. Mobile Map dùng pan/pinch/tap/long-press; close và damage cue luôn ở safe area. [Mobile Inventory / Map](mockups/mobile-inventory-map.html) minh họa cả hai state trong một delta reference.

[ASSUMPTION: UX-009/UX-032] Map/Phase đặt header ở góc trên trái, phase/timer ở góc trên phải, legend ở góc dưới trái và bindings ở góc dưới phải. Bo hiện tại dùng nét liền; bo kế tiếp chỉ hiện sau server reveal và dùng nét đứt. [Mockup Map / Phase](mockups/map-phase.html) — minh họa bốn corner anchor và next-zone đã lộ bằng nét đứt.

[ASSUMPTION: UX-014/UX-037/UX-045] Bốn desktop visual reference load-bearing cho Lobby, Match HUD, Inventory và Map/Phase được giữ nguyên; mobile delta thêm đúng hai reference cho Match HUD và Inventory/Map. Pause/Settings, Results và các surface còn lại dựng từ spine; không yêu cầu reference thứ bảy.

### Central safe frame, breakpoint và reflow

[ASSUMPTION: UX-021/UX-024] Central competitive frame là hình 16:9 lớn nhất vừa viewport: `frame-width = min(viewport-width, viewport-height × 16/9)`, căn giữa. HUD critical và live world Standard nằm trong inset/frame này; phần ultrawide ngoài frame chỉ chứa side matte/chrome không tương tác, không có player, loot, vehicle, projectile hoặc cue gameplay.

| Breakpoint theo central-frame width | Gutter | Reflow bắt buộc |
|---|---|---|
| Compact: 1280–1599px | `{spacing.compact-gutter}` | rút khoảng trống; squad giữ 4 hàng; subtitle/context xếp dọc; không giảm text dưới minimum |
| Base: 1600–2559px | `{spacing.base-gutter}` | bố cục chuẩn 1920×1080 |
| Large: ≥2560px | `{spacing.large-gutter}` | tăng whitespace và scale theo setting; không tăng mật độ thông tin |

Nếu chiều cao khả dụng dưới 720px, surface không được shrink tiếp: bật scroll cho menu/Settings, còn HUD giữ module critical và loại decorative chrome. Inventory giữ dải thế giới giữa ≥32%; khi text dài, panel mở rộng vào phần 68% đã cấp trước khi giảm cỡ chữ.

### Overlay lane và collision

[ASSUMPTION: UX-023] Lane dưới đây là contract duy nhất cho anchor/collision; priority và preemption hành vi nằm trong `EXPERIENCE.md`.

- **Lane A — top-center:** `compass`; `status-banner` nằm dưới compass và không chồng bearing/marker.
- **Lane B — center:** `reticle` độc quyền vùng tâm; `damage-direction-indicator` bao ngoài nhưng không che reticle.
- **Lane C — center-lower:** `context-prompt`, `context-action-card`, rồi `subtitle-line` reflow lên/xuống theo thứ tự đó; mỗi lane rộng tối đa `{spacing.overlay-lane}` trừ subtitle.
- **Lane D — top-right:** `network-warning` nằm trên `minimap-zone-panel`; không đẩy minimap ra khỏi safe frame.
- **Lane E — bottom:** `health-boost-bar` dưới giữa, `weapon-ammo-panel` phải dưới; subtitle không được giao với hai vùng này.

`subtitle-line` rộng tối đa `{spacing.subtitle-max-width}`, tối đa hai dòng mỗi cue trong vùng giữa; ưu tiên đặt trên Lane C, sau đó đẩy lên trên `context-action-card`. Nó không bao giờ che `reticle`, key prompt, timer cứu/heal, HP hoặc ammo. Nếu đồng thời quá nhiều cue, giữ backplate và xếp theo hàng dọc; không giảm font.

## Elevation & Depth

Ba lớp duy nhất: thế giới; HUD/panel bán trong; modal xác nhận hoặc cảnh báo ưu tiên cao trên `{colors.scrim}`. Độ sâu đến từ tonal layering và viền `{colors.border-subtle}`, không từ shadow lớn. Inventory/Map không pause trận; chúng không được làm thế giới biến mất về mặt nhận thức. Không xếp quá một modal trên một surface.

Trong trận, cảnh báo mạng, gục/cứu và danger state được ưu tiên bằng vị trí/nhịp trước màu. Không blur hậu cảnh trong combat vì blur làm giảm khả năng đọc nguy cơ và tốn GPU.

Z-order cố định: world 0 → persistent HUD 10 → Inventory/Map 20 → contextual action 30 → critical damage/network/friendly-fire 40 → Pause/confirm 50 → blocking system modal 60. Critical layer 40 vẫn nhìn thấy trên Map/Inventory nhưng không xuyên blocking modal. Cùng một lane chỉ có một item ở mỗi priority; item thấp hơn xếp hàng, không chồng alpha.

## Shapes

Ngôn ngữ hình gần vuông: `{rounded.sm}` cho tick/nhãn nhỏ, `{rounded.DEFAULT}` cho control và HUD panel, `{rounded.md}` cho modal; `{rounded.lg}` chỉ cho container lớn ngoài trận. `{rounded.full}` chỉ dành cho điểm marker hoặc vòng progress có ý nghĩa hình học, không dùng làm nút pill mặc định.

Viền 1px cho panel; `focus-ring` 2px và không bị crop. Health, boost, zone và progress dùng silhouette khác nhau để giữ color+shape redundancy. Không dùng băng keo, ốc vít hay giấy rách trang trí.

## Components

Tên component dưới đây là contract chính xác và phải trùng trong `EXPERIENCE.md`.

| Component | Đặc tả thị giác |
|---|---|
| `action-button` | Khối thấp, fill `{colors.surface-raised}`, chữ `{colors.text-primary}`; primary/focus bằng viền và vạch `{colors.signal-attention}`, không tô neon toàn nút. |
| `navigation-item` | Một hàng chữ với vạch active 2px; không badge đỏ, không số thưởng. |
| `focus-ring` | Viền 2px `{colors.signal-attention}`, offset đủ không chồng chữ; luôn thấy ở keyboard navigation. |
| `status-banner` | Panel ngang ngắn, icon + nhãn + severity; tối đa hai dòng ở 100% UI scale. |
| `network-warning` | Icon kết nối đứt + ping/loss dạng số; danger chỉ khi vượt ngưỡng bắt buộc. |
| `match-hud` | Lớp neo chứa các module HUD, không có khung trang trí bao toàn màn. |
| `compass` | Vạch bearing, hướng chính và marker; số mono, tick nhẹ, marker team có shape riêng. |
| `squad-panel` | Tối đa bốn hàng: số thành viên, HP/state, voice; gục/chết khác nhau bằng icon và pattern. |
| `health-boost-bar` | HP là bar đặc có mốc; boost là bar mảnh khác chiều cao; low HP thêm icon/pulse có thể tắt. |
| `weapon-ammo-panel` | Ammo hiện tại nổi bật bằng `{typography.hud-critical}`, dự trữ nhỏ hơn; weapon mode và stance bằng icon + label. |
| `minimap-zone-panel` | Field chart ít texture, bo hiện tại/tiếp theo khác nét; không icon loot/địch. |
| `context-prompt` | Keycap + động từ + đối tượng, một dòng khi có thể; xuất hiện gần tâm dưới. |
| `damage-direction-indicator` | Cung 30° ngắn, không mũi tên tọa độ/độ xa; intensity không được giả thành damage number. |
| `reticle` | Bốn arm dài 8px, gap tâm 6px, stroke 2px + outline tối 1px ở 100% UI scale; preset chỉ đổi line/hit token. Hit confirm là corner burst ngắn theo server confirmation; không lead marker, snap, range hoặc enemy highlight. Scope reticle dùng asset vũ khí nhưng vẫn tuân dual-contrast và Reduce Flash. |
| `context-action-card` | Icon, tên hành động và progress; healing/revive/vehicle/throwable dùng anatomy chung nhưng icon khác. |
| `inventory-panel` | Hai panel bán trong, đường chia mảnh; thế giới trung tâm vẫn lộ. |
| `item-row` | Icon/hình hộp + tên + số lượng + khối lượng; ammo/rank không chỉ mã hóa bằng màu. |
| `equipment-slot` | Silhouette slot rõ; armor/helmet có label cấp, durability bar, số current/max và broken icon/crosshatch ở 0. Trên 50% dùng neutral, 1–50% dùng attention + notch, 0 dùng danger + BROKEN; attachment nằm sát weapon; empty có outline/nhãn. |
| `map-marker-layer` | Địa danh, flight path, current-zone solid và next-zone dashed chỉ khi được lộ; teammate 1–4 dùng Circle/1, Square/2, Triangle/3, Diamond/4 trên map/compass/world. Màu preset đổi nhưng shape/số giữ nguyên. |
| `party-panel` | Danh sách 1–4 người; identity cố định Circle/1, Square/2, Triangle/3, Diamond/4 khớp mọi marker; leader/ready/network/voice bằng icon + nhãn, không avatar skin lớn. |
| `voice-ping-indicator` | Icon speaker/mute/ping nhỏ; active có `{colors.signal-zone}` và chuyển động nhẹ có reduced-motion fallback. |
| `progress-timer` | Vòng/đường progress + số mono; interrupted chuyển icon và nhãn, không chỉ đổi đỏ. |
| `results-table` | Bảng số liệu thẳng hàng mono; placement và survival time ưu tiên hơn mỹ phẩm. |
| `settings-control` | Hàng label + value/control; slider có số hiện tại, toggle có text On/Off hoặc Bật/Tắt. |
| `subtitle-line` | Speaker label, tối đa hai dòng, backplate ≥92%, max width 60% central frame; collision reflow theo Lane C, không che reticle/prompt/progress/HP/ammo. |
| `safe-area-root` | Container gốc áp OS safe inset + 8px content inset; mọi critical control nằm trong boundary, debug build có outline để chụp kiểm tra notch/cutout. |
| `touch-stick` | Base 96px, thumb 48px, contrast kép và opacity vừa đủ đọc địa hình; neutral/pressed/dragged state rõ nhưng không animation đàn hồi. |
| `touch-look-zone` | Vùng trong suốt tối thiểu 40% chiều ngang bên phải; chỉ debug mới hiện viền, production không phủ scrim hoặc texture làm giảm tầm nhìn. |
| `touch-action-button` | Target thường tối thiểu 48 logical units; fire/exit/close tối thiểu 64 khi safe area cho phép; icon + label ngắn, pressed state bằng viền/opacity chứ không flash. |
| `control-layout-editor` | Grid 8px, handle tối thiểu 48px, boundary/overlap invalid bằng viền + label; luôn có Apply/Cancel/Reset và preview safe-area/device class. |

[ASSUMPTION: UX-032] `minimap-zone-panel` anatomy: map square; player heading ở tâm; teammate shape/number; current safe-zone line solid; next-zone line dashed chỉ sau server reveal; ngoài bo dùng hatch hướng vào trong; phase chip gồm `Pha N`, trạng thái `Chờ/Đang thu` và timer mono. Phase đổi bằng line motion + label, không flash toàn panel. Panel không có loot, enemy, sound source hoặc prediction.

[ASSUMPTION: UX-038/UX-040] Mobile landscape có ba lớp inset: OS safe area → `safe-area-root` → reach/layout groups. Phone 20:9, phone 16:9 và tablet 4:3 đều giữ reticle ở tâm live world; notch/camera island không được đẩy lệch aim center. Touch control opacity không thấp hơn mức vẫn nhận biết trên cảnh sáng/sương và không tạo vùng che liên tục quanh reticle.

### Motion & flash budget

[ASSUMPTION: UX-035] Budget này là floor v1.0; test photosensitivity chuyên môn có thể siết chặt hơn nhưng không được nới rộng nếu chưa review lại.

- HUD enter/exit: 120–180ms; contextual fade-out ≤120ms; translation ≤12px; không overshoot, bounce, parallax hoặc camera-linked UI drift.
- Một thời điểm chỉ một element HUD được pulse; pulse ≤1,5Hz và tối đa hai chu kỳ cho một event. Không strobe hoặc oscillation vô hạn.
- UI không dùng full-screen white flash. Critical flash chiếm ≤10% central frame và không vượt 3 lần/giây; victory transition chỉ một sweep ≤300ms sau server confirmation.
- Reduce Motion đặt translation về 0 và dùng opacity/state swap ≤100ms. Reduce Flash thay mọi pulse/flash bằng icon + steady backplate; timing gameplay không đổi.
- Hit/reticle confirmation giữ cùng thời lượng giữa preset thường và ba preset mù màu; accessibility không kéo dài cue thành radar lịch sử.

## Do's and Don'ts

| Làm | Không làm |
|---|---|
| Giữ thông tin chiến đấu ở vị trí ổn định, dùng progressive disclosure cho ngữ cảnh. | Kill-feed toàn cục dày, damage number, footstep radar hoặc enemy detection. |
| Dùng màu + icon + shape + label cho mọi trạng thái quan trọng. | Dùng rarity, ammo, team hoặc danger chỉ bằng hue. |
| Giữ thế giới đọc được khi mở kho; giữ audio đầy đủ khi mở map. | Inventory che toàn màn hoặc map làm người chơi an toàn giả tạo. |
| Dùng animation ngắn, có mục đích, tôn trọng Reduce Motion/Flash. | Confetti, loot glow, reward loop hoặc motion live-service. |
| Dùng anchors/containers và safe frame cạnh tranh. | Cho ultrawide thêm HUD data hay đẩy module chiến thuật quá xa tâm. |
| Giữ mọi touch control trong safe area, theo reach zone và cho phép chỉnh bố cục. | Đặt nút bắn/thoát/đóng sát notch, dưới system gesture hoặc chồng reticle. |
| Giữ cùng lượng thông tin giữa Touch và Keyboard/Mouse. | Thêm visual footstep, enemy cue, auto-fire hoặc loot recommendation riêng cho mobile. |
| Giữ `reticle` dual-stroke và chỉ phản ánh trạng thái aim/hit hợp lệ. | Lead indicator, snap cue, range-to-enemy hoặc reticle đổi vì có địch sau cover. |
| Giữ geometry/timing y hệt giữa preset mù màu. | Dùng preset để tăng kích thước, thời lượng hoặc phạm vi phát hiện. |
| Giữ menu nông, không storefront/news/reward rail. | Badge đỏ, streak, countdown reward, battle pass hay CTA thương mại. |

### Chỉ mục giả định áp dụng

| ID | Áp dụng tại |
|---|---|
| UX-004 | Brand & Style; phạm vi desktop–mobile, Việt/Anh và font coverage |
| UX-005 | Brand & Style; Field Instrument |
| UX-006 | Layout & Spacing; bố cục HUD |
| UX-007 | Layout & Spacing; Inventory |
| UX-008 | Thuộc `EXPERIENCE.md` — IA menu |
| UX-009 | Thuộc `EXPERIENCE.md` — Map |
| UX-010 | Colors |
| UX-011 | Layout & Spacing; responsive |
| UX-012 | Colors; contrast và redundancy |
| UX-013 | Thuộc `EXPERIENCE.md` — Key Flows |
| UX-014 | Layout & Spacing; bốn desktop mockup đã promote và được distill |
| UX-021 | Typography; Layout & Spacing; central safe frame và breakpoint |
| UX-022 | Colors; contrast sau compositing và map boundary |
| UX-023 | Layout & Spacing; overlay lane/collision |
| UX-024 | Layout & Spacing; live-world ultrawide fairness |
| UX-025 | Colors; `reticle`; teammate marker identity |
| UX-032 | `minimap-zone-panel` anatomy và reveal styling |
| UX-033 | `equipment-slot`; vehicle/context visual states |
| UX-035 | Motion & flash budget |
| UX-037 | Layout & Spacing; coverage bốn desktop reference đã đóng |
| UX-038 | Layout & Spacing; phạm vi five-platform và landscape Touch |
| UX-039 | Thuộc `EXPERIENCE.md` — semantic input family và pool disclosure |
| UX-040 | Components; safe area, touch controls và reach zones |
| UX-041 | Layout & Spacing; mobile Match HUD |
| UX-042 | Layout & Spacing; mobile Inventory/Map |
| UX-043 | Thuộc `EXPERIENCE.md` — mobile lifecycle và permission |
| UX-044 | Components/Motion; Gyro, haptic, audio interruption và accessibility mobile |
| UX-045 | Layout & Spacing; đúng hai mobile delta reference |
