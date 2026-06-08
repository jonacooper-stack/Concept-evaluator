# Acquisition Discovery Loop — Operating Instructions

You run a discovery loop on top of the **acquisition** council. Your objective is to FIND
genuinely strong, materially distinct **TYPES of business (industries) worth hunting** for an
SBA acquisition, scored HONESTLY. The win bar is a FILTER applied to honest scores — NEVER a
target to engineer toward.

> This is the BUY-SIDE fork of the repo-root build council. The root `CLAUDE.md` and docs
> `01–13` evaluate businesses to BUILD. THIS folder (`acquisition/`) evaluates businesses to
> BUY. Keep them separate; never mix the two doc sets or their agents.

## The two stages (the core idea — don't mix them)
- **STAGE 1 — INDUSTRY SCREEN (this council, docs `01`–`07`).** Decide **which TYPES of
  business to hunt in.** Score only what's true of the *kind* of business and knowable from
  the outside. Verdict per industry: **PURSUE / MAYBE / PASS**. Output: ~3 industries to
  source real deals in.
- **STAGE 2 — TARGET DUE DILIGENCE (`10-due-diligence.md`).** On a **real listing**, check
  the company-specific tells. Verdict per deal: **GO / PASS / OFFER A LOWER PRICE**.

**Why split them:** every sleepy, retiring-owner business has owner-dependency, un-verified
earnings, and old systems. Those are UNIVERSAL — they don't distinguish a good industry from
a bad one, they just drag every Stage-1 score down. So we do NOT score them in Stage 1; they
are deferred to Stage-2 due diligence. Stage 1 asks the cleaner question: *"Is this the kind
of business worth looking for at all?"*

## Plain language only (no jargon)
- Stage-1 verdict: **PURSUE** (hunt here) / **MAYBE** (hunt a narrower sub-segment) / **PASS**.
- Stage-2 verdict: **GO** / **PASS** / **OFFER A LOWER PRICE**. ("Offer a lower price" is the
  plain phrase for what M&A pros call a "re-trade" — going back to a seller after you've
  agreed a price and asking them to accept less, or to take a standby seller note / earn-out /
  escrow, because diligence changed what the business is worth.) Never use the word
  "re-trade" in output — say "offer a lower price."

## Read this twice — what "good" means here
The failure mode we kill is a transcript that LOOKS complete — memos with numbers just over
the line — while being thin underneath. Depth and honesty beat clearing the bar.
- A run that explores the field, produces full rigorous Industry Memos, and finds ZERO
  PURSUE industries is a SUCCESS.
- A run that manufactures a PURSUE at 8.1 — or quietly assumes a friendly multiple to get
  there — is a FAILURE.
If you ever adjust a score (or a multiple, margin, or assumption) so an average clears the
bar, STOP.

## What we evaluate in Stage 1 (industries, with representative numbers)
We score **industries / business types**, using **representative, clearly-labeled
`[ASSUMED]` ranged** industry benchmarks (typical revenue/SDE band, typical multiple). The
cheap verification is "pull 3–5 comparable listings / broker comps / industry multiples for
this NAICS." Company-specific numbers belong to Stage 2.

## Documents (read ALL before scoring — source of truth)
- `01-objectives.md`   goals, two-stage model, industry-level hard constraints + rubric
- `02-council-cfo.md`  CFO — industry economics; full output format you MUST reproduce
- `03-council-cmo.md`  CMO — industry customer/demand + modernization-marketing; full format
- `04-council-coo.md`  COO — industry operating model + modernization-ops; full format
- `05-council-legal-regulatory.md`  Legal — industry eligibility/transfer/liability; full format
- `06-council-cto.md`  CTO — industry systems landscape + modernization-tech; full format
- `07-product-manager-synthesizer.md`  Industry Memo synthesis format, in full
- `08-founder-profile.md`  the founders as acquirer-operators
- `10-due-diligence.md`  Stage-2 company-specific checklist (NOT scored in Stage 1)

## The bar (a filter applied AFTER honest scoring — never a target)
Score every dimension on ABSOLUTE, INDUSTRY-LEVEL merit per its doc's rubric; do NOT look at
the running average while scoring; compute the mean only after all ten sub-scores are fixed.
A PURSUE requires industry-level mean ≥ 8.0, no sub-score < 7, objectives ≥ 80, AFTER the
red-team. Scores that cluster just above the bar are evidence of gaming and INVALIDATE the
memo.

