## Document Summary
- **Purpose:** Canonical UX contracts for Godot architecture and story development.
- **Audience:** Human and AI downstream implementers.
- **Reader type:** llm
- **Structure model:** Reference/Database applied as a two-file peer-contract set.
- **Current length:** 10,925 words across 39 Markdown headings: `DESIGN.md` has 3,615 words and 13 headings; `EXPERIENCE.md` has 7,310 words and 26 headings.
- **Core question:** What visual, behavioral, state, input, accessibility, and journey contracts must downstream implementation preserve for OutSurvive?
- **Existence statement:** This document set exists to help human and AI downstream implementers build OutSurvive's Godot UI/HUD without inventing behavior, breaking fairness, or losing decision traceability.

### Section map — `DESIGN.md`

| Major section | Words |
|---|---:|
| Frontmatter + title | 535 |
| Brand & Style | 201 |
| Colors | 441 |
| Typography | 229 |
| Layout & Spacing | 710 |
| Elevation & Depth | 159 |
| Shapes | 85 |
| Components | 823 |
| Do's and Don'ts | 432 |
| **Total** | **3,615** |

### Section map — `EXPERIENCE.md`

| Major section | Words |
|---|---:|
| Frontmatter + title | 37 |
| Foundation | 211 |
| Information Architecture | 466 |
| Voice and Tone | 176 |
| Component Patterns | 763 |
| State Patterns | 833 |
| Interaction Primitives | 624 |
| HUD & Diegetic UI | 365 |
| Input Schemes | 235 |
| Inventory, Map & Party | 630 |
| Reporting & Replay Summary | 134 |
| Game Feel & Juice | 435 |
| Accessibility Floor | 185 |
| Inspiration & Anti-patterns | 106 |
| Responsive & Platform | 195 |
| Surface Closure | 432 |
| Key Flows | 1,483 |
| **Total** | **7,310** |

### Structural analysis

- `DESIGN.md` follows the locked gds-ux body order exactly: Brand & Style → Colors → Typography → Layout & Spacing → Elevation & Depth → Shapes → Components → Do's and Don'ts; its YAML token groups precede the body as required.
- `EXPERIENCE.md` preserves the required gds-ux sequence among Foundation, Information Architecture, Voice and Tone, Component Patterns, State Patterns, Interaction Primitives, Accessibility Floor, and Key Flows; game-specific sections appear where their dependencies are already defined.
- The two files remain peer contracts: `DESIGN.md` owns visual specifications and `EXPERIENCE.md` owns behavior, states, input, feedback, accessibility, and journeys. The 25 component keys retain exact 1:1 parity.
- Repetition across component, state, surface-closure, and journey tables is purposeful contract reinforcement for random-access LLM use, not identical source duplication. Upstream GDD content remains referenced by path rather than copied wholesale.
- Assumption IDs, `[NOTE FOR UX]` gates, inline mock links, and named-protagonist climax journeys are required traceability or gds-ux closure mechanisms and should remain in place.
- Critical scope and authority appear in Foundation/frontmatter before downstream detail; component definitions precede state and flow usage. No premature detail, missing scaffolding, structural anti-pattern, scope violation, or buried implementation-critical section was found.

## Recommendations

No substantive changes recommended -- document structure is sound

## Summary
- **Total recommendations:** 0
- **Estimated reduction:** 0 words (0% of original)
- **Meets length target:** No target specified
- **Comprehension trade-offs:** None. Structural cuts would weaken canonical section compliance, component parity, LLM random access, or decision traceability without removing true redundancy.
