# 09 — Acquisition Discovery Loop (the funnel + the goal command)

This file holds the goal command for the acquisition track, plus how to run it. The loop
*rules* live in this folder's `CLAUDE.md`. This file is reference only.

The acquisition funnel mirrors the build council's cheap-to-expensive funnel, re-pointed
at buying a business:

generate 60–100 target profiles → triage by consensus to ~12 → fine-cut to ~5 → FULL
acquisition council deep-dive on the finalists → ranked shortlist of acquisition theses.

## Dials
- POOL size: 60–100 target profiles (industry × size × situation)
- COARSE cut: top ~12 by consensus
- DEEP-DIVE count: top ~5 (drop to 3 to save cost)
- QUALITY FLOOR (deep dive only): mean of five expert averages >= 8.0, no sub-score < 7,
  objectives >= 80. (As with the build council, the honest field may cluster below 8.0 —
  a shortlist of NEAR-MISSES with the dimensions holding them back is a correct outcome.
  If rounds keep coming up empty, the honest fix is to relax the bar to ~7.5 here, not to
  inflate scores, multiples, or add-backs.)

---

## The goal command (paste everything after `/goal`, or run the steps manually)

```
/goal Run a CHEAP-TO-EXPENSIVE acquisition funnel: generate a wide pool of business-to-ACQUIRE target profiles, rank them cheaply by consensus, then spend the full acquisition council only on the top ~5. Output: a ranked shortlist of acquisition theses for manual deep-dive. Honesty first; the quality floor is a filter, never a target. Work entirely from the acquisition/ doc set, NOT the repo-root build council.

STAGES (in order; do not skip):
1) GENERATE: dispatch acq-idea-generator to produce 60–100 diverse target profiles (industry × size × situation) that fit acquisition/01-objectives.md and acquisition/08-founder-profile.md. Maximize diversity across industries, sizes, and situations; no near-duplicates.
2) COARSE TRIAGE (cheap): dispatch acq-idea-triage over the full pool in batches. It drops hard-constraint fails (not SBA-eligible, can't service debt, non-transferable, owner-is-the-business, non-bridgeable credential), scores each on a fast consensus, returns a ranked table. Keep the TOP ~12.
3) FINE TRIAGE (cheap): dispatch acq-idea-triage again on those ~12 with stricter instructions (no ties; justify each). Select the TOP ~5 — the deep-dive targets.
4) DEEP DIVE (expensive, full rigor): for EACH finalist, write a clean-room target one-pager and run the FULL acquisition council — dispatch acq-cfo-reviewer, acq-cmo-reviewer, acq-coo-reviewer, acq-legal-reviewer, acq-cto-reviewer as a fresh parallel batch (each sees only the one-pager + its own doc + acquisition/01-objectives.md, never the bar/target/each other), write each review to a file, then run acq-deal-synthesizer with a mandatory red-team. Apply the no-compression and evidence-at-the-point-of-scoring rules.
   (If the acq-* agents are not loaded in this session, dispatch general-purpose subagents pointed at the specific acquisition/0X-*.md docs instead — same isolation.)

END STATE (done when ALL true):
- 60+ target profiles generated; the full pool triaged; the triage scoreboard saved and shown.
- All ~5 deep-dive finalists have a COMPLETE, uncompressed council deal memo + red-team.
- A final ranked shortlist marks each as SHORTLIST (honest mean >= 8.0 AND no sub-score < 7 AND objectives >= 80) or NEAR-MISS (with the exact dimensions holding it back). No padding, no inflation.
- The shortlisted theses are materially distinct on industry + customer/revenue shape + deal structure / modernization angle.

CHECK (surface in plain text AND saved files under acquisition/runs/<date>/):
- Triage scoreboard: all profiles with hard-constraint result, objectives total, lens scores, consensus, and the two cut lines.
- For each finalist: its full council deal memo (every expert's complete doc format with inline evidence) + the documented red-team; verdict SHORTLIST / NEAR-MISS.
- One line per finalist: why it is distinct, and the single biggest diligence question for the manual deep-dive.

CONSTRAINTS:
- Triage (stages 1–3) is fast/cheap/honest, NOT a substitute for the council.
- Deep dive (stage 4) uses FULL rigor. Never disclose the floor/target/round count to any council subagent. Clean-room each target; never refine in place.
- Score each dimension on absolute merit; never tune toward the floor; a flattering multiple, add-back, DSCR, or churn assumption with no source invalidates the score it supports.
- Read the acquisition/ docs 01–08 first; honor every doc-01 hard constraint and the doc-08 founder limits (owner-operator, manages but does not personally perform a licensed trade; avoid PE-roll-up bidding wars).
- Keep going until the END STATE is met.
```

---

## Why this is safe as well as cheap
Triage noise can only let a mediocre profile into the deep dive (a little wasted effort)
— it cannot fake a finalist, because the deep dive re-scores from scratch and marks a
weak promote NEAR-MISS. The real risk is triage dropping a good profile early; the wide,
diverse pool and two-stage cut are the hedge.

## Handoff
Take each SHORTLIST thesis into deal sourcing: search BizBuySell / broker networks /
direct outreach to retiring owners for REAL listings that match the profile, then re-run
the SAME council on the actual financials before signing an LOI.