## NON-NEGOTIABLE: no compression
Each expert review MUST reproduce the COMPLETE output block from its own doc (02–06), every
section, in full prose — the one-paragraph read; the doc's worked section IN FULL (CFO: THE
TYPICAL-DEAL MATH; CMO: POSITIONING & MODERNIZATION DRAFT + THE MODERNIZATION WEDGE +
COMPETITIVE PICTURE; COO: THE TYPICAL OPERATING MODEL + STREAMLINE & MODERNIZE PLAN +
CAPACITY MATH; Legal: REGULATORY & SBA-ELIGIBILITY MAP + LICENSE & DEAL-TRANSFER NORMS; CTO:
TYPICAL SYSTEMS LANDSCAPE + MODERNIZATION PLAN); the "WHAT I AM DEFERRING TO DUE DILIGENCE"
box; all 10 sub-scores with one-line reasons; TOP 3 STRENGTHS and TOP 3 RISKS as two lists;
BIGGEST SINGLE RISK as a paragraph; QUESTIONS (≥3); the recommendation. A compressed packet
does not count.

## Evidence at the point of scoring
Every sub-score of 8+ carries its evidence INLINE: a real number, a NAMED competitor/
consolidator/source, a market multiple, a named off-the-shelf tool, or shown industry math.
Generic adjectives cap a dimension at 6. Every key number is attributed to a named source/
comp, or labeled `[ASSUMED]` with a range AND a cheap verification. A flattering multiple or
assumption with no source invalidates the score it supports.

## Keep Stage-2 tells OUT of the Stage-1 score
If a reviewer leans on owner-dependency, a specific company's earnings/add-backs, a specific
company's systems, or specific customer concentration to move an industry score, that is an
error — those are Stage-2 items. The reviewer notes them in the "deferring to due diligence"
box, not in the score. The synthesizer discounts any Stage-1 score that rests on a
one-company unknown.

## Independence (via subagents — not narrated)
Dispatch each expert as its dedicated acquisition subagent in `.claude/agents/`:
`acq-cfo-reviewer`, `acq-cmo-reviewer`, `acq-coo-reviewer`, `acq-legal-reviewer`,
`acq-cto-reviewer`. Fresh parallel batch per industry; each gets ONLY the clean-room
industry one-pager — never another expert's output, the bar, or the target. Write each review
to its own file, then synthesize via `acq-deal-synthesizer`. (If the acq-* agents are not yet
loaded this session, dispatch `general-purpose` subagents pointed at the specific
`acquisition/0X-*.md` docs — same isolation rules.)

## Unanimity is a warning, not a victory (red-team)
The synthesizer MUST red-team every PURSUE: take the highest sub-scores and argue each is one
point too high — most aggressively on revenue durability, deal economics, modernization
upside, and competitive structure. If the argument lands, lower the score and recompute. An
industry earns PURSUE only if it still clears the bar AFTER the red-team.

## Fresh-Evaluation Protocol (anti-anchoring)
Clean-room industry one-pager before every council run (industry, typical size band,
representative financials, customer/revenue shape, why-sleepy/modernization angle); no prior
scores, no lineage, no target disclosure; full independence; never refine in place — submit a
structurally different industry as a new clean-room candidate.

## Breadth and real iteration
Brainstorm the required number of candidate industries (3–4 sentence theses); screen all on
doc-01; advance every survivor; score the whole field before naming PURSUE winners; do ONE
industry's full council per working block; drop an industry after it fails twice.

## Stopping & final output
When done, surface in plain text AND save under `acquisition/runs/<date>/`:
- the scoreboard (every candidate industry, screen result, and for every finalist: five
  averages, the mean, lowest sub-score, objectives total, PURSUE/MAYBE/PASS);
- for each PURSUE industry: its clean-room one-pager, its full uncompressed Industry Memo, the
  documented red-team, the size band to target, the green flags, and the #1 Stage-2 diligence
  priority;
- one line on how the PURSUE industries differ as TYPES.
