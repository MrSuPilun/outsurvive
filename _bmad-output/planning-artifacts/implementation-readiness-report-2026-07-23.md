---
project: 'outsurvive'
date: '2026-07-23'
workflow: 'implementation-readiness'
stepsCompleted: [1, 2, 3, 4, 5, 6]
status: 'complete'
readiness: 'NOT_READY'
findingCount: 17
includedFiles:
  - '_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md'
  - '_bmad-output/game-architecture.md'
  - '_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/epics.md'
  - '_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/DESIGN.md'
  - '_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md'
  - '_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/decision-log.md'
  - '_bmad-output/planning-artifacts/sprint-change-proposal-2026-07-22.md'
  - '_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/final-ux-verification.md'
  - '_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/mobile-delta-validation.md'
  - '_bmad-output/project-context.md'
---

# Implementation Readiness Assessment Report

**Date:** 2026-07-23
**Project:** outsurvive

## Document Inventory

### Canonical Assessment Inputs

| Type | Path | Size | Modified |
|---|---|---:|---|
| GDD | `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/gdd.md` | 53,940 bytes | 2026-07-22 13:34 +0700 |
| Architecture | `_bmad-output/game-architecture.md` | 94,309 bytes | 2026-07-22 23:26 +0700 |
| Epics & Stories | `_bmad-output/planning-artifacts/gdds/gdd-outsurvive-2026-07-22/epics.md` | 15,761 bytes | 2026-07-22 13:36 +0700 |
| UX Design | `_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/DESIGN.md` | 33,166 bytes | 2026-07-22 13:46 +0700 |
| UX Experience | `_bmad-output/planning-artifacts/ux-designs/ux-outsurvive-2026-07-22/EXPERIENCE.md` | 58,721 bytes | 2026-07-22 13:46 +0700 |

`DESIGN.md` và `EXPERIENCE.md` là hai phần bổ trợ của UX source-of-truth, không phải duplicate.

### Supplemental Inputs

- GDD decision log.
- Five-platform sprint change proposal.
- Final UX verification và mobile delta validation.
- Completed AI-agent project context.

### Discovery Resolution

- Không có required document bị thiếu.
- Không phát hiện whole/sharded duplicate cần xử lý.
- `.working/`, intermediate reviews/audits và mockup HTML không được dùng làm nguồn chuẩn; chỉ truy vết nếu canonical documents mâu thuẫn.

## GDD Analysis

### Functional Requirements

**FR001 — Standard match:** Hệ thống phải cung cấp trận battle royale Standard 100 người, nơi mọi người xuất phát tay trắng, tự chọn điểm rơi, loot tại chỗ, di chuyển theo vùng an toàn thu hẹp và kết thúc khi chỉ còn một người hoặc một đội sống.

**FR002 — Match loop:** Trận phải thực hiện tuần tự các pha chuẩn bị 60 giây, quan sát đường bay 30–45 giây, đổ bộ 20–90 giây, trang bị ban đầu 2–5 phút, đọc bo, di chuyển/giao tranh, kết thúc và kết quả; kết quả chỉ trao thống kê/replay tóm tắt, không trao sức mạnh cho trận sau.

**FR003 — Win, loss and elimination:** Solo thắng khi là người sống cuối; Duo/Squad thắng khi còn ít nhất một thành viên và mọi đội khác bị loại. HP bằng 0 loại người chơi trong Solo; trong đội, người chơi bị loại khi bị kết liễu ở trạng thái Gục hoặc khi không còn thành viên có thể chiến đấu. Standard không có hồi sinh, mua lại, tự cứu hoặc trạm triệu hồi.

**FR004 — Team modes and post-elimination flow:** Hệ thống phải hỗ trợ Solo, Duo và Squad bốn người. Rời trận sau khi máy bay khởi hành tính là thất bại; người bị loại có thể xem đồng đội tới khi đội bị loại, và hình phạt rời trận không áp dụng sau khi đội đã bị loại.

**FR005 — Ground movement:** Người chơi phải có đi bộ 2,3 m/s, chạy 4,5 m/s, chạy nước rút 6,3 m/s với 0,35 giây đưa súng lên sau khi dừng, ngồi 1,8 m/s với recoil dọc ×0,80 và nằm 0,8 m/s với recoil dọc ×0,60; không có stamina bar.

**FR006 — Traversal and posture:** Người chơi phải nhảy tối đa 0,9 m với recovery 0,45 giây và không ADS trên không; leo/vượt vật cản 0,6–1,4 m trong 0,45–0,90 giây, khóa bắn và tạo âm thanh; nghiêng tối đa 18° trong 0,15 giây với tốc độ ×0,65. Rơi trên 3 m bắt đầu gây sát thương và từ 8 m có thể tử vong khi không đầy máu.

**FR007 — Water traversal:** Nước sâu phải giảm tốc người chơi còn 2,0 m/s, khóa vũ khí và cho phép lặn tối đa 20 giây trước khi mất HP.

**FR008 — Health and hit regions:** Mỗi người chơi có 100 HP, không tự hồi; damage modifier là đầu ×2,20, ngực ×1,00, bụng ×0,90 và tay/chân ×0,75.

**FR009 — Armor and helmets:** Áo giáp cấp 1/2/3 giảm damage thân 15%/30%/45% với durability 160/220/280; mũ cấp 1/2/3 giảm damage đầu 30%/45%/55% với durability 80/150/230. Viên đạn làm durability về 0 vẫn được giảm damage, sau đó trang bị bị phá.

**FR010 — Healing and boost:** Băng dùng 3,5 giây, hồi 10 HP trong 4 giây và không vượt 75 HP; túi cứu thương dùng 6 giây, đưa HP lên 75 và bị ngắt bởi di chuyển/damage; bộ cứu thương lớn dùng 9 giây và đưa HP lên 100; nước tăng lực dùng 4 giây cho 40 boost; thuốc giảm đau dùng 6 giây cho 60 boost; boost tối đa 100.

**FR011 — DBNO and revive:** Trong Duo/Squad, HP về 0 gây Gục với 100 bleed HP, mất 2 HP/giây lần đầu và gấp đôi sau mỗi lần gục tiếp theo. Hồi đồng đội mất 10 giây và bị ngắt khi người cứu di chuyển/chịu damage. Người gục chỉ bò 0,7 m/s, ping và voice; không bắn, hồi máu hoặc tự cứu.

**FR012 — Inventory capacity and slots:** Cơ thể có 50 capacity; ba cấp ba lô tăng tổng lên 120/180/250. Inventory có hai ô súng chính, một súng ngắn, một cận chiến và một vật ném đang chọn; ammo, healing và throwables dùng capacity, attachment đã gắn không dùng capacity.

**FR013 — Pickup behavior:** Quick pickup mất 0,20 giây mỗi món; drag/drop UI không làm chậm thời gian trận. Không auto-pickup vũ khí, giáp hoặc attachment; người chơi chỉ có thể bật auto-pickup đúng cỡ ammo tới ngưỡng tự đặt.

**FR014 — Weighted loot:** Mọi người bắt đầu không loadout. Spawn point thuộc nhóm logic theo loại không gian và item cụ thể được chọn bằng weighted randomness mỗi trận. Sau 90 giây loot một compound trung bình, mục tiêu là 95% có ít nhất một súng, 70% có vũ khí chính, 50% có giáp hoặc mũ và 35% có healing.

**FR015 — Loot geography:** Khu dân cư nhỏ ưu tiên trang bị cơ bản; quân sự, cảng và công nghiệp có loot tốt hơn nhưng nhiều hướng tiếp cận và tranh chấp cao hơn. Không vật phẩm thiết yếu nào bị giới hạn chỉ trong airdrop.

