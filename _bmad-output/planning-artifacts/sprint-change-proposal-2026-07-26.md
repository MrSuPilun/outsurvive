---
project: outsurvive
date: 2026-07-26
status: implemented-and-validated
mode: batch
trigger:
  - _bmad-output/planning-artifacts/implementation-readiness-report-2026-07-26.md
approval:
  source: user
  statement: "Làm đi, tôi muốn bạn tự hoàn thành để đảm bảo phiên sau sẽ có thể bắt đầu start coding"
scope: major
canonical_backlog: _bmad-output/planning-artifacts/epics.md
---

# Sprint Change Proposal — Remediation trước Production

## 1. Issue Summary

Implementation Readiness ngày 2026-07-26 kết luận `NOT READY` dù GDD, UX, Architecture và backlog có độ chi tiết cao. Trigger không đến từ một Story đang code mà từ pre-production gate, trước khi tạo `sprint-status.yaml`.

Ba nhóm nguyên nhân:

1. 12 requirement-coverage finding: 10 thiếu và 2 phủ một phần.
2. 6 UX/Architecture alignment finding.
3. 13 Epic-quality finding: 1 critical, 9 major và 3 minor.

Không có code production cần rollback. GDD 1.1.0 và tầm nhìn Standard 100 người/năm nền tảng vẫn giữ nguyên.

## 2. Change Navigation Checklist

| ID | Trạng thái | Kết quả |
|---|---|---|
| 1.1 | N/A | Trigger là readiness gate, chưa có Story implementation. |
| 1.2 | Done | Vấn đề là thiếu traceability, decision ownership và backlog packaging/sequencing. |
| 1.3 | Done | Evidence là 31 finding và exit criteria trong readiness report 2026-07-26. |
| 2.1–2.5 | Done | Epic 5 phải reframe; Epic 10 chỉ giữ outcome release; foundation/UX/ops được đưa sớm và dependency đổi sang Story/contract. |
| 3.1 | N/A | Không có PRD; GDD không cần đổi scope. |
| 3.2 | Done | Architecture cần tham chiếu backlog chuẩn, ADR/policy reconnect, spectator, audio, localization, input và map. |
| 3.3 | Done | UX spine giữ nguyên; các NOTE gate được đóng bằng owner decision từ Architecture. |
| 3.4 | Done | Backlog, project context, CI/SBOM/observability ownership và readiness report cần đồng bộ. |
| 4.1 | Viable | Direct Adjustment; effort cao, risk trung bình và không đổi MVP. |
| 4.2 | Not viable | Chưa có code để rollback. |
| 4.3 | Not viable | Không cần giảm MVP; scope vẫn đạt nếu sửa planning trước coding. |
| 4.4 | Done | Chọn Direct Adjustment vì bảo toàn GDD và loại rework sớm nhất. |
| 5.1–5.5 | Done | Proposal này định nghĩa issue, impact, path, plan và handoff. |
| 6.1–6.2 | Done | Checklist/proposal đã đối chiếu với readiness exit criteria. |
| 6.3 | Done | Người dùng phê duyệt batch và yêu cầu tự hoàn thành. |
| 6.4 | Done | Đã tạo và validate `_bmad-output/implementation-artifacts/sprint-status.yaml` sau khi readiness đạt `READY`. |
| 6.5 | Done | Codex hoàn tất artifact changes và Create Story 1.1; phiên sau bắt đầu bằng `gds-dev-story`. |

## 3. Impact Analysis

### Epic và Story

- Epic 1: tách scaffold, boundary, toolchain/CI và Prototype Survivor thành các Enabler độc lập; tạo UX/localization foundation sớm.
- Epic 3: thu nhỏ catalog kernel; definition theo consumer; tách throwable capability khỏi evidence gate.
- Epic 5: đổi từ technical slice thành outcome người chơi “Khám phá và thoát hiểm trong vùng thử nghiệm”; tách schema/bake vừa đủ.
- Epic 6: sở hữu server container, observability và reconnect/spectator communication policy tại thời điểm capability online xuất hiện.
- Epic 8: trở thành hardening/consolidation; HUD, Inventory, Map và Party integration được ghép với capability sở hữu thay vì chờ Epic 1–7 hoàn tất.
- Epic 10: chỉ giữ qualification, performance và release-candidate outcome người chơi; dependency/SBOM/CI/container/observability không bị trì hoãn đến release.

### Artifact

- GDD: không đổi nội dung; toàn bộ 93 FR phải được truy vết đầy đủ trong backlog.
- Architecture: cập nhật source reference 10 Epic và khóa UX-A1–A5 bằng policy/ADR.
- UX: không đổi behavior; NOTE gate được coi là resolved-by-Architecture.
- Project Context: đồng bộ rule mới để coding agent không suy diễn lại decision.

### Technical

- CI, dependency lock, SBOM, signing boundary, container và observability xuất hiện cùng capability đầu tiên cần chúng.
- Mọi dependency readiness dùng Story ID + named artifact/contract.
- Gate chỉ tạo evidence/promotion decision; không chứa feature implementation ẩn.

## 4. Detailed Change Proposals

### Backlog packaging

**OLD:** Story 1.1 chứa scaffold, monorepo, bootstrap, sáu artifacts, toolchain, quarantine và CI.  
**NEW:** các Story độc lập cho local bootstrap, boundary, toolchain/SBOM, build-smoke expansion và quarantine/CI validation.

