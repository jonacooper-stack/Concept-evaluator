---
name: deliverables-and-artifacts
description: The plain-English artifacts the founders actually read and share — a Concept Dossier and a one-page Scorecard per concept, plus a master comparison sheet across the whole field. Defines the required sections, the plain-language standard, and exactly how to render them to Word (.docx), text (.txt), Markdown (.md), and Excel (.xlsx), save them to the repo, and deliver them as attachments. No Google Drive. The point: NEVER make the founders dig through GitHub markdown to understand or share a concept.
---

# 14 — Deliverables & Artifacts (plain English, shareable)

The council packets (docs 02–06b) are the rigorous internal record. They are NOT the
deliverable the founders read. **For every concept you surface (especially the top
2–3), you MUST also produce plain-English artifacts**, written for a smart non-expert
(the other founder, Mike), and deliver them as files — not as markdown buried in
GitHub.

## The plain-language standard
- Write like you're explaining it to a sharp friend over coffee. No jargon, no
  acronyms without a plain gloss, no council-speak, no unexplained scores.
- Lead with what it is and why anyone would pay. Put the money in plain terms.
- Every number a normal person can follow ("about 120 customers paying ~$2,500/mo
  gets each founder to ~$300K/yr"). Flag estimates as estimates.
- One dossier should be readable in 5–10 minutes and forwardable as-is.

## Artifact 1 — CONCEPT DOSSIER (one per surfaced concept)
Required sections, in this order:

```
<CONCEPT NAME>
Tier: [A Advisor-Ready / B Promising / C Pass]   |   Objectives Score: [x]/100   |   Date

1. IN ONE PARAGRAPH
   What it is, in plain English. The customer, what we sell them, how they use it.

2. WHO PAYS — AND WHY THEY CAN'T SAY NO
   Name the buyer. State the FORCING FUNCTION explicitly and which of the five types
   it is (regulatory mandate / contractual requirement / critical input to their
   production / operational-financial continuity / effectively-mandatory risk). Say
   what breaks for them, and how fast, if they don't buy. This is the need-to-have test.

3. THE MONEY (PLAIN TERMS)
   Price, how often they pay, and the simple math to each founder's income on the
   ladder (~$300K by mo12, ~$500K+ by mo24). Show the customer count needed. Label
   assumptions.

4. WHY WE WIN
   The sleepy incumbents we out-position (named), and the founders' edge (marketing,
   positioning, software, founder-led close). Why now.

5. THE COMPETITION (FROM THE ANALYST)
   The 3–5 most relevant named players and why they're beatable (or the real danger),
   in plain language. Pricing benchmarks. Whether a big platform could move in.

6. THE BIGGEST RISKS (TOP 3, PLAIN)
   The three things most likely to make this not work, stated honestly.

7. WHAT WE'D TEST NEXT (CHEAP EXPERIMENTS)
   The 3–5 fastest, cheapest ways to validate the thesis before building — the
   concept-stage next steps (e.g., interviews to run, a landing-page smoke test, a
   pricing call). These are NEXT STEPS, not reasons the score is lower.

8. THE SCORECARD (PLAIN)
   The 9 objectives dimensions with one plain sentence each on why it scored what it
   did. The Legal risk-gate rating in one line. The honest tier and what would move
   it up a tier.

9. APPENDIX — full council packet
   The six complete expert reviews + PM synthesis + the documented red-team, verbatim,
   for anyone who wants the rigor behind the plain-English summary.
```

## Artifact 2 — ONE-PAGE SCORECARD (one per surfaced concept)
A single page: concept name, tier, Objectives Score /100, the 9 dimension scores in
a small table with one-line reasons, the six expert averages, the Legal risk-gate
rating, the lowest single sub-score, and the one-line "what moves it up a tier."

## Artifact 3 — MASTER COMPARISON SHEET (one per run)
A single table covering the WHOLE field: every concept that reached council, one row
each — name, forcing-function type, Objectives Score, the six expert averages, lowest
sub-score, Legal risk-gate rating, tier, and a one-line "what it is." Sorted by
Objectives Score. This is the at-a-glance scoreboard the founders skim first.

## Rendering & delivery (REQUIRED formats: .docx, .txt, .md; .xlsx for the sheet)
Write each prose artifact (Concept Dossier, Scorecard) as Markdown first, then render
with the helper script in this repo:

```
# Prose dossier / scorecard -> .md + .txt + .docx
python3 scripts/build_deliverables.py deliverables/<concept>-dossier.md --outdir deliverables/

# Master comparison sheet / scoreboard: write a .csv, render to .xlsx
python3 scripts/build_deliverables.py deliverables/scoreboard.csv --outdir deliverables/
```

The prose mode emits `<name>.md`, `<name>.txt`, and `<name>.docx` (via python-docx).
The CSV mode emits `<name>.csv` and a formatted `<name>.xlsx` (via openpyxl). Install
the backends once if missing: `pip install python-docx openpyxl`. (PDF is NOT part of
the standard set; pass `--pdf` only if someone explicitly wants one — it needs
LibreOffice or reportlab.)

Then:
1. Save all rendered files under `deliverables/<run-date>/` in the repo.
2. **Deliver every file to the user as an attachment** (the Concept Dossiers, the
   Scorecards, and the Excel comparison sheet) so they can open and forward to Mike
   without touching GitHub. Do NOT use Google Drive or any external upload — just
   attach the files.

## Acceptance check
A run is not "done" until, for each surfaced concept, a Concept Dossier + Scorecard
exist as .docx + .txt + .md, the master comparison sheet exists as .xlsx (+ .csv),
all are saved to the repo AND delivered to the user as attachments, and the dossiers
read in plain English a non-expert could act on. Burying the analysis in markdown
does not count.