**FR016 — Airdrop:** Mỗi pha bo 1–5 phải có một airdrop tại vị trí tiếp cận được, khói thấy từ 800 m, chứa một vũ khí đặc biệt cùng armor/healing cấp cao.

**FR017 — Throwables:** Frag có fuse 5 giây, lethal radius 3 m và damage tới 8 m; smoke phát sau 1,5 giây, tồn tại 25 giây với đường kính 12 m; stun có fuse 2,5 giây và hiệu lực tối đa 5 giây trong 5 m có line of sight; incendiary cháy 12 giây trong vùng 4 m, gây 10 damage/giây.

**FR018 — Throwable handling:** Capacity phải giới hạn người chơi ở tối đa sáu throwables; trajectory preview chỉ hiện trong 1,5 giây đầu khi ngắm.

**FR019 — Vehicles:** Hệ thống phải cung cấp sedan bốn chỗ, jeep bốn chỗ, pickup bốn chỗ, motorcycle hai chỗ, boat bốn chỗ và truck sáu chỗ; tốc độ tối đa 80–125 km/h, âm nghe 250–450 m. Xe dùng fuel, có tire damage, cháy cảnh báo ba giây trước explosion khi HP về 0; va chạm trên 35 km/h gây damage và trên 70 km/h có thể knock người không có cover. Không có xe bọc thép mua ngoài trận.

**FR020 — Semantic input:** Gameplay chỉ tiêu thụ semantic command chung; Keyboard/Mouse, Touch và Gyro là input adapter, không tạo luật gameplay theo nền tảng.

**FR021 — Keyboard and mouse controls:** Default mapping phải bao phủ WASD movement, mouse camera/aim, Shift sprint, Ctrl walk, C crouch, Z prone, Space jump/vault, Q/E lean, F interact, R reload, G throwable và Tab inventory.

**FR022 — Touch controls:** Touch landscape phải có left movement stick, right look region, right fire và optional left fire, contextual stance/interact/reload/ADS/throwable/vehicle controls; layout, size và opacity lưu theo device class.

**FR023 — Gyro and touch fairness:** Gyro là optional aim input. Touch không có target snap, auto-fire, enemy detection hoặc visual footstep indicator; aim slowdown/friction chỉ có thể được cân nhắc sau fairness prototype trong Touch pool và mặc định tắt.

**FR024 — Camera and anti-peek:** Standard dùng TPP với shoulder swap; ADS dùng first-person sight. Camera phải đẩy về trước gần tường và không render object/opponent nếu line of sight từ đầu nhân vật bị che hoàn toàn.

**FR025 — Control customization:** Người chơi phải remap toàn bộ keyboard hoặc Touch layout, chỉnh sensitivity riêng cho hip-fire/ADS/từng zoom và chọn hold/toggle cho ADS, lean, crouch và sprint.

**FR026 — Weapon roster:** v1.0 target gồm 3 pistol, 3 SMG, 3 shotgun, 5 AR, 3 DMR, 3 sniper, 2 LMG và 3 melee (25 weapons); 5 ammo calibers; 4 muzzle, 4 grip, 3 magazine, 2 stock và 7 sight types. Weapon không level-up, không mang qua trận và không có skin trong v1.0.

**FR027 — Weapon ballistic baselines:** Pistol/SMG/Shotgun/AR 5.56/AR 7.62/DMR/Bolt sniper/LMG lần lượt có baseline damage 35/31/9×18/41/47/55/85/43; RPM 450/800/75/700/600/300 max/45/650; magazine 15/30/5/30/30/10/5/60; velocity 350/400/350/820/715/780/850/750 m/s; tactical reload 1,8/2,3/0,65 mỗi viên/2,6/2,9/2,7/3,5/5,5 giây; falloff 40→150/50→200/25→80/100→500/80→450/180→800/300→1.000/120→600 m và giữ 55% base damage sau mốc cuối. Primary weapons không hitscan.

**FR028 — Spread and recoil baselines:** Pistol/SMG/Shotgun/AR 5.56/AR 7.62/DMR/Bolt sniper/LMG có ADS time 0,18/0,22/0,24/0,28/0,30/0,33/0,42/0,32 giây; hip spread 2,4°/2,0°/5,0°/2,6°/2,8°/3,0°/3,2°/3,2°; ADS spread 0,10°/0,09°/3,5° pellet/0,06°/0,07°/0,04°/0,02°/0,10°; vertical recoil 1,0°/0,7°/4,0°/0,9°/1,2°/2,0°/5,5°/1,0° và horizontal recoil ±0,40°/±0,35°/±1,50°/±0,45°/±0,60°/±0,80°/±1,00°/±0,55°.

**FR029 — Fire behavior and TTK:** AR target TTK ở 20 m là 0,17–0,25 giây không giáp và 0,25–0,40 giây qua armor level 2; standard AR 5.56 là 3 hits/0,171 giây và 4 hits/0,257 giây, AR 7.62 là 3 hits/0,200 giây và 4 hits/0,300 giây. Recoil tăng trong 8 viên đầu, ổn định sau viên 12; dừng 0,25 giây bắt đầu recovery. Spread modifier: crouch ×0,75, prone ×0,55, walk ×1,30, run ×2,20, jump ×4,00.

**FR030 — Combat feedback:** Mỗi shot phải có report, mechanical sound, muzzle flash, casing và camera reaction riêng. Standard không hiển thị floating damage. Hit phản hồi bằng blood/dust theo setting, âm nhẹ và body reaction; kill chỉ xác nhận sau server. Người bị bắn nhận direction indicator cung 30°, không nhận vị trí hoặc khoảng cách shooter.

**FR031 — Aim and melee:** Combat phải có TPP hip-fire, over-shoulder aim và ADS; scope từ 4× cho hold breath tối đa 8 giây rồi sway ×2 trong 4 giây; zeroing 100–800 m theo bước 100 m; aim punch tối đa 1,5°/hit với threshold 0,12 giây. Mouse không aim assist, magnetism hoặc curved bullet. Melee có range 1,8 m, wind-up 0,35–0,55 giây và damage 35–60.

**FR032 — Match authority:** Match server phải xác nhận position, shot, damage, ammo, loot, vehicle, zone và win/loss; client không được quyết định competitive outcome.

**FR033 — Network combat behavior:** Lag compensation tối đa 150 ms; vượt ngưỡng hiển thị connection warning. Region target là median ping ≤80 ms và packet loss <1%; nếu không có region đạt ngưỡng, Standard chỉ bắt đầu sau khi người chơi xác nhận. Hit trade được chấp nhận khi cả hai shot hợp lệ rời nòng trước elimination; evidence phải giữ confirmation order.

**FR034 — AI scope:** Standard chỉ có human opponents, không monster/boss/combat NPC và không silent bot fill. Experimental bot queue phải disclose bot count trước khi vào trận. Training Grounds có static targets, moving targets 2–8 m/s và bots với ba hành vi chạy qua khoảng trống, đổi cover, peek/fire; training không ảnh hưởng competitive stats.

**FR035 — Đảo Vọng content:** Map target là 8×8 km với khoảng 58% mainland, 12% small islands và 30% water/unwalkable boundary; 18 named POI, 55 small compounds, ít nhất 420 enterable buildings, 180 weighted vehicle positions và 12 boat docks.

**FR036 — Tactical map rules:** Combat distance target là 0–25 m indoor, 40–150 m village/forest, 150–400 m field/hill/road và 400–800 m chỉ ở selected sightline. Mỗi open span trên 120 m phải có ít nhất hai lựa chọn từ hard cover, depression, smoke, vehicle hoặc detour. Bridge/pass là choke có slower bypass; không có single mandatory choke vào circle. Final circle không đặt quá 50% trên water, unstandable cliff hoặc inaccessible roof. Cover tĩnh; không phá nhà, đào đất hoặc xây fortification.

