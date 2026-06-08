# 09 — Acquisition Discovery Loop (the funnel + the goal command)

This file holds the goal command for the acquisition track, plus how to run it. The loop
*rules* live in this folder's `CLAUDE.md`. This file is reference only.

## The two stages (don't mix them)
- **STAGE 1 — INDUSTRY SCREEN (this funnel).** Choose **which TYPES of business (industries)
  to hunt in.** Score only industry-level traits (docs `01`–`07`). Output: a short list of
  **~3 industries to go source real deals in**, each rated **PURSUE / MAYBE / PASS**.
- **STAGE 2 — TARGET DUE DILIGENCE (`10-due-diligence.md`).** Later, on a **real listing**,
  check the company-specific tells (earnings quality, owner-dependency, systems, staff,
  concentration) and decide **GO / PASS / OFFER A LOWER PRICE**.

The Stage-1 funnel: generate 60+ candidate industries/types → triage by consensus to ~12 →
fine-cut to ~5 distinct types → FULL Stage-1 council on the finalists → land on ~3 PURSUE.

## Dials
- POOL size: 60–100 candidate industries/types
- COARSE cut: top ~12 by consensus
- DEEP-DIVE count: top ~5 distinct types
- TARGET OUTPUT: ~3 industries rated PURSUE
- QUALITY FLOOR (deep dive): industry-level mean ≥ 8.0, no sub-score < 7, objectives ≥ 80.
  (If the honest field clusters lower, a ranked PURSUE/MAYBE shortlist with the dimensions
  holding each back is the correct output. Never inflate a score, a multiple, or an
  assumption to clear the floor.)

---

## The goal command (paste everything after `/goal`, or run the steps manually)

```
/goal Run a STAGE-1 INDUSTRY SCREEN for an SBA acquisition: generate a wide pool of candidate business TYPES (industries), rank them cheaply by consensus, then spend the full acquisition council only on the top ~5 distinct types, and land on ~3 industries rated PURSUE. Score ONLY industry-level traits — what is true of the TYPE and knowable from the outside. Do NOT score company-specific tells (owner-dependency, earnings verification, this company's systems, customer concentration) — those are Stage-2 due diligence (acquisition/10-due-diligence.md). Honesty first; the quality floor is a filter, never a target. Work entirely from the acquisition/ doc set, NOT the repo-root build council.

STAGES (in order; do not skip):
1) GENERATE: dispatch acq-idea-generator for 60–100 diverse candidate industries/types that fit acquisition/01-objectives.md and acquisition/08-founder-profile.md. Maximize diversity; no near-duplicates.
2) COARSE TRIAGE (cheap): dispatch acq-idea-triage over the pool. Drop industry-level hard-constraint fails (not SBA-eligible, can't finance at typical multiples, no inherent recurring revenue, non-bridgeable owner credential, active PE bidding war). Keep the TOP ~12 by consensus.
3) FINE TRIAGE (cheap): dispatch acq-idea-triage again on those ~12 with stricter instructions and a DISTINCTNESS constraint — the finalists must be materially different TYPES (don't pick five flavors of one shape). Select the TOP ~5.
4) DEEP DIVE (full rigor): for EACH finalist industry, write a clean-room industry one-pager and run the FULL Stage-1 council — acq-cfo-reviewer, acq-cmo-reviewer, acq-coo-reviewer, acq-legal-reviewer, acq-cto-reviewer as a fresh parallel batch (each sees only the one-pager + its own doc + acquisition/01-objectives.md, never the bar/target/each other), write each review to a file, then run acq-deal-synthesizer with a mandatory red-team. Apply no-compression and evidence-at-the-point-of-scoring.
   (If the acq-* agents are not loaded in this session, dispatch general-purpose subagents pointed at the specific acquisition/0X-*.md docs instead — same isolation.)

END STATE (done when ALL true):
- 60+ industries generated; the full pool triaged; the triage scoreboard saved and shown.
- All ~5 deep-dive finalists have a COMPLETE, uncompressed Stage-1 council Industry Memo + red-team.
- A final ranked shortlist names ~3 industries as PURSUE (industry-level mean ≥ 8.0, no sub-score < 7, objectives ≥ 80), with the rest MAYBE/PASS and the exact dimensions holding them back. No padding, no inflation.
- The PURSUE industries are materially distinct TYPES, each with: the sub-segment/size band to target, the green flags that make a good individual company, and the single biggest Stage-2 due-diligence priority.

CHECK (surface in plain text AND saved under acquisition/runs/<date>/):
- Triage scoreboard for all candidate industries.
- For each finalist: its full Stage-1 council Industry Memo (every expert's complete doc format with inline evidence) + the documented red-team; verdict PURSUE / MAYBE / PASS.
- One line per PURSUE industry: why it is distinct, the size band to target, and the #1 Stage-2 diligence priority.

CONSTRAINTS:
- Triage (1–3) is fast/cheap/honest, NOT a substitute for the council.
- Deep dive (4) is full rigor. Never disclose the floor/target/round count to any council subagent. Clean-room each industry.
- Score each dimension on absolute, INDUSTRY-LEVEL merit; never tune toward the floor; a flattering multiple or assumption with no source invalidates the score it supports.
- Do NOT score company-specific tells in Stage 1 — defer them to acquisition/10-due-diligence.md.
- Read the acquisition/ docs 01–08 first; honor every doc-01 industry-level hard constraint and the doc-08 founder limits (owner-operator; manages but does not personally perform a licensed trade; avoid PE-roll-up bidding wars).
- Keep going until the END STATE is met.
```

---

## Why this is safe as well as cheap
Triage noise can only let a mediocre industry into the deep dive (a little wasted effort) —
it cannot fake a PURSUE, because the deep dive re-scores from scratch and marks a weak
promote MAYBE/PASS. The wide, diverse pool and two-stage cut hedge against dropping a good
industry early.

## Handoff to Stage 2
Take each PURSUE industry into deal sourcing (BizBuySell / broker networks / direct outreach
to retiring owners). On each REAL listing, run the Stage-2 due-diligence checklist
(`10-due-diligence.md`) — earnings quality, owner-dependency, systems, staff, concentration,
liabilities — and decide GO / PASS / OFFER A LOWER PRICE on that specific deal.
