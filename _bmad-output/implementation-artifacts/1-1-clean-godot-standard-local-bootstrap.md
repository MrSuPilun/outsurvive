---
baseline_commit: NO_VCS
---

# Story 1.1: Clean Godot Standard local bootstrap

Status: done

## Story

As a developer,  
I want một dự án Godot sạch có thể khởi động cục bộ,  
so that capability đầu tiên được xây trên baseline tái tạo được.

## Outcome và ranh giới

- **Delivery Type:** Enabler.
- **Sizing:** S — tối đa 3 ngày làm việc.
- **Source Requirements:** FR13; NFR31, NFR49; Architecture clean-project decision.
- **Depends on:** Không.
- **Blocks:** Story 1.2–1.8.
- **Phạm vi nền tảng của Story:** local editor và Linux headless import.
- **Kết quả duy nhất:** một Godot Standard bootstrap tối thiểu có thể import, chạy, tự kiểm tra và đóng sạch.

Story này không tạo gameplay, backend, network, module dependency scanner, CI, SBOM, export matrix, asset pipeline, Theme/presenter production hoặc localization. Các capability đó thuộc Story 1.2–1.8.

## Acceptance Criteria

### AC1 — Engine preflight fail-closed

**Given** một Godot binary được chọn qua `GODOT_BIN` hoặc `PATH`  
**When** preflight chạy trước lần import đầu tiên  
**Then** binary phải báo structured version tương ứng `major=4`, `minor=7`, `patch=1`, `status=stable`, official Standard build  
**And** binary thiếu hoặc version/build không khớp phải trả exit code khác `0` trước import  
**And** export template đã được chọn/phát hiện phải cùng `4.7.1-stable`; template chưa cài được báo `not_applicable` cho Story không export này, không được ghi thành evidence đã pass  
**And** không được ghi evidence “pass” hoặc artifact hợp lệ giả.

### AC2 — Clean project boot

**Given** repository chưa có project gameplay  
**When** scaffold được tạo và chạy bằng Godot Standard `4.7.1-stable`  
**Then** typed GDScript project phải mở main scene `BootRoot` và chuyển lifecycle hợp lệ `BOOTING → READY`  
**And** diagnostic surface phải hiển thị `build_id`, engine version và lifecycle state  
**And** bootstrap không cần backend, network live, addon, starter kit, framework gameplay bên thứ ba hoặc MCP.

### AC3 — Clean shutdown

**Given** bootstrap đang ở `READY`  
**When** smoke mode hoặc yêu cầu đóng ứng dụng được xử lý  
**Then** lifecycle phải chuyển `READY → SHUTTING_DOWN`, ghi structured shutdown event và gọi `SceneTree.quit(0)`  
**And** transition sai phải trả typed failure; không chỉ log rồi tiếp tục  
**And** headless smoke phải trả exit code `0`, còn mọi failure phải trả code `1..125`.

### AC4 — Reproducible local/headless baseline

**Given** source sạch không chứa `.godot/` hoặc generated import cache  
**When** import, bootstrap unit smoke và main-scene launch/quit được chạy lại  
**Then** import phải hoàn tất không warning/error; unit và main-scene smoke phải assert hoặc emit cùng ba diagnostic field  
**And** không import hoặc tham chiếu file nào từ `prepare-asset/`  
**And** Linux phải chạy lại import + smoke tương đương trước khi Story được đánh dấu `done`.

### Definition of Done

Từ clean checkout/worktree, preflight chọn đúng Godot Standard 4.7.1 official build; headless import, bootstrap test runner và main-scene smoke đều trả `0`; local main project đạt `READY` rồi đóng qua `SHUTTING_DOWN`; negative preflight trả non-zero; Linux headless evidence tồn tại; không có cache, asset quarantine hoặc dependency ngoài phạm vi trong source.

Checksum reconciliation: Story 1.1 ghi digest quan sát và xác minh official engine version/commit. Trusted dependency/checksum manifest bền vững thuộc Story 1.3; Story 1.1 không được bịa checksum chuẩn hoặc tuyên bố đã hoàn thành dependency lock. Nếu `GODOT_SHA256` được cung cấp từ một nguồn tin cậy, preflight phải so sánh và fail khi lệch.