**FR037 — Weather:** Match chọn clear 70%, rain 15% hoặc fog 15% lúc bắt đầu và không đổi đột ngột. Rain giảm footstep hearing 15%; fog giới hạn target contrast sau 180–250 m. Không full darkness; bốn default outfits phải nằm trong detection variance 5%.

**FR038 — Matchmaking and team counts:** Solo có 100 người, Duo tối đa 50 đội và Squad 25 đội bốn người. Matchmaking ưu tiên network region và wait time; soft MMR chỉ tách người mới khỏi nhóm kỹ năng cao nhất trong 10 trận đầu.

**FR039 — Input pools:** Keyboard/Mouse pool dành cho Windows/Linux/macOS, Touch pool cho Android/iOS. Mixed party vào Mixed/Keyboard-Mouse pool sau disclosure trước ready. Input family được lock trong match; external keyboard/mouse trên mobile buộc leave queue và requeue. Không silent bot fill, silent pool switch hoặc fairness-rule relaxation.

**FR040 — Shared online identity:** Account, progression, party và backend dùng chung; mọi platform dùng cùng balance data, protocol và server authority. Mobile client không nhận thêm combat information.

**FR041 — Team communication and friendly fire:** Team có voice, location ping và tám contextual pings; ping không auto-detect enemy qua obstacle. Friendly fire bật 100% sau khi lên máy bay; UI hiển thị damage source và có report flow.

**FR042 — Standard ruleset:** Standard là mode chính; không đổi viewpoint hoặc loot rules trong cùng queue. Ranked, public custom server và tournament tools hoãn tới khi Standard ổn định; FPP-only chỉ là post-v1 candidate nếu population không bị phân mảnh.

**FR043 — Safe-zone schedule:** Hệ thống phải thực hiện chín phase: P1 wait/shrink 4:00/4:00, radius 2.500 m, 0,4 HP/s, target 70–85 alive; P2 2:30/3:30, 1.600 m, 0,7 HP/s, 50–65; P3 2:00/3:00, 1.000 m, 1,2 HP/s, 35–50; P4 1:30/2:30, 600 m, 2,0 HP/s, 22–35; P5 1:15/2:00, 360 m, 3,5 HP/s, 14–24; P6 1:00/1:30, 180 m, 6 HP/s, 8–16; P7 0:45/1:00, 90 m, 9 HP/s, 4–10; P8 0:30/0:45, 45 m, 14 HP/s, 2–6; P9 0:15/0:30, 0 m, 20 HP/s, một đội.

**FR044 — Safe-zone behavior:** Circle center có land-playability weight nhưng vẫn bất định; next center lộ lúc wait phase bắt đầu; không có forecast item hoặc random bombing zone. Phase 1–3 cho deliberate outside-zone heal/travel, từ phase 6 không còn là chiến thuật bền vững.

**FR045 — In-match progression:** Gear curve phải đi từ tay trắng tới self-defense trong 0–3 phút; hoàn thiện hai weapon roles, basic bag/armor và route trong 3–10 phút; nâng attachment/healing/throwables và tranh vị trí/airdrop trong 10–22 phút; từ phút 22, position, smoke, information và trigger discipline phải quan trọng hơn loot.

**FR046 — Account progression:** Không stat, perk, weapon, attachment hoặc capacity tăng ngoài trận. Profile lưu match count, top 10, wins, kill distance, accuracy và season history. Weapon Mastery chỉ mở advanced stats và profile badge, không skin hoặc power. Long-term achievement reward không hết hạn và không đòi daily login.

**FR047 — Product integrity and commerce:** v1.0 không có in-game store, premium currency, microtransaction, loot box, gacha, battle pass, daily login streak, ads hoặc live-event. Map, weapon và gameplay rules thuộc cùng product entitlement. Mọi commerce proposal hậu v1 phải qua post-launch vision gate.

**FR048 — Balance governance:** Không common-loot weapon nào vượt 22% kills trong mẫu ≥10.000 kills; airdrop weapon không vượt 8% kills và phải có measurable access risk. Drop-site win rate không vượt ±20% quanh mean sau skill/team-size control. Mỗi archetype có ít nhất một favorable và một unfavorable context. Balance change không gắn commercial calendar và phải được thử nghiệm/công bố lý do bằng data.

**FR049 — Spatial layout rules:** High-loot POI cách nhau 800–1.500 m và có ít nhất hai land routes; mỗi major POI có một vehicle-free escape route không chậm hơn main route quá 70%; combat roof có hai approaches hoặc một blind spot; 80% combat windows dùng consistent height/silhouette; penetration material có visual language nhất quán; signage/material color/place name hỗ trợ navigation không chỉ dựa minimap.

**FR050 — Art direction:** Visual phải restrained-realistic, ưu tiên readable silhouette/material; saturated color chỉ cho critical gameplay information. Character không có hero silhouette, aura, wing, combat pet hoặc luminous outfit. Weapon dùng fictional name/shape/sound; blood có reduce/recolor setting nhưng hit clarity tương đương.

**FR051 — HUD:** In-match HUD chỉ hiển thị HP/boost, ammo, stance, compass, minimap, team status và zone phase; không store, mission, ad hoặc battle-pass banner.

**FR052 — Inventory and map UI:** Desktop inventory tối đa 70% screen. Mobile inventory là tabbed panel tối đa 62% width và giữ ≥38% world-risk strip. Full map hiển thị flight path, current/next circle, team marker và place name; không loot hoặc opponents.

**FR053 — Audio behavior:** Không background music khi player còn sống; music chỉ ở menu, results và victory. Run/walk/slow-walk footsteps nghe tới 70/45/20 m với distinct material spectra; unsuppressed guns nghe tới 1.000 m và suppressed 400–600 m; vehicles 250–450 m. Aircraft/airdrop không được mask hoàn toàn nearby combat gunfire.

**FR054 — Accessibility:** Hệ thống phải hỗ trợ full key/Touch remap, hold/toggle, FOV, per-mode sensitivity, Gyro, haptic, camera shake và flash intensity; ba color-blind presets cho zone/marker/hit/reticle; item tier không chỉ dùng color; subtitle cho system message và team ping; competitive queue không có visual footstep indicator.

**FR055 — Voice permission and interruption:** Voice permission chỉ hỏi theo ngữ cảnh; focus loss, phone call và audio-route change không được làm input bị kẹt hoặc voice phát ngoài ý muốn.

**FR056 — Cross-platform contract:** Một gameplay core, weapon/loot/zone data, authoritative simulation và network protocol phải phục vụ Windows, Linux, macOS, Android và iOS. Platform difference chỉ nằm sau input adapter, presentation/quality profile, lifecycle, secure storage, identity/invite/permission và release pipeline; collision và gameplay visibility không được đổi theo quality profile.

**FR057 — Mobile lifecycle:** Mobile client phải thực hiện `Active → Interrupted → Backgrounded → Reconnecting → Restored/Timed out/Team eliminated/Match ended`; resume không giữ slot vô hạn và không tạo immunity.

**FR058 — Integrity operations:** Release phải có player report, block, match log và evidence replay cho investigation. Team-kill lặp lại và cheating có review process riêng; server-authoritative result phải được giữ khi disconnect/reconnect.

**Total FRs: 58**

### Non-Functional Requirements

**NFR001 — Engine and release platforms:** v1.0 phải dùng Godot 4.x và phát hành Windows 10/11 x64, Linux x64, macOS 13+ Intel/Apple Silicon, Android 10+ ARM64 và iOS 16+ ARM64.

