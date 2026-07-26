# Asset Intake Register

Tài liệu này ghi nhớ các đợt asset người dùng bổ sung vào `prepare-asset/`. Mọi nội dung tại đây vẫn là quarantine cho tới khi đạt provenance/license và technical review; việc có mặt trong register không đồng nghĩa được phép ship.

## Intake 2026-07-26

### Prototype character and animation source

- Candidate character: Quaternius Universal Base Characters — model `Regular`.
- Candidate animation sources: Quaternius Universal Animation Library và Universal Animation Library 2.
- Intended use: controlled placeholder cho Epic 1 và Combat Sandbox; không phải survivor art production.
- License stated by publisher: CC0. Bản tải cụ thể vẫn phải lưu URL, retrieval date, original archive, license copy và per-file checksum trước khi promote.
- Runtime contract: fixed-30-Hz authoritative `CharacterMotor`; animation is presentation-only; no locomotion root motion; shared humanoid skeleton and timings across desktop/mobile.

### Audio drop

- Quarantine path: `prepare-asset/audio/`.
- Inventory: 2.072 files, khoảng 105 MB.
- Formats: 1.926 OGG, 85 MP3, 61 WAV.
- Snapshot fingerprint over the sorted per-file SHA-256 list: `29983680d0cfb1c4bdebad0fd9ce1624fea23efe60264ba4f1d7727455e3cd23`.
- No README, license, provenance or manifest was found at intake time.
- Candidate routing:
  - Epic 1: footsteps, movement, vault/jump, swim and UI feedback.
  - Epic 2: weapons, gunshots, bullet impacts, shells, melee and explosions.
  - Epic 5: vehicles and environmental ambience.
  - Epic 8: mix, output controls, accessibility cues and approved music timing.
- Default exclusion: monster/zombie audio, named-character VO, cutscene/event cues, red-zone-like content, and unknown files until separately approved and licensed.

### Terrain texture drop

- Quarantine path: `prepare-asset/textures/`.
- Inventory: 36 PNG files, khoảng 16 MB.
- Dimensions: 256×256, 512×512 and 1024×1024; one 256×512 image.
- Snapshot fingerprint over the sorted per-file SHA-256 list: `fd4a9ee367dde43271579bd0fbba8ec92d8f5735447b90a9b956be670c5b12ff`.
- No README, license, provenance, naming manifest or PBR channel metadata was found at intake time.
- Visual spot-check indicates surface-color candidates for dirt, soil/grass, concrete and rock. This does not establish seamless tiling, physical scale or PBR role.
- Intended use after promotion:
  - Combat Sandbox: a small approved material subset for movement/readability validation.
  - Epic 5 Terrain3D slice: approved terrain materials with explicit albedo/normal/roughness/mask relationships.
  - Epic 7: production expansion only after seam, texel-density, streaming-memory and mobile-compression gates.

## Promotion checklist

An asset may move out of quarantine only when all applicable fields are recorded:

- Source URL or supplier, author, exact license and retrieval date.
- Original archive checksum plus per-file checksum.
- Stable content ID and human-readable name.
- Derived-edit chain and responsible owner.
- Technical role, scale, color space/channel semantics and import settings.
- Platform variants, LOD/compression policy and memory budget.
- Collision/topology/rig review for 3D assets.
- Seam/tiling/PBR validation for terrain textures.
- Loudness, loop, channel layout and content classification for audio.
