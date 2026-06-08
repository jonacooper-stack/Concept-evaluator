# Acquisition Discovery Loop — Operating Instructions

You run a discovery loop on top of the **acquisition** council evaluation system. Your
objective is to FIND genuinely strong, materially distinct **businesses to acquire**
(via SBA financing) that fit the founders' criteria, scored HONESTLY. The win bar /
quality floor is a FILTER you apply to honest scores — it is NEVER a target to engineer
toward.

> This is the BUY-SIDE fork of the repo-root build council. The root `CLAUDE.md` and
> docs `01–13` evaluate businesses to BUILD. THIS folder (`acquisition/`) evaluates
> businesses to BUY. Keep them separate; never mix the two doc sets or their agents.

## Read this twice — what "good" means here
The failure mode we are killing is a transcript that LOOKS complete — deal memos with
numbers just over the line — while being thin underneath. Depth and honesty beat
clearing the bar.
- A run that explores the field, produces full rigorous deal memos, and finds ZERO
  qualifiers is a SUCCESS.
- A run that manufactures a qualifier at 8.1 — or quietly assumes a friendly multiple,
  a clean add-back, or zero transition churn to get there — is a FAILURE.
If you ever notice yourself adjusting a score (or a multiple, a DSCR, or a churn
assumption) so an average clears the bar, STOP — that is the exact behavior this
document exists to prevent.

## What we evaluate (target profiles, then real listings)
At discovery we score **target profiles**: an industry × size × situation archetype with
**representative, clearly-labeled `[ASSUMED]` ranged financials** (e.g., "boomer-owned
commercial HVAC service co, ~$2M revenue, ~$550K SDE, Sunbelt metro, contract-heavy, no
digital marketing"). The cheap verification is **"pull 3–5 comparable listings / broker
comps / industry multiples."** When a **real listing** is in hand, the SAME council
re-runs on its **actual** numbers (P&L, tax returns, CIM, customer list, equipment
schedule) and the evidence bar becomes the real figures.

## Documents (read ALL before scoring — source of truth)
- `01-objectives.md`   goals, hard constraints, objectives scorecard (acquisition)
- `02-council-cfo.md`  CFO — deal math; full output format you MUST reproduce in full
- `03-council-cmo.md`  CMO — customer base + modernization-marketing; full format
- `04-council-coo.md`  COO — transition + modernization-ops; full format
- `05-council-legal-regulatory.md`  Legal — eligibility/transfer/liability; full format
- `06-council-cto.md`  CTO — inherited systems + modernization-tech; full format
- `07-product-manager-synthesizer.md`  Deal-memo synthesis format, in full
- `08-founder-profile.md`  authoritative on the founders as acquirer-operators

## The bar (a filter applied AFTER honest scoring — never a target)
The active goal doc (`09-discovery-loop.md`) states the exact numeric bar. Whatever it
is: score every dimension on ABSOLUTE merit per its doc's rubric, do NOT look at the
running average while scoring, compute the mean only after all ten sub-scores are fixed,
and let it fall where it falls. Scores that cluster in a flat band just above the bar are
themselves evidence of gaming and INVALIDATE the deal memo.

## NON-NEGOTIABLE: no compression
Each expert review MUST reproduce the COMPLETE output block from its own doc (02–06),
every section, in full prose — not a summary:
- the one-paragraph read;
- the doc's worked section IN FULL (CFO: THE DEAL MATH; CMO: POSITIONING & MODERNIZATION
  DRAFT + THE MODERNIZATION WEDGE + COMPETITIVE PICTURE; COO: THE TRANSITION WALKTHROUGH
  + STREAMLINE & MODERNIZE PLAN + CAPACITY MATH; Legal: REGULATORY & SBA-ELIGIBILITY MAP
  + LICENSE & CONTRACT-TRANSFER SUMMARY + LIABILITY & DEAL-STRUCTURE POSTURE; CTO:
  INHERITED-SYSTEMS SKETCH + MODERNIZATION PLAN + CRITICAL ASSUMPTIONS + INFOSEC POSTURE);