**NFR002 — Input and display scope:** Input family v1 là Keyboard/Mouse và Touch; controller/console ngoài scope. Desktop hỗ trợ 1280×720–3840×2160 cùng ultrawide, baseline 1920×1080; mobile landscape phone/tablet phải tôn trọng safe area/notch.

**NFR003 — Desktop hardware classes:** Minimum target là CPU bốn nhân đời 2017, 8 GB RAM, GTX 1060/RX 580-class GPU và SSD; recommended target là CPU sáu nhân đời 2020, 16 GB RAM và RTX 2060/RX 6600-class GPU.

**NFR004 — Mobile hardware classes:** Minimum target là Snapdragon 778G/Dimensity 920-class với 6 GB hoặc iPhone 11/A13; recommended là Snapdragon 8 Gen 1/Dimensity 8100-class với 8 GB hoặc iPhone 13/A15.

**NFR005 — Desktop minimum performance:** Trên minimum desktop, standard replay 30 phút gồm city, vehicle, smoke và final circle phải đạt 60 FPS median và p95 frame time ≤25 ms ở 1080p/Low.

**NFR006 — Desktop recommended performance:** Trên recommended desktop với cùng replay, phải đạt 90 FPS median và p95 ≤16,7 ms ở 1080p/High.

**NFR007 — Desktop memory:** Client phải dùng ≤6 GB RAM sau trận 45 phút đi qua ba map regions.

**NFR008 — Desktop load time:** Cold-cache minimum SSD phải đi từ matchmaking confirmation tới pre-match lobby trong ≤45 giây p95.

**NFR009 — Mobile minimum performance:** Minimum mobile phải đạt 45 FPS median và p95 frame time ≤33,3 ms ở Low trong standard replay và thermal soak.

**NFR010 — Mobile recommended performance:** Recommended mobile phải đạt 60 FPS median và p95 frame time ≤25 ms ở Medium trong standard replay và thermal soak.

**NFR011 — Mobile memory and lifecycle reliability:** Working memory mobile ≤3 GB và không bị OS termination trong trận 45 phút gồm foreground/background transitions.

**NFR012 — Mobile thermal:** FPS median không giảm quá 15% sau 30 phút thermal soak trên representative devices.

**NFR013 — Mobile load time:** Minimum mobile cold cache phải vào pre-match lobby trong ≤60 giây p95 từ matchmaking confirmation.

**NFR014 — Crash-free reliability:** Crash-free sessions phải ≥99,5% trong cửa sổ 30 ngày.

**NFR015 — Server simulation:** Match server phải giữ 30 Hz ổn định cho 100 players với ≥10% load headroom trong soak 45 phút và final-circle stress; Alpha target envelope là ≤8 vCPU/16 GB mỗi match.

**NFR016 — Damage latency:** Damage event phải được xử lý trong ≤1 server tick ở p95 với 100 players, 80 ms RTT và 1% packet loss.

**NFR017 — Client bandwidth:** Average network traffic phải ≤1,5 Mbps mỗi chiều/client trong trận 100 người 30 phút.

**NFR018 — Network positional accuracy:** Visible position versus confirmed position phải lệch ≤0,5 m p95 ở 80 ms RTT/1% packet loss; lag compensation không vượt 150 ms.

**NFR019 — Regional connectivity:** ≥95% players trong launch region phải được ghép vào region có median ping ≤80 ms; region target packet loss <1%.

**NFR020 — Install and patch budget:** Desktop install ≤25 GB, mobile install ≤12 GB; balance patch không buộc tải lại >2 GB unchanged content.

**NFR021 — Smoke load:** Client phải giữ minimum FPS target với tối đa sáu dense smoke volumes đồng thời trong bán kính 100 m quanh một player.

**NFR022 — Audio localization:** Stereo/HRTF phải cho tester xác định đúng cung 30° của nguồn âm ở ≥85% trials trong cự ly 20–80 m.

**NFR023 — Touch UI sizing:** Mobile touch target tối thiểu 48 logical units; fire, exit-vehicle và close tối thiểu 64 khi safe area cho phép.

**NFR024 — Information parity:** Renderer/LOD/dynamic-resolution và desktop/mobile visual variants không được thay collision, cover, silhouette, openings hoặc gameplay visibility; bốn default outfits phải nằm trong 5% detection variance.

**NFR025 — Valid match completion:** ≥99,0% matches phải được server kết thúc với valid result.

**NFR026 — Hitreg quality:** <0,5% valid shots tạo complaint mà evidence replay xác nhận sai >0,5 m hoặc >1 tick.

**NFR027 — Population viability:** Mỗi input pool phải chứng minh đủ population cho trận 100 người trong approved wait threshold; không bot hoặc silent pool fallback để đạt metric.

**NFR028 — Match duration:** Median match duration 28–32 phút và p90 không vượt 35 phút.

**NFR029 — Survival curve:** ≥80% beta matches phải nằm trong alive-count target của bảng chín phase.

**NFR030 — Loot availability:** 60–75% players có primary weapon trong 90 giây và <5% không tìm thấy súng sau khi loot hết một average compound.

**NFR031 — Death readability:** ≥80% playtesters phải giải thích được quyết định chính dẫn tới death; ≥90% death situations phải được independent viewer giải thích đúng từ internal replay.

**NFR032 — Positional value:** ≥70% testers rating “position và information quan trọng hơn gear rarity” ở mức 4/5+; win-rate gap giữa armor level 2 và 3 dưới 8 percentage points sau skill control.

**NFR033 — Resource-tradeoff comprehension:** ≥60% testers phải chỉ ra được ít nhất một resource tradeoff quyết định match outcome.

**NFR034 — Competitive acquisition integrity:** 100% gameplay-affecting equipment chỉ có thể tiếp cận bằng action trong match, không bằng money/account progression; không common archetype nào vượt 22% kills trong sufficiently large balance sample.

**NFR035 — Release validation:** Performance thresholds phải đạt trong ba soak sessions liên tiếp; v1 chỉ pass khi full 100-player loop, bốn pillars và release-candidate family cùng đạt trên Windows, Linux, macOS, Android và iOS.

**Total NFRs: 35**

### Additional Requirements

**Production gates:** R1 yêu cầu 8-client Combat Sandbox cùng five-platform smoke và desktop/mobile command/network path; R2 yêu cầu staffing re-estimate, 24 mixed clients, Touch HUD/lifecycle và pass mobile memory/thermal/information parity; R3 yêu cầu 100-client protocol mix, server ≤8 vCPU/16 GB, device lab và population test từng pool; R4 yêu cầu QA/security/backend, signing/certification, regional operations, beta 100 người thật và release-candidate family trên cả năm platforms.

**Content lock constraint:** 25 weapons, 6 vehicles, 18 POI, 420 enterable buildings, 8 architecture kits, 4 default outfits và map 8×8 km là target tạm thời; chỉ được khóa sau mobile viability và server-scale gates. Core loop/platform parity được ưu tiên nếu cần scope change.

**Permanent exclusions from Standard:** Pay-to-win, paid stats/weapons, loot box, gacha, expiring battle pass, hero/class/ultimate, supernatural skill, combat pet, out-of-match loadout, respawn/self-revive/buyback/summon station, branded ads/event stage và luminous cosmetics trong Standard.

**v1 exclusions:** Console/controller/aim assist, second map, PvE campaign/zombie/boss/story missions, ranked/esports/public custom server/modding/UGC, destructible building/terrain/base building/crafting/hunger/thirst/body temperature, full user replay/competitive kill-cam/advanced spectator, dynamic weather/day-night/natural disaster và all store/premium currency/login mission/collab/live-event systems.

