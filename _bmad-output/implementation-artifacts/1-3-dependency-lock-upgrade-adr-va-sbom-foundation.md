---
baseline_commit: 8115e6a4cc160b5d9b8eb4b5dc3471c8c9e55d2c
---

# Story 1.3: Dependency lock, upgrade ADR và SBOM foundation

Status: done

<!-- Note: Validation is optional. Run validate-create-story for quality check before dev-story. -->

## Story

As a build engineer,  
I want dependency/toolchain được pin và kiểm kê từ đầu,  
so that mọi artifact sau có nguồn gốc và upgrade path kiểm soát được.

## Outcome và ranh giới

- **Delivery Type:** Enabler — consumer là Story 1.4/1.5 và mọi release qualification (Epic 10).
- **Sizing:** S — tối đa 3 ngày làm việc.
- **Source Requirements (chuẩn):** NFR31, NFR49, NFR55; Additional Requirements (dependency version/license/checksum/wrapper/owner + SBOM); ADR-18, ADR-20.
- **Source cite note:** Epic liệt kê `NFR26` cho Story 1.3, nhưng NFR26 hiện là packet-validation — **không dùng làm yêu cầu Story này**. Neo đúng là NFR49/NFR55 (+ NFR31 parity toolchain, NFR30 không lộ secret/PII trong SBOM/log).
- **Depends on:** Story 1.1 (epic formal). **Implementation context bắt buộc:** Story 1.2 đã `done` — tái sử dụng `infrastructure/ci/**`, Python 3.12 stdlib, fail-closed JSON, narrow GitHub workflow.
- **Blocks:** Story 1.4–1.6 và Story 10.1–10.11.
- **Module/File Ownership:** Version/checksum lock manifest, dependency policy, SBOM generator, upgrade ADR template, verifier CI hẹp.
- **Phạm vi nền tảng:** Tooling + pin toolchain cho năm client và Linux headless. Không export/build game artifact trong Story này.
- **Kết quả duy nhất:** baseline lock + SBOM tái lập được, verifier fail-closed, upgrade chỉ qua ADR template + impacted-platform smoke matrix; bootstrap có thể tiêu thụ trusted digest từ lock.

Story này **không** tạo canonical Linux client artifact (1.4), five-platform export/signing (1.5), asset quarantine promotion (1.6), container/image SBOM (6.9), CVE ops product đầy đủ, hoặc promote plugin/SDK (Nakama/Terrain3D/EOS/Agones) vào runtime. Các baseline đã verified chỉ được **đăng ký** trong lock với trạng thái `not_promoted` / `toolchain` / `editor_only` tương ứng.

## Acceptance Criteria

### AC1 — Dependency lock là source of truth có version + checksum

**Given** engine, export template, plugin, SDK hoặc tool được khai báo trong lock  
**When** dependency resolution / verify chạy  
**Then** mỗi entry phải có tối thiểu: `id`, `kind`, `version`, `source`, `license`, `checksum` (thuật toán + hex), `wrapper`, `owner`, `platform_applicability`, `promotion_status`  
**And** Godot Engine Standard và export templates phải pin đúng `4.7.1-stable` (không Mono/.NET)  
**And** không được có floating version (`latest`, branch tip không gắn commit, unpinned range)  
**And** mismatch version/checksum, entry thiếu field bắt buộc, hoặc checksum malformed phải fail-closed (non-zero, không auto-fetch latest, giữ lock hiện tại).

### AC2 — SBOM tái lập có license / source / hash

**Given** lock manifest hợp lệ  
**When** SBOM generator chạy  
**Then** phải phát một CycloneDX JSON (specVersion `1.6` hoặc `1.7`) chứa mọi component đang trong lock với license, source/purl hoặc externalReference, và hash khớp lock  
**And** cùng lock input phải tạo SBOM deterministic (cùng component set/order/hash; timestamp metadata có thể cố định hoặc strip khi so sánh reproducibility)  
**And** component unknown/unapproved/`promotion_status` không hợp lệ không được xuất hiện như “approved for promote”  
**And** SBOM và log không chứa signing secret, platform token, raw PII hoặc credential (NFR30).

