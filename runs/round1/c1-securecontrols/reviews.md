# Concept 1 — SecureControls Defense Tier-2 — Council Reviews

## CFO REVIEW (avg 7.8)
Scores: Startup capital 9, Working-capital 9, Cash-flow self-funding 8, Unit economics 8, Gross margin 7, Path to ladder 7, Obtainable market 8, Risk concentration 8, Scaling economics 6, Financeability 8. AVG 7.8. REC: GO.
Biggest risk: sold/priced as software but delivered as labor; judgment-heavy onboarding (110-control assessment realistically $8–15K loaded labor) is a margin drag and throughput bottleneck; past ~60–70 accounts each marginal account needs a hire before its revenue, flattening the founder-income curve at the $500K rung. GO conditioned on proving onboarding covers its own loaded cost, renewal-year hours fall, and attestation liability is insured/contractually placed on the supplier.

## CMO REVIEW (avg 7.6)
Scores: Positioning 9, Differentiation 7, Wedge 8, GTM fit 9, Distribution 8, CAC realism 7, Brand/story 8, Competitive air 7, Defensibility 6, Customer truth 7. AVG 7.6. REC: GO.
Named competitors: Exostar, Summit 7, PreVeil, Vanta/Drata (adding 800-171/CMMC), long tail of CMMC RPOs/C3PAOs. Air is in the SMB-managed seam (fixed-price, human prime-facing reassurance). Biggest risk: positioning collision with "CMMC" keyword + down-market push of well-funded automation SaaS (Vanta/Drata); differentiation is service/positioning, not tech — copyable. Must lock prime-referral + MEP channel before SaaS players move down-market.

## COO REVIEW (avg 7.5)
Scores: Delivery clarity 8, Supply chain 9, Logistics 9, Customer-ops scalability 7, Vendor dependency 8, Hiring 7, Throughput 8, QC simplicity 6, Geo/seasonality 7, Tooling maturity 6. AVG 7.5. REC: GO.
Capacity: ~32 human-hrs/subscriber/yr steady state; ~78 subscribers at month-24 (~$1.4M ARR) ≈ 3,700 delivery-hrs ≈ 2.5 FTE → founders + 2–3 analysts + fractional advisor. Bottleneck = onboarding throughput + judgment depth (rests on one fractional advisor). Biggest risk: asymmetric failure severity (FCA / failed prime audit) vs thin judgment bench; needs hard QC gate (advisor sign-off on every SPRS score) + bus-factor plan.

## LEGAL REVIEW (avg 7.3)
Scores: Industry burden 6, Licensing 9, Data privacy 5, Employment 8, Consumer protection 9, IP cleanliness 8, Contract simplicity 6, Liability exposure 5, Jurisdictional 9, Trajectory 8. AVG 7.3. REC: GO.
No licensing gate; federally uniform; clean B2B (no ROSCA/CCPA thicket); regulatory tailwind (CMMC final rule eff. 2024-12-16). Biggest risk: False Claims Act spillover (31 USC §3729; DOJ Civil Cyber-Fraud Initiative — Aerojet $9M 2022, Verizon $4.09M 2023) — firm becomes witness/contribution target in a customer FCA matter. Portal holds CUI (32 CFR 2002) + latent ITAR "deemed export" risk → data-privacy 5, liability 5. Mitigable via MSA (customer owns attestation), E&O, CUI-aware architecture.

## CTO REVIEW (avg 7.9)
Scores: Feasibility 9, Build vs buy 8, Architecture 8, Time-to-MVP 9, Assumption risk 7, Third-party dependency 8, Data architecture 7, Infosec 7, Scaling headroom 9, Maintenance 7. AVG 7.9. REC: GO.
Boring CRUD portal + scheduler + vault, ~8–12 dev-weeks; revenue starts on document-delivered onboarding before portal done. Biggest risk: CUI boundary × breach blast-radius — if customers upload real CUI, provider inherits 800-171/CMMC + GovCloud/GCC-High hosting (multi-quarter, capital-heavy); platform concentrates many suppliers' POA&M weakness maps = extinction-level breach target. Mitigation: scope portal as artifact/attestation system-of-record, ban raw CUI by ToS/design, harden launch controls, SOC 2 Type II early.