## Tasks / Subtasks

- [x] 1. Chạy preflight môi trường trước khi tạo/import project (AC: 1)
  - [x] Đặt `GODOT_BIN`; trên máy hiện tại dùng `/Applications/Godot.app/Contents/MacOS/Godot` vì `godot` chưa nằm trong `PATH`.
  - [x] Xác nhận `"$GODOT_BIN" --version` trả `4.7.1.stable.official.a13da4feb`.
  - [x] Xác nhận đây là Standard build, không có Mono/.NET feature; nếu export template đã cài, từ chối version khác `4.7.1-stable`.
  - [x] Ghi SHA-256 của binary/archive làm evidence quan sát; nếu có trusted `GODOT_SHA256`, so sánh fail-closed. Không gọi digest tự tính là dependency lock của Story 1.3.
  - [x] Tạo preflight tối thiểu trả non-zero khi binary/version sai. Không xây SBOM, upgrade ADR hoặc CI.

- [x] 2. Tạo Godot Standard project tối thiểu (AC: 2, 4)
  - [x] Tạo `game/project.godot` bằng Godot Standard 4.7.1; `res://` phải là thư mục `game/`.
  - [x] Khai báo rõ main scene `res://scenes/boot/boot_root.tscn`.
  - [x] Khai báo desktop renderer `forward_plus`, mobile override `mobile`; không đổi Compatibility để né lỗi.
  - [x] Bật typed-GDScript warning cho untyped declaration ở mức Error.
  - [x] Thêm `game/.gitignore` cho `.godot/` và generated translation cache; không thêm repository policy hoặc Git LFS workflow của Story 1.2/1.3.

- [x] 3. Tạo bootstrap kernel tối thiểu (AC: 1–3)
  - [x] Tạo typed `OperationResult` cho success/failure và mã lỗi `BOOT_*`.
  - [x] Tạo `BuildInfo` facade đọc `build_id`, expected engine version và structured `Engine.get_version_info()`.
  - [x] Tạo `AppKernel` với guarded states `BOOTING`, `READY`, `SHUTTING_DOWN`; không dùng nhóm boolean, service locator hoặc `*Manager`.
  - [x] Tạo `GameLog` structured JSON tối thiểu; direct `print()` chỉ được nằm bên trong logger.
  - [x] Autoload chỉ `BuildInfo` và `AppKernel`; `GameLog`/`OperationResult` là typed classes, không thêm `PlatformGateway` trước consumer.

- [x] 4. Tạo diagnostic smoke scene (AC: 2, 3)
  - [x] Tạo `BootRoot` bằng primitive Godot `Control`/`Label`, không asset ngoài, Theme production hoặc font tùy biến.
  - [x] Hiển thị đúng `build_id`, structured engine version và lifecycle state từ bootstrap state.
  - [x] Đánh dấu text là developer diagnostics, không phải player-facing localization contract.
  - [x] Đọc `OS.get_cmdline_user_args()`; chỉ tự chạy/thoát smoke khi nhận `--bootstrap-smoke` sau engine delimiter `--`.
  - [x] Đặt `SceneTree.auto_accept_quit = false` trước khi xử lý `NOTIFICATION_WM_CLOSE_REQUEST`; route manual close qua cùng shutdown transition.

- [x] 5. Tạo zero-dependency test baseline (AC: 1–4)
  - [x] Tạo GDScript test runner nguyên bản `extends SceneTree`; không thêm GUT hoặc framework test bên thứ ba.
  - [x] Kiểm tra project config/main scene, `build_id`, engine fields, lifecycle transition graph, BootRoot instantiate, diagnostic fields và exit code.
  - [x] Kiểm tra runtime không có Mono/.NET feature; không cần export template để chạy local/headless import.
  - [x] Expected-rejection fixtures cho thiếu/invalid build ID và lifecycle transition bất hợp lệ phải assert rejection nhưng vẫn để test runner trả `0`; negative preflight subprocess với engine/version/checksum sai phải trả non-zero.
  - [x] Chứng minh test không cần renderer thật, socket, backend, platform SDK, addon hoặc `prepare-asset/`.

