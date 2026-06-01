# 12 — Guided Funnel (human-in-the-loop, checkpoints)

The supervised mode. Opus generates and makes the first cut, then YOU steer at two
checkpoints before any expensive council runs. This is NOT one fire-and-forget
/goal — it is THREE prompts you paste in sequence, with your input in between.
Your judgment kills bad branches early, which is what keeps it token-efficient
even though the top of the funnel now uses Opus.

Requires the Opus agents idea-generator + idea-triage and the council agents in
`.claude/agents/`. Reads 01-objectives.md (new ladder + must-have weighting) and
08-founder-profile.md.

---

## PROMPT 1 — Generate + first cut + STOP for your ranking
Paste this as a normal message (not /goal):

```
Run the guided funnel, Stages 1-2 only, then STOP and wait for me.

1) GENERATE: dispatch idea-generator (Opus) to produce >= 100 diverse, on-thesis concept theses per 01-objectives.md and 08-founder-profile.md. Enforce the quality bar: must-have/painkiller only, beatable stale incumbents, NO field-ops-core models, NO regulatory/SME-moat markets, recurring revenue, low capital. Save the full pool to a file.
2) FIRST CUT: dispatch idea-triage (Opus) over the full pool in batches; rank by consensus (must-have weighted heaviest). Take the TOP 30.
3) STOP. Present the top 30 as a numbered, ranked list. For EACH: a 1-2 line description (customer + the must-have pain + revenue mechanism) and its consensus score. Then ask me to give you my own ranking / keeps / kills. Do NOT proceed to narrowing until I reply.
```

→ You reply with your ranking, keeps, and kills.

---

## PROMPT 2 — Narrow to ~10 + STOP for your picks
After you've sent your ranking, paste:

```
Incorporate my ranking and feedback (my input outweighs the model ranking). Narrow to the TOP ~10. Present them with a deeper read each: one short paragraph covering customer, the must-have pain & why-now, the recurring revenue mechanism, and why these founders win it (marketing/positioning vs stale incumbents). Then STOP and ask me which of the ~10 should advance to the full council (I will pick 3-5). Do NOT start the council until I reply.
```

→ You reply with the finalists to deep-dive.

---

## PROMPT 3 — Full council deep dive on YOUR picks (this one is /goal)
After you've named the finalists, paste:

```
/goal Run the full council deep dive on the finalists I selected, with full rigor.

END STATE (done when ALL true):
- Each selected finalist has a clean-room one-pager and a COMPLETE, uncompressed council packet: cfo-reviewer, cmo-reviewer, coo-reviewer, legal-reviewer, cto-reviewer dispatched as a fresh parallel batch (each sees only the one-pager + its own doc + 01-objectives.md, never the target or each other), each review written to a file, then pm-synthesizer with a mandatory red-team.
- Each finalist is marked SHORTLIST (mean of five averages >= 8.0 AND no sub-score < 7 AND objectives >= 80) or NEAR-MISS (with the exact dimensions holding it back). Do not pad and do not inflate to reach the floor.

CHECK (plain text + saved files):
- Scoreboard: each finalist's five averages, the mean, lowest sub-score, objectives total, verdict.
- For each finalist: the full council packet with inline evidence + the documented red-team.
- One line per finalist: why it is distinct, and the single biggest open question for the manual deep-dive.

CONSTRAINTS:
- Score on absolute merit; never tune toward the floor; unattributed convenient numbers invalidate the score.
- INCOME TARGET = the ladder in 01-objectives.md (~$300K/founder mo12, ~$500K+ mo24, growing; $2M upside not required). Honor the rubric emphasis: must-have heaviest; do not over-penalize learnable domains; penalize field-ops and regulatory/SME-moat models.
- Clean-room each candidate; never refine in place; never disclose the floor/target to a council subagent.
- Read docs 01-08 first.
- Keep going until the END STATE is met.
```

---

## Going unsupervised later
Once this earns your trust, collapse Prompts 1-2 into a single /goal that auto-cuts
to ~5 without stopping (i.e., the funnel in `11-funnel.md` with the new agents),
and keep only Prompt 3's deep dive. Keep the checkpoints for now.
