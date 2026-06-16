# 11 — Funnel (wide-to-deep /goal variant)

Use this when you want to start from a wide pool and spend the expensive six-member
council ONLY on the few finalists.

Funnel shape: generate 100+ ideas -> coarse consensus triage to ~15 -> fine triage
to ~5 -> FULL six-member council deep-dive on the 5 -> plain-English deliverables.
The triage stages use the `idea-generator` / `idea-triage` subagents (fast, cheap,
honest — NOT a substitute for the council). The deep dive uses the six council
subagents (cfo/cmo/coo/legal/cto-reviewer + **competitive-analyst**) + pm-synthesizer
under the CLAUDE.md rigor rules. The deep-dive count is the main cost driver — lower
it from 5 to 3 to cut spend further.

## Dials (edit in the /goal block below)
- POOL size: 100+ theses, diverse across the FIVE forcing-function types.
- COARSE cut: top ~15
- DEEP-DIVE count: top 5 (drop to 3 to save cost)
- TIERS (deep dive, from doc-01 on the Objectives Weighted Score after the
  red-team): A Advisor-Ready / B Promising / C Pass. Surface the honest top 2–3.

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Run a WIDE-TO-DEEP funnel: generate a wide pool, rank it cheaply by consensus, then spend the full six-member council only on the top ~5. Output: a ranked, tiered shortlist of finalists with plain-English deliverables. Honesty first; tiers are descriptive, never a target to engineer toward.

STAGES (in order; do not skip):
1) GENERATE: dispatch idea-generator to produce >= 100 diverse concept theses that fit doc-01 and doc-08, spread across all five forcing-function types (regulatory, contractual, critical-input, continuity, risk-mitigation) — do NOT cluster on compliance.
2) COARSE TRIAGE (cheap): dispatch idea-triage over the full pool in batches (~25 per batch). It drops hard-constraint fails, scores each on a fast consensus, returns a ranked table. Keep the TOP ~15.
3) FINE TRIAGE (cheap): dispatch idea-triage again on those ~15 with stricter instructions (no ties; justify each). Select the TOP 5 — the deep-dive candidates.
4) DEEP DIVE (expensive, full rigor): for EACH of the 5, write a clean-room one-pager and run the FULL six-member council — dispatch cfo-reviewer, cmo-reviewer, coo-reviewer, legal-reviewer, cto-reviewer, competitive-analyst as a fresh parallel batch (each sees only the one-pager + its own doc + 00 + 01, never the target or each other), write each review to a file, then run pm-synthesizer with a two-directional red-team. Apply CLAUDE.md no-compression and stage-aware evidence rules.

END STATE (done when ALL true):
- >= 100 theses generated; the full pool triaged; the triage scoreboard saved and shown.
- All 5 deep-dive candidates have a COMPLETE, uncompressed six-member council packet + pm-synthesizer two-directional red-team.
- Each of the 5 is labeled TIER A / B / C on the Objectives Weighted Score (with the Legal risk-gate rating). Surface the honest top 2–3, ranked. Do not pad and do not inflate to reach a tier.
- For each finalist, the doc-14 deliverables exist (plain-English Concept Dossier + Scorecard as .docx/.txt/.md, saved to the repo and delivered as attachments — NO Google Drive) + a master comparison sheet in Excel (.xlsx).
- Finalists are materially distinct on customer / market / forcing function / revenue mechanism.

CHECK (surface in plain text AND saved files):
- Triage scoreboard: all >=100 ideas with hard-constraint result, consensus score, and the two cut lines.
- For each deep-dive candidate: its full six-member council packet (complete doc format with inline evidence) + the documented red-team; its six expert averages, Objectives Weighted Score, lowest sub-score, Legal risk-gate rating, and TIER.
- One line per finalist: why it is distinct, and the single biggest open question for the manual deep-dive.

CONSTRAINTS:
- Triage (stages 1-3) uses idea-generator / idea-triage — fast, honest, NOT a substitute for the council.
- Deep dive (stage 4) uses the six council subagents with FULL rigor. Score on absolute merit per 00-evaluation-stage.md: symmetric (no inflation AND no deflation), stage-aware (no penalty for missing interviews/build/traction). Never disclose tiers/target/round count to a council subagent. Clean-room each candidate; never refine in place.
- "Must-have" = a strong forcing function of ANY of the five doc-01 types; regulation is one path, not required. Legal is a RISK GATE — do not down-tier a regulated-but-navigable concept. The Competitive Analyst must NAME real players with researched data.
- Read docs 00-08 + 06b + 14 first; honor every doc-01 hard constraint and doc-08 founder limit.
- Keep going until the END STATE is met.
```

---

## Why this is safe as well as cheap
Triage noise can only let a MEDIOCRE idea into the deep dive (a little wasted cost)
— it cannot fake a finalist, because the deep dive re-scores from scratch and will
tier a weak promote as B or C. The only real risk is triage dropping a good idea
before the deep dive; the wide, diverse 100+ pool and the two-stage cut are the
hedge. Raise the coarse cut to ~20 for extra insurance.

## Handoff
Take each top-tier finalist (and its plain-English dossier) into a fresh
conversation with the full council workflow, one at a time, with your own pushback.