### AC3 — Upgrade chỉ chấp nhận qua ADR + impacted-platform smoke matrix

**Given** đề xuất upgrade engine/plugin/SDK/database/orchestrator/native tool  
**When** review/gate chạy  
**Then** phải có ADR theo template dự án (tham chiếu ADR-18 build/versioning và ADR-20 evidence-based promotion)  
**And** ADR phải khai báo compatibility branch, protocol/content migration impact (hoặc “none” có lý do), và impacted-platform smoke matrix  
**And** CVE/license chưa quyết định (`undecided` / thiếu `license_decision`) phải chặn promote  
**And** schema validator từ chối ADR thiếu field bắt buộc; không có “soft approve”.

### AC4 — Verifier + CI hẹp fail-closed; không chiếm scope 1.4

**Given** lock, SBOM generator, ADR template/schema và fixtures  
**When** local entrypoint hoặc workflow dependency-lock chạy  
**Then** unit fixtures (lock drift, checksum corruption, SBOM completeness, upgrade-ADR schema) và real-repo verify phải pass trước khi check xanh  
**And** corruption/drift fixture trong isolated worktree làm check đỏ; không `continue-on-error`, warning-only, hay waiver mặc định  
**And** workflow/job giữ stable check name `dependency-lock / dependency_lock`; `permissions: contents: read`; Python 3.12; **không** tải Godot, không build/export/publish game artifact  
**And** workflow `module-boundaries` của Story 1.2 vẫn xanh và không bị thay thế  
**And** canonical build smoke aggregation thuộc Story 1.4 — Story 1.3 chỉ cung cấp lock/SBOM + verifier để 1.4 tiêu thụ.

### AC5 — Bootstrap tiêu thụ trusted digest từ lock (không fork preflight)

**Given** lock có trusted checksum cho Godot editor binary/archive theo platform host  
**When** bootstrap preflight chạy với cơ chế load lock (env từ helper hoặc documented path)  
**Then** `GODOT_SHA256` / trusted compare path hiện có trong `verify_local_bootstrap.sh` phải được cấp từ lock, không hardcode digest “giả chính thức” trong script  
**And** mismatch trusted vs observed vẫn fail-closed như Story 1.1  
**And** không viết lại version/flavor/preflight semantics; chỉ wire lock → trusted digest  
**And** nếu platform host chưa có trusted binary digest trong lock (chỉ có archive hash), hành vi phải rõ: fail-closed khi policy yêu cầu trusted, hoặc documented `observed_only` chỉ khi entry đánh dấu thiếu binary digest — **không** bịa digest.

### AC6 — Không regression Story 1.1 / 1.2

**Given** thay đổi Story 1.3  
**When** boundary verifier và bootstrap verifier chạy  
**Then** `infrastructure/ci/verify_module_boundaries.sh` exit `0`  
**And** `GODOT_BIN=<absolute-standard-binary> game/tools/bootstrap/verify_local_bootstrap.sh` exit `0`  
**And** không thêm PyPI package, addon runtime, Autoload mới, hoặc sửa bootstrap runtime chỉ để checker pass  
**And** `.DS_Store` / thay đổi ngoài scope trong worktree không được “dọn” như một phần Story này.

### Definition of Done

- Lock manifest + human docs tồn tại, schema/version rõ; Godot Standard + export templates `4.7.1-stable` được pin với checksum từ nguồn chính thức (xem Dev Notes).
- SBOM CycloneDX tái lập từ lock; completeness/reproducibility tests xanh.
- Upgrade ADR template + schema validator chặn promote khi thiếu ADR/smoke matrix hoặc CVE/license undecided.
- Narrow CI `dependency-lock / dependency_lock` đỏ với witness drift/corruption và xanh sau khi bỏ witness; không phá `module-boundaries`.
- Bootstrap có đường tiêu thụ trusted digest từ lock; 1.1 + 1.2 regression xanh.
- Baseline lock/SBOM sẵn sàng để Story 1.4 “dùng bởi build smoke” — không cần Story 1.4 implement trong story này, nhưng contract tiêu thụ phải được ghi rõ (path + CLI).

## Tasks / Subtasks

