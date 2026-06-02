# 13 — Autonomous Funnel (unsupervised /goal, regenerating loop)

The hands-off mode. One /goal runs the full funnel in a loop — generate, triage,
deep-dive the top few, learn from the failures, generate again — until 2 distinct
concepts clear 8.0 OR a safety bound stops it. No checkpoints. Uses the Opus
agents (generator, triage) and the council/PM subagents under CLAUDE.md rigor.

## Before you run
- Commit the latest agents (idea-generator + idea-triage now carry the
  light-integration / no-encroachment discriminators) and 01/08.
- Start a FRESH session so agents reload. "Accept edits" mode is fine.
- This is unattended and bounded; check back periodically. Be ready to Ctrl-C.

## Dials (in the /goal block)
- SUCCESS COUNT: 2 distinct clearers (raise to 3 if you want).
- BOUND: 3 rounds OR 12 deep-dives (lower to 2 rounds / 8 deep-dives for a
  cheaper first autonomous run — the Opus deep dive is the only real cost driver).
- BAR: mean > 8.0, no sub-score < 7, objectives >= 80 (if rounds keep coming up
  empty, the honest fix is to relax the bar to ~7.5 here, not to inflate scores).

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Autonomously find 2+ DISTINCT concepts that clear the SHORTLIST bar (mean of five expert averages > 8.0 AND no sub-score < 7 AND objectives >= 80) on HONEST, red-teamed scores. Loop generate -> triage -> deep-dive across rounds, learning between rounds, until 2 clear OR the bound is hit. Honesty over success: zero clears is an acceptable, honest outcome — NEVER inflate or tune a score to satisfy this goal.

ROUND LOOP (repeat until END STATE):
1) GENERATE: dispatch idea-generator (Opus) for ~80-100 diverse, on-thesis theses. SEED toward the proven winning shape: a mandate/regulation/standard/contractual/insurance requirement forcing a recurring, budgeted MUST-HAVE, in a fragmented segment whose incumbents are STALE and NON-tech (sleepy consultants, generalist MSPs, old-line vendors), with LIGHT integration, NO well-funded strong-tech incumbent, and no horizontal platform that could encroach within ~2 quarters. From round 2 on, ALSO seed AWAY from the failure modes recorded in prior rounds (e.g., labor-vs-margin hinge, uninsurable liability tails, build/maintenance treadmills, strong-tech incumbents, encroachable niches).
2) TRIAGE: dispatch idea-triage (Opus) over the pool; rank by consensus (must-have heaviest; penalize heavy integration + encroachable niches). Take the top ~4 DISTINCT candidates (distinct on customer + market + revenue mechanism); drop near-duplicates of already-failed concepts.
3) DEEP DIVE (one concept per working block): write a clean-room one-pager, then a FRESH parallel batch of cfo/cmo/coo/legal/cto-reviewer (each blind to the others, the bar, and the target; each sees only the one-pager + its own doc + 01-objectives.md), write each review to a file, then pm-synthesizer with a mandatory red-team. Mark SHORTLIST or NEAR-MISS with the exact dimensions holding it back. Apply CLAUDE.md no-compression + evidence-at-the-point-of-scoring.
4) RECORD to a running scoreboard. After each round, distill that round's recurring failure modes into a short note that seeds the next round's generation.

END STATE (done when EITHER):
A) 2+ DISTINCT concepts have complete red-teamed packets and clear the bar (mean > 8.0, no sub-score < 7, objectives >= 80); OR
B) BOUND reached — 3 generation rounds completed OR 12 concepts deep-dived, whichever comes first — with fewer than 2 clearing. Then STOP and report: the full cross-round scoreboard, the 3 strongest near-misses ranked, and for each the single cheapest experiment that would most move it toward GO.

CONSTRAINTS (hold throughout):
- Score on absolute merit; do NOT look at the running average while scoring; NEVER tune a score toward 8.0; unattributed convenient numbers invalidate the score.
- INCOME TARGET = the ladder in 01-objectives.md (~$300K/founder mo12, ~$500K+ mo24, growing; $2M is upside, not required). A bridgeable regulatory/expertise moat with sleepy incumbents is a PLUS; avoid high-performing well-funded strong-tech incumbents (hard constraint #5) and encroachable niches.
- Clean-room every candidate (no version/lineage/prior scores/target to any council subagent). Never refine a failed concept in place — it may re-enter only as a structurally NEW clean-room candidate. Drop a concept after two failures.
- Read docs 01-08 first; honor every doc-01 hard constraint and doc-08 founder limit.
- Do not stop before END STATE A or B, and do not exceed the bound.
```

---

## What to expect
Across your runs so far, the honest field has clustered at ~6.6-7.2 with zero
clearing 8.0. So outcome B (bound hit, near-misses returned) is a realistic
result — and a correct one. If it keeps landing there, the decision is yours, not
the model's: relax the bar to ~7.5, or take the top near-misses into manual
pre-build validation and re-score on real numbers. Either is better than a
manufactured 8.1.