- [x] 6. Thu evidence và chỉ đóng Story khi không còn “pass giả” (AC: 1–4)
  - [x] Chạy clean headless import.
  - [x] Chạy bootstrap unit smoke và main-scene smoke.
  - [x] Chạy local editor launch/quit thủ công.
  - [x] Chạy static scan cho direct `print()` và dependency ngoài phạm vi.
  - [x] Chạy lại import/smoke trên Linux headless.
  - [x] Workspace hiện chưa có `.git`; coding có thể bắt đầu, nhưng không đánh dấu AC “clean checkout” đạt cho tới khi có clean checkout/worktree evidence thực.

### Review Findings

- [x] [Review][Patch] Subshell exit flaw in shell script helper functions [`game/tools/bootstrap/verify_local_bootstrap.sh`]
- [x] [Review][Patch] GODOT_BIN path resolution when provided as relative command name [`game/tools/bootstrap/verify_local_bootstrap.sh:79`]
- [x] [Review][Patch] Window close request lockup during non-READY states [`game/src/client/bootstrap/app_kernel.gd:18-20`]
- [x] [Review][Patch] request_shutdown crash if AppKernel is unparented [`game/src/client/bootstrap/app_kernel.gd:64`]
- [x] [Review][Patch] start_bootstrap() failure in _ready() does not prevent downstream node execution [`game/src/client/bootstrap/app_kernel.gd:13-16`]
- [x] [Review][Patch] Hexadecimal case sensitivity bug in commit hash verification [`game/tools/bootstrap/verify_local_bootstrap.sh:98`]
- [x] [Review][Patch] Non-ISO-8601 UTC timestamp formatting in GameLog [`game/src/shared/diagnostics/game_log.gd:18`]
- [x] [Review][Patch] Incomplete .gitignore rules [`game/.gitignore`]



## Dev Notes

### Current workspace facts

- Chưa có thư mục `game/`; tất cả implementation file của Story là **NEW**.
- Godot không nằm trong `PATH`, nhưng binary đã được xác minh tại `/Applications/Godot.app/Contents/MacOS/Godot`.
- Binary hiện tại báo `4.7.1.stable.official.a13da4feb`, đúng baseline đã khóa.
- Chưa phát hiện export template cục bộ; điều này không chặn project import/smoke và không được mô tả là template evidence đã pass.
- Git `2.55.0` tồn tại nhưng workspace chưa có `.git`; không có previous Story hoặc Git history để tái sử dụng.
- `prepare-asset/` chứa nội dung quarantine và không được Godot scan/import trong Story này.

### Proposed file structure

```text
game/
├── .gitignore
├── project.godot
├── scenes/
│   └── boot/
│       └── boot_root.tscn
├── src/
│   ├── shared/
│   │   ├── kernel/
│   │   │   ├── operation_result.gd
│   │   │   └── build_info.gd
│   │   └── diagnostics/
│   │       └── game_log.gd
│   └── client/
│       └── bootstrap/
│           ├── app_kernel.gd
│           └── boot_root.gd
├── tests/
│   └── unit/
│       └── client/
│           └── test_bootstrap.gd
└── tools/
    └── bootstrap/
        └── verify_local_bootstrap.sh
```

Do not create the rest of the architecture tree as empty placeholders. Story 1.2 creates repository/module boundaries when consumers exist.

### Bootstrap contracts

#### `BuildInfo`

- Use one typed facade for project build metadata.
- Store a non-empty local default such as `local-dev`; do not derive network/content compatibility fields before their owner Story.
- Use exact keys `outsurvive/build/build_id` and `outsurvive/build/expected_engine_version`; do not let each caller invent its own key.
- Compare structured version fields from `Engine.get_version_info()` rather than a display string alone.
- `build="official"` and upstream commit hash may be evidence; neither replaces a platform archive checksum.