**Assumptions:** A-001 Đảo Vọng/theme Đông Nam Á có thể đổi không ảnh hưởng core loop; A-002 preferred commercial model là one-time purchase nhưng price/server cost cần business validation; A-003 team size/budget chưa xác định và milestones là learning gates; A-004 PC-first staffing envelope đã bị thay thế, five-platform scope phải được re-estimate trước R2; A-005 100 players/8×8 km là v1 north-star nhưng breadth chỉ lock sau scale/mobile proof.

**Dependencies:** Regional server infrastructure; đủ testers cho mốc 24 và 100; legal review cho weapon names/shapes/sounds/referenced assets; Godot architecture proof cho streaming/network/100-player simulation; macOS/Xcode/provisioning/real Apple devices; Android ARM64 AAB/Gradle/signing/device lab.

**Unresolved non-blocking business decisions:** One-time purchase price và long-term server policy; final island name/theme; launch-region order after closed beta.

### GDD Completeness Assessment

GDD v1.1.0 có phạm vi, mechanic baselines, measurable acceptance criteria, five-platform contract, production gates và explicit exclusions đủ mạnh để làm nguồn truy vết. Điểm chưa khóa chủ yếu nằm ở business/staffing/region decisions và empirical feasibility; chúng không ngăn bắt đầu Combat Sandbox nhưng ngăn phê duyệt R2/R3, content lock và v1 release. GDD tự mô tả `ready-for-architecture`; Architecture hiện đã hoàn tất, nên readiness assessment phải kiểm tra Epics có biến toàn bộ 58 FR, 35 NFR và production gates thành stories/acceptance criteria hay chưa.

## Epic Coverage Validation

`epics.md` không chứa FR-ID map vì các FR được chuẩn hóa trong assessment này sau khi GDD được viết. Coverage dưới đây vì vậy là mapping do assessment suy ra từ story ownership; nó chứng minh đường triển khai ở mức high-level, không chứng minh story quality hoặc acceptance-criteria completeness.

### Coverage Matrix

| FR | GDD requirement | Epic/story coverage | Status |
|---|---|---|---|
| FR001 | Standard 100-player, start empty, loot/zone/last survivor | E4-S1–S6; E6-S1/S7 | Covered |
| FR002 | Full lobby→drop→loot→zone→result loop | E4-S1–S7 | Covered |
| FR003 | Win/loss, elimination, no respawn | E4-S4/S5 | Covered |
| FR004 | Solo/Duo/Squad, leave/spectate flow | E4-S5/S6/S8 | Covered |
| FR005 | Walk/run/sprint/crouch/prone baselines | E1-S1/S2/S7 | Covered |
| FR006 | Jump/fall/vault/lean | E1-S2/S3/S7 | Covered |
| FR007 | Swimming, deep-water speed, weapon lock and diving | **NOT FOUND** | **Missing** |
| FR008 | HP and hit-region modifiers | E2-S4 | Covered |
| FR009 | Armor/helmet reduction and durability | E2-S4; E3-S6 | Covered |
| FR010 | Healing/boost timing, effects and interruption | E3-S4 | Covered |
| FR011 | DBNO, bleed, revive and restrictions | E4-S4 | Covered |
| FR012 | Capacity, backpacks and equipment slots | E3-S2/S6 | Covered |
| FR013 | Pickup timing, drag/drop and bounded ammo auto-pickup | E1-S5; E3-S2/S3/S9 | Covered |
| FR014 | Empty start, weighted loot and 90-second availability | E3-S1/S8 and E3 gate | Covered |
| FR015 | Loot geography and no essential airdrop-only item | E3-S1/S7 | Covered |
| FR016 | Airdrop phases, smoke and high-tier contents | E3-S7 | Covered |
| FR017 | Four throwables and exact behavior | E3-S5 | Covered |
| FR018 | Throwable capacity and trajectory-preview constraint | E3-S2/S5 | Covered |
| FR019 | Six vehicles, fuel/tire/HP/explosion/collision | E5-S5/S6/S9 | Covered |
| FR020 | Shared semantic input | E1-S8 | Covered |
| FR021 | Keyboard/mouse default controls | E1-S6/S8 | Covered |
| FR022 | Landscape Touch controller and saved layout | E1-S9; E7-S10 | Covered |
| FR023 | Optional Gyro and prohibited Touch assists | E2-S9; E7-S11 | Covered |
| FR024 | TPP/ADS/shoulder swap and anti-peek | E1-S4 | Covered |
| FR025 | Full remap, sensitivity and hold/toggle | E1-S6; E7-S10/S11 | Covered |
| FR026 | v1 weapon/ammo/attachment roster and no weapon skins | E2-S6/S7; E8-S3 | Covered |
| FR027 | Damage/RPM/magazine/velocity/reload/falloff baselines | E2-S2/S6 | Covered |
| FR028 | ADS/spread/recoil baselines | E2-S3/S6 | Covered |
| FR029 | TTK, recoil recovery and stance modifiers | E2-S3/S8 | Covered |
| FR030 | Shot/hit/damage feedback, no floating damage | E2-S5 | Covered |
| FR031 | Aim states, breath, zeroing, aim punch, no assist and melee | E2-S1/S6/S7/S9 | Covered |
| FR032 | Authoritative competitive state | E2-S8; E6-S1 | Covered |
| FR033 | Lag cap, region confirmation, position error and hit trade | E2-S8; E6-S3/S5/S8 | Covered |
| FR034 | Humans-only Standard and disclosed training bots | E6-S9; E7-S7 | Covered |
| FR035 | 8×8 km Đảo Vọng and content targets | E5-S1/S2/S6 | Covered |
| FR036 | Combat distances, open-space options, choke/final-circle rules | E5-S3/S6 | Covered |
| FR037 | Clear/rain/fog distribution and readability | E5-S7; E7-S9 | Covered |
| FR038 | Team counts, region/wait preference and newcomer soft MMR | E4-S6; E6-S5 | Covered |
| FR039 | Touch/Keyboard/Mixed pools, disclosure and match lock | E6-S5/S9 | Covered |
| FR040 | Shared account/progression/party/balance/protocol | E6-S4; E8-S1/S8 | Covered |
| FR041 | Voice, contextual pings and friendly fire | E6-S4; E4-S6 | Covered |
| FR042 | Stable Standard rules; defer ranked/custom/FPP | E6-S5/S9; E8-S4/S5 | Covered |
| FR043 | Exact nine-phase safe-zone schedule | E4-S3 | Covered |
| FR044 | Zone reveal, land weight and no bombing zone | E4-S3; E5-S6 | Covered |
| FR045 | In-match progression curve | E3; E4; E5 gates | Covered |
| FR046 | Non-power profile, stats, mastery and permanent achievements | E8-S1/S2 | Covered |
| FR047 | No v1 commerce/FOMO; common gameplay entitlement | E8-S3–S7 | Covered |
| FR048 | Weapon/drop-site/archetype balance governance | E3-S8; E8-S5/S6; E9-S7 | Covered |
| FR049 | POI route/roof/window/material/navigation layout rules | E5-S3/S4/S6 | Covered |
| FR050 | Restrained, readable art and cosmetic constraints | E7-S9; E8-S4 | Covered |
| FR051 | Minimal in-match HUD without commerce | E7-S1; E8-S4 | Covered |
| FR052 | Desktop/mobile inventory and map information contract | E3-S9; E7-S2/S10 | Covered |
| FR053 | Music, footsteps, gun and vehicle audio behavior | E7-S3–S5 | Covered |
| FR054 | Remap, visual/audio/accessibility settings | E1-S6; E7-S6/S10/S11 | Covered |
| FR055 | Contextual voice permission and audio interruption | E6-S4; E7-S11 | Covered |
| FR056 | Shared five-platform core and presentation-only variants | E1-S8/S9; E5-S8/S9; E6; E9-S6/S9 | Covered |
| FR057 | Explicit mobile lifecycle | E4-S9; E6-S6; E7-S11; E9-S10 | Covered |
| FR058 | Report, block, evidence, moderation and reconnect result | E6-S6/S8; E9-S3–S5 | Covered |

