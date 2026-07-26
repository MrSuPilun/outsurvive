---
project_name: 'outsurvive'
user_name: 'Project Owner'
date: '2026-07-23'
sections_completed: ['technology_stack', 'engine_rules', 'performance_rules', 'organization_rules', 'testing_rules', 'platform_rules', 'anti_patterns', 'usage_guidelines']
existing_patterns_found: 16
status: 'complete'
rule_count: 78
optimized_for_llm: true
---

# Project Context for AI Agents

_Tài liệu này chứa các quy tắc và pattern quan trọng mà AI agent phải tuân thủ khi triển khai mã game. Chỉ giữ những chi tiết dễ bị bỏ sót hoặc dễ bị suy diễn sai; Game Architecture vẫn là nguồn chuẩn đầy đủ._

---

## Technology Stack & Versions

| Layer | Baseline bắt buộc |
|---|---|
| Engine | Godot Engine Standard 4.7.1-stable, typed GDScript, Jolt Physics built-in |
| Client targets | Windows 10/11 x64, Linux x64, macOS 13+ Intel/Apple Silicon, Android 10+ ARM64, iOS 16+ ARM64 |
| Rendering | Forward+ trên desktop; Mobile renderer trên Android/iOS; Metal cho Apple, Vulkan cho Linux/Android, D3D12 cho Windows |
| Realtime networking | ENet/UDP transport với custom binary protocol, authoritative dedicated server 30 Hz |
| Terrain/world | Terrain3D 1.0.2 chỉ dùng trong editor; runtime đọc versioned `TerrainTileData` và baked world manifests |
| Control plane | Nakama 3.40.0, Nakama Common 1.47.0, Nakama Godot SDK 3.4.0 sau adapter/contract test |
| Persistence | CockroachDB 26.2.3 cho production control-plane data; match state nằm trong RAM của dedicated server |
| Fleet | Agones 1.59.0 trên Kubernetes 1.35.6; một Linux headless process/pod cho mỗi trận |
| Backend tooling | Go 1.26.5 cho standalone tooling; OCI-compatible container runtime cho local integration |
| Voice | EOS Voice service sau five-platform spike; portal SDK artifact phải pin version/checksum trước khi promote |
| Optional MCP | GoPeak 2.3.9 và Context7 3.2.4 chỉ là development tooling, không thuộc runtime/build dependency |

- Không tự nâng engine, plugin, database, orchestrator hoặc native SDK. Mọi thay đổi version cần ADR, checksum/version manifest và compatibility gate tương ứng; nâng Godot bắt buộc five-platform smoke test.

## Critical Implementation Rules

### Engine-Specific Rules

- `SceneTree` và `Node` chỉ dùng cho composition, lifecycle cục bộ và presentation; authoritative gameplay state nằm trong typed simulation data, không nằm rải rác trong scene.
- Chỉ `AppKernel`, `BuildInfo`, `PlatformGateway` và service thực sự sống suốt ứng dụng mới được làm Autoload. Không tạo `*Manager` toàn cục để né dependency injection.
- Application và match lifecycle phải dùng guarded state machine; không biểu diễn trạng thái bằng nhiều boolean hoặc chuyển scene tùy ý.
- Chỉ dùng ba communication lane: direct typed call cho command có một owner; Godot signal past-tense `snake_case` cho notification local/presentation; deterministic domain-event queue cho simulation/evidence. Không dùng signal khi caller cần kết quả đồng bộ.
- Main thread sở hữu `SceneTree`, `Node` lifecycle và Jolt. Worker không giữ `Node` reference hoặc sửa scene; dữ liệu qua thread boundary phải immutable/ownership-transfer, kết quả async cần generation/cancellation ID.
- Replicated entity chỉ được tạo qua factory; không replicate nguyên SceneTree, `NodePath`, RPC name hoặc scene instance ID.
- Authoritative simulation chạy qua fixed 30 Hz phase scheduler; không thêm `_physics_process()` riêng lẻ cho gameplay system.
- Không giả định Jolt deterministic giữa client và server. Character dùng custom kinematic motor; projectile không dùng một `RigidBody3D` cho mỗi viên.
- Custom Resource chỉ là authoring input; runtime gameplay đọc manifest đã validate/bake. Generated terrain, world và protocol files là read-only.
- UI nhận immutable `ViewState` từ presenter; widget không đọc packet hoặc authoritative entity trực tiếp.
- Mọi player-facing string dùng `StringId` + typed args và immutable Việt/Anh `LocaleCatalog`; English fallback. Domain không phát display string, missing key không được trở thành chuỗi rỗng.

