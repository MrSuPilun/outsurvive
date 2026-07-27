---
baseline_commit: 4746491d6da714d153185a4c72f2b8cad172d498
---

# Story 1.2: Repository và module dependency boundaries

Status: review

## Story

As a developer,  
I want boundary monorepo được kiểm tra tự động,  
so that gameplay core không bị khóa vào client, platform hoặc backend.

## Outcome và ranh giới

- **Delivery Type:** Enabler — consumer đầu tiên là Story 1.13 `GameplayCommand`.
- **Sizing:** S — tối đa 3 ngày làm việc.
- **Source Requirements:** NFR31, NFR55; Architecture domain-driven monorepo.
- **Depends on:** Story 1.1 — hiện đã `done`.
- **Blocks:** Story 1.6–1.7, Story 1.13, mọi shared-simulation Story; Story 1.4 cũng tiêu thụ boundary check qua dependency `1.1–1.3`.
- **Phạm vi nền tảng:** Repository và CI; scanner phải chạy độc lập với renderer, backend, network live, GoPeak và Context7.
- **Kết quả duy nhất:** một owner/dependency graph có machine-readable policy, scanner fail-closed, forbidden-edge fixtures và merge check hẹp.

Story này không tạo gameplay, platform/provider implementation thật, dependency lock, SBOM, canonical build artifact, export matrix hoặc asset-promotion pipeline. NFR31/NFR55 chưa hoàn tất toàn cục khi Story này xong; Story 1.2 chỉ đóng phần code/dependency boundary của chúng.

## Acceptance Criteria

### AC1 — Monorepo roots và ownership là nguồn chuẩn kiểm tra được

**Given** repository có các boundary gốc `game`, `native`, `backend`, `infrastructure`, `content-source`, `prepare-asset`, `test-harness` và `docs`  
**When** boundary policy được load  
**Then** mỗi source/config file thuộc phạm vi scan phải map tới đúng một module owner, layer và tập edge được phép  
**And** root chưa có consumer phải được materialize bằng owner README có nội dung, không bằng cây thư mục rỗng hoặc `.gitkeep` hàng loạt  
**And** owner không biết, owner trùng hoặc policy/schema sai phải fail-closed.

### AC2 — Shared core không thể kéo dependency hướng ra ngoài

**Given** source hiện tại và source mới trong `game/src/shared/**`  
**When** static dependency graph được dựng từ GDScript, Godot resource/scene và project configuration  
**Then** `shared` chỉ được phụ thuộc shared module khác và Godot built-in type/singleton nằm trong policy allowlist có tên rõ  
**And** mọi edge từ `shared` tới client, server, scene/UI, renderer/presentation, platform port/adapter/SDK, backend implementation, tooling, test harness, raw content hoặc quarantine phải bị từ chối  
**And** implicit `class_name` reference, type hint/static call, `preload/load/extends`, `ext_resource` và Autoload/resource path đều phải được xét; không được chỉ grep import path.

### AC3 — Platform/provider chỉ đi qua typed port/adapter và composition root

**Given** một capability platform/provider trong fixture  
**When** port, adapter và consumer được scan  
**Then** port trung lập phải ở `game/src/platform/ports/**`, có `class_name *Port`, `extends RefCounted` và type annotation cho mọi parameter/return public  
**And** adapter/provider implementation phải ở `game/src/platform/adapters/**` hoặc `native/**`, có `class_name *Adapter` khi là GDScript, và phụ thuộc hướng vào port/shared contract  
**And** application/domain consumer chỉ được biết port; chỉ composition root được policy khai báo mới được biết concrete adapter để inject  
**And** gọi SDK trực tiếp từ shared, client/server domain hoặc đặt implementation ngoài adapter/native bridge phải bị từ chối  
**And** synthetic fixture phải chứng minh composition-root injection; current bootstrap `client/bootstrap → shared/{kernel,diagnostics}` chỉ là allowed-edge regression và không được biến thành port/provider giả.

### AC4 — Violation có bằng chứng machine-readable và fail-closed

**Given** một forbidden import/ownership fixture  
**When** scanner chạy  
**Then** process phải trả non-zero và mỗi violation phải chứa tối thiểu `rule_id`, `source_file`, `line`, `from_module`, `to_module` hoặc unresolved symbol/path, và `forbidden_edge`  
**And** output phải deterministic để cùng input tạo cùng thứ tự graph/violation  
**And** scanner không được phát success summary, artifact “pass” hoặc exit `0` khi policy, parse, owner hay edge resolution thất bại.

### AC5 — Repository/CI gate chặn regression nhưng không chiếm scope Story 1.4

**Given** scanner, fixtures và repository source  
**When** local entrypoint hoặc workflow `module_boundaries` chạy  
**Then** policy tests, forbidden fixtures và real-repository scan phải pass trước khi check xanh  
**And** một forbidden edge được cấy trong isolated fixture/worktree phải làm check đỏ; workflow không dùng `continue-on-error`, warning-only hoặc waiver mặc định  
**And** workflow/job phải giữ stable check name `module-boundaries / module_boundaries`; chính job check đó phải được cấu hình làm required check để literal merge-block claim có evidence  
**And** nếu thiếu quyền branch-protection thì Story chưa đạt DoD, không được ghi “merge đã bị chặn”  
**And** canonical build/import/unit/launch aggregation vẫn thuộc Story 1.4; workflow hẹp này không publish game artifact.

