# 13 — Autonomous Funnel (unsupervised /goal, regenerating loop)

The hands-off mode. One /goal runs the full funnel in a loop — generate, triage,
deep-dive the top few, learn from the failures, generate again — until 2–3 distinct
concepts are surfaced with honest tiers OR a safety bound stops it. No checkpoints.
Uses the `idea-generator` + `idea-triage` agents and the six council/PM subagents
under CLAUDE.md rigor.

## Before you run
- Commit the latest agents (including the new `competitive-analyst`) and docs
  (00–14, 06b).
- Start a FRESH session so agents reload. "Accept edits" mode is fine.
- This is unattended and bounded; check back periodically. Be ready to Ctrl-C.

## Dials (in the /goal block)
- SUCCESS: 2–3 distinct A-tier concepts (or, if the field is thin, the strongest
  B-tier finalists surfaced honestly with what holds them back).
- BOUND: 3 rounds OR 12 deep-dives, whichever first.
- TIERS (from doc-01, on the Objectives Weighted Score after the red-team):
  A Advisor-Ready / B Promising / C Pass.

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Autonomously find and surface the 2-3 strongest DISTINCT need-to-have concepts with honest tiers (A Advisor-Ready / B Promising / C Pass) on HONEST, two-directional-red-teamed scores, each with plain-English deliverables. Loop generate -> triage -> six-member-council deep-dive across rounds, learning between rounds, until 2-3 strong concepts are surfaced OR the bound is hit. Honesty over success: zero A-tier is an acceptable, honest outcome (surface the strongest B-tier and what holds them back) — NEVER inflate, and NEVER deflate a genuinely strong concept.

ROUND LOOP (repeat until END STATE):
1) GENERATE: dispatch idea-generator for ~80-100 diverse, on-thesis theses. SEED across ALL FIVE forcing-function types (regulatory/compliance; contractual/counterparty; critical input to a production-or-revenue process; operational/financial continuity; effectively-mandatory risk mitigation) in a fragmented segment whose incumbents are STALE and NON-tech, with LIGHT integration, NO well-funded strong-tech incumbent, and no horizontal platform that could encroach within ~2 quarters. Do NOT cluster on compliance — regulation is one path, not the only one. From round 2 on, ALSO seed AWAY from the failure modes recorded in prior rounds.
2) TRIAGE: dispatch idea-triage over the pool; rank by consensus (must-have heaviest, competition next; penalize heavy integration + encroachable niches). Take the top ~4 DISTINCT candidates (distinct on customer + market + forcing function + revenue mechanism); drop near-duplicates of already-failed concepts.
3) DEEP DIVE (one concept per working block): write a clean-room one-pager, then a FRESH parallel batch of cfo/cmo/coo/legal/cto-reviewer + competitive-analyst (each blind to the others and to any target; each sees only the one-pager + its own doc + 00 + 01), write each review to a file, then pm-synthesizer with a two-directional red-team. Assign the Objectives Weighted Score and TIER; record the Legal risk-gate rating. Produce the doc-14 deliverables. Apply CLAUDE.md no-compression + stage-aware evidence.
4) RECORD to a running scoreboard. After each round, distill that round's recurring failure modes into a short note that seeds the next round.

END STATE (done when EITHER):
A) 2-3 DISTINCT concepts have complete red-teamed packets + doc-14 deliverables and land at TIER A (or the founders accept the strongest B-tier as the surfaced set); OR
B) BOUND reached — 3 generation rounds OR 12 concepts deep-dived. Then STOP and report: the full cross-round scoreboard, the 3 strongest concepts ranked by Objectives Weighted Score with their tiers, and for each the single cheapest experiment that would most move it up a tier. Produce deliverables for those 3.

CONSTRAINTS (hold throughout):
- Score on absolute merit per 00-evaluation-stage.md: do NOT look at the running total while scoring; symmetric (NEVER tune toward a tier; NEVER deflate a genuinely strong, evidenced dimension); stage-aware (no penalty for missing interviews/build/traction — list as next experiments).
- INCOME TARGET = the ladder in 01-objectives.md (~$300K/founder mo12, ~$500K+ mo24, growing; $2M is upside, not required).
- "Must-have" = a strong forcing function of ANY of the five doc-01 types. A bridgeable regulatory/expertise/supply moat with sleepy incumbents is a PLUS. Legal is a RISK GATE — do NOT down-tier a regulated-but-navigable concept; only FATAL gates down. Avoid high-performing well-funded strong-tech incumbents (hard constraint #5) and encroachable niches. The Competitive Analyst must NAME real players with researched data.
- Clean-room every candidate (no version/lineage/prior scores/target to any council subagent). Never refine a failed concept in place — it may re-enter only as a structurally NEW clean-room candidate. Drop after two failures.
- Read docs 00-08 + 06b + 14 first; honor every doc-01 hard constraint and doc-08 founder limit.
- Do not stop before END STATE A or B, and do not exceed the bound.
```

---

## What to expect
Earlier runs of the OLD framework clustered at ~6.6–7.2 with nothing clearing 8.0 —
but that was an artifact of a miscalibrated rubric: reviewers were asked to cite
evidence they had no tools to gather, capped at 6 for anything unsupported, then
judged against an 8.0 bar they couldn't reach. That is fixed here: the market-facing
reviewers now research the web, the evidence standard matches the concept stage, and
calibration is symmetric. Expect a wider, more honest spread — genuinely strong
concepts can now earn A-tier, and genuinely weak ones still land at C. If a round
honestly surfaces only B-tier finalists, that is a real result: take the top 2–3
into manual advisor review and the cheapest tier-moving experiment for each.