### Performance Rules

- Desktop minimum: 60 FPS median, p95 frame time ≤25 ms ở 1080p/Low; recommended: 90 FPS median, p95 ≤16,7 ms ở 1080p/High.
- Mobile minimum class phải đạt 45 FPS median, p95 ≤33,3 ms ở Low; recommended class phải đạt 60 FPS median, p95 ≤25 ms ở Medium.
- Mobile working memory ≤3 GB; không bị OS terminate trong trận 45 phút; FPS median không giảm quá 15% sau 30 phút thermal soak.
- Dedicated server phải giữ simulation 30 Hz cho 100 người với ≥10% headroom; damage xử lý trong ≤1 tick p95; mục tiêu envelope ≤8 vCPU/16 GB mỗi trận.
- Băng thông trung bình không vượt 1,5 Mbps mỗi chiều/client; snapshot phải dùng relevance, delta và update tiers, không replicate toàn bộ scene.
- Preload combat-critical assets trước trận. World cell dùng threaded loading, bounded cache và main-thread instantiation budget.
- Không unload cell khi còn projectile, vehicle, door transition hoặc gameplay reference chưa giải quyết.
- Chỉ pool VFX, casing, impact và UI marker khi có `reset_for_reuse()`. Không pool object mang authoritative identity nếu reset chưa được chứng minh.
- Không ghi log mỗi frame/tick trong hot path; dùng aggregated metrics cho tick time, relevance count, snapshot bytes, correction, hitch, memory và thermal.
- Mọi thay đổi renderer, LOD hoặc dynamic resolution phải giữ nguyên collision, cover, silhouette, opening và thông tin gameplay.
- Scale theo chuỗi 8 → 24 → 50 → 100 protocol-mixed clients; không khóa bản đồ/art production trước khi vượt world-streaming, final-circle và mobile-soak gates.
- Nếu 100 người hoặc bản đồ 8×8 km không đạt budget, giữ quy mô ở mức đã chứng minh; không bù bằng client authority, hidden bot hoặc giảm gameplay parity.

### Code Organization Rules

- Tuân thủ domain-driven monorepo: `game/src/shared` giữ contracts/simulation/protocol/world/data; `client` giữ input/prediction/presentation/streaming/UI/audio; `server` giữ authority/relevance/lag compensation/evidence; platform/provider code nằm trong `game/src/platform` hoặc `native`.
- Dependency chỉ đi vào shared ports/contracts/simulation; `shared` không import client, server, platform SDK hoặc backend. Backend chỉ chia sẻ generated contracts với Godot.
- Đặt code theo domain sở hữu; không tạo `utils`, `helpers`, `common` hoặc manager chung thiếu boundary rõ.
- Tất cả file/folder dùng ASCII `snake_case`, không khoảng trắng. GDScript `.gd`, scene `.tscn`, Resource `.tres`, test `test_*.gd`.
- Class/enum dùng `PascalCase`; function/variable dùng `snake_case`; private member `_snake_case`; constant `UPPER_SNAKE_CASE`.
- Command kết thúc bằng `Command`; domain event dùng quá khứ; port kết thúc bằng `Port`; implementation theo provider/platform kết thúc bằng `Adapter`.
- Gameplay/network identity dùng stable ID như `weapon.ar_556_01`; không dùng path, `NodePath`, instance ID hoặc display name.
- Generated file phải có `generated_do_not_edit`; chỉnh source schema rồi regenerate, không sửa generated output bằng tay.
- Asset 3D dùng mét; LOD là `lod00`, `lod01`, `lod02`. Collision/gameplay shell không có hậu tố platform; visual variant mới dùng `_desktop`/`_mobile`.
- Asset ngoài dự án bắt buộc có license/provenance. `prepare-asset/` là quarantine; không import trực tiếp hoặc đưa `_unresolved` vào manifest.
- Native/GDExtension chỉ nằm trong `native/` và chỉ được thêm sau profiling, ADR cùng five-platform parity gate.

### Testing Rules

