# 09 — Goal Loop (the `/goal` command to kick off discovery)

This file holds the `/goal` command you paste to start the loop. The loop *rules*
live in `CLAUDE.md`, which Claude Code auto-loads from the project root. This file
is reference only — Claude Code does not execute it automatically.

---

## How to run

1. Put all the docs (`00`–`14`, including `06b`) + `CLAUDE.md` + the `.claude/agents/`
   folder in one local folder.
2. Open that folder as your project in Claude Code (terminal or desktop app).
3. Start a FRESH session so the agents (including the new `competitive-analyst`)
   load.
4. In the prompt box, type `/`, choose `/goal`, then paste the block below.
5. Let it run. Stay nearby and be ready to interrupt; don't leave an open-ended run
   going overnight.

---

## The `/goal` command (paste everything after `/goal`)

```
/goal Find and fully evaluate the TWO-TO-THREE strongest, materially distinct, need-to-have business concepts, scored HONESTLY the way real expert advisors would, and produce plain-English deliverables for each.

END STATE (done when ALL are true):
- The surfaced concepts are materially distinct from each other on customer AND market AND forcing function AND revenue mechanism (not flavors of one idea).
- Each surfaced concept has a COMPLETE frozen council packet: all SIX independent expert reviews (CFO, CMO, COO, Legal, CTO, Competitive Analyst) in their exact doc formats via the .claude/agents subagents run as a fresh parallel batch, plus a doc-07 PM Synthesis with a two-directional red-team.
- Each concept is scored on the doc-01 weighted rubric, assigned an Objectives Weighted Score (0-100) and a TIER (A Advisor-Ready / B Promising / C Pass), with the Legal RISK-GATE rating recorded. Surface the honest TOP 2-3 of the field, ranked — drawn from A and, if needed, the strongest B concepts. If the best are B-tier, say so plainly and surface them anyway; do NOT inflate to manufacture an A.
- For each surfaced concept, the doc-14 deliverables exist: a plain-English Concept Dossier + one-page Scorecard rendered to Word (.docx), text (.txt), and Markdown (.md), saved to the repo and delivered to the user as attachments (NO Google Drive); plus a master comparison sheet in Excel (.xlsx) covering the whole field.
- Each packet was produced under CLAUDE.md "Fresh-Evaluation Protocol": a clean-room restatement, no version number, no prior scores, no target disclosed to any council subagent.

CHECK (surface in plain text):
- Print a final scoreboard listing EVERY concept evaluated: its six expert averages, the Objectives Weighted Score, its lowest single sub-score, the Legal risk-gate rating, and its TIER.
- For EACH surfaced concept, restate 3 of its >=8 sub-scores with the specific inline evidence backing each (a named competitor/comparable, shown math, or a documented market signal). If any restated >=8 score is vague or unjustified, correct it (down OR up) and re-tier.
- State in one line how the surfaced concepts differ on customer + market + forcing function + revenue mechanism.

CONSTRAINTS (hold throughout):
- Score on ABSOLUTE merit per 00-evaluation-stage.md: symmetric calibration (do not inflate AND do not deflate), stage-aware (never deduct for missing user interviews / no built product / no traction — list those as next experiments). A genuinely strong, evidenced concept SHOULD earn 8s and 9s.
- "Must-have" = a strong forcing function of ANY of the five types in doc-01 (regulatory, contractual, critical-input, continuity, risk-mitigation). Regulation is one favorite path, not required. Maximize diversity across forcing-function types; do not cluster on compliance plays.
- Legal is a RISK GATE, not a weighted drag: a regulated-but-navigable business is NOT down-tiered for being regulated. Only a FATAL legal rating gates a concept down.
- Competition is first-class: the Competitive Analyst must NAME real incumbents/substitutes with researched data. A competitive section naming no real players is incomplete.
- Never disclose the tiers, prior scores, round count, or refinement status to any council subagent. Clean-room each candidate; never refine in place.
- Read docs 00-08 + 06b + 14 before scoring; honor every doc-01 hard constraint and doc-08 founder limit.
- Keep iterating until the END STATE is met, OR stop and print the full scoreboard + deliverables after 40 turns, whichever comes first.
```

---

## Tuning notes

- The output is the honest **top 2–3, ranked, with tiers** — not a binary pass/fail.
  A run can legitimately conclude "the best of the field is B-tier; here are the two
  strongest and what would move them to A." That is a correct, useful result.
- If you want a stricter shortlist, require TIER A only. If the field is thin, allow
  the strongest B concepts through to manual advisor review — the founders compare
  the top 2–3 against real experts regardless.
- The deliverables (doc 14) are mandatory: you should end every run with shareable
  .docx/.txt/.md dossiers + an .xlsx master comparison sheet, delivered to the user
  as attachments — not just markdown in the repo, and not via Google Drive.