- [x] 1. Khóa baseline và chốt contract lock/SBOM (AC: 1, 2, 6)
  - [x] Xác nhận Story 1.1 và 1.2 `done`; ghi `HEAD` triển khai vào Dev Agent Record.
  - [x] Giữ nguyên thay đổi ngoài scope (`.DS_Store`, file story/sprint đang dirty nếu có); dùng clean detached worktree cho evidence.
  - [x] Chốt schema lock TOML/JSON tại `infrastructure/ci/` (đề xuất: `infrastructure/ci/dependency_lock.toml`) với `schema_version`.
  - [x] Chốt SBOM: CycloneDX JSON `specVersion` `1.6` (tối thiểu) sinh bằng Python stdlib từ lock — **không** thêm PyPI/`cyclonedx-bom` trừ khi có ADR riêng (không thuộc story này).
  - [x] Ghi rõ: archive checksum chính thức Godot lấy từ `SHA512-SUMS.txt` của release `4.7.1-stable` (godot-builds); binary SHA-256 local là field riêng cho preflight (`checksum_sha256` hoặc `artifacts[].sha256`) — không nhầm archive SHA512 với binary SHA256 đã quan sát ở 1.1.

- [x] 2. Tạo dependency lock + tài liệu policy (AC: 1, 3)
  - [x] Tạo lock với entry bắt buộc:
    - `godot.editor` — Godot Engine Standard `4.7.1-stable`, flavor standard, commit `a13da4feb`, promotion `toolchain`.
    - `godot.export_templates` — `4.7.1-stable` (non-mono), promotion `toolchain`.
    - Các baseline đã verified nhưng **chưa promote**: Terrain3D `1.0.2` (`editor_only` / `not_promoted`), Nakama `3.40.0`, Nakama Common `1.47.0`, Nakama Godot SDK `3.4.0`, CockroachDB `26.2.3`, Agones `1.59.0`, Kubernetes `1.35.6`, Go `1.26.5`, EOS Voice portal artifact (`not_promoted`, checksum TBD cho đến khi pin portal artifact).
  - [x] Mỗi entry: `version`, `source` (URL hoặc registry identity), `license`, checksum (`sha512` và/hoặc `sha256` theo artifact), `wrapper` (path hoặc `none` + lý do), `owner` module, `platform_applicability`, `promotion_status` ∈ {`toolchain`, `editor_only`, `not_promoted`, `promoted`}, `license_decision` ∈ {`approved`, `undecided`, `rejected`}.
  - [x] MCP GoPeak/Context7: **không** đưa vào lock như build/runtime dependency; có thể ghi chú trong docs là optional dev tooling.
  - [x] Tạo `docs/architecture/dependency_lock.md` — quy trình thêm dependency, promote, upgrade; TOML là SoT, MD không phải allowlist thứ hai.
  - [x] Tạo upgrade ADR template tại `docs/adr/templates/upgrade_dependency.md` (hoặc tương đương) với field bắt buộc khớp schema validator.

- [x] 3. Xây verifier + SBOM generator bằng Python stdlib (AC: 1–4)
  - [x] `infrastructure/ci/check_dependency_lock.py` — validate schema, no floating versions, checksum format, promotion/license rules, fail-closed JSON stdout.
  - [x] `infrastructure/ci/generate_sbom.py` — đọc lock → CycloneDX JSON deterministic; ghi `infrastructure/ci/sbom/outsurvive.cdx.json` (hoặc path tương đương dưới `infrastructure/`) kèm header/comment `generated` nếu cần; generator là source of truth, không sửa SBOM tay.
  - [x] `infrastructure/ci/check_upgrade_adr.py` (hoặc subcommand) — validate ADR instance/fixture theo template schema.
  - [x] `infrastructure/ci/verify_dependency_lock.sh` — chạy unittest rồi real verify + SBOM regenerate/check.
  - [x] Reuse pattern Story 1.2: `pathlib`, `tomllib`, `json`, `unittest`, `hashlib`, `subprocess`, `tempfile`; `sys.executable`; exit `0` chỉ khi hợp lệ; failure `1..125`.
  - [x] Không dùng `GameLog`/`print()` policy cho Python CI tool; structured JSON là diagnostic.