#### `AppKernel`

- Own only local application bootstrap lifecycle.
- Allowed transitions: `BOOTING → READY → SHUTTING_DOWN`.
- Any invalid transition returns `OperationResult.failure(&"BOOT_TRANSITION_REJECTED", context)`.
- It must not initialize account, platform, network, content manifest, gameplay simulation or live service.
- Set `SceneTree.auto_accept_quit = false` during bootstrap, handle `NOTIFICATION_WM_CLOSE_REQUEST`, then perform the guarded shutdown and explicit `quit(0)`.
- Keep the path extensible for later architecture lifecycle without implementing future states now.

#### `GameLog`

- Emit one JSON object per event with at least `timestamp_utc`, `level`, `service`, `subsystem`, `event`, `build_id` and `fields`.
- Event names are past-tense `snake_case`, for example `application_booted` and `application_shutdown_started`.
- No token, secret, PII, raw voice or per-frame log.
- `print()`/`printerr()` outside this bootstrap logger is forbidden.

### Project configuration guardrails

- Use Godot Standard, typed GDScript and Jolt built-in baseline; no C#, GDExtension or native module.
- Explicitly set desktop Forward+ and mobile Mobile rendering baselines.
- Set the main scene, project name and local build ID explicitly.
- Do not hard-code a guessed `config_version`; let Godot 4.7.1 create/save `project.godot`.
- In Godot 4.7, new-project stretch defaults changed; set diagnostic layout intentionally if it relies on stretch behavior.
- Never check `OS.has_feature("headless")`; `headless` is a launch mode, not a documented default feature tag.
- Do not invent engine flags. User arguments must follow `--` and be read through `OS.get_cmdline_user_args()`.

### Architecture compliance

- `SceneTree`/Node own composition and local lifecycle only; no authoritative gameplay state exists yet.
- Use direct typed calls for owned commands and local signals only for notifications; no global string event bus.
- Autoload is limited to actual application-lifetime owners. Do not use `get_node("/root/...")` or introduce a service locator.
- Expected errors use typed results. Engine/config mismatch is process-fatal and fail-closed.
- File/folder names are ASCII `snake_case`; class/enum names `PascalCase`; functions/variables `snake_case`; constants `UPPER_SNAKE_CASE`.
- No `load()` by arbitrary path, network identity, backend SDK, platform SDK or runtime asset dependency is needed.

### UX applicability

`BootRoot` is a developer-only diagnostic surface. Production brand treatment, responsive matrix, safe-area work, accessibility components, Noto fonts, Theme/presenter and `StringId`/Việt–Anh localization belong to Story 1.7–1.8. A plain readable Label is sufficient and avoids false UX scope.

### Explicitly out of scope

- Repository dependency scanner or full monorepo scaffolding — Story 1.2.
- Dependency lock, approved checksum manifest, SBOM and upgrade ADR — Story 1.3.
- CI and reproducible canonical artifact — Story 1.4.
- Export presets, five-platform artifacts and signing — Story 1.5.
- Asset provenance/promotion/import — Story 1.6.
- Theme, presenter, accessibility primitives and localization — Story 1.7–1.8.
- Character, animation, input, gameplay, network, backend, HUD or product UI — later Stories.

### Verification commands

```bash
export GODOT_BIN=/Applications/Godot.app/Contents/MacOS/Godot
"$GODOT_BIN" --version
shasum -a 256 "$GODOT_BIN"

game/tools/bootstrap/verify_local_bootstrap.sh
"$GODOT_BIN" --headless --path game --import
"$GODOT_BIN" --headless --path game --script res://tests/unit/client/test_bootstrap.gd
"$GODOT_BIN" --headless --path game -- --bootstrap-smoke
"$GODOT_BIN" --path game
"$GODOT_BIN" --editor --path game  # optional editor-open check

rg -n '\b(print|printerr)\s*\(' game/src game/tests
rg -n 'prepare-asset|addons/|MultiplayerAPI|HTTPRequest|Nakama|EOS' \
  game/project.godot game/src game/scenes game/tests
```

