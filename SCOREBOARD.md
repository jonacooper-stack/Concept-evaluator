# Master Scoreboard — Guided Funnel Run (2026-06-01)

Branch: `claude/sweet-dirac-Ko4lR`. Bar (active /goal): **SHORTLIST** = mean of the five
expert averages ≥ 8.0 AND no sub-score < 7 AND objectives ≥ 80; else **NEAR-MISS**.
The bar is a FILTER applied to honest scores, never a target.

## Funnel summary
- **Stage 1 (generate):** 106 on-thesis theses (idea-generator, Opus) → `stage1-idea-pool.md`
- **Stage 2 (first cut):** triaged in 3 parallel Opus batches → top 30 → `stage2-triage-top30.md`
- **User checkpoint 1:** keeps/kills/maybes → narrowed to top 10 → `stage2b-top10-finalists.md`
- **User checkpoint 2:** killed GLBAsafeguards (Drata encroachment) + PatientRightsDesk (crowded/EMR-integration); requested quick pass on the remaining 8 then full council on the top 4
- **Stage 3 (quick pass):** sharpened lens (horizontal-platform encroachment + integration depth) → top 4 → `stage3-quickpass-top4.md`
- **Stage 4 (full council):** 4 concepts × (clean-room one-pager + 5 blind reviewers + PM red-team) → `councils/`

## FULL-COUNCIL RESULTS (post red-team)

| # | Concept | CFO | CMO | COO | Legal | CTO | MEAN | Lowest sub | Objectives | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DefenseFOCIdesk | 7.5 | 7.2 | 6.2 | 5.6 | 6.9 | **6.68** | 3 (Legal) | 77 | NEAR-MISS → REFINE |
| 2 | ContractorPrevailingWage | 7.4 | 7.4 | 6.8 | 7.3 | 6.7 | **7.12** | 5 | ~78 | NEAR-MISS → REFINE (strongest) |
| 3 | InsuranceLicenseHub | 6.7 | 6.5 | 6.5 | 6.4 | 6.8 | **6.6** | 4 (CMO air) | 66 | NEAR-MISS leaning FAIL (trips hard-constraint #5) |
| 4 | CLIAlabComply | 7.3 | 7.2 | 6.7 | 6.3 | 7.6 | **6.96** | 4 (Legal PHI) | 78 | NEAR-MISS → REFINE (one number from GO) |

**SHORTLIST qualifiers: ZERO.** No concept cleared mean ≥ 8.0 with no sub-score < 7 and
objectives ≥ 80. Scored honestly, the field produced four NEAR-MISSes and no pass. Per the
operating doc, a rigorous run that finds zero qualifiers is a SUCCESS, not a failure — the
value is the honest depth, not a manufactured 8.1.

## Ranking of the near-misses
1. **ContractorPrevailingWage (7.12)** — best mean; cleanest demand + legal posture; the gap is buildable operational/technical drag (software-vs-headcount margin hinge, jurisdiction/portal maintenance treadmill), not anything structural.
2. **CLIAlabComply (6.96)** — best CTO score (7.6) and genuinely clean competitive air; "one validated cost-to-serve number from GO"; held by HIPAA/PHI floor + credentialed-specialist throughput dependency.
3. **DefenseFOCIdesk (6.68)** — strongest must-have pull in the field, but a cleared-personnel single-point-of-failure, an uninsurable FCA/ITAR liability tail, and a defense-grade CUI self-compliance burden (Legal 3s).
4. **InsuranceLicenseHub (6.6)** — plausibly trips hard-constraint #5: AgentSync (well-funded, a16z/Tiger, modern-tech, purpose-built) + Vertafore/Sircon; the managed-service wedge is a delivery motion a funded incumbent can replicate in ~2 quarters.

## How the (non-)qualifiers differ — customer × market × revenue mechanism
- **DefenseFOCIdesk** — small cleared defense contractors with foreign ownership · DCSA/NISPOM clearance-retention mandate · annual subscription + managed self-inspection retainer.
- **ContractorPrevailingWage** — public-works construction contractors/subs · Davis-Bacon weekly certified payroll (payment withheld if missed) · per-project/month subscription + managed filing.
- **InsuranceLicenseHub** — multi-state insurance agencies/MGAs · producer licensing/appointment/CE (lapse voids commissions) · per-producer/month subscription + per-transaction filing fees.
- **CLIAlabComply** — independent/small clinical & physician-office labs · CLIA quality program + biennial inspection (lapse halts testing & billing) · per-lab/certificate subscription + inspection-prep retainer.

## Single biggest open question per concept (for any manual deep-dive)
- DefenseFOCIdesk: can the cleared-personnel dependency become a durable multi-person bench, and can the full scope stay on the uncleared-administration side of the classified/CUI line?
- ContractorPrevailingWage: what is the true per-project human-exception rate under the perjury-grade standard (software service vs headcount consultancy)?
- InsuranceLicenseHub: is there a sub-segment AgentSync structurally cannot/will not serve, and does NIPR grant bootstrap-viable Gateway access (not routed through competitor Vertafore/Sircon)?
- CLIAlabComply: how many labs can one credentialed specialist carry through a full biennial cycle, and what does that do to blended gross margin?

## Artifacts
- `stage1-idea-pool.md`, `stage2-triage-top30.md`, `stage2b-top10-finalists.md`, `stage3-quickpass-top4.md`
- `councils/01-defensefoci/`, `councils/02-prevailingwage/`, `councils/03-insurancelicense/`, `councils/04-cliacomply/` — each with `one-pager.md`, five reviewer files, and `SYNTHESIS.md`