### AC6 — Story 1.1 không bị regression

**Given** bootstrap ở commit baseline và thay đổi Story 1.2  
**When** full local bootstrap verifier chạy sau boundary tests  
**Then** các stage có tên `preflight`, `project-config`, `headless-import`, `bootstrap-unit` và `main-scene-smoke` của verifier vẫn pass với Godot Standard `4.7.1-stable`  
**And** chỉ `BuildInfo` cùng `AppKernel` là Autoload, `prepare-asset` không bị import, direct `print()` vẫn chỉ nằm trong logger hiện hành  
**And** không sửa/move runtime bootstrap chỉ để checker pass; nếu scanner báo false positive, sửa scanner/policy có fixture regression.

### Definition of Done

- Canonical owner/edge policy và human-readable graph tồn tại, schema/version rõ, mọi governed path có đúng một owner.
- Real repository scan pass từ source checkout không cần `.godot/`, renderer, live backend, SDK hoặc MCP.
- Tất cả positive/negative fixtures pass; mỗi expected rejection trả non-zero và chỉ rõ file, line, rule cùng forbidden edge.
- Synthetic fixture chứng minh typed port/adapter/composition-root injection; current bootstrap chỉ là allowed-edge regression `client/bootstrap → shared`.
- Workflow hẹp `module_boundaries` đỏ với forbidden-edge witness và xanh sau khi bỏ witness; required-check evidence tồn tại.
- Không thêm PyPI package, addon, engine/plugin/SDK upgrade, SBOM, canonical artifact hoặc platform implementation.

## Tasks / Subtasks

- [x] 1. Khóa baseline và materialize top-level ownership (AC: 1, 6)
  - [x] Xác nhận Story 1.1 `done`, ghi commit triển khai thực tế và chạy baseline verifier trước mutation.
  - [x] Giữ nguyên thay đổi ngoài scope trong worktree; `.DS_Store` hiện đang dirty và không được xóa/sửa/commit như một phần Story này.
  - [x] Tạo owner README ngắn cho các root còn thiếu: `native`, `backend`, `infrastructure`, `content-source`, `test-harness`.
  - [x] Không tạo toàn bộ subtree tương lai. Chỉ tạo directory có consumer là policy/scanner/test hoặc owner marker thật.
  - [x] Ghi rõ `prepare-asset` là quarantine, `content-source` là raw/DCC source, và production runtime không được phụ thuộc hai root này.

- [x] 2. Tạo policy và tài liệu boundary làm source of truth (AC: 1–3)
  - [x] Tạo `infrastructure/ci/module_boundaries.toml` với `schema_version`, module ID, path pattern, owner, layer, allowed edge, forbidden symbol/provider pattern, composition-root path và scan exclusion.
  - [x] Tạo `docs/architecture/module_boundaries.md` giải thích graph, owner, cách thêm module/edge và quy trình đổi boundary qua Architecture/ADR khi cần.
  - [x] Mã hóa partition path không giao nhau trong bảng **Normative ownership partition** bên dưới; pattern cha phải exclude toàn bộ pattern con, không dùng match-order để giải quyết overlap.
  - [x] Giữ direction chuẩn:
    - client/server application → shared contracts/simulation;
    - platform adapter → typed platform port + shared contract;
    - composition root → port + concrete adapter để inject;
    - tools → shared schemas;
    - backend → generated contracts;
    - shared → shared + Godot core primitives được phép.
  - [x] Policy phải từ chối runtime → tools/tests/test-harness/prepare-asset/content-source; client → server implementation; server → scene/UI/audio/visual asset; backend → GDScript/game implementation.
  - [x] Tên root có dấu gạch nối như `content-source`, `prepare-asset`, `test-harness` là tên canonical từ Architecture; file mới vẫn dùng ASCII `snake_case`.

- [x] 3. Xây scanner repo-wide bằng Python standard library (AC: 1–4)
  - [x] Tạo `infrastructure/ci/check_module_boundaries.py`, chạy bằng Python 3.12+, không PyPI dependency.
  - [x] Walk working tree để bắt cả untracked source; không dựa riêng `git ls-files`.
  - [x] Canonicalize path trong repository; symlink/path escape, unknown/ambiguous owner hoặc policy parse failure phải fail-closed.
  - [x] Chỉ triển khai bounded lexical scanner, không viết full GDScript parser: bỏ comment an toàn, đọc string/path literal và các construct dưới đây; syntax thuộc construct được quản trị nhưng không parse được phải trả `BOUNDARY_PARSE_UNSUPPORTED`.
  - [x] Phân loại file theo bảng **Normative scan classes**; source/executable type mới trong governed runtime root mà chưa được phân loại phải fail-closed thay vì bị bỏ qua âm thầm.
  - [x] Parse dependency cho:
    - GDScript explicit path dependency từ `preload`, `load`, quoted `extends`;
    - GDScript implicit dependency qua symbol table `class_name`, type hint, constructor/static reference;
    - `.tscn`/`.tres` external resource path; `uid://` resolve bằng checked-in `.uid` sidecar hoặc `UID::fallback_path`, không cần `.godot/`;
    - `project.godot` Autoload/resource path;
    - configured provider/SDK symbols và forbidden Godot presentation/input APIs theo source module.
  - [x] Resolve `load()`/`preload()` argument là literal trực tiếp hoặc local `const`/`var` gán một string literal trong cùng function/file; current `load(scene_path)` trong `test_bootstrap.gd` phải resolve. Argument còn động phải fail bằng rule riêng trừ loader/facade path chính xác được policy cho phép và có fixture.
  - [x] Normalize Godot Autoload prefix `*res://` trước khi resolve path.
  - [x] Loại comment/string false positive nhưng vẫn giữ literal path đang tạo dependency; thêm fixture chứng minh.
  - [x] Không crawl body binary của `prepare-asset`; chỉ map owner/root và phát hiện source/runtime reference đi vào quarantine.
  - [x] Output một JSON document deterministic theo schema **Evidence contract** bên dưới. Exit `0` chỉ khi policy + graph đều hợp lệ; dùng non-zero trong dải `1..125` cho policy/parse/edge failure.
  - [x] Không dùng `GameLog` trong Python tool; structured JSON của tool là CI diagnostic, còn rule cấm `print()` tiếp tục áp dụng cho production GDScript.

