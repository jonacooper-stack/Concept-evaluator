# Concept 12 — TrialKeeper (clinical-research-site qualification network) — Council Reviews

## CFO (avg 7.6, GO conditional)
Startup 9, Working-cap 9, Cash-flow 8, Unit econ 7, Margin 8, Path 7, **Market 6**, **Concentration 6**, Scaling 8, Financeability 8.
Pristine cash mechanics; ~55-90 sites ($18K) for ladder. Biggest risk: ARPU compression — buyer already has a regulatory coordinator → prices vs "coordinator hours saved" (low WTP $9-12K) not "studies won" (high WTP); finite/consolidating market (SMO roll-ups).

## CMO (avg 5.8, REFINE) ← KILLER
Positioning 7, **Differentiation 5**, Wedge 7, GTM fit 7, **Distribution 6**, **CAC 6**, **Brand 6**, **Competitive air 5**, **Defensibility 4**, **Customer truth 5**.
Wedge ok (SCRS Global Site Solutions Summit, ACRP, DIA; ~3,000-6,000 US sites). Biggest risk: TWO-SIDED COLD-START WITH VALUE ON THE WRONG SIDE — the "qualify once reuse" moat needs sponsors/CROs to ratify, but they re-verify per study because their OWN GCP/ICH-E6 audit duty requires it (a third party attesting doesn't discharge sponsor duty). Named encroachers: **Veeva SiteVault ($2B+, free-to-sites, sponsor-connected — directly building the connectivity layer this calls its moat)**, Florence eHub, RealTime-CTMS, Advarra Clinical Conductor. Collides with hard-constraint #5 (strong-tech incumbent).

## COO (avg 7.5, GO w/ gating experiment)
Delivery clarity 7, Supply chain 9, Logistics 10, **Customer-ops 6**, Vendor dependency 8, Hiring 7, Throughput 7, **QC 6**, Geo 9, **Tooling 6**.
No field ops; ~5.5 people serve ~85 sites IF auto-map holds. Biggest risk: the 75/25 light/heavy auto-map split is THE load-bearing assumption — if questionnaires are mostly bespoke (40% not 75%), the lone practitioner bottleneck caps the business at 40-50 sites.

## Legal (avg 7.3, GO) ← clean-ish
Industry burden 7, **Licensing 9**, Data privacy 7, Employment 8, Consumer protection 8, IP 7, **Contract 6**, **Liability 6**, Jurisdictional 8, Trajectory 7.
Surgically scoped OUTSIDE the regulated perimeter (NO PHI, NO trial conduct/monitoring; site remains 21 CFR Parts 50/54/56/312 + ICH-GCP responsible party, signs own 1572). Neither HIPAA covered-entity nor business-associate. Risks: stale/wrong reused record → negligence/breach E&O (insurable/cappable), scope-leakage (PHI creep flips HIPAA on), sponsor-questionnaire confidentiality.

## CTO (avg 7.4, GO w/ gating experiment)
Feasibility 8, Build vs buy 8, Architecture 8, Time-to-MVP 8, **Assumption risk 5**, Third-party dependency 7, Data architecture 8, Infosec 7, Scaling 8, Maintenance 7.
Boring CRUD + cron expiry + templated export ~8-12 dev-weeks; no-PHI shrinks threat model. Biggest risk: integration+overlap — if questionnaires funnel through sponsor portals (Veeva Vault, no site-side write API) + questions are idiosyncratic, degrades to "organized filing cabinet" + human re-typing.