- [x] 4. Fixtures và unit tests (AC: 1–4)
  - [x] `game/tests/unit/tools/test_dependency_lock.py` bằng `unittest`.
  - [x] Positive: lock tối thiểu hợp lệ + SBOM completeness (license/source/hash) + ADR schema hợp lệ.
  - [x] Negative / expected-rejection:
    - lock drift (version đổi không cập nhật checksum);
    - checksum corruption / length/charset sai;
    - missing license/source/wrapper/owner;
    - floating version;
    - `license_decision=undecided` khi cố `promotion_status=promoted`;
    - SBOM thiếu component hoặc hash lệch lock;
    - upgrade ADR thiếu smoke matrix / compatibility branch / ADR-20 spike evidence field.
  - [x] Expected-rejection: subprocess non-zero, parent suite xanh; assert field JSON (`rule_id`, path, message).
  - [x] Chạy generator hai lần, assert SBOM so sánh reproducibility (strip/normalize timestamp nếu cần).

- [x] 5. Wire bootstrap trusted digest + CI hẹp (AC: 4–6)
  - [x] Helper nhỏ (shell hoặc python) đọc lock → export `GODOT_SHA256` cho platform hiện tại khi binary digest có trong lock; tích hợp vào docs và optional path trong `verify_dependency_lock.sh` / bootstrap docs — **không** phá `verify_local_bootstrap.sh` API hiện có (`GODOT_SHA256` env vẫn là contract).
  - [x] Nếu chỉ pin được archive SHA512 từ official sums trong ngày làm việc: ghi rõ trong lock `artifacts` tách `archive` vs `installed_binary`; bootstrap wire chỉ khi `installed_binary.sha256` có mặt. Không bịa binary digest từ archive hash.
  - [x] Tạo `.github/workflows/dependency_lock.yml`: name `dependency-lock`, job `dependency_lock`, `permissions: contents: read`, Python 3.12, chạy `verify_dependency_lock.sh`.
  - [x] Không thay thế `module_boundaries.yml`.
  - [x] Trong isolated worktree: cấy lock drift hoặc checksum corruption → check đỏ; bỏ witness → check xanh. Lưu run URL/ID không chứa secret.
  - [x] Required-check trên protected branch: cố gắng cấu hình `dependency-lock / dependency_lock`; nếu thiếu quyền admin, ghi blocker thật — không claim merge-block giả. (Story 1.2 đã làm public repo + required check pattern.)

- [x] 6. Regression và evidence cuối (AC: 1–6)
  - [x] `python3.12 -m unittest game/tests/unit/tools/test_dependency_lock.py` → exit `0`.
  - [x] `infrastructure/ci/verify_dependency_lock.sh` → exit `0`.
  - [x] `infrastructure/ci/verify_module_boundaries.sh` → exit `0`.
  - [x] Bootstrap với trusted digest từ lock (khi có) + không lock env vẫn pass theo contract 1.1.
  - [x] Xác nhận không có addon/`game/addons`, không PyPI, không promote SDK.
  - [x] Ghi inventory entry count, SBOM component count, fixture counts, CI run URLs, lock schema version vào Dev Agent Record.
  - [x] Document consumer contract cho Story 1.4: path lock, path SBOM, CLI verify phải xanh trước canonical build.

### Review Findings

- [x] [Review][Patch] Fix trailing markdown code block delimiter in verify_dependency_lock.sh [infrastructure/ci/verify_dependency_lock.sh:59]
- [x] [Review][Patch] Prevent re.error in _contains_version when version string contains regex special characters [infrastructure/ci/check_dependency_lock.py:67]
- [x] [Review][Patch] Fix table header filtering in check_upgrade_adr.py smoke matrix validator [infrastructure/ci/check_upgrade_adr.py:136]
- [x] [Review][Patch] Apply PLATFORM_MAP normalization when --platform flag is specified in export_godot_sha256.py [infrastructure/ci/export_godot_sha256.py:69]
- [x] [Review][Patch] Guard against None value for checksum_hex in export_godot_sha256.py [infrastructure/ci/export_godot_sha256.py:59]
- [x] [Review][Patch] Add Python 3.12+ version validation check in verify_dependency_lock.sh [infrastructure/ci/verify_dependency_lock.sh:19]