- [x] 4. Tạo bounded boundary fixtures và test runner (AC: 2–4, 6)
  - [x] Tạo `game/tests/unit/tools/test_module_boundaries.py` bằng `unittest` standard library.
  - [x] Tạo positive fixtures cho client → shared, adapter → typed port/shared, synthetic composition root → concrete adapter, cùng current bootstrap allowed-edge graph.
  - [x] Tạo negative fixtures cho:
    - shared → client;
    - shared → server;
    - shared → UI/renderer/presentation;
    - shared → platform port/adapter/provider/backend;
    - client domain → server implementation hoặc concrete adapter bypass;
    - server → scene/UI/audio/visual asset;
    - runtime → tools/tests/test-harness/content-source/prepare-asset;
    - provider/SDK ngoài adapter/native bridge;
    - malformed policy, unknown owner, ambiguous owner, unknown governed source type, unresolved path/UID, dynamic runtime load và path escape.
  - [x] Bao phủ cả path import, `uid://`, implicit `class_name`, type reference, scene/resource reference và Autoload; assert exact non-zero + file/line/rule/edge, không chỉ snapshot text.
  - [x] Chạy scanner hai lần trên cùng fixture và assert output/order giống nhau.
  - [x] Expected-rejection fixtures phải làm subprocess scanner fail nhưng test suite pass; test runner tự trả non-zero nếu assertion fail.
  - [x] Live repository scan phải exclude deliberate fixture tree `game/tests/fixtures/module_boundaries/**`; unit test phải gọi scanner với fixture root/policy riêng để negative fixture vẫn thực sự được parse, không được “pass” nhờ cùng exclusion.

- [x] 5. Tạo local/CI entrypoint hẹp và merge-block evidence (AC: 4–5)
  - [x] Tạo `infrastructure/ci/verify_module_boundaries.sh` hoặc entrypoint tương đương chạy unit fixtures rồi real-repository scan.
  - [x] Tạo `.github/workflows/module_boundaries.yml` với workflow name `module-boundaries` và job ID/name `module_boundaries`; chỉ setup Python 3.12, chạy entrypoint và fail job khi command non-zero.
  - [x] Không tải Godot, không build/export/publish artifact trong workflow này; Story 1.4 sẽ consume cùng entrypoint trong canonical build smoke.
  - [x] Đây là narrow merge gate bắt buộc trực tiếp bởi Story 1.2, không phải canonical build của Story 1.4 và không phụ thuộc Story 1.3. Cấu hình `module-boundaries / module_boundaries` làm required check trên protected branch và lưu evidence không chứa token/secret.
  - [x] Trong isolated branch/worktree, cấy một forbidden edge, chứng minh required check đỏ, rồi bỏ fixture/witness và chứng minh check xanh.
  - [x] Nếu không có quyền repository-admin, ghi blocker thật và giữ Story chưa `done`; không thay bằng ảnh/log giả hoặc local-only claim.

- [x] 6. Chạy regression và thu evidence cuối (AC: 1–6)
  - [x] Chạy `python3.12 -m unittest game/tests/unit/tools/test_module_boundaries.py`; expected exit `0`.
  - [x] Chạy `infrastructure/ci/verify_module_boundaries.sh` từ clean checkout/worktree; expected exit `0`, trong khi từng expected-rejection subprocess vẫn non-zero.
  - [x] Chạy `GODOT_BIN=<absolute-standard-binary> game/tools/bootstrap/verify_local_bootstrap.sh`; expected exit `0`.
  - [x] Chạy `rg -n '^[[:space:]]*print\(' game/src` và xác nhận match duy nhất vẫn là `game/src/shared/diagnostics/game_log.gd`; quarantine/provider/Autoload regression do boundary entrypoint và bootstrap verifier kiểm tra.
  - [x] Xác nhận không có runtime/bootstrap file nào thay đổi ngoài file list đã khai báo.
  - [x] Ghi owner/rule inventory, số file/edge scan, positive/negative fixture count, exit codes, clean-worktree status và required-check run URL/ID vào Dev Agent Record.

## Dev Notes

### Current workspace facts