### Missing Requirements

#### High Priority — FR007 Water Traversal

**Requirement:** Nước sâu phải giảm tốc người chơi còn 2,0 m/s, khóa vũ khí và cho phép lặn tối đa 20 giây trước khi mất HP.

**Impact:** Không có story sở hữu state transition ground↔swim↔dive, underwater weapon restriction, breath/HP, animation/camera/input, authoritative replication hoặc mobile controls. E5-S5 chỉ sở hữu boat; E5-S1/S6 chỉ sở hữu coast/water map data. Nếu không bổ sung, 30% water/boundary của Đảo Vọng và WaterVolume architecture sẽ có hành vi không được triển khai/kiểm thử.

**Recommendation:** Thêm story **E1-S10 — Swimming and Diving Survivor Controller** cho movement/state/input/camera và mở acceptance dependency sang E5 water volumes cùng E6 authoritative replication. Story phải được hoàn thành trước World/Network/Mobile Slice 2×2 km.

### Epic Requirements Not Explicitly Originating as GDD FRs

- E8-S8 mở rộng privacy/account-data lifecycle và secure entitlement từ platform boundary thành story riêng.
- E9-S3 mở rộng alert/runbook; E9-S8 thêm rollback và post-release data verification.
- E6-S9 dùng signed input-family claim như giải pháp Architecture cho GDD match-lock requirement.

Đây là operational/architecture elaboration hợp lệ, không phải scope drift.

### Coverage Statistics

- Total GDD FRs: **58**
- Fully covered in high-level epics: **57**
- Missing: **1**
- Coverage: **98.3%**
- Traceability caveat: Epic document chưa gắn FR IDs; mapping hiện do readiness report duy trì.

## UX Alignment Assessment

### UX Document Status

**Found and final.** Canonical UX gồm `DESIGN.md` (visual system, 30 components) và `EXPERIENCE.md` (IA, behavior, state, input, flows). `final-ux-verification.md` báo **20 Closed · 5 Accepted dependency · 0 Open**; mobile delta báo **8 Closed · 0 Open · 3 implementation dependencies**. Hai spine là complementary sources, không duplicate.

### UX ↔ GDD Alignment

| Area | Assessment |
|---|---|
| Core Standard journey | Minh/Lan/Quân/Mai flows bao phủ Solo, Squad, onboarding/training và full mobile lifecycle; không thay core loop GDD |
| Information integrity | HUD chỉ giữ bảy content groups, không enemy cue, footstep radar, damage number, loot recommendation hoặc next-zone prediction |
| Desktop/mobile input | Shared semantic commands, Touch/Gyro, remap và input-pool disclosure khớp GDD; không mobile-only aim/information assistance |
| Inventory risk | GDD desktop ≤70% được UX siết thành panels ≤68%/world ≥32%; mobile giữ đúng ≤62%/≥38%; đây là refinement tương thích |
| Map/zone | Flight path/current/next zone, marker và place name khớp; next zone chỉ sau server-confirmed wait phase |
| Audio | No music while alive, directional combat audio, voice/ping và ≥85% 30° metric khớp GDD; UX chỉ tách internal/output controls rõ hơn |
| Accessibility | Color+shape+label, remap, UI scaling, subtitles, Gyro/haptic, reduced motion/flash và contextual permission mở rộng GDD nhưng không tạo combat information |
| Product integrity | IA không Store/News/Reward rail/FOMO; UX tone/motion không thêm commerce loop |
| Visual fairness | Central 16:9 competitive frame, anti-peek, same information density và desktop/mobile collision/visibility parity khớp GDD |

**Conclusion:** Không phát hiện UX requirement nào trực tiếp mâu thuẫn GDD. Field Orientation là optional, skippable, replayable và không reward/stat, nên là elaboration hợp lệ của E7 onboarding thay vì meta-progression mới.

### UX ↔ Architecture Alignment

Architecture hỗ trợ các contract chính bằng Godot `Control`/`Container`/`Theme`, 30-component contract, presenter + immutable `ViewState`, desktop/mobile layout composition riêng dùng chung state, `safe-area-root`, semantic input adapters, explicit lifecycle state machines, platform/voice adapters, central 16:9 fairness, native audio/spatial test và five-platform CI/device gates. UI không đọc packet hoặc authoritative entity trực tiếp; đây là boundary đúng cho server-confirmed reticle, heal/revive, map/zone và result states.

### Alignment Issues and Story Gates

#### UXA-01 — High: Localization and font pipeline has no explicit owner

UX yêu cầu Việt/Anh, Noto Sans/Condensed/Mono, Unicode fallback cùng x-height, no missing glyph, localized aliases cho binding và snapshot trên năm platform. Architecture chỉ có `fonts/` folder và localized message key; Epics không có story sở hữu locale catalog, plural/date/number, font import/fallback, Vietnamese glyph snapshots hoặc IME decision.

**Action:** Thêm story vào E7 trước UI component production: **Localization, Font Fallback and Five-platform Text Snapshot**. Story phải khóa supported locales v1, catalog ownership, formatting policy, font license/provenance, SDF/raster profile, fallback metrics và Việt/Anh snapshot matrix.

#### UXA-02 — High: Reconnect/AFK timeout and avatar outcome remain policy gaps

Architecture xác định owner/state/token/replay protection nhưng vẫn ghi timeout, avatar protection và outcome chưa được khóa. UX cố ý chỉ hiển thị state owner trả về. E4-S8/S9 và E6-S6 không thể có deterministic acceptance criteria nếu thiếu numeric timeout, AFK behavior, DBNO/alive avatar behavior và process-eviction outcome.

**Action:** Trước khi refine E4-S8, tạo ADR/policy cho owner API, reconnect grace theo match phase, AFK neutral input, avatar vulnerability, token expiry/rotation và destinations `Restored/Timed out/Team eliminated/Match ended`.

#### UXA-03 — Medium: Input-label/raw-input acceptance remains unresolved

UX khóa full action inventory, conflict rules, non-QWERTY và extra mouse buttons nhưng raw-input default và Linux OS key display-name mapping chưa được Architecture khóa.

**Action:** E1-S6/S8 phải có spike/acceptance trên Windows/Linux/macOS cho raw mouse choice, physical-vs-logical key policy, localized OS key labels, required escape bindings và atomic Apply/Cancel persistence.

#### UXA-04 — Medium: Map orientation and zoom limits are not locked

UX định nghĩa pan/pinch/tap/long-press, damage cue và next-zone reveal nhưng ghi rõ map orientation default và zoom limits chưa khóa.

**Action:** Khóa trong E7-S2 trước implementation; lựa chọn không được đổi world-camera-relative damage cue hoặc cho thêm information range trên platform khác.

#### UXA-05 — Medium: Spectator voice/ping rights after elimination are not locked

Teammate-follow information parity đã có, nhưng quyền voice và tạo ping mới sau khi bị loại vẫn là note mở.

**Action:** Gameplay/UX policy trước E4-S6/E6-S4: mặc định spectator không tạo marker chiến thuật mới; nếu voice còn hoạt động, phải xác định rõ team-only scope và parity.