## Dev Notes

### Current workspace facts

- Sprint: `1-1` done, `1-2` done, `1-3` backlog → promote `ready-for-dev` khi story này được tạo.
- `HEAD` gần nhất (tại lúc create-story): merge Story 1.2 (`8115e6a` / PR #1). Ghi lại `git rev-parse HEAD` khi bắt đầu implement.
- Đã có: `infrastructure/ci/{module_boundaries.toml,check_module_boundaries.py,verify_module_boundaries.sh}`, `.github/workflows/module_boundaries.yml`, bootstrap `GODOT_SHA256` hook.
- **Chưa có:** lockfile, SBOM, `docs/adr/**`, dependency CI, PyPI/go.mod/package.json, `game/addons/`.
- Observed SHA-256 (evidence 1.1, **không** tự phong là lock cho đến khi đối chiếu nguồn chính thức / pin có chủ đích):
  - macOS Godot binary: `ecc8da2d60100102cfca6e833d3860d7436b46ae062fa072ce89a6c95d664a3f`
  - Linux x86_64 Godot binary: `32f8d7596c4b41185512b1c49d69f2da3be018fd784a53e349fa92a98a97bcde`
- Official release assets: https://github.com/godotengine/godot-builds/releases/tag/4.7.1-stable — dùng `SHA512-SUMS.txt` cho archive/tpz; có thể có `.sha256` sidecar cho source tarball. Pin đúng artifact name (`Godot_v4.7.1-stable_*`, `Godot_v4.7.1-stable_export_templates.tpz`), **không** pin Mono variants.

### Architecture compliance (bắt buộc)

- [Source: `_bmad-output/game-architecture.md` — Build, Deployment and Compatibility]: dependency lock/SBOM thuộc Foundation 1.3–1.5; pin version/checksum; generate SBOM.
- [Source: ADR-18]: five-platform CI / build manifest v1 / exact compatibility — Story 1.3 chuẩn bị pin + upgrade path; không implement full build matrix.
- [Source: ADR-20]: plugin/native chỉ promote sau spike + ADR; lock entries `not_promoted` cho đến khi có evidence.
- [Source: Verified Technology Baselines 2026-07-22]: bảng version ở trên — đăng ký trong lock, không âm thầm nâng.
- Addon rule: chỉ `game/addons` với version/license/checksum/wrapper/owner — chưa tạo addon trong 1.3.
- Không tự nâng engine/plugin/DB/orchestrator/SDK; mọi upgrade cần ADR + manifest + compatibility gate; Godot upgrade cần five-platform smoke.
- MCP không phải runtime/build dependency; pipeline phải chạy không có MCP.

### Normative lock schema (tối thiểu)

```toml
schema_version = 1

[[dependencies]]
id = "godot.editor"
kind = "engine"
version = "4.7.1-stable"
flavor = "standard"  # reject mono/net
source = "https://github.com/godotengine/godot-builds/releases/tag/4.7.1-stable"
license = "MIT"
license_decision = "approved"
wrapper = "none"
owner = "infrastructure"
platform_applicability = ["windows_x64", "linux_x64", "macos_universal", "android_arm64", "ios_arm64", "linux_headless"]
promotion_status = "toolchain"
# artifacts: tách archive (sha512 từ SHA512-SUMS.txt) và installed_binary (sha256) theo platform
```

Fail rules (gợi ý `rule_id`): `LOCK_SCHEMA_INVALID`, `LOCK_FLOATING_VERSION`, `LOCK_CHECKSUM_INVALID`, `LOCK_CHECKSUM_MISMATCH`, `LOCK_LICENSE_UNDECIDED_PROMOTE`, `LOCK_PROMOTION_INVALID`, `SBOM_INCOMPLETE`, `SBOM_HASH_MISMATCH`, `SBOM_NONDETERMINISTIC`, `ADR_SCHEMA_INVALID`, `ADR_SMOKE_MATRIX_MISSING`.

### Evidence contract (verifier JSON stdout)

Một document deterministic mỗi lần chạy:

```json
{
  "schema_version": 1,
  "status": "pass",
  "lock_path": "infrastructure/ci/dependency_lock.toml",
  "lock_schema_version": 1,
  "dependency_count": 0,
  "sbom_path": "infrastructure/ci/sbom/outsurvive.cdx.json",
  "sbom_component_count": 0,
  "sbom_spec_version": "1.6",
  "checks": ["schema", "checksums", "promotion", "sbom", "adr_template"],
  "violations": []
}
```

Khi fail: `status=failure`, `violations[]` chứa `rule_id`, `dependency_id` (nếu có), `path`, `message`. Không emit success summary khi có violation.

### Consumer contract cho Story 1.4 (không implement ở 1.3)

1.4 phải gọi `infrastructure/ci/verify_dependency_lock.sh` (exit 0) trước canonical build; đọc cùng `dependency_lock.toml` để pin Godot/export-template inputs; đính kèm `outsurvive.cdx.json` (hoặc regenerate+diff) vào artifact evidence. 1.3 không tạo Linux client binary.

### CycloneDX mapping (stdlib generator)

| Lock field | CycloneDX |
|---|---|
| id/name/version | `components[].name` / `version` |
| kind | `components[].type` (`application`/`library`/`framework`) |
| license | `components[].licenses[]` (SPDX id khi có) |
| source | `purl` và/hoặc `externalReferences[]` |
| checksum | `components[].hashes[]` (`alg`: `SHA-256` / `SHA-512`, `content`: hex) |
| bom metadata | `bomFormat=CycloneDX`, `specVersion=1.6`, `serialNumber`/`version` ổn định từ hash(lock) |

Không cần full OWASP toolchain; subset hợp lệ đủ AC. Prefer `.cdx.json` suffix.

### Upgrade ADR template — field bắt buộc

- `title`, `status`, `date`, `dependency_id`, `from_version`, `to_version`
- `rationale`, `compatibility_branch`
- `protocol_impact`, `content_manifest_impact` (`none` | mô tả migration)
- `impacted_platform_smoke_matrix` (list platform + gate owner)
- `adr20_spike_evidence` (link/path hoặc `n/a` chỉ khi `kind` không phải plugin/native)
- `license_decision`, `cve_decision` (`cleared` | `undecided` | `accepted_risk` + justification)
- `rollback_plan`

Validator từ chối `cve_decision=undecided` hoặc `license_decision=undecided` khi ADR `status=accepted` cho promote.

### Files sẽ UPDATE (đọc trước khi sửa)

1. **`game/tools/bootstrap/verify_local_bootstrap.sh`**
   - Hiện: so sánh `GODOT_SHA256` nếu set; không biết lock.
   - Story đổi: **ưu tiên không sửa** nếu helper bên ngoài export env; chỉ sửa tối thiểu nếu cần load lock path documented (giữ exit codes/`BOOT_*`, JSON shape).
   - Preserve: version/flavor checks, `observed_only` khi không có trusted digest.

2. **`game/tests/unit/tools/test_verify_local_bootstrap.sh`** (nếu wire thay đổi hành vi)
   - Thêm fixture trusted-from-lock nếu API đổi; không làm yếu negative checksum cases.

3. **Không sửa** `module_boundaries.toml` / scanner trừ khi path mới cần classification — file mới `.py`/`.sh`/`.toml`/`.md`/`.yml`/`.json` đã được hỗ trợ bởi metadata suffixes; tránh executable type lạ.

### Project Structure Notes

```text
infrastructure/ci/
  dependency_lock.toml          # NEW — SoT
  check_dependency_lock.py      # NEW
  generate_sbom.py              # NEW
  check_upgrade_adr.py          # NEW (hoặc gộp subcommand)
  verify_dependency_lock.sh     # NEW
  sbom/outsurvive.cdx.json      # NEW generated
  module_boundaries.*           # UNCHANGED (regression)

.github/workflows/
  dependency_lock.yml           # NEW narrow gate
  module_boundaries.yml         # UNCHANGED

docs/architecture/dependency_lock.md
docs/adr/templates/upgrade_dependency.md
docs/adr/README.md              # ngắn: ADRs sống trong architecture + template upgrade

game/tests/unit/tools/test_dependency_lock.py
game/tests/fixtures/dependency_lock/**   # isolated fixtures
```

ASCII `snake_case` paths. Không tạo `utils/`/`helpers/` chung.

### Previous Story Intelligence

**Từ 1.1**
- Trusted lock/SBOM/upgrade ADR bị trì hoãn có chủ đích tới 1.3.
- Preflight đã sẵn `GODOT_SHA256`; observed ≠ lock.
- Shell helpers phải return status; checksum hex case-insensitive; assert process exit.

**Từ 1.2**
- Pattern giao hàng: TOML SoT + Python stdlib verifier + shell entrypoint + narrow workflow + MD docs + unittest fixtures + clean worktree evidence + explicit `permissions`.
- Không PyPI; `sys.executable`; fail-closed JSON; không commit `.DS_Store`.
- Deferred: cyclic UI↔client allowlist — **không** đụng trong 1.3 (`deferred-work.md`).

**Git gần đây**
- PR #1 hoàn tất module boundaries; required check `module-boundaries / module_boundaries` đã có evidence.
- Tái sử dụng pattern evidence đỏ/xanh trên isolated branch.

### Git Intelligence Summary

- Commit style: concise why-focused messages (English in recent commits).
- CI tools sống dưới `infrastructure/ci/`; tests dưới `game/tests/unit/tools/`.
- Không mở rộng scope sang export/signing.

### Latest Technical Information

- **CycloneDX:** spec hiện tại 1.7 (ECMA-424, 2025-10); dùng `1.6` hoặc `1.7` JSON. Media type `application/vnd.cyclonedx+json`. Filename `*.cdx.json`.
- **Godot 4.7.1-stable:** official checksums qua `SHA512-SUMS.txt` trên godot-builds releases; pin Standard (non-mono) editor + `Godot_v4.7.1-stable_export_templates.tpz`.
- **Không** auto-fetch latest; mismatch giữ lock cũ (heritage AC từ archived Story 10.1).

### Project Context Rules

- Engine: Godot Standard 4.7.1-stable, typed GDScript; không tự nâng version.
- Dependency pin version/checksum + SBOM; controls ở Story 1.3–1.5.
- Addon: version/license/checksum/wrapper/owner; native chỉ sau profiling + ADR + five-platform parity.
- MCP optional; không runtime/build dep; không secret trong prompt/repo/SBOM.
- Tests: `game/tests/{unit,...}`; tooling tests không cần renderer; static checks fail-closed.
- Logging: không `print()` trong production GDScript; CI Python dùng JSON stdout.
- Secrets/signing: ngoài repo (1.5/10.x) — SBOM không được nhúng secret.
- Monorepo ownership: tooling CI thuộc `infrastructure`; docs thuộc `docs`.

### Anti-patterns (cấm)

- Bịa “official” binary SHA-256 từ quan sát local mà không ghi nguồn/provenance trong lock.
- Thêm Syft/Trivy/npm/PyPI SBOM stack “cho nhanh” phá zero-third-party-CI-tooling rule.
- Promote Nakama/EOS/Terrain3D trong 1.3.
- Gộp canonical build/export vào workflow dependency-lock.
- Thay thế hoặc tắt `module_boundaries`.
- Floating `main`/`latest` trong lock.
- Sửa generated SBOM bằng tay.
- Đưa GoPeak/Context7 vào SBOM runtime components.

### References

- [Source: `_bmad-output/planning-artifacts/epics.md` — Story 1.3, NFR49/NFR55, Additional Requirements, Foundation Wave]
- [Source: `_bmad-output/planning-artifacts/archive/pre-readiness-remediation-2026-07-26/epics.md` — legacy Story 10.1 richer ACs]
- [Source: `_bmad-output/game-architecture.md` — Build/Deployment, ADR-18/20, Verified Technology Baselines]
- [Source: `_bmad-output/project-context.md` — Technology Stack, Platform & Build Rules]
- [Source: `_bmad-output/implementation-artifacts/1-1-clean-godot-standard-local-bootstrap.md`]
- [Source: `_bmad-output/implementation-artifacts/1-2-repository-va-module-dependency-boundaries.md`]
- [Source: `game/tools/bootstrap/verify_local_bootstrap.sh` — `GODOT_SHA256` hook]
- [Source: CycloneDX ECMA-424 / https://cyclonedx.org/specification/overview/]
- [Source: https://github.com/godotengine/godot-builds/releases/tag/4.7.1-stable]

## Dev Agent Record

### Agent Model Used

{{agent_model_name_version}}

### Debug Log References

- 2026-07-27 — Baseline `8115e6a4cc160b5d9b8eb4b5dc3471c8c9e55d2c`; Story 1.1 và 1.2 đều `done`; worktree ban đầu chỉ có story/sprint planning changes.
- 2026-07-27 — RED: 12 test lock/SBOM/ADR thất bại vì verifier/generator chưa tồn tại; 2 test digest helper thất bại trước implementation.
- 2026-07-27 — GREEN: `python3 -m unittest game/tests/unit/tools/test_dependency_lock.py` → 16/16 pass; môi trường không có executable tên `python3.12`, verifier dùng Python 3.14.6 tương thích `>=3.12`.
- 2026-07-27 — Detached worktree witness: baseline verifier exit `0`; đổi checksum Godot thành non-hex làm exit `1` với `LOCK_CHECKSUM_INVALID`; restore lock làm exit `0`. Không có hosted run URL vì workflow chưa được commit/push; không tự tạo commit/PR.
- 2026-07-27 — GitHub branch protection API xác nhận `strict=true`, required contexts `module_boundaries` và `dependency_lock` trên `main`.
- 2026-07-27 — Regression: dependency verifier exit `0`; module boundaries 18/18 + real scan exit `0`; bootstrap full dùng SHA-256 từ lock exit `0`; preflight không trusted env trả `observed_only` và exit `0`; Python tooling discovery 34/34 pass.

### Completion Notes List

- Ultimate context engine analysis completed - comprehensive developer guide created
- Tạo lock schema v1 gồm 11 dependency/toolchain entry; tách Godot official archive SHA-512 khỏi installed-binary SHA-256 quan sát có provenance.
- Tạo CycloneDX 1.6 deterministic gồm 11 component, validator fail-closed và generator Python stdlib; không PyPI/addon/runtime promotion.
- Tạo upgrade ADR template/validator với compatibility branch, protocol/content impact, ADR-20 evidence, CVE/license gate, rollback và platform smoke matrix.
- Wire bootstrap qua helper export `GODOT_SHA256` theo host; giữ nguyên API/semantics Story 1.1 và fail-closed khi host thiếu binary digest.
- Thêm workflow `dependency-lock / dependency_lock`, giữ nguyên module-boundary workflow, cấu hình required context thật trên protected `main`.
- Hoàn tất 16 test Story 1.3 (positive, negative/rejection, deterministic SBOM, ADR, secrets, baseline Godot, digest helper) và toàn bộ regression.

### File List

- `.github/workflows/dependency_lock.yml`
- `_bmad-output/implementation-artifacts/1-3-dependency-lock-upgrade-adr-va-sbom-foundation.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`
- `docs/adr/README.md`
- `docs/adr/templates/upgrade_dependency.md`
- `docs/architecture/dependency_lock.md`
- `game/tests/fixtures/dependency_lock/valid_upgrade_adr.md`
- `game/tests/unit/tools/test_dependency_lock.py`
- `infrastructure/ci/check_dependency_lock.py`
- `infrastructure/ci/check_upgrade_adr.py`
- `infrastructure/ci/dependency_lock.toml`
- `infrastructure/ci/export_godot_sha256.py`
- `infrastructure/ci/generate_sbom.py`
- `infrastructure/ci/sbom/outsurvive.cdx.json`
- `infrastructure/ci/verify_dependency_lock.sh`

## Change Log

- 2026-07-27: Tạo story context sẵn sàng cho `dev-story` (status `ready-for-dev`).
- 2026-07-27: Triển khai dependency lock schema v1, CycloneDX SBOM, upgrade ADR gate, trusted Godot digest helper, CI required check và regression evidence.