- Test nằm trong `game/tests/{unit,integration,deterministic,fixtures,golden}`; load, replay, impairment, map và device testing nằm trong `test-harness/`.
- Shared simulation unit test không cần renderer, UI, platform SDK, network socket hoặc live backend.
- Deterministic test dùng fixed server tick, match seed và purpose-specific RNG stream; so sánh state hash hoặc golden result.
- Protocol codec cần golden byte fixtures, round-trip tests và fuzz malformed/untrusted packets theo chuỗi `decode → validate → apply`.
- Thay đổi fixed-tick phase order, protocol schema, content manifest hoặc stable ID cần deterministic regression test và compatibility decision.
- Mọi bug hit registration, desync hoặc kết quả trận phải có evidence/replay fixture tái hiện lỗi trước khi sửa.
- Backend command test phải chứng minh idempotency: cùng `command_id` trả cùng kết quả; cùng ID nhưng payload khác là security error.
- Map bake CI chạy route, connectivity, sightline, terrain seam, water, collision, visibility và cell-budget validators trước khi ký manifest.
- World schema mở rộng theo consumer: Story terrain không được tạo trước POI/road/building/weather fields; mỗi extension cần version/migration/validator/hash parity.
- Desktop/mobile visual variants cần automated parity test cho collision, cover, openings, silhouette và line of sight.
- Network tests bao gồm latency, jitter, packet loss, burst loss, reconnect và Wi-Fi↔cellular handoff; scale theo 8→24→50→100 clients.
- Mobile gate chạy trên Android/iOS minimum và recommended devices, không chỉ simulator; kiểm tra safe area, interruption, memory, thermal, Touch ownership và Gyro.
- Build/test phải chạy được khi không cài GoPeak hoặc Context7.
- Static checks chặn direct `print()`, platform SDK ngoài adapter, arbitrary asset path, generated-file edits, entity spawn ngoài factory và client authority.
- Không nới acceptance threshold hoặc bỏ qua flaky/failing gate để merge; thay đổi budget cần bằng chứng profiling và ADR.

### Platform & Build Rules

- V1 bắt buộc hỗ trợ Windows x64, Linux x64, macOS Universal 2, Android ARM64 và iOS ARM64; Linux headless server là artifact độc lập.
- Gameplay chỉ nhận semantic `GameplayCommand`; chỉ input adapter được đọc raw keyboard, mouse, Touch hoặc Gyro.
- Gameplay binding dùng physical key identity; text entry dùng logical/Unicode. Desktop aim dùng captured unaccumulated relative mouse delta; localized OS label không làm command identity.
- Không tạo desktop/mobile gameplay branch. Platform chỉ khác presentation quality, layout, lifecycle và adapter; combat, collision, visibility và content manifest phải giống nhau.
- Renderer baseline: Windows Forward+/D3D12, Linux Forward+/Vulkan, macOS Forward+/Metal, Android Mobile/Vulkan, iOS Mobile/Metal.
- Platform SDK chỉ được gọi qua typed ports/adapters cho identity, entitlement, invite, voice permission, lifecycle, secure storage và build info.
- Adapter failure trả capability/state rõ; không âm thầm thay luật gameplay hoặc fallback sang provider khác.
- Input-family claim do backend ký và khóa suốt trận. Gắn keyboard/mouse trên mobile không tự đổi pool; mixed party phải disclosure trước ready.
- Mobile lifecycle xử lý `Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended`.
- Reconnect: party clear Ready ngay; queue/loading/pre-aircraft grace 60 giây; live sau aircraft grace 120 giây với neutral input + avatar vulnerable. Timeout live direct-eliminate/drop/defeat, không DBNO; connected-AFK chỉ telemetry, không protection/autopilot/kick.
- Chỉ cho client cùng trận khi `protocol_version`, `gameplay_schema_version` và `content_manifest_hash` tương thích chính xác.
- CI pin Godot editor/export-template version và checksum, tạo SBOM, rồi build/test cả năm client target cùng Linux headless server.
- Dependency/SBOM/CI/signing boundary phải tồn tại ở Story 1.3–1.5; container/observability ở Story 6.9–6.10, không chờ release Epic.
- macOS/iOS signing, notarization và TestFlight chạy trên isolated macOS runner. Android phát hành ARM64 AAB.
- Signing key, provisioning profile, store credential và production token không được vào repository, Resource, artifact log, prompt hoặc MCP.
- Plugin, GDExtension và native SDK mới chỉ được promote sau desktop, Android, iOS và macOS build/parity spike.
- Desktop-only anti-cheat/attestation chỉ là tín hiệu bổ sung; không tạo tiêu chuẩn công bằng mà mobile không thể đáp ứng.
- EOS Voice failure phải hiển thị degraded capability; không thay bằng ping tự phát hiện kẻ địch hoặc thay đổi gameplay information.
- Eliminated spectator được giữ team voice nhưng mọi world/context/Map ping hoặc tactical marker mới bị server từ chối.
- Player-facing audio chỉ có Master/World/Team Voice/UI/Music; Ambience/Footsteps/Weapons/Vehicles là child bus nội bộ dưới World, không expose tactical EQ/boost/night mode.
- Full Map north-up, minimap heading-up; zoom 0,75×–6× và bounded pan; platform không được đổi information extent.

