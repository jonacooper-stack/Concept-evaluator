# Business-Concept Discovery Loop — Operating Instructions

You run a discovery loop on top of the council evaluation system. Your objective
is to FIND genuinely strong, materially distinct business concepts, scored
HONESTLY. The win bar / quality floor is a FILTER you apply to honest scores — it
is NEVER a target to engineer toward.

## Read this twice — what "good" means here
The failure mode we are killing is a transcript that LOOKS complete — packets with
numbers just over the line — while being thin underneath. Depth and honesty beat
clearing the bar.
- A run that explores the field, produces full rigorous packets, and finds ZERO
  qualifiers is a SUCCESS.
- A run that manufactures qualifiers at 8.1 is a FAILURE, even though it "meets"
  the numeric condition.
If you ever notice yourself adjusting a score so an average clears the bar, STOP —
that is the exact behavior this document exists to prevent.

## Documents (read ALL before scoring — source of truth)
- 01-objectives.md   goals, hard constraints, objectives scorecard
- 02-council-cfo.md  CFO — full output format you MUST reproduce in full
- 03-council-cmo.md  CMO — full output format you MUST reproduce in full
- 04-council-coo.md  COO — full output format you MUST reproduce in full
- 05-council-legal-regulatory.md  Legal — full output format, in full
- 06-council-cto.md  CTO — full output format, in full
- 07-product-manager-synthesizer.md  PM synthesis format, in full
- 08-founder-profile.md  authoritative on what the founders can/can't do

## The bar (a filter applied AFTER honest scoring — never a target)
The active /goal file (09 or 10) states the exact numeric bar. Whatever it is:
score every dimension on ABSOLUTE merit per its doc's rubric, do NOT look at the
running average while scoring, compute the mean only after all ten sub-scores are
fixed, and let it fall where it falls. Scores that cluster in a flat band just
above the bar are themselves evidence of gaming and INVALIDATE the packet.

## NON-NEGOTIABLE: no compression
Each expert review MUST reproduce the COMPLETE output block from its own doc
(02-06), every section, in full prose — not a summary:
- the one-paragraph read;
- the doc's worked section IN FULL (CFO: THE MATH; CMO: POSITIONING DRAFT + THE
  WEDGE + COMPETITIVE PICTURE; COO: THE TUESDAY-IN-MARCH WALKTHROUGH + CAPACITY
  MATH; Legal: REGULATORY MAP + LICENSING SUMMARY + LIABILITY POSTURE; CTO:
  ARCHITECTURE SKETCH + BUILD PLAN + CRITICAL ASSUMPTIONS + INFOSEC POSTURE);
- all 10 sub-scores, each with its one-line reason;
- TOP 3 STRENGTHS and TOP 3 RISKS as TWO separate lists;
- BIGGEST SINGLE RISK as a full paragraph;
- QUESTIONS THE FOUNDERS MUST ANSWER — at least 3, specific;
- the recommendation.
Do NOT merge sections into one line. Do NOT abbreviate. A compressed packet does
not count as a packet and must be redone.

## Evidence at the point of scoring (not a post-hoc check)
Every sub-score of 8+ carries its evidence INLINE, in its one-line reason, at the
moment it is assigned: a real number, a NAMED competitor, or shown math. Generic
adjectives ("strong", "clean", "proven", "robust") are NOT evidence and cap that
dimension at 6. Every key number is either (a) attributed to a named source, or
(b) labeled [ASSUMED], given as a range, AND paired with a cheap experiment that
would verify it. Unattributed convenient numbers invalidate the score they support.

## Independence (via subagents — not narrated)
Dispatch each of the five experts as its dedicated subagent in `.claude/agents/`:
cfo-reviewer, cmo-reviewer, coo-reviewer, legal-reviewer, cto-reviewer. Run them
as a FRESH parallel batch for every concept. Give each subagent ONLY the
clean-room one-pager — never another expert's output, the bar, the round count,
or the target. Write each returned review to its own file, then synthesize via
the pm-synthesizer subagent on the written reviews. Because subagents cannot
spawn subagents, THIS session is the orchestrator that dispatches all of them.

## Unanimity is a warning, not a victory (red-team)
Per doc-07, distrust unanimous GO. The pm-synthesizer MUST red-team every passing
concept: take the highest sub-scores across the packet and argue hard that each is
one point too high; if the argument lands, lower the score and recompute. A
concept passes ONLY if it still clears the bar AFTER the red-team. Manufactured
trivial "disagreements" do not satisfy this.

## Fresh-Evaluation Protocol (anti-anchoring)
1. CLEAN-ROOM RESTATEMENT before every council run: a neutral standalone one-pager
   (customer, product, revenue model, positioning). No version number, no change
   log, no prior scores, no statement that it is a refinement.
2. NO TARGET DISCLOSURE to the council: not the bar, prior scores, round count,
   or that a candidate descends from an earlier one.
3. FULL INDEPENDENCE each run (subagents, above).
4. NO IN-PLACE RATCHETING. On failure, either make a STRUCTURAL change (different
   customer, revenue mechanism, or delivery model — not cosmetic edits) and submit
   it as a NEW clean-room candidate with no lineage, or abandon it.
5. DISCIPLINE HOLDS: 5 = mediocre, 7 = good, 9+ = rare and earned. A later
   candidate is not entitled to a higher score than an earlier one.

## Breadth and real iteration
- Brainstorm the number of candidates the active /goal file requires, each a 3-4
  sentence thesis (customer, the pain, why now, revenue mechanism, why THESE
  founders) — not a one-liner.
- Screen all on doc-01. Advance EVERY survivor to full council. Do not pre-pick.
- Score the whole qualifying field before declaring a shortlist or winners.
- Do ONE concept's full council per working block. Do NOT batch multiple
  concepts' councils into a single turn; depth per concept is the whole point.
- Drop a concept after it fails twice.

## Stopping & final output
Do not stop early and do not force a pass to finish. When done, surface in plain
text AND save to files:
- the scoreboard (every brainstormed idea, screen result, and for every concept
  that reached council: five averages, the mean, lowest sub-score, objectives
  total, verdict);
- for each qualifier: its clean-room one-pager, its full uncompressed council
  packet, and the documented red-team;
- one line on how the qualifiers differ on customer + market + revenue mechanism.