- Tại thời điểm tạo Story, `HEAD` là `4746491d6da714d153185a4c72f2b8cad172d498`; commit này đóng Story 1.1 và sửa các review finding của bootstrap.
- Sprint hiện ghi Story 1.1 `done`; workflow này đã promote Story 1.2 từ `backlog` sang `ready-for-dev`.
- Worktree có một thay đổi ngoài scope: `.DS_Store`. Không dùng main worktree dirty làm clean evidence; dùng isolated worktree/fixture và không đụng file của người dùng.
- Root hiện có: `game`, `prepare-asset`, `docs`. Root còn thiếu: `native`, `backend`, `infrastructure`, `content-source`, `test-harness`.
- `game/src` hiện chỉ có `shared/{kernel,diagnostics}` và `client/bootstrap`. Chưa có server, platform, simulation, protocol hoặc UI consumer.
- Current dependency graph hợp lệ: client bootstrap dùng `OperationResult`, `BuildInfoFacade`, `GameLog`; shared chỉ dùng Godot core primitives và không import client/server/platform/backend.
- Baseline Story 1.1 đã chứng minh 13/13 project-config checks, 10/10 verifier fixtures, 33 GDScript assertions, macOS/Linux import và launch/quit.

### Canonical boundary model

```text
client application ───────────┐
server application ───────────┼──> shared contracts/simulation/data
platform ports/adapters ──────┘

composition roots ───────────────> typed port + concrete adapter (injection only)
game tools/devtools ─────────────> shared schemas/contracts
backend ─────────────────────────> generated contracts
shared ──────────────────────────> shared + approved Godot core primitives only

production runtime -X-> tools | tests | test-harness | content-source | prepare-asset
shared             -X-> client | server | UI/renderer | platform | backend
client domain      -X-> server implementation | concrete provider adapter
server             -X-> scenes | UI | audio | visual assets
```

`game/src/platform/ports/**` là contract platform trung lập; adapter/provider implementation nằm dưới governed platform/native path. Shared gameplay không import platform port. Chỉ composition root được phép biết concrete adapter để inject vào consumer typed theo port.

### Normative ownership partition

Các pattern này là partition, không phải ordered allowlist. Mỗi pattern cha phải khai báo `exclude` cho mọi child row; file match 0 hoặc hơn 1 row đều fail.

| Path partition | Module owner / layer | Dependency parsing |
|---|---|---|
| `game/src/shared/**` | `shared` / domain-contract-simulation | Có |
| `game/src/client/bootstrap/**` | `client_composition` / composition-root | Có |
| `game/src/client/ui/**`, `game/scenes/**` | `client_presentation` / UI-renderer-scene | Có |
| `game/src/client/**` trừ `bootstrap/**`, `ui/**` | `client` / application | Có |
| `game/src/server/**` | `server` / authoritative application | Có |
| `game/src/platform/ports/**` | `platform_port` / neutral contract | Có |
| `game/src/platform/adapters/**` | `platform_adapter` / provider adapter | Có |
| `game/project.godot` | `game_config` / composition configuration | Chỉ Autoload/resource path |
| `game/.gitignore` | `game_config` / repository configuration | Ownership-only |
| `game/tools/**` | `game_tools` / development tooling | Ownership-only cho `.sh`; dependency parse cho Godot resource path nếu có |
| `game/tests/**` trừ `fixtures/module_boundaries/**` | `game_tests` / test code | Có với `.gd/.tscn/.tres`; ownership-only với `.sh/.py` |
| `backend/**` | `backend` / service implementation | Ownership-only trong Story này |
| `native/**` | `native` / bridge implementation | Ownership-only trong Story này; provider registry vẫn áp dụng |
| `infrastructure/**` | `infrastructure` / build-CI tooling | Ownership-only |
| `content-source/**` | `content_source` / raw-DCC source | Ownership-only; runtime edge vào đây bị cấm |
| `prepare-asset/**` | `quarantine` / untrusted intake | Path/owner-only, không đọc binary body |
| `test-harness/**` | `test_harness` / external harness | Ownership-only |
| `docs/**`, `.github/**` | `docs`, `ci` / documentation-automation | Ownership-only |

`generated contracts` chỉ được thêm như một child partition chính xác khi Story sở hữu schema/codegen materialize path đó; không tạo path giả trong Story 1.2.

### Normative scan classes

- **Dependency source:** `.gd`, `.tscn`, `.tres`, `project.godot`; parse các construct đã liệt kê trong Task 3.
- **Owner-mapped executable/tooling:** `.py`, `.sh`; map owner và executable type, nhưng Story 1.2 không tự xây Python/shell import graph.
- **Owner-mapped metadata/config/docs:** `.gd.uid`, `.toml`, `.yml`, `.yaml`, `.json`, `.md`; `.gd.uid` chỉ cung cấp UID → sibling source mapping.
- **Quarantine/binary:** map root và không đọc body. Runtime textual reference tới path này vẫn là forbidden edge.
- Unknown executable/source suffix dưới `game/src/**`, `game/scenes/**`, `game/tools/**`, `game/tests/**`, `backend/**` hoặc `native/**` trả `BOUNDARY_SOURCE_TYPE_UNGOVERNED`; asset/content binary dưới quarantine/content-source không bị hiểu nhầm là source.

Current-source cases bắt buộc pass:

- `.gd.uid` là metadata, không phải dependency source.
- `project.godot` path `*res://...` bỏ prefix `*` rồi resolve.
- `test_bootstrap.gd` local literal `scene_path = "res://..."` truyền vào `load(scene_path)` được constant-resolve.
- Project `class_name` tạo dependency edge; Godot built-in không tự biến thành unresolved project symbol.

### Typed port/provider rules

- `[godot].allowed_shared_symbols` ban đầu là exact list: `Array`, `Dictionary`, `Engine`, `JSON`, `Node`, `ProjectSettings`, `RefCounted`, `String`, `StringName`, `Time`, `Variant`, `bool`, `int`, `void`. Thêm symbol mới cần policy diff và positive fixture.
- Project-defined `class_name` luôn thắng built-in allowlist trùng tên và tạo repository edge.
- Port là GDScript trong `platform/ports/**`, `class_name` kết thúc `Port`, `extends RefCounted`; public method thiếu parameter hoặc return annotation bị `BOUNDARY_PORT_UNTYPED`.
- Adapter GDScript nằm trong `platform/adapters/**`, `class_name` kết thúc `Adapter`, và phải reference ít nhất một declared Port. Native provider phải ở `native/**`; mỗi provider registry row phải khai báo exact `provider_path`, `adapter_module` và `port_module`, đồng thời chỉ declared adapter/composition root được reference provider đó.
- Provider detection dùng registry exact symbol/path/API pattern trong TOML; fixture policy khai báo fake provider symbols để chứng minh scanner bắt được. Không dùng heuristic “mọi identifier viết hoa là SDK”.
- Chỉ `client_composition` và composition-root fixture path được phép reference concrete adapter. Bootstrap hiện không phải port-injection proof; nó chỉ là allowed `client_composition → shared` regression.

### Evidence contract

Scanner phát đúng một JSON document, key order và array order deterministic:

```json
{
  "schema_version": 1,
  "status": "pass",
  "policy_sha256": "<lowercase-hex>",
  "files_scanned": 0,
  "edges": [],
  "violations": []
}
```

Mỗi edge có `source_file`, `line`, `from_module`, `to_module`, `kind`, `target`; mỗi violation có `rule_id`, `source_file`, `line`, `from_module`, `to_module` hoặc `unresolved_target`, và `forbidden_edge`. Path là repo-relative POSIX; array sort theo `(source_file, line, rule_id, target)`. Failure trước graph construction vẫn phát document `status=fail`, `edges=[]` và typed violation, không in mixed prose ra stdout.

### Policy và scanner guardrails

- Policy TOML là machine-readable source of truth; tài liệu Markdown giải thích rationale và workflow, không được trở thành allowlist thứ hai bị drift.
- Mỗi governed file map đúng một owner. Pattern overlap không được chọn “first match”; đó là `BOUNDARY_AMBIGUOUS_OWNER`.
- Minimum stable rule IDs:
  - `BOUNDARY_FORBIDDEN_EDGE`
  - `BOUNDARY_UNKNOWN_OWNER`
  - `BOUNDARY_AMBIGUOUS_OWNER`
  - `BOUNDARY_PLATFORM_PROVIDER_OUTSIDE_ADAPTER`
  - `BOUNDARY_RUNTIME_DEPENDS_ON_TOOLING`
  - `BOUNDARY_POLICY_INVALID`
  - `BOUNDARY_DEPENDENCY_UNRESOLVED`
  - `BOUNDARY_SOURCE_TYPE_UNGOVERNED`
  - `BOUNDARY_DYNAMIC_RESOURCE_PATH`
  - `BOUNDARY_PARSE_UNSUPPORTED`
  - `BOUNDARY_PORT_UNTYPED`
- Không dùng broad allowlist như `shared -> game/**`, blanket waiver theo filename, warning-only, hay “known false positive” không có expiry/owner/fixture.
- Không scan chỉ tracked files. Forbidden source mới/untracked phải bị bắt trước commit.
- Không dựa duy nhất vào regex path. Existing `AppKernel` dùng global `class_name` symbols mà không `preload`; scanner path-only sẽ bỏ sót graph thật.
- Không tự sửa/move code sang allowlisted folder để xanh. Thay đổi boundary cần owner/rationale, Architecture/ADR khi đổi quyết định, và fixture cập nhật cùng policy.

### Project structure dự kiến

```text
outsurvive/
├── .github/
│   └── workflows/
│       └── module_boundaries.yml                 # NEW
├── backend/
│   └── README.md                                 # NEW owner marker
├── content-source/
│   └── README.md                                 # NEW owner marker
├── infrastructure/
│   ├── README.md                                 # NEW owner marker
│   └── ci/
│       ├── module_boundaries.toml                # NEW source of truth
│       ├── check_module_boundaries.py            # NEW scanner
│       └── verify_module_boundaries.sh           # NEW stable entrypoint
├── native/
│   └── README.md                                 # NEW owner marker
├── test-harness/
│   └── README.md                                 # NEW owner marker
├── docs/
│   └── architecture/
│       └── module_boundaries.md                  # NEW human guide
└── game/
    └── tests/
        ├── unit/tools/
        │   └── test_module_boundaries.py         # NEW
        └── fixtures/module_boundaries/            # NEW fixture roots/files
            ├── allowed_client_to_shared/
            ├── allowed_composition_root_to_adapter/
            ├── forbidden_shared_to_client/
            ├── forbidden_shared_to_server/
            ├── forbidden_shared_to_presentation/
            ├── forbidden_shared_to_platform/
            ├── forbidden_client_to_server/
            ├── forbidden_server_to_presentation/
            ├── forbidden_runtime_to_tooling/
            ├── forbidden_provider_outside_adapter/
            └── malformed_or_unknown_owner/
```