#### UXA-06 — Medium: Accessibility scope decision required before v1 readiness

UX floor đã khóa contrast, remap, color presets, subtitles, motion/flash và Touch targets; screen reader/menu narration, detailed subtitle controls, motor playtest, professional photosensitivity limits và hearing accessibility ngoài ping/subtitle vẫn chưa được scope.

**Action:** Product/accessibility decision trước E7 refinement: đưa từng mục vào v1 hoặc ghi explicit defer cùng risk/owner. Không được hiểu im lặng là “không cần”.

#### UXA-07 — Accepted dependency: Invite/report/replay provider depth

Platform invite provider, deep report taxonomy/evidence attachment/moderation SLA và deep replay payload chưa khóa. UX đã có minimum safe behavior; Architecture có adapters, evidence schema, privacy/retention và provider gates.

**Action:** Không block Combat Sandbox. Gate E6-S4, E9-S4 và Results story bằng API/schema/retention/security contract trước implementation tương ứng.

### Warnings

- Static HTML/mockup validation không thay Godot/device testing. Desktop matrix, font rendering, real notch/cutout, left-handed layout, 100/120/140% scale, multi-touch ownership, Gyro fatigue, haptic và audio-route restoration vẫn là implementation acceptance.
- UX status `final` nghĩa tài liệu UX khép kín, không có nghĩa các accepted dependencies đã được implementation chứng minh.
- Không cần thêm mockup để bắt đầu; các gap hiện tại là policy/story/architecture ownership, không phải thiếu visual reference.

## Epic Quality Review

### Structural Summary

- **9 epics**, tất cả có value statement, pillar và measurable epic gate.
- **83 entries**, nhưng chính tài liệu ghi rõ đây chỉ là **high-level stories** và acceptance criteria sẽ được tạo ở workflow khác.
- **0/83 detailed stories** có user-story statement, Given/When/Then AC, error/recovery AC, file/module ownership hoặc explicit dependency.
- Epic dependency chain chỉ đi lùi về epics trước; không có circular epic dependency.

### Epic-by-Epic Assessment

| Epic | Player/user value | Independence/dependency | Story-quality finding |
|---|---|---|---|
| E1 Survivor foundation | Pass | **Fail:** five-platform smoke gate không có setup/build story; phụ thuộc ngầm E9-S9 | E1-S1/S2 có thể tách; E1-S7 là enabler; không AC |
| E2 Reliable gunplay | Pass | Dùng E1 hợp lệ | E2-S8 gộp protocol, 8 clients, authority, lag comp và nhiều test families; quá lớn |
| E3 Survival inventory | Pass | Dùng E1/E2 hợp lệ | Armor/helmet/durability ownership chồng E2-S4 và E3-S6; không AC/error cases |
| E4 Battle-royale lifecycle | Pass | Dùng E1–E3, nhưng 24 mixed-client gate thiếu story network integration rõ | E4-S8/S9 overlap reconnect/lifecycle với E6-S6; policy timeout/outcome chưa khóa |
| E5 Đảo Vọng/vehicles | Pass | Dùng earlier outputs, nhưng E5-S2 nhắc deliverable “sau E6” | E5-S1 8×8/18 POI và E5-S2 modular kit/content target quá lớn/không độc lập |
| E6 Competitive multiplayer | Pass | Dùng E1–E5 hợp lệ | E6-S1 và S7 là epic-sized; control plane, allocator, protocol harness/fleet ownership chưa thành stories |
| E7 Clarity/accessibility | Pass | Dùng earlier outputs hợp lệ | E7-S9 18 POI/420 buildings là epic-sized; thiếu localization/font story |
| E8 Profile/product integrity | Pass ở epic level | Dùng earlier outputs hợp lệ | E8-S7 là business decision-record task, không phải implementable player story |
| E9 Stability/certification | Player release value hợp lệ | Dùng E1–E8 hợp lệ | E9-S6/S9/S10 mỗi mục bao phủ nhiều platform/test/certification systems, quá lớn |

### Critical Violations

#### EQ-01 — No implementation-ready stories or acceptance criteria

Tất cả 83 mục là title-level scope. Không mục nào có actor/value statement, Given/When/Then, happy/error/recovery paths, exact NFRs, test boundary hoặc Definition of Done. Epic gates không thay thế story AC.

**Impact:** Implementation agent phải tự suy diễn gameplay detail, architecture boundary và test expectation; story không thể estimate, review, sign off hoặc chứng minh Done độc lập.

**Remediation:** Chạy `gds-create-epics-and-stories` sau báo cáo này để tạo detailed backlog. Mỗi story phải reference FR/NFR/UX/ADR IDs, module ownership, dependencies và AC cho Keyboard/Mouse + Touch khi có player impact.

#### EQ-02 — Greenfield project initialization is unowned

Architecture yêu cầu Godot Standard 4.7.1 clean project, domain-driven monorepo, tests và exact five-platform build smoke. E1 gate yêu cầu build smoke trên năm platform, nhưng không story nào trước E1 gameplay tạo `game/project.godot`, project structure, test runner, import baseline, export presets hoặc CI smoke. E9-S9 đến quá muộn và là full release pipeline, không phải initial scaffold.

**Impact:** E1 không độc lập và không thể đạt gate; mọi story đầu tiên sẽ tự tạo cấu trúc/build convention khác nhau.

**Remediation:** Thêm story đầu E1: **Initialize Godot 4.7.1 Project and Five-platform Smoke Baseline**. Story chỉ scaffold cấu trúc cần cho first slice, pin toolchain/checksum, headless import/test và smoke Windows/Linux/macOS/Android/iOS; full signing/release vẫn ở E9.

#### EQ-03 — Several entries are epic-sized, not independently completable stories

Các mục tối thiểu cần split:

- **E2-S8:** protocol foundation; headless match host; 8-client harness; authority; lag compensation; deterministic combat regression.
- **E5-S1/S2:** terrain/coast/hydrology greybox; POI/road graphs; two representative POIs; 18-POI placement; modular building kit và validators.
- **E6-S1:** authority theo movement, combat, inventory/loot, vehicle, zone/result thay vì một story toàn match.
- **E6-S7:** harness + 24 gate + 50 gate + 100/final-circle gate + impairment profiles.
- **E7-S9:** modular content/parity pipeline và POI batches, không một story “18 POI/420 buildings”.
- **E9-S6/S9/S10:** tách test matrix/build/sign/certification/device families theo artifact và gate, giữ cross-platform parity acceptance chung.

### Major Issues

#### EQ-04 — No explicit FR/NFR/UX/ADR traceability at story level

Mechanism matrix chỉ map system→Epic. Không story nào claim FR/NFR/UX/ADR; readiness report phải tự suy ra 57/58 FR coverage. 35 NFRs chỉ được nhắc rải ở epic gates/E9.

**Remediation:** Mỗi detailed story cần `Source Requirements` và AC chứa exact applicable budgets; tạo generated coverage matrix làm CI/document check.

#### EQ-05 — Story dependencies and implementation order are absent

Chỉ có epic chain; không có dependency graph trong Epic. Ví dụ E2-S8 phụ thuộc weapon state/ballistics/damage, E3-S6 chồng E2-S4, E4-S8/S9 và E6-S6 chia ownership reconnect, E5-S8 cần streaming/tooling chưa có story nền.

**Remediation:** Trong refinement, ghi `Depends on`, `Blocks`, first-needed data/schema và vertical-slice acceptance. Cấm dependency vào story tương lai trong cùng sequence.

#### EQ-06 — Duplicate or ambiguous ownership

