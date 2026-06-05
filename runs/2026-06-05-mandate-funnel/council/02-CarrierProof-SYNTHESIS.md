# PM SYNTHESIS — CarrierProof (Appointment-Maintenance Managed Service for Insurance Agencies)

## VERDICT: NEAR-MISS (leaning FAIL) — REFINE
Post-red-team **mean 7.1/10** · lowest sub-score **5** (CMO Customer truth; COO QC simplicity; Legal Jurisdictional) · objectives ~low-to-mid 70s. Clears NONE of the three PASS gates (mean ≥8.0, no sub <7, objectives ≥80). Council's modal verdict was REFINE (3 REFINE, 2 conditional GO).

## SCORE SUMMARY
| Expert | Avg (pre-RT) | Avg (post-RT) |
|---|---|---|
| CFO | 7.8 | 7.7 |
| CMO | 6.4 | 6.4 |
| COO | 6.7 | 6.7 |
| Legal | 6.8 | 6.8 |
| CTO | 7.8 | 7.7 |
| **MEAN** | **7.1** | **7.1** |

## RED-TEAM (what got lowered)
- CFO Working-capital 9 → 8 (annual-upfront prepay is an assumption; slow cash-conscious small-agency buyers may push monthly).
- CTO Time-to-MVP 9 → 8 ("revenue before code on a spreadsheet" imports the manual-labor exposure the COO flags — double-counts a strength that's also a liability).
- Survived: CFO capital efficiency 9, CTO feasibility 9, COO logistics 9.

## KEY TENSION
CFO/CTO (7.8, architecture + build strong) vs CMO/COO (6.4/6.7, demand + labor unproven). PM call: CMO/COO frames are load-bearing — felt urgency and labor-templatability are upstream of the strong economics. **AgentSync** ($100M+ raised, $1.2B valuation 2021, modern NIPR API, strong-tech) contradicts the one-pager's "sleepy incumbents" framing and bears on hard-constraint #5; does NOT auto-disqualify (target is genuinely downmarket of AgentSync's carrier/large-distributor focus; play is relationship/positioning-led managed service, not an engineering arms race) but caps competitive-air at 6 and is a live tail risk.

## TOP 5 RISKS
1. Felt-urgency / customer-truth gap — is appointment risk felt/budgeted BEFORE a lapse, or a vitamin requiring education? Upstream of everything.
2. ACV compression at the small end (3-15 producer shops may see a $600/yr tracker not a $6-12K retainer).
3. Managed-service labor creep / template-vs-bespoke ratio (margin toward 50% = the manual model 01 penalizes).
4. Well-funded strong-tech incumbent (AgentSync/Vertafore Sircon) moving downmarket with a self-serve concierge tier.
5. Low-error-tolerance QC + carrier surge events (a single false "all clear" freezes an agency's book).

## DIMENSIONS HOLDING IT BACK
Market pull/customer truth (CMO 5), competitive landscape (air 6, AgentSync), operational QC/labor templatability (COO 5/6), jurisdictional surface (Legal 5).

## PATH TOWARD GO (60-75 day sprint)
1. 15-20 principal interviews — % burned/budgeted felt urgency (target ≥40%).
2. 15-20 price probes at three sizes — blended ACV ≥~$6K, ideally a $15-30K MGA tier.
3. Reposition wedge from concierge to a software-outcome "Appointment Risk Score / never-lapse"; bespoke filing a priced add-on.
4. Time-study 50 attestations across top 15 carriers + 3 onboardings — confirm ≥70% margin holds.
5. Secure one cluster-network/IIABA endorsement as a downmarket moat vs AgentSync.

**Single proof metric:** of 15-20 principals, % personally burned by a lost/suspended appointment AND would commit to a ≥$6K/year retainer — painkiller vs vitamin.