Không thêm `.uid` bằng tay cho Python/TOML/README/fixture ngoài Godot import workflow. Không tạo `game/src/server`, `game/src/platform` hoặc deep architecture tree trước consumer.

### Existing files — current state, preservation và change decision

Story implementation dự kiến **không cần UPDATE runtime/bootstrap file nào**. Nếu dev chọn tích hợp scanner vào verifier hiện hữu, phải giải thích vì sao standalone workflow chưa đủ và cập nhật test contract tương ứng; mặc định giữ tách scope.

- `game/tools/bootstrap/verify_local_bootstrap.sh`
  - **Hiện tại:** preflight → project-config → headless import → bootstrap unit → main-scene smoke; capture exit code, reject warning/error và required evidence.
  - **Giữ nguyên:** exact 4.7.1 Standard/checksum/template semantics, structured failure, năm check hiện tại và explicit helper return status.
  - **Story 1.2:** chạy nó như regression evidence. Story 1.4 sẽ aggregate boundary entrypoint vào canonical build.
- `game/tests/unit/client/test_bootstrap.gd`
  - **Hiện tại:** lifecycle/config/main-scene bootstrap smoke với 33 assertions và process exit rõ.
  - **Giữ nguyên:** dùng làm runtime regression evidence; synthetic fixture riêng chứng minh port/adapter injection.
- `game/tests/unit/tools/test_verify_local_bootstrap.sh`
  - **Hiện tại:** isolated temp fixtures, cleanup trap, 10 positive/negative preflight cases.
  - **Giữ nguyên:** chỉ update nếu bootstrap verifier contract thực sự đổi.
- `game/project.godot`
  - **Hiện tại:** main scene, Forward+/Mobile, strict untyped warning; chỉ `BuildInfo` và `AppKernel` Autoload.
  - **Giữ nguyên:** không thêm `PlatformGateway`, scanner Autoload, manager hoặc policy setting.
- `game/src/client/bootstrap/app_kernel.gd`
  - **Hiện tại:** guarded `BOOTING → READY → SHUTTING_DOWN`; typed results và shared diagnostics.
  - **Giữ nguyên:** đây là positive `client_composition → shared` edge; scanner phải hiểu implicit class symbols.
- `game/src/shared/{kernel,diagnostics}/**`
  - **Hiện tại:** typed primitives/facade/logger chỉ dùng Godot core.
  - **Giữ nguyên:** scanner phải pass; direct `print()` exception duy nhất vẫn là `game_log.gd`.
- `prepare-asset/**` và `docs/asset-intake-register.md`
  - **Hiện tại:** quarantine cùng intake register.
  - **Giữ nguyên:** không parse binary asset body, move/promote asset hoặc sửa provenance trong Story này.

### Previous Story intelligence

- Story 1.1 cố ý deferred monorepo scanner/full tree sang Story 1.2; không diễn giải thiếu directory là bug của bootstrap.
- Tám review finding đã sửa cung cấp guardrail trực tiếp:
  - shell helper phải trả status cho caller; không để command substitution che failure;
  - relative executable path và uppercase hex cần fixture;
  - failure phải ngăn downstream work, không chỉ log;
  - test success/failure dựa trên process exit, không dựa `push_error()` hay text;
  - cleanup phải hoạt động cả node không nằm trong tree;
  - timestamp structured cần UTC `Z`;
  - ignore generated/platform junk đầy đủ.
- Expected rejection phải làm child process non-zero nhưng parent test suite pass.
- Không dùng dirty main làm clean evidence. Historical `baseline_commit: NO_VCS` và HALT log cũ trong Story 1.1 không được copy thành current fact.

### Git intelligence

- Repository có hai commit liên quan:
  - `311755b` — initial project/artifact import và bootstrap implementation.
  - `4746491` — Story 1.1 review fixes, status `done`, helper return semantics, shutdown safety, UTC log và ignore rules.
- Pattern cần giữ: POSIX shell `set -u`, `mktemp` + cleanup trap, structured JSON diagnostics, explicit non-zero exit, zero third-party test framework.
- Không sửa hoặc commit `.DS_Store` ngoài scope.

### Testing requirements

- Python tests dùng standard `unittest`, temp directory và subprocess; mọi fixture hoàn toàn isolated.
- Test policy schema trước graph scan; không cho malformed policy rơi về permissive default.
- Test path normalization trên POSIX và Windows-style input bằng `pathlib`/pure paths nơi phù hợp.
- Positive real-repository scan phải bao gồm untracked source nhưng exclude `.git`, `.godot`, `_bmad`, `_bmad-output`, `.DS_Store`, generated caches, binary quarantine body và deliberate negative-fixture tree. Fixture-mode scan phải override exclusion bằng isolated scan root.
- Negative test phải assert process status và structured fields; không chỉ assert substring “failed”.
- Verification set gồm:
  1. static allowed fixture port/adapter/injection;
  2. current bootstrap graph resolution;
  3. existing runtime bootstrap smoke.