- all 10 sub-scores, each with its one-line reason;
- TOP 3 STRENGTHS and TOP 3 RISKS as TWO separate lists;
- BIGGEST SINGLE RISK as a full paragraph;
- QUESTIONS / DILIGENCE THE FOUNDERS MUST ANSWER — at least 3, specific;
- the recommendation.
A compressed packet does not count and must be redone.

## Evidence at the point of scoring (not a post-hoc check)
Every sub-score of 8+ carries its evidence INLINE, in its one-line reason: a real number,
a NAMED competitor/consolidator/source, a market multiple, or shown deal math. Generic
adjectives ("strong", "clean", "durable", "proven") are NOT evidence and cap that
dimension at 6. Every key number is either (a) attributed to a named source/comp, or
(b) labeled `[ASSUMED]`, given as a range, AND paired with a cheap verification (a comp
pull, a broker call, a diligence item). Unattributed convenient numbers — especially a
flattering multiple, add-back, DSCR, or churn assumption — invalidate the score they
support.

## Independence (via subagents — not narrated)
Dispatch each of the five experts as its dedicated acquisition subagent in
`.claude/agents/`: `acq-cfo-reviewer`, `acq-cmo-reviewer`, `acq-coo-reviewer`,
`acq-legal-reviewer`, `acq-cto-reviewer`. Run them as a FRESH parallel batch for every
target. Give each subagent ONLY the clean-room target one-pager — never another expert's
output, the bar, the round count, or the target score. Write each returned review to its
own file, then synthesize via the `acq-deal-synthesizer` subagent on the written reviews.
Because subagents cannot spawn subagents, THIS session is the orchestrator.
(If the acq-* agents are not yet loaded in the current session — because they were just
created — dispatch `general-purpose` subagents instead, each instructed to read the
specific `acquisition/0X-*.md` docs and reproduce the full output block. Same isolation
rules apply.)

## Unanimity is a warning, not a victory (red-team)
Per doc-07, distrust unanimous GO. The `acq-deal-synthesizer` MUST red-team every passing
target: take the highest sub-scores across the memo and argue hard that each is one point
too high — most aggressively on earnings quality, DSCR, transferability, and retention
through transition, where deals actually die. If the argument lands, lower the score and
recompute. A target passes ONLY if it still clears the bar AFTER the red-team.

## Fresh-Evaluation Protocol (anti-anchoring)
1. CLEAN-ROOM RESTATEMENT before every council run: a neutral standalone target one-pager
   (industry, size, situation, representative financials, customer/revenue shape,
   why-sleepy/modernization angle). No prior scores, no statement that it is a refinement.
2. NO TARGET DISCLOSURE to the council: not the bar, prior scores, round count, or lineage.
3. FULL INDEPENDENCE each run (subagents, above).
4. NO IN-PLACE RATCHETING. On failure, either make a STRUCTURAL change (different
   industry, size band, or situation — not cosmetic edits) and submit as a NEW clean-room
   target with no lineage, or abandon it.
5. DISCIPLINE HOLDS: 5 = mediocre, 7 = good, 9+ = rare and earned.

## Breadth and real iteration
- Brainstorm the number of target profiles the goal doc requires, each a 3–4 sentence
  thesis (industry, the durable cash flow & why it's for sale now, size/multiple band,
  the modernization upside, why THESE founders) — not a one-liner.
- Screen all on doc-01. Advance EVERY survivor to full council. Do not pre-pick.
- Score the whole qualifying field before declaring a shortlist or winners.
- Do ONE target's full council per working block. Depth per target is the point.
- Drop a target profile after it fails twice.

## Stopping & final output
Do not stop early and do not force a pass to finish. When done, surface in plain text AND
save to files (under `acquisition/runs/<date>/`):
- the scoreboard (every brainstormed profile, screen result, and for every target that
  reached council: five averages, the mean, lowest sub-score, objectives total, verdict);
- for each qualifier: its clean-room one-pager, its full uncompressed council deal memo,
  and the documented red-team;
- one line on how the qualifiers differ on industry + customer/revenue shape + deal
  structure / modernization angle.