**OLD:** Story 1.2 chứa provenance, rig, animation graph, aim layer và parity/package.  
**NEW:** các Story độc lập cho intake/rig, locomotion graph, upper-body layer và parity/package evidence.

**OLD:** Story 3.1 định nghĩa toàn item domain.  
**NEW:** stable-ID/catalog kernel tối thiểu; weapon/ammo, equipment/capacity, healing và throwable definitions thuộc Story consumer.

**OLD:** Story 3.11 vừa triển khai throwable vừa gate Epic.  
**NEW:** throwable capability và promotion evidence là hai Story khác nhau.

**OLD:** Story 5.1 tạo toàn bộ MapDefinition/TerrainTileData/pipeline.  
**NEW:** terrain-slice contract/bake tối thiểu trước; schema được mở rộng trong streaming/route/building/weather Story.

**OLD:** Epic 10 là technical release program.  
**NEW:** technical controls chuyển về Epic 1/6 và owner Story; Epic 10 chỉ giữ player/platform qualification, hardening và RC acceptance.

### Requirement coverage

- FR55 → Story 5.6 và 7.7: histogram sightline theo 0–25/40–150/150–400/400–800 m.
- FR57 → Story 5.5/5.6/7.4: validator cấm destructibility/terrain digging/building.
- FR59 → Story 5.7/7.9 và UX evidence: không full-night; outfit detection delta ≤5%.
- FR65 → Story 9.7: Standard chính; ranked/custom/tournament/FPP-only deferred.
- FR70 → Story 4.13: telemetry progression 0–3/3–10/10–22/22+.
- FR75 → weapon manifest/balance evidence: mỗi archetype có một strength và một disadvantage.
- FR76 → Story 5.4/7.3/7.7: POI 800–1.500 m, hai ground route, non-vehicle escape ≤70% chậm hơn.
- FR77 → Story 5.5/7.4/7.5: roof counterplay, 80% window silhouette, material penetration language.
- FR78 → Story 7.8: navigation bằng landmark/sign/material, không phụ thuộc minimap.
- FR79 → character/weapon/world content contracts: restrained realism, ordinary survivor silhouette, fictional weapon identity.
- FR85 → Story 8.12/7.8: footstep/gunshot ranges, material spectrum và masking gate.
- FR93 → Story 9.7: mọi post-release proposal khai báo P1–P4 + metric và reject/tách Standard nếu giảm tension/fairness/readability.

### Architecture decisions

- Reconnect: avatar luôn vulnerable, neutral input; live-match grace 120 giây; hết hạn áp dụng leave-after-aircraft defeat và server elimination/drop; reconnect chỉ phục hồi state authoritative.
- Spectator: teammate-follow; được nghe/nói team voice, không tạo world/context ping hoặc marker mới sau elimination.
- Audio: player-facing `Master/World/Team Voice/UI/Music`; Footsteps/Weapons/Vehicles/Ambience là child bus nội bộ dưới World và không được expose tactical boost/EQ.
- Localization: `StringId` + immutable `LocaleCatalog`; Việt/Anh, English fallback; gameplay không phát display string.
- Input: physical key identity cho gameplay binding, logical text cho text entry; localized OS label; captured unaccumulated relative mouse delta cho aim và explicit fallback capability.
- Map: Full Map north-up cố định trong Standard; zoom 0.75×–6× theo map extent, pan clamp vào authored bounds; minimap player-heading-up.

## 5. Recommended Approach

Chọn **Direct Adjustment**.

- Effort: High cho planning artifact, không có code migration.
- Risk: Medium; giảm xuống Low sau automated trace/dependency/readiness checks.
- Timeline: thêm một remediation pass trước Sprint Planning, đổi lại tránh big-bang UX, CI và platform rework.
- MVP: không đổi; không thêm feature mới ngoài quyết định cần thiết để implement behavior đã được UX/GDD yêu cầu.

## 6. Implementation Handoff

**Classification:** Major.

**Thực hiện hiện tại:** Codex đóng vai Product Manager + Architect + Developer cho artifact remediation theo ủy quyền batch.

**Success criteria:**

1. 93/93 GDD FR có đường triển khai rõ.
2. Architecture tham chiếu backlog chuẩn và không còn UX-A1–A5 open gate.
3. Không còn technical Epic; oversized critical-path Story đã split.
4. CI/reproducibility/security/observability xuất hiện tại owner capability.
5. Dependency graph dùng Story/contract cụ thể, không cycle/forward dependency.
6. Readiness rerun kết luận `READY`.
7. Sprint Planning và Create Story 1.1 đã hoàn tất; phiên sau có thể bắt đầu coding trực tiếp bằng `gds-dev-story`.

## 7. Implementation Outcome

**Completed:** 2026-07-26.

- Readiness rerun: `_bmad-output/planning-artifacts/implementation-readiness-report-2026-07-26-post-remediation.md` — `READY`, 0 critical, 0 major, 1 controlled non-blocking concern.
- Canonical sprint tracker: `_bmad-output/implementation-artifacts/sprint-status.yaml` — 10 Epic, 144 Story, 10 retrospective; YAML hợp lệ.
- First implementation Story: `_bmad-output/implementation-artifacts/1-1-clean-godot-standard-local-bootstrap.md` — `ready-for-dev`.
- Tracker transition: `epic-1 = in-progress`; `1-1-clean-godot-standard-local-bootstrap = ready-for-dev`.
- Next terminal workflow: `gds-dev-story` cho Story 1.1. Không có gameplay/project code nào được tạo trong remediation/Create Story pass này.
