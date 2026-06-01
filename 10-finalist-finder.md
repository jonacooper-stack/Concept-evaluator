# 10 — Finalist Finder (breadth-first /goal variant)

Use this INSTEAD of 09-goal-loop.md when you want the loop to do the wide,
honest search and hand you a ranked shortlist of strong finalists — which you
then deep-dive yourself with the original orchestration prompt (one finalist at
a time, with your own pushback). That manual pass is where the deepest analysis
comes from; this loop's job is to find the field cheaply and honestly.

Loop RULES still live in `CLAUDE.md`. Council INDEPENDENCE is enforced by the
subagents in `.claude/agents/` (cfo-reviewer, cmo-reviewer, coo-reviewer,
legal-reviewer, cto-reviewer, pm-synthesizer) — see the architecture note from
the assistant.

---

## The bars (raise or lower in ONE place — keep in sync with CLAUDE.md)
- BRAINSTORM POOL: at least 20 candidate theses.
- SCREEN to reach council: objectives weighted total >= 78 AND no objectives
  dimension below 6.  (Raised from the system default of 70.)
- QUALITY FLOOR to be a finalist: honest council mean >= 8.0 AND no sub-score
  below 7 AND objectives >= 80.
- SHORTLIST SIZE: the top 4-5 qualifiers, ranked by mean.
- (Stricter option: push the QUALITY FLOOR mean to >= 8.2 if you want a tighter
  shortlist. Change it here AND in the /goal block below.)

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Run an HONEST, breadth-first search and surface a ranked shortlist of up to 5 strong, distinct finalist concepts for manual deep-dive. Honesty over quantity: if only 2-3 clear the quality floor, surface those plus the closest near-misses — do NOT pad the shortlist with weak ideas. Scores are honest first; the floor is a filter, never a target.

END STATE (done when ALL true):
- At least 20 candidate concepts were brainstormed (each a 3-4 sentence thesis) and screened on doc-01.
- Every concept that passed the screen (objectives >= 78 AND no objectives dimension < 6) received a FULL independent council pass — five experts via the .claude/agents subagents, run as a fresh parallel batch for that concept — and an honest score.
- A ranked shortlist of up to 5 finalists is produced: concepts clearing the QUALITY FLOOR (honest council mean >= 8.0 AND no sub-score < 7 AND objectives >= 80), shown top-down by mean. If fewer than 4 clear, show those that do PLUS the 2-3 closest NEAR-MISSES, each labeled with the exact dimensions holding it back.
- Finalists are materially distinct from one another on customer / market / revenue mechanism; if two are flavors of one idea, keep the stronger and pull in the next qualifier.

CHECK (surface in plain text AND saved files):
- Scoreboard: every brainstormed idea, its screen result, and for each council-scored concept its five expert averages, the mean, the lowest single sub-score, the objectives total, and SHORTLIST / NEAR-MISS / FAIL.
- For each shortlisted finalist: its FULL uncompressed council packet (every expert's complete doc-format review with inline evidence) plus a LIGHT red-team via pm-synthesizer (challenge the 2 highest sub-scores; defend with hard evidence or lower).
- For each finalist: one line on why it is distinct from the others, and a one-line handoff note naming the single biggest open question the manual deep-dive should resolve first.

CONSTRAINTS (hold throughout):
- Score each dimension on absolute merit via the dedicated council subagents (cfo-reviewer, cmo-reviewer, coo-reviewer, legal-reviewer, cto-reviewer) in .claude/agents/, dispatched as a FRESH parallel batch per concept. Never pass one expert's output to another. Never disclose the floor, screen, target, or round count to a council subagent. Synthesize via pm-synthesizer.
- Clean-room every candidate (no version number, lineage, or prior scores). Never refine in place: on failure make a STRUCTURAL change as a NEW candidate or drop. Drop after two failures.
- Do NOT look at the running average while scoring; never tune a score toward the floor. Convenient unattributed numbers invalidate the score they support.
- Read docs 01-08 first; honor every doc-01 hard constraint and every doc-08 founder limit.
- Keep going until the END STATE is met. Do not stop early and do not pad the shortlist.
```

---

## Handoff to the deep-dive
For each finalist, take its clean-room one-pager into a fresh conversation with
your ORIGINAL orchestration prompt (the seven-doc workflow), one finalist at a
time, and push back hard with real market knowledge. The finalist packets here
are the starting point, not the final word.
