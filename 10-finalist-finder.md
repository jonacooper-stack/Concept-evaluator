# 10 — Finalist Finder (breadth-first /goal variant)

Use this INSTEAD of 09 when you want the loop to do a wide, honest search and hand
you a ranked shortlist of strong finalists — which you then deep-dive yourself, one
at a time, with your own pushback. That manual pass is where the deepest analysis
comes from; this loop's job is to find the field cheaply and honestly.

Loop RULES live in `CLAUDE.md`. Council independence is enforced by the six
subagents in `.claude/agents/` (cfo-reviewer, cmo-reviewer, coo-reviewer,
legal-reviewer, cto-reviewer, **competitive-analyst**), synthesized by
pm-synthesizer.

---

## The dials (edit in ONE place — keep in sync with CLAUDE.md)
- BRAINSTORM POOL: at least 20 candidate theses, diverse across the FIVE
  forcing-function types (not just compliance).
- SCREEN to reach council: Objectives Weighted Score >= 70 AND no objectives
  dimension below 6 AND must-have (dim 1) >= 6.
- TIERS (from doc-01, on the Objectives Weighted Score after the red-team):
  A = Advisor-Ready (>=80, must-have >=8, competition >=7, no FATAL gate);
  B = Promising (68–79, or >=80 with one serious open risk); C = Pass.
- SHORTLIST: the honest top 4–5, ranked — A-tier first, then strongest B. Do NOT
  pad with weak ideas and do NOT inflate to reach a tier.

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Run an HONEST, breadth-first search and surface a ranked shortlist of up to 5 strong, distinct finalist concepts for manual deep-dive, each with plain-English deliverables. Honesty over quantity: surface the genuine top of the field with honest tiers; do NOT pad with weak ideas and do NOT inflate to reach a tier.

END STATE (done when ALL true):
- At least 20 candidate concepts were brainstormed (each a 3-4 sentence thesis: customer, the forcing-function must-have, why now, revenue mechanism, why these founders) and screened on doc-01, diverse across the five forcing-function types.
- Every concept that passed the screen received a FULL independent SIX-member council pass — cfo/cmo/coo/legal/cto-reviewer + competitive-analyst via the .claude/agents subagents, run as a fresh parallel batch per concept — and an honest score, then pm-synthesizer with a two-directional red-team.
- A ranked shortlist of up to 5 finalists is produced, labeled by TIER (A/B/C) on the Objectives Weighted Score, shown top-down. Include the strongest concepts even if the best are B-tier, each labeled with the exact dimensions holding it back.
- Finalists are materially distinct on customer / market / forcing function / revenue mechanism.
- For each finalist, the doc-14 deliverables exist (plain-English Concept Dossier + Scorecard as .docx/.txt/.md, saved to the repo and delivered as attachments — NO Google Drive), plus a master comparison sheet in Excel (.xlsx) for the whole field.

CHECK (surface in plain text AND saved files):
- Scoreboard: every brainstormed idea, its screen result, and for each council-scored concept its six expert averages, the Objectives Weighted Score, the lowest single sub-score, the Legal risk-gate rating, and its TIER.
- For each finalist: its FULL uncompressed council packet (every expert's complete doc-format review with inline evidence) plus a documented two-directional red-team (challenge the highest sub-scores down; correct any timid deflation up).
- For each finalist: one line on why it is distinct, and the single biggest open question the manual deep-dive should resolve first.

CONSTRAINTS (hold throughout):
- Score on absolute merit per 00-evaluation-stage.md: symmetric (no inflation AND no deflation) and stage-aware (no penalty for missing interviews/build/traction — list as next experiments). Dispatch the six council subagents as a FRESH parallel batch per concept; never pass one expert's output to another; never disclose tiers/screen/target/round count to a council subagent. Synthesize via pm-synthesizer.
- "Must-have" = a strong forcing function of ANY of the five doc-01 types; regulation is one path, not required. Legal is a RISK GATE — do not down-tier a regulated-but-navigable concept. Competition is first-class — the Competitive Analyst must NAME real players with researched data.
- Clean-room every candidate (no version/lineage/prior scores). Never refine in place: on failure make a STRUCTURAL change as a NEW candidate or drop. Drop after two failures.
- Read docs 00-08 + 06b + 14 first; honor every doc-01 hard constraint and doc-08 founder limit.
- Keep going until the END STATE is met. Do not stop early and do not pad the shortlist.
```

---

## Handoff to the deep-dive
For each finalist, take its clean-room one-pager (and its plain-English dossier)
into a fresh conversation with the full six-doc council workflow, one finalist at a
time, and push back hard with real market knowledge. The finalist packets here are
the starting point, not the final word.
