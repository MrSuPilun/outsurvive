# Dependency lock và SBOM

`infrastructure/ci/dependency_lock.toml` là source of truth duy nhất cho version, nguồn, license, checksum, wrapper, owner, phạm vi nền tảng và trạng thái promotion. Tài liệu này mô tả quy trình; nó không phải allowlist thứ hai.

## Contract

- Lock schema hiện tại: `schema_version = 1`.
- Godot editor và export templates dùng Standard `4.7.1-stable`; Mono/.NET không thuộc baseline.
- Mỗi dependency có ít nhất một artifact record với SHA-256 hoặc SHA-512. `archive` là checksum artifact tải về, `installed_binary` là checksum binary sau unpack, còn `catalog_identity` chỉ khóa identity đã khảo sát và không đủ làm bằng chứng promotion.
- Checksum archive Godot lấy từ `SHA512-SUMS.txt` chính thức của release. Checksum `installed_binary` của macOS/Linux là evidence quan sát trong Story 1.1 và chỉ được tin cho đúng archive đã pin.
- Entry `not_promoted` hoặc `editor_only` chỉ là inventory. Nó không cho phép runtime/build sử dụng dependency.
- EOS Voice chưa có portal artifact đã pin. Catalog checksum hiện tại chỉ bảo vệ record `portal-artifact-tbd`; promotion phải thay version, source và checksum bằng artifact portal thật.
- GoPeak và Context7 là tooling phát triển tùy chọn, không phải build/runtime dependency và không xuất hiện trong lock/SBOM.

## Local entrypoints

```sh
infrastructure/ci/verify_dependency_lock.sh
python3 infrastructure/ci/generate_sbom.py \
  --lock infrastructure/ci/dependency_lock.toml \
  --output infrastructure/ci/sbom/outsurvive.cdx.json
```

Verifier chạy unit fixtures, validate lock, regenerate SBOM vào file tạm, so sánh byte-for-byte với SBOM tracked, validate upgrade ADR fixture và phát một JSON evidence document. Mọi lỗi trả non-zero; không có waiver hoặc auto-fetch `latest`.

## Thêm hoặc promote dependency

1. Thêm entry đầy đủ vào TOML, giữ version tuyệt đối và nguồn gắn version/commit.
2. Pin checksum artifact từ nguồn chính thức. Không dùng `catalog_identity` để promote.
3. Ghi license decision, wrapper boundary, owner và platform applicability.
4. Với plugin/native/provider, hoàn tất spike ADR-20 và parity gate trước khi đổi `promotion_status`.
5. Sinh lại SBOM bằng generator; không sửa `.cdx.json` bằng tay.
6. Chạy verifier và module-boundary regression.

`promotion_status = "promoted"` yêu cầu `license_decision = "approved"`. CVE/license chưa quyết định phải giữ dependency ở `not_promoted`.

## Upgrade gate

Mọi upgrade engine, plugin, SDK, database, orchestrator hoặc native tool phải tạo ADR từ `docs/adr/templates/upgrade_dependency.md`. Validator yêu cầu compatibility branch, protocol/content migration impact, ADR-20 spike evidence, license/CVE decision, rollback plan và impacted-platform smoke matrix. ADR `accepted` không thể giữ quyết định license/CVE ở `undecided`.

Upgrade Godot phải chạy smoke trên cả Windows, Linux, macOS, Android và iOS. Dependency khác chỉ chạy nền tảng bị ảnh hưởng nhưng matrix phải ghi rõ gate và owner. Lock hiện tại được giữ nguyên khi ADR hoặc checksum không hợp lệ.

## Bootstrap trusted digest

API Story 1.1 được giữ nguyên: `verify_local_bootstrap.sh` chỉ nhận trusted binary SHA-256 qua `GODOT_SHA256`. Helper `infrastructure/ci/export_godot_sha256.py` đọc artifact `installed_binary` theo host và phát câu lệnh shell an toàn:

```sh
eval "$(python3 infrastructure/ci/export_godot_sha256.py \
  --lock infrastructure/ci/dependency_lock.toml)"
GODOT_BIN=/absolute/path/to/godot \
  game/tools/bootstrap/verify_local_bootstrap.sh --preflight-only
```

Nếu host không có `installed_binary.sha256`, helper fail-closed theo mặc định. `--allow-observed-only` phát biến rỗng và diagnostic JSON trên stderr để giữ contract `observed_only`; nó không bịa digest.

## Consumer contract cho Story 1.4

Story 1.4 phải:

1. chạy `infrastructure/ci/verify_dependency_lock.sh` thành công trước canonical build;
2. đọc Godot/export-template inputs từ `infrastructure/ci/dependency_lock.toml`;
3. regenerate và diff `infrastructure/ci/sbom/outsurvive.cdx.json`;
4. đính kèm SBOM cùng build evidence.

Story 1.3 không tạo client/server binary, export, signing artifact hoặc container SBOM.