- Armor/helmet/durability: E2-S4 và E3-S6.
- Reconnect/mobile lifecycle: E4-S8/S9 và E6-S6.
- Performance/device gates: E5-S8/S9 và E9-S1/S2/S10.
- Reporting/evidence: E6-S8 và E9-S4.

**Remediation:** Khóa layer ownership: shared gameplay rules vs inventory presentation; lifecycle state/UI vs network/token/backend; slice gate vs release regression; evidence generation vs moderation workflow.

#### EQ-07 — Forward reference inside E5-S2

E5-S2 ghi “420 công trình là content target sau E6”. Một story không được chứa deliverable phụ thuộc future Epic.

**Remediation:** E5 chỉ giao modular kit + two representative POIs/validators. Full content expansion chuyển hoàn toàn sang E7 after E6 gate; không giữ half-deferred acceptance trong E5 story.

#### EQ-08 — Technical/business task presented as player story

E8-S7 “Decision record cho mô hình phát hành và chi phí máy chủ” là product/ADR task, không tạo increment người chơi kiểm chứng được.

**Remediation:** Chuyển sang product/operations decision backlog hoặc đóng như prerequisite business gate; không tính vào story velocity/player-value completion.

#### EQ-09 — Architecture enablers are hidden inside broad stories

Custom protocol/versioning, bake/manifest validators, map parity tooling, Nakama control plane, Cockroach migrations, Agones allocator/fleet, observability schema và device/load harness chưa có first-class stories. Chúng có thể là enabler stories nếu gắn trực tiếp với playable increment, nhưng không nên bị agent tự tạo bên trong feature story.

**Remediation:** Tạo enabler stories just-in-time, mỗi story chỉ tạo data/schema/tooling cần cho playable slice hiện tại và có consumer/test rõ.

### Minor Concerns

- Story titles không dùng “As a / I want / so that”; title ngắn có thể giữ, nhưng detailed story body phải nêu actor, outcome và value.
- Không có explicit severity/priority hoặc milestone assignment trên từng story; epic gates một mình chưa đủ cho sprint planning.
- Không có Definition of Ready/Done chung cho five-platform player-impact stories.

### Positive Practices to Preserve

- Mọi Epic đều có player/operational value rõ; không có database/API/infrastructure-only Epic.
- Dependency chain không circular và production content được đặt sau scale gates.
- Epic gates chứa nhiều metric tốt: ±5% movement, hitreg ≤0,5 m, 95% gun availability, 20 stable matches, 1.000 zone seeds, 30 Hz/+10% headroom, audio 85% và three release-candidate families.
- Mobile viability bắt đầu từ E1 thay vì port sau desktop.

### Quality Verdict

`epics.md` là **roadmap-quality, not implementation-backlog-quality**. Nó phù hợp làm input cho detailed story generation nhưng không được giao trực tiếp cho implementation agent.

## Summary and Recommendations

### Overall Readiness Status

# NOT READY

OutSurvive **chưa sẵn sàng vào Phase 4 implementation**. GDD, UX, Architecture và Project Context đủ chất lượng để làm nguồn thiết kế; blocker nằm ở backlog: 83 entries chỉ là high-level story titles, không có acceptance criteria, dependency, module ownership hoặc Definition of Done. Bắt đầu code lúc này sẽ buộc implementation agent tự thiết kế thay vì thực thi thiết kế.

Điều này không phủ nhận tính khả thi của Combat Sandbox. Các empirical network/mobile/world gates chỉ có thể được chứng minh bằng code; nhưng trước khi viết code, ít nhất first-slice stories phải được refine tới mức implementation-ready.

### Readiness by Artifact

| Artifact/area | Status | Evidence |
|---|---|---|
| GDD | Ready for backlog refinement | 58 FR, 35 NFR, measurable gates và explicit exclusions |
| Game Architecture | Ready | 20 ADR, 16 patterns, validation PASS và Project Context 78 rules |
| UX | Ready with story-specific dependencies | Two final canonical spines; 20 closed, 5 accepted dependencies, 0 UX-document opens |
| FR epic coverage | Needs work | 57/58 covered; FR007 swimming/diving missing |
| Epic structure | Roadmap-ready | 9 player-value epics, backward-only dependency chain và measurable gates |
| Story backlog | **Not ready** | 0/83 detailed stories; 0 BDD acceptance criteria |
| Greenfield startup | **Not ready** | Không có story sở hữu clean Godot scaffold và early five-platform smoke |

### Critical Issues Requiring Immediate Action

1. **Generate detailed stories and acceptance criteria.** Không giao 83 high-level entries trực tiếp cho implementation.
2. **Add the greenfield initialization story.** Godot 4.7.1 project, domain structure, test/import baseline và five-platform smoke phải là first story, không chờ E9.
3. **Split epic-sized entries.** Tối thiểu E2-S8, E5-S1/S2, E6-S1/S7, E7-S9 và E9-S6/S9/S10.
4. **Add FR007 swimming/diving ownership.** E1 movement story phải tích hợp E5 WaterVolume và E6 authority before 2×2 km slice.
5. **Lock reconnect/AFK policy.** Owner API, timeout, avatar vulnerability/outcome và token behavior phải có ADR trước E4-S8/S9/E6-S6 refinement.
6. **Add localization/font story.** Việt/Anh catalog, Noto/fallback/license, formatting và five-platform text snapshots cần owner trước production UI.

### Recommended Next Steps

1. **Correct the roadmap inputs**
   - Add E1 initialization story and FR007 swimming/diving story.
   - Remove E5-S2 forward-deferred 420-building deliverable; keep only modular kit/two representative POIs in E5 and move full expansion to E7.
   - Move E8-S7 business decision record out of player-story backlog.

2. **Resolve policy gates before affected story refinement**
   - Create reconnect/AFK/avatar-outcome ADR.
   - Lock map orientation/zoom, spectator voice/ping after elimination and raw-input/OS-key-label policy.
   - Record v1/deferred decisions for screen reader, narration, extended subtitles, motor/hearing and photosensitivity scope.

3. **Run detailed Epic & Story creation**
   - Use GDD + Architecture + UX + this readiness report.
   - Give each story Source Requirements (`FR`, `NFR`, `UX`, `ADR`), actor/outcome, dependencies, module/file ownership, Given/When/Then AC, error/recovery paths and five-platform applicability.
   - Create just-in-time enabler stories for protocol, content bake/validators, backend/allocator/fleet and test harness, each tied to a playable slice.

4. **Re-run Implementation Readiness**
   - Required target: 58/58 FR mapping, detailed first-slice backlog, no forward dependency, every applicable NFR represented in AC and no unresolved critical policy gate.

5. **Only then enter Sprint Planning and implementation**
   - First implementation sequence: project/five-platform smoke → semantic input + movement slice → network combat sandbox 8 clients → world/mobile 2×2 km slice.

### Issue Count

Assessment identified **17 numbered findings across three categories**:

- Epic coverage: 1
- UX alignment/story gates: 7
- Epic quality: 9

Critical and high findings must be resolved before Phase 4. Medium story-specific policy decisions may be resolved just before refining/starting their owning stories, but must not be silently inferred by implementation agents.

### Final Note

OutSurvive có nền móng thiết kế tốt hơn phần lớn greenfield projects: vision nhất quán, mobile-in-v1 rõ, architecture có boundary mạnh và UX đã đóng. Kết luận NOT READY không phải vì thiếu ý tưởng hay thiếu kiến trúc; nó vì khoảng cách giữa roadmap và executable backlog chưa được lấp. Hành động đúng tiếp theo là **refine epics/stories**, không phải thêm mockup và cũng chưa phải bắt đầu xây toàn bộ project.

**Assessment completed:** 2026-07-23

**Assessor:** Codex — Game Producer / Scrum Master readiness review