Expected:

- preflight, import, unit smoke and main-scene smoke return `0`;
- expected-rejection fixtures pass inside the unit runner; separate negative preflight invocations return non-zero;
- direct `print()` appears only in `game_log.gd`;
- no addon/backend/network/provider/quarantine dependency is present;
- manual main-project launch reaches `READY` and closes through `SHUTTING_DOWN`; editor-open is a separate optional check.

Run the same preflight/import/smoke commands with a Linux Godot Standard 4.7.1 binary before `done`.

### Testing requirements

- Unit/smoke tests must run headless without rendering, socket or live service.
- A failure must call `SceneTree.quit(code)` with a non-zero code; `push_error()` alone is not a test failure contract.
- Test exact allowed/forbidden lifecycle transitions.
- Instantiate `BootRoot` from the configured main scene, not a duplicate test scene.
- Test both missing and malformed build configuration.
- Headless import creates `.godot/`; prove it is ignored and absent from source evidence.
- Do not mark the Story complete using only macOS evidence; Linux headless import is part of its declared applicability.

## Project Context Rules

- Engine remains Godot Engine Standard `4.7.1-stable`; no automatic upgrade/downgrade.
- Build/test must work without GoPeak or Context7.
- Do not add manager singletons, global event bus, raw `print()`, arbitrary asset loading, platform SDK or client authority.
- Keep `prepare-asset/` quarantined and outside the Godot project.
- Logging must be structured; failures must be typed and fail-closed.
- Do not change Architecture or relax acceptance thresholds to make a failing implementation appear complete.

## Latest Godot 4.7.1 specifics

- `--import` is the dedicated editor import command; it waits for import and quits. `--headless` selects headless display and Dummy audio drivers.
- `--path game` must point at the directory containing `project.godot`.
- Unknown engine arguments may be ignored without warning. Put `--bootstrap-smoke` after `--`.
- Read user arguments with `OS.get_cmdline_user_args()`.
- `SceneTree.quit(0)` is required for explicit success; use `1..125` for failures.
- `SceneTree.quit()` does not emit `NOTIFICATION_WM_CLOSE_REQUEST`; manual close needs its own handler.
- Godot 4.7.1 is the locked baseline even if a newer release exists; upgrades require the later ADR/parity workflow.

Official references:

- [Godot 4.7.1 release](https://godotengine.org/article/maintenance-release-godot-4-7-1/)
- [Godot 4.7.1 archive](https://godotengine.org/download/archive/4.7.1-stable/)
- [Command-line tutorial](https://docs.godotengine.org/en/4.7/tutorials/editor/command_line_tutorial.html)
- [`Engine.get_version_info()`](https://docs.godotengine.org/en/4.7/classes/class_engine.html#get-version-info)
- [`SceneTree.quit()`](https://docs.godotengine.org/en/4.7/classes/class_scenetree.html#class-scenetree-method-quit)
- [Handling quit requests](https://docs.godotengine.org/en/4.7/tutorials/inputs/handling_quit_requests.html)
- [GDScript static typing](https://docs.godotengine.org/en/4.7/tutorials/scripting/gdscript/static_typing.html)
- [Version-control ignores](https://docs.godotengine.org/en/4.7/tutorials/best_practices/version_control_systems.html)

## References

- [Source: `_bmad-output/planning-artifacts/epics.md` — Story 1.1 and Additional Requirements]
- [Source: `_bmad-output/game-architecture.md` — Engine & Framework, Cross-cutting Concerns, Project Structure, Development Environment]
- [Source: `_bmad-output/project-context.md` — Engine, organization, testing and prohibited-shortcut rules]
- [Source: `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md` — five-platform north-star]
- [Source: `_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/DESIGN.md` — Story 1.7–1.8 UX evidence ownership]
- [Source: `_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md` — no open Foundation product-decision gate]

## Dev Agent Record

### Agent Model Used

GPT-5 Codex

### Debug Log References

- Kế hoạch triển khai: thực hiện tuần tự từng task bằng RED–GREEN–REFACTOR; preflight shell trước import, project config, typed bootstrap contracts, diagnostic scene, native GDScript runner, rồi evidence macOS/Linux.
- Task 1 RED: `test_verify_local_bootstrap.sh` thất bại vì verifier chưa tồn tại (4 case success/evidence fail).
- Task 1 GREEN/REFACTOR: 9/9 preflight tests pass; binary local xác minh `4.7.1.stable.official.a13da4feb`, SHA-256 quan sát `ecc8da2d60100102cfca6e833d3860d7436b46ae062fa072ce89a6c95d664a3f`, export template `not_applicable`, trusted checksum không được cung cấp.
- Task 2 RED: 0/9 project-config assertions pass trước khi `project.godot` và `.gitignore` tồn tại.
- Task 2 GREEN/REFACTOR: Godot 4.7.1 tự ghi `config_version=5`; 9/9 config assertions và toàn bộ 9 preflight tests pass.
- Task 3 RED: GDScript runner báo thiếu toàn bộ bốn bootstrap contract trước implementation.
- Task 3 GREEN/REFACTOR: 20 kernel assertions pass; regression phát hiện Godot loại renderer default và đã được sửa để giữ explicit `forward_plus`/`mobile`; 13/13 project-config và 9/9 preflight tests pass.
- Task 4 RED: unit runner trả `1` vì configured `BootRoot` chưa tồn tại.
- Task 4 GREEN/REFACTOR: 29 assertions pass; headless main-scene smoke phát đủ `build_id`, structured engine version, `READY`, rồi `SHUTTING_DOWN` và trả `0`; full regression pass.
- Task 5 RED: 32/33 assertions pass; fixture bắt `build_id` sai kiểu đang bị phân loại nhầm thành `BOOT_BUILD_ID_MISSING`.
- Task 5 GREEN/REFACTOR: semantics sửa thành `BOOT_BUILD_ID_INVALID`; 33/33 GDScript assertions, 13/13 config tests, 9/9 preflight tests và main smoke pass. Hai vòng lặp xác minh renderer declarations ổn định sau class-cache import.
- Task 6 RED: verifier mặc định chấp nhận binary giả chỉ in version; regression mới thất bại 9 pass/1 fail như dự kiến.
- Task 6 GREEN/REFACTOR: verifier mặc định chạy config + import + unit + main smoke, từ chối missing diagnostic/warning/error và binary giả; 10/10 verifier tests pass.
- Evidence macOS: cache cũ được archive khỏi `game/`; clean import từ `.godot` absent trả `0` không warning/error. Full verifier pass với SHA-256 binary quan sát `ecc8da2d60100102cfca6e833d3860d7436b46ae062fa072ce89a6c95d664a3f`; export template `not_applicable`, trusted checksum không được cung cấp.
- Evidence GUI macOS: Metal/Forward+ launch đạt `READY`; native quit request phát diagnostic `trigger=window_close`, chuyển `SHUTTING_DOWN` và process trả `0`.
- Evidence static: direct `print()` chỉ có trong `game_log.gd`; không có `prepare-asset`, addon, MultiplayerAPI, HTTPRequest, Nakama, EOS, root service lookup hoặc `*Manager`.
- Evidence Linux x86_64: Debian container chạy official Standard `4.7.1-stable` artifact; full verifier pass import + 33 assertions + main smoke, SHA-256 quan sát `32f8d7596c4b41185512b1c49d69f2da3be018fd784a53e349fa92a98a97bcde`.
- HALT gate: workspace vẫn không có `.git` (`baseline_commit: NO_VCS`), nên không có clean checkout/worktree evidence; Task 6 và Story không được đánh dấu hoàn tất/review.
- Resume Task 6 RED: repository đã tồn tại nhưng worktree chính có thay đổi người dùng không liên quan `.DS_Store`, nên không được dùng làm clean-worktree evidence.
- Resume Task 6 GREEN: detached worktree sạch tại commit `311755b343278428796aeeae90e135b4d1d1b949` có status count `0` trước test; macOS clean import + 10/10 verifier tests + 13/13 config tests + 33 assertions + main smoke + static scan đều pass; status count sau test vẫn `0`.
- Resume Linux x86_64: tách `.godot` trước import, chạy lại official Standard `4.7.1-stable` trên chính detached worktree; verifier và smoke pass. Post-check trong container thiếu `git` bị phát hiện, không được dùng làm evidence; Git host trên cùng bind mount xác nhận commit `311755b343278428796aeeae90e135b4d1d1b949`, status count `0`, và `.godot` được ignore bởi `game/.gitignore`.
- Completion regression: không còn checkbox chưa hoàn tất; 10/10 verifier tests, 13/13 config tests, 33 GDScript assertions, import, main smoke và static checks đều pass sau khi cập nhật Task 6; File List bao phủ toàn bộ file dưới `game/`.

### Completion Notes List

- Ultimate context engine analysis completed — comprehensive developer guide created.
- Story context only; no gameplay/project code has been implemented in this workflow.
- Story is ready to enter `gds-dev-story`.
- Task 1 hoàn tất: preflight fail-closed xác minh exact official Standard build, checksum tùy chọn và version export template được chọn; negative fixtures đều trả non-zero.
- Task 2 hoàn tất: project root `game/` khai báo main scene, Forward+/Mobile renderer, strict untyped warning, build metadata và ignore cache tối thiểu.
- Task 3 hoàn tất: typed result, build facade, structured logger và guarded bootstrap lifecycle đã được triển khai; chỉ `BuildInfo`/`AppKernel` là Autoload.
- Task 4 hoàn tất: `BootRoot` developer diagnostics dùng primitive UI, smoke opt-in sau `--`, và window-close cùng đi qua guarded shutdown.
- Task 5 hoàn tất: zero-dependency SceneTree runner bao phủ config, Standard runtime, exact lifecycle graph, expected rejections, BootRoot integration và diagnostic parity; mọi failure path dùng process exit code.
- Task 6 đã đạt toàn bộ macOS/Linux runtime, GUI và static evidence; còn chặn duy nhất là clean checkout/worktree evidence do workspace không có Git repository.
- Task 6 hoàn tất: clean detached worktree evidence tại commit `311755b343278428796aeeae90e135b4d1d1b949` đạt trên macOS và Linux x86_64, trước/sau validation đều không có source change.
- Story 1.1 hoàn tất implementation và Definition of Done; trạng thái chuyển sang `review`.

### File List

- `_bmad-output/implementation-artifacts/1-1-clean-godot-standard-local-bootstrap.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`
- `game/tests/unit/tools/test_verify_local_bootstrap.sh`
- `game/tests/unit/tools/test_project_config.sh`
- `game/tests/unit/client/test_bootstrap.gd`
- `game/tests/unit/client/test_bootstrap.gd.uid`
- `game/tools/bootstrap/verify_local_bootstrap.sh`
- `game/.gitignore`
- `game/project.godot`
- `game/scenes/boot/boot_root.tscn`
- `game/src/client/bootstrap/app_kernel.gd`
- `game/src/client/bootstrap/app_kernel.gd.uid`
- `game/src/client/bootstrap/boot_root.gd`
- `game/src/client/bootstrap/boot_root.gd.uid`
- `game/src/shared/diagnostics/game_log.gd`
- `game/src/shared/diagnostics/game_log.gd.uid`
- `game/src/shared/kernel/build_info.gd`
- `game/src/shared/kernel/build_info.gd.uid`
- `game/src/shared/kernel/operation_result.gd`
- `game/src/shared/kernel/operation_result.gd.uid`

## Change Log

- 2026-07-26 — Tạo Godot Standard 4.7.1 bootstrap tối thiểu, fail-closed preflight, typed lifecycle/result, structured diagnostics, zero-dependency tests và clean macOS/Linux worktree evidence; chuyển Story sang `review`.