- CI workflow pin Python major/minor phù hợp baseline; dependency/SBOM checksum pin thuộc Story 1.3.
- Không nới threshold, skip fixture, add blanket waiver hoặc mark flaky test pass để merge.

### UX/GDD applicability

- Story không tạo player-facing surface; không thêm Theme, font, localization, safe-area, HUD hoặc product copy.
- GDD chỉ tác động qua contract: một gameplay core/data/protocol cho năm platform; khác biệt nằm sau adapter/presentation/lifecycle.
- Scanner/CI JSON là developer diagnostics, không cần `StringId`/LocaleCatalog.
- Story 1.7–1.8 sở hữu presenter/Theme và Việt/Anh localization.

### Explicitly out of scope

- Engine/plugin/SDK upgrade, dependency checksum, SBOM, CVE/license workflow, upgrade ADR — Story 1.3.
- Canonical/reproducible game build, artifact manifest và aggregate CI — Story 1.4.
- Export presets, five-platform artifact/signing matrix — Story 1.5.
- Asset promotion/provenance validator — Story 1.6.
- Theme/presenter/localization — Story 1.7–1.8.
- `GameplayCommand`, simulation/server/network/backend/provider implementation — Story 1.13+ và Epic sở hữu.
- Refactor/move Story 1.1 runtime, thêm Autoload/manager/service locator, hoặc import/promote quarantine assets.

### Project Context Rules

- Giữ Godot Standard `4.7.1-stable`, typed GDScript và Jolt baseline; không tự nâng version.
- Domain-driven paths và dependency direction là contract, không phải gợi ý.
- `shared` không import client/server/platform/backend; backend chỉ chia sẻ generated contracts với Godot.
- Platform SDK chỉ qua typed port/adapter; native chỉ trong `native/` sau profiling + ADR/parity gate.
- Test nằm trong `game/tests`; build/test phải chạy khi không có GoPeak/Context7.
- Production runtime không phụ thuộc tooling/test/quarantine; generated file không sửa tay.
- Không manager singleton, global service locator, absolute `NodePath`, arbitrary asset path hoặc direct platform SDK.
- Không thay Architecture/rule/threshold để hợp thức hóa implementation.

### Latest technical information

- Godot `4.7.1-stable` vẫn là stable release hiện hành ngày 2026-07-26, build từ commit `a13da4feb`; Godot công bố không có incompatibility đã biết với 4.7. Godot 4.8 mới ở development snapshot, không phải lý do nâng baseline.
- `ResourceLoader.get_dependencies()` của Godot 4.7 trả dependency dạng path hoặc `UID::fallback_path`, nhưng resource cần được import và API không bao phủ top-level repository ownership, backend/tooling hay mọi implicit global-class use. Có thể dùng nó làm parity cross-check sau import, không được dùng làm source of truth duy nhất cho pre-import scanner.
- Python 3.12 đã là architecture prerequisite. Dùng `pathlib`, `tomllib`, `json`, `unittest`, `tempfile` và `subprocess` từ standard library; không thêm package chỉ để parse policy/walk tree.

Official references:

- [Godot 4.7.1 maintenance release](https://godotengine.org/article/maintenance-release-godot-4-7-1/)
- [Godot 4.7.1 archive](https://godotengine.org/download/archive/4.7.1-stable/)
- [Godot 4.7 ResourceLoader.get_dependencies](https://docs.godotengine.org/en/4.7/classes/class_resourceloader.html#class-resourceloader-method-get-dependencies)
- [Python 3.12 pathlib](https://docs.python.org/3.12/library/pathlib.html)
- [Python 3.12 tomllib](https://docs.python.org/3.12/library/tomllib.html)

### References

- [Source: `_bmad-output/planning-artifacts/epics.md:826-849` — Story 1.2 foundation, AC, error/test boundary và DoD]
- [Source: `_bmad-output/planning-artifacts/epics.md:306,354,356-361` — NFR31/NFR55 và monorepo requirements]
- [Source: `_bmad-output/planning-artifacts/epics.md:876-899` — Story 1.4 consumes boundary smoke in canonical CI]
- [Source: `_bmad-output/game-architecture.md:941-1193` — domain-driven project structure]
- [Source: `_bmad-output/game-architecture.md:1194-1226` — system location/owner mapping]
- [Source: `_bmad-output/game-architecture.md:1287-1317` — canonical dependency direction và mandatory boundaries]
- [Source: `_bmad-output/game-architecture.md:1569-1588` — ports và composition-root injection]
- [Source: `_bmad-output/game-architecture.md:1765-1802` — enforcement mapping và prohibited shortcuts]
- [Source: `_bmad-output/game-architecture.md:1858-1893` — Python/Godot/MCP development prerequisites]
- [Source: `_bmad-output/project-context.md:67-97` — organization, testing và static-check rules]
- [Source: `_bmad-output/project-context.md:99-116` — platform adapters, CI/SBOM split và secrets]
- [Source: `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md:491-507` — five-platform gameplay-core/adapter contract]
- [Source: `_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/final-ux-verification.md:1-22` — UX final-ready, không có Foundation decision mở]
- [Source: `_bmad-output/implementation-artifacts/1-1-clean-godot-standard-local-bootstrap.md:113-166` — review fixes, current structure và deferred boundaries]
- [Source: `game/tools/bootstrap/verify_local_bootstrap.sh:150-199` — existing verification flow to preserve]
- [Source: `game/project.godot:11-40` — current Autoload/rendering/build configuration]
- [Source: `game/src/client/bootstrap/app_kernel.gd:15-120` — positive `client_composition → shared` edge]

## Dev Agent Record

### Agent Model Used

GPT-5 Codex

### Debug Log References

- 2026-07-27 — Baseline `4746491d6da714d153185a4c72f2b8cad172d498`
  verified with Godot Standard 4.7.1; all five bootstrap stages passed before mutation.
- 2026-07-27 — RED confirmed: boundary test runner failed because the scanner did
  not exist; GREEN/REFACTOR reached 18 passing unittest cases and a real repository
  scan with 3,165 files, 39 deterministic edges, and 0 violations.
- 2026-07-27 — HALT at Task 5 required-check evidence: `gh` is unavailable and the
  connected GitHub API returned `404 Not Found` for private remote
  `MrSuPilun/outsurvive`; branch protection and red/green workflow run evidence
  cannot be configured or verified from the current credentials.
- 2026-07-27 — Resume audit: GitHub CLI authentication is now available and confirms
  `viewerPermission: ADMIN`, but both Branch Protection and Repository Rulesets APIs
  return HTTP `403` with “Upgrade to GitHub Pro or make this repository public to
  enable this feature.” Required-check configuration is unavailable for the current
  private-repository plan, so AC5 remains blocked.
- 2026-07-27 — Repository visibility changed to public; configured strict protected
  `main` with required context `module_boundaries` and admin enforcement. PR
  `https://github.com/MrSuPilun/outsurvive/pull/1` was `BLOCKED` when forbidden
  witness commit `5637f31` produced failed run `30228482390`, then became `CLEAN`
  after witness removal commit `476c113` produced successful run `30228537150`.
- 2026-07-27 — Final regression used clean detached worktree `476c113`
  (`clean_before=0`) and Python 3.12.13: 18 unittest methods passed, representing
  7 isolated positive fixtures and 24 expected-rejection fixtures. Real scan passed
  with 18 module owners, 11 stable rules, 3,165 files, 39 edges, 0 violations, and
  exit `0`; every expected rejection returned non-zero inside the passing suite.
- 2026-07-27 — Bootstrap regression passed 10/10 preflight fixtures, 13/13 project
  config checks, 33 GDScript assertions, headless import and main-scene smoke using
  Godot Standard 4.7.1. Direct `print()` matched only
  `game/src/shared/diagnostics/game_log.gd:33`; runtime/bootstrap diff from baseline
  was empty.

### Completion Notes List

- Ultimate context engine analysis completed — comprehensive developer guide created.
- Materialized five top-level owner roots without creating speculative runtime trees;
  `.DS_Store` remained untouched and outside scope.
- Added the TOML ownership/edge policy, bounded fail-closed Python scanner, structured
  deterministic JSON evidence, typed port/adapter rules, isolated positive/negative
  fixtures, and narrow local/GitHub Actions entrypoints.
- Task 5 was initially blocked while the private repository plan lacked protected
  branch support; that blocker was later resolved when repository visibility became
  public.
- Repository administration access is confirmed; the remaining external blocker is
  GitHub plan visibility/feature availability. Upgrade the private repository to a
  plan supporting protected branches/rulesets, or explicitly authorize making the
  repository public, before resuming required-check evidence.
- The repository is now public and the external blocker is resolved. Required-check
  red/green evidence is recorded without tokens or secrets; Task 5 is complete.
- Final Python 3.12, boundary, bootstrap, direct-print, Autoload/quarantine/provider,
  and runtime-preservation regressions all pass; Tasks 1–6 satisfy AC1–AC6.
- Story 1.2 meets the enhanced Definition of Done and is ready for code review.

### File List

- `.github/workflows/module_boundaries.yml`
- `_bmad-output/implementation-artifacts/1-2-repository-va-module-dependency-boundaries.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`
- `backend/README.md`
- `content-source/README.md`
- `docs/architecture/module_boundaries.md`
- `game/tests/unit/tools/test_module_boundaries.py`
- `infrastructure/README.md`
- `infrastructure/ci/check_module_boundaries.py`
- `infrastructure/ci/module_boundaries.toml`
- `infrastructure/ci/verify_module_boundaries.sh`
- `native/README.md`
- `test-harness/README.md`

## Change Log

- 2026-07-27 — Implemented repository ownership policy, fail-closed boundary scanner,
  fixtures, documentation, and narrow CI gate; halted before required-check evidence
  because repository-admin/API access is unavailable.
- 2026-07-27 — Re-audited GitHub access; admin permission is available, but protected
  branch/ruleset enforcement is disabled by the current private-repository plan
  (HTTP 403), so Story status remains `in-progress`.
- 2026-07-27 — Repository became public; configured strict required check and captured
  real blocked-red/clean-green evidence on PR #1. Task 5 completed.
- 2026-07-27 — Completed final clean-worktree regression and quantitative evidence;
  all Story tasks and acceptance criteria pass.
- 2026-07-27 — Definition of Done passed; Story status moved to `review`.