### Critical Don't-Miss Rules

- Không tin client về movement validity, hit, damage, ammo, inventory, loot, vehicle collision, zone hoặc match result.
- Packet không tin cậy phải kiểm tra type, length, range, cadence, sequence, ownership và state transition trước khi mutate. Cấm `var_to_bytes()`/object deserialization cho network input.
- Client prediction chỉ dành cho state được phép; hit marker, damage và impact cạnh tranh phải chờ server confirmation.
- Không dùng RPC name, `NodePath`, scene instance ID hoặc file path làm protocol/gameplay identity.
- Gameplay time dùng `ServerTick`; timeout local dùng monotonic clock. Cấm wall-clock và global RNG trong simulation.
- Mỗi random stream có purpose ID riêng. Thêm VFX/audio không được làm thay đổi loot, vehicle, zone hoặc weather result.
- Lag compensation chỉ rewind bounded hitbox history tối đa 150 ms; không rewind toàn world.
- Match seed không sinh lại hình học runtime; địa hình, POI, đường và nhà là authored/baked content.
- Visual wave không quyết định water height, swimming hoặc buoyancy. Desktop/mobile dùng cùng `WaterVolume` gameplay.
- Remote config không đổi damage, recoil, loot odds, bo, input-pool policy hoặc số bot; chỉ được disable queue, region hoặc provider với trạng thái hiển thị rõ.
- Standard match không có bot, hero skill, hồi sinh, loadout ngoài trận, storefront, premium currency, battle pass hoặc live-event injection.
- Local file chỉ lưu setting/layout/token an toàn; không có authority với profile, progression hoặc match result.
- Lỗi dùng typed result; không nuốt lỗi hoặc chỉ log rồi tiếp tục mutation. Logging đi qua `GameLog`, không gọi `print()` trực tiếp.
- Không log raw voice, platform token, signing secret hoặc PII. Combat telemetry dùng account hash và retention policy.
- Không khóa 18 POI/420 công trình, native provider hoặc release v1 trước khi các network, mobile, streaming, parity, voice và certification gates tương ứng vượt chuẩn.

---

## Usage Guidelines

**Cho AI agent:**

- Đọc file này trước khi viết, sửa hoặc review game code; đọc [Game Architecture](./game-architecture.md) khi cần rationale, project tree hoặc pattern đầy đủ.
- Tuân thủ tất cả rule. Khi tài liệu chưa nói rõ, chọn phương án hạn chế authority/dependency hơn và không tự mở rộng scope.
- Không sửa rule để hợp thức hóa implementation. Nếu cần đổi boundary, version, budget hoặc pattern, cập nhật ADR/Architecture và validation trước hoặc cùng change.
- GDD/UX quyết định trải nghiệm; Architecture/project context quyết định implementation. Khi có xung đột chưa được phân xử, dừng mutation liên quan và báo rõ tài liệu cùng điều khoản xung đột.

**Cho con người:**

- Giữ file ngắn và chỉ chứa chi tiết agent dễ bỏ sót; không sao chép toàn bộ Architecture, GDD hoặc coding tutorial.
- Cập nhật cùng change khi engine/dependency, platform, budget, ADR hoặc implementation pattern thay đổi.
- Review sau mỗi architecture change và milestone validation; xóa rule lỗi thời hoặc đã được enforcement tự động bao phủ hoàn toàn.

Last Updated: 2026-07-26
