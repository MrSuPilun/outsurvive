# UX-037 Visual Check — OutSurvive

- **Renderer:** Google Chrome headless, local `file://` only
- **Standard:** 1920×1080, device scale factor 1.0
- **Compact/UI scale:** 914×514 CSS viewport at device scale factor 1.4, producing a 1280×720 PNG
- **Checked:** 2026-07-22

## Result matrix

| Mock | 1920×1080 / 100% | 1280×720 / 140% | Evidence |
|---|---|---|---|
| Lobby | Pass | Pass | `lobby-1920x1080-100.png`, `lobby-1280x720-140.png` |
| Match HUD | Pass | Pass after fit correction | `match-hud-1920x1080-100.png`, `match-hud-1280x720-140.png` |
| Inventory | Pass | Pass | `inventory-1920x1080-100.png`, `inventory-1280x720-140.png` |
| Map / Phase | Pass | Pass | `map-phase-1920x1080-100.png`, `map-phase-1280x720-140.png` |

## Inspection notes

- **Lobby:** left navigation, world-center negative space and right party/action panel remain separated. No crop, overlap or commerce rail.
- **Match HUD:** six fixed modules, reticle and contextual prompt remain inside the 16:9 safe frame. The first compact render let the page caption consume vertical space; the mock state width was capped at `150vh`, then both configurations were re-rendered and passed. `match-hud-both-states-1920-wide.png` additionally confirms the P0 vehicle-fire card does not move persistent anchors or cover the reticle.
- **Inventory:** both 34% panels remain readable; the 32% world strip stays visible; capacity and armor durability do not collide with the close prompt.
- **Map / Phase:** header, phase/timer, legend and bindings retain their four corner anchors. Current-zone solid and revealed next-zone dashed lines remain distinguishable; teammate markers stay inside the map surface.

## Acceptance

No gameplay-critical module, focus/prompt region, phase information or required world-risk strip is cropped or overlapped in either configuration. Eye travel remains consistent with the distilled anchors in `DESIGN.md` and `EXPERIENCE.md`. This closes UX-037 at the document/mock level; Godot implementation snapshots remain required by UX-021 before the corresponding UI stories are Done.
