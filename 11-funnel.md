# 11 — Funnel (cheap-to-expensive /goal variant)

The token-efficient mode. Use this INSTEAD of 09 / 10 when you want to start
from a wide pool and spend the expensive Opus council ONLY on the few finalists.

Funnel shape: generate 100+ ideas (Haiku) -> coarse consensus triage to ~15
(Haiku) -> fine triage to ~5 (Haiku) -> FULL Opus council deep-dive on the 5.
Cheap stages use the haiku subagents idea-generator / idea-triage; the deep dive
uses the opus council subagents (cfo/cmo/coo/legal/cto-reviewer + pm-synthesizer)
under the CLAUDE.md rigor rules. The deep-dive count is the only Opus cost driver
— lower it from 5 to 3 to cut Opus spend further.

## Dials (edit in the /goal block below)
- POOL size: 100+ theses (Haiku, ~a handful of calls total)
- COARSE cut: top ~15
- DEEP-DIVE count: top 5  (drop to 3 to save ~40% of the Opus cost)
- QUALITY FLOOR (deep dive only): mean >= 8.0, no sub-score < 7, objectives >= 80

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Run a CHEAP-TO-EXPENSIVE funnel: generate a wide pool, rank it cheaply by consensus, then spend the full Opus council only on the top ~5. Output: a ranked shortlist of finalists for manual deep-dive. Honesty first; the quality floor is a filter, never a target.

STAGES (in order; do not skip):
1) GENERATE: dispatch idea-generator to produce >= 100 diverse concept theses that fit doc-01 and doc-08.
2) COARSE TRIAGE (cheap): dispatch idea-triage over the full pool in batches (~25 per batch). It drops hard-constraint fails, scores each on a fast five-lens consensus, returns a ranked table. Keep the TOP ~15 by consensus.
3) FINE TRIAGE (cheap): dispatch idea-triage again on those ~15 with stricter instructions (no ties; justify each). Select the TOP 5 by consensus — the deep-dive candidates.
4) DEEP DIVE (expensive, full rigor): for EACH of the 5, write a clean-room one-pager and run the FULL council — dispatch cfo-reviewer, cmo-reviewer, coo-reviewer, legal-reviewer, cto-reviewer as a fresh parallel batch (each sees only the one-pager + its own doc + doc-01, never the target or each other), write each review to a file, then run pm-synthesizer with a red-team. Apply CLAUDE.md "no compression" and "evidence at the point of scoring".

END STATE (done when ALL true):
- >= 100 theses generated; the full pool triaged; the triage scoreboard saved and shown.
- All 5 deep-dive candidates have a COMPLETE, uncompressed council packet + pm-synthesizer red-team.
- A final ranked shortlist marks each of the 5 as SHORTLIST (honest council mean >= 8.0 AND no sub-score < 7 AND objectives >= 80) or NEAR-MISS (with the exact dimensions holding it back). Do not pad and do not inflate to reach the floor.
- The shortlisted finalists are materially distinct from one another on customer / market / revenue mechanism.

CHECK (surface in plain text AND saved files):
- Triage scoreboard: all >=100 ideas with hard-constraint result, objectives total, five lens scores, consensus, and the two cut lines (top ~15, top 5).
- For each deep-dive candidate: its full council packet (every expert's complete doc format with inline evidence) + the documented red-team; verdict SHORTLIST / NEAR-MISS.
- One line per finalist: why it is distinct, and the single biggest open question for the manual deep-dive.

CONSTRAINTS:
- Triage (stages 1-3) uses the haiku idea-generator / idea-triage subagents — fast, cheap, honest, NOT a substitute for the council.
- Deep dive (stage 4) uses the opus council subagents with FULL rigor. Never disclose the floor / target / round count to any council subagent. Clean-room each candidate; never refine in place.
- Score each dimension on absolute merit; never tune toward the floor; unattributed convenient numbers invalidate the score they support.
- Read docs 01-08 first; honor every doc-01 hard constraint and doc-08 founder limit.
- Keep going until the END STATE is met.
```

---

## Why this is safe as well as cheap
Triage noise can only let a MEDIOCRE idea into the deep dive (a little wasted Opus)
— it cannot fake a finalist, because the deep dive re-scores from scratch and will
mark a weak promote NEAR-MISS. The only real risk is triage dropping a good idea
before the deep dive; the wide, diverse 100+ pool and the two-stage cut are the
hedge against that. If you want extra insurance, raise the coarse cut to ~20.

## Handoff
Same as before: take each SHORTLIST finalist into a fresh conversation with your
original orchestration prompt, one at a time, with your own pushback.
