# SCOREBOARD — Discovery Run 2026-06-09 (branch claude/stoic-thompson-48nvvx)

## The bar (set by the operator this session)
A concept QUALIFIES only if BOTH hold, on honest red-teamed scores:
- **Objectives weighted total (doc-01) > 75 / 100**, AND
- **each of the five expert averages (CFO, CMO, COO, Legal, CTO) ≥ 7.5 / 10.**

The bar is a FILTER applied to honest scores, never a target. Scores were fixed
before the mean was computed; the PM red-team only ever LOWERED scores.

## Outcome: 5 council passes (the operator's cap), ZERO qualifiers.
Per CLAUDE.md, a rigorous run that finds zero qualifiers is a SUCCESS, not a failure.
Nothing was nudged to clear the line. This reproduces the prior-corpus pattern:
across ~45 earlier concepts in 10 branches, none ever cleared the (stricter) native bar.

## Brainstorm → triage (14 fresh candidates, all clear of the 45-concept prior ledger)

| Triage rank | Concept | Triage obj /100 | Disposition |
|---|---|---|---|
| 1 | AccessGuard | 82 | → COUNCIL |
| 2 | ChemSDS | 80 | → COUNCIL |
| 3 | FranAudit | 78 | → COUNCIL |
| 4 | ProxyDocket | 77 | → COUNCIL |
| 5 | GovRenew | 75 | → COUNCIL |
| 6 | TariffLedger | 74 | held (triage only) |
| 7 | EmissionsLedger | 72 | held (triage only) |
| 8 | FundFiler | 71 | held (triage only) |
| 9 | RenewRail | 70 | held (triage only) |
| 10 | AdReg | 68 | dropped |
| 11 | BoardBinder | 67 | dropped (field/vendor-ops drift) |
| 12 | AgMandate | 66 | dropped (farm-side manual capture) |
| 13 | CredentialVault | 64 | dropped (funded incumbents + integration) |
| 14 | PrevailFile | 62 | dropped (VC-funded PA warzone; constraint #5) |

Note: triage obj is a fast gut-check. This run's triage→council gap averaged ~8 points
(triage optimism), so the held/dropped triage estimates are likely high.

## Full-council results (POST red-team) — the five passes

| # | Concept | CFO | CMO | COO | Legal | CTO | Mean | Lowest expert avg | Obj /100 | PASS? |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AccessGuard | 7.4 | 7.5 | 6.7 | 7.2 | 6.9 | **7.14** | 6.7 (COO) | **72.0** | FAIL |
| 2 | ChemSDS | 7.5 | 7.3 | 7.6 | 6.5 | 6.6 | **7.10** | 6.5 (Legal) | **75.0** | FAIL |
| 3 | FranAudit | 7.3 | 7.7 | 6.0 | 4.8 | 7.2 | **6.60** | 4.8 (Legal) | **71.5** | FAIL |
| 4 | ProxyDocket | 7.0 | 7.2 | 6.4 | 6.2 | 6.1 | **6.58** | 6.1 (CTO) | **69.5** | FAIL |
| 5 | GovRenew | 7.5 | 7.3 | 6.9 | 6.0 | 7.4 | **7.02** | 6.0 (Legal) | **70.5** | FAIL |

Bar test: NONE cleared obj > 75 (ChemSDS touched 75.0 exactly, not >75), and NONE
had all five expert averages ≥ 7.5. Every concept was held below the bar by at least
one structural drag, and the red-team widened (never closed) those gaps.

## Why each missed (the one structural drag per concept)
- **AccessGuard** — the part that scales (the automated WCAG crawler) isn't the part
  that protects the client; the defensible work (manual audit + legal-grade
  attestation) is human labor that scales near-linearly (COO 6.7, CTO 6.9). Plus a
  funded incumbent in the lane (AudioEye, public).
- **ChemSDS** — authoring a safety document carries a third-party bodily-injury /
  failure-to-warn liability tail that contracts can't fully cap (Legal 6.5), and the
  chemist sign-off + hazard-data dependency may not compress with software (CTO 6.6).
- **FranAudit** — the FDD IS a legal document; preparing/amending it and answering
  examiner comment letters is the practice of law → UPL + Rule 5.4 fee-split; the
  compliant structure collapses the margin/differentiation (Legal 4.8). Plus a
  Dec-31 fiscal-year-end seasonality spike + single-attorney bottleneck (COO 6.0).
- **ProxyDocket** — demand bifurcates (acute audit/VDA minority vs latent cold
  majority — the latent-demand trap); the true unit of work is bespoke financial-data
  ingestion + specialist judgment that resists software (CTO 6.1, COO 6.4); Oct-31
  seasonality spike; multi-state jurisdictional complexity is the product (Legal 6.2).
- **GovRenew** — the headline credential (SAM) is FREE/DIY, anchoring WTP low; the
  premium differentiator (eligibility attestation) imports the False Claims Act +
  UPL, fraud-excluded by E&O and founder-personal (Legal 6.0). The part that
  justifies the price is the part that must be cut for safety.

## Recurring failure modes across BOTH this run and the 45-concept prior corpus
1. The software-vs-BPO margin hinge (the defensible work is human and scales linearly).
2. Liability coupling (the value prop and the largest liability are the same thing).
3. Latent vs forced demand (a "should-comply" deferred until enforcement is acute).
4. Funded/strong-tech incumbent encroachment in the lane (constraint #5).
5. UPL / "this is legal work" when the deliverable is a legal document or opinion.
