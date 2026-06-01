# 09 — Goal Loop (the `/goal` command to kick off discovery)

This file just holds the `/goal` command you paste to start the loop, plus a
quick reminder of how to run it. The loop *rules* live in `CLAUDE.md`, which
Claude Code auto-loads from the project root. This file is reference only —
Claude Code does not execute it automatically.

---

## How to run

1. Put this folder's eight docs (`01`–`08`) + `CLAUDE.md` in one local folder.
2. Open that folder as your project in Claude Code (terminal or desktop app).
3. Confirm Claude Code is **v2.1.139 or later** (`/goal` requires it).
4. In the prompt box, type `/` to browse slash commands, choose `/goal`, then
   paste the entire block below as the condition.
5. Let it run. A separate evaluator checks the transcript after every turn and
   keeps the session going until the END STATE is met (or the 40-turn cap hits).
   The goal clears itself automatically once two winners are confirmed.
6. Stay nearby and be ready to interrupt; don't leave an open-ended run going
   overnight.

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Find and fully validate TWO distinct business concepts that each clear the council bar.

END STATE (done only when ALL are true):
- The transcript contains TWO concepts that are materially distinct from each other on customer AND market AND revenue mechanism (not two flavors of one idea).
- Each concept has a COMPLETE frozen council packet: the doc-01 Objectives Scorecard, all five independent expert reviews (CFO, CMO, COO, Legal, CTO) in their exact doc formats, and a doc-07 PM Synthesis.
- For each concept: the MEAN of the five expert averages is > 8.0, AND no single expert sub-score is below 7, AND the Objectives weighted total is >= 80.
- Each winning packet was produced under CLAUDE.md "Fresh-Evaluation Protocol": a clean-room restatement with no version number, no change log, no prior scores, no statement that it is a refinement.

CHECK (surface in plain text so the evaluator can read it from the transcript):
- Print a final scoreboard listing EVERY concept evaluated: its five expert averages, the mean of those five, its lowest single sub-score, its objectives total, and PASS/FAIL.
- For EACH of the two winners, restate 3 randomly chosen >=8 sub-scores per expert with the specific evidence backing each (a number, a named competitor, or shown math, per that expert doc's style rules). If any restated >=8 score is vague or unjustified, mark that concept FAIL and keep going.
- State in one line how the two winners differ on customer + market + revenue mechanism.

CONSTRAINTS (hold throughout):
- Never refine a concept in place and re-score it as the same concept. On failure, either make a STRUCTURAL change targeting the failing dimensions or generate a new concept, then submit it to the council as a brand-new clean-room candidate with NO lineage.
- Never tell the council the target, the win bar, prior scores, the round count, or that a candidate is a refinement. (This goal condition is for you, the worker; the council scoring step stays blind to it.)
- Apply scoring discipline literally: 5 = mediocre, 7 = good, 9+ = rare and earned. Scores must not drift upward across rounds; a later candidate is not entitled to a higher score than an earlier one.
- Drop any concept that fails twice.
- Read docs 01-08 (including 08-founder-profile.md) before scoring; honor every hard constraint in doc 01 and the founder limits in doc 08.
- Keep iterating until the END STATE is met, OR stop and print the full scoreboard after 40 turns, whichever comes first.
```

---

## Tuning notes

- The bar is strict (mean > 8 with a hard floor of 7, plus the evidence
  spot-check that can fail an inflated score), so expect many candidates to be
  burned and the 40-turn cap to sometimes hit before two clean winners emerge.
- If it caps out: raise the turn limit, or temporarily relax the objectives
  gate (drop the `>= 80` clause), then re-run.
- To loosen the win bar, edit both this command AND the `## The win bar`
  section of `CLAUDE.md` so they stay in sync.
