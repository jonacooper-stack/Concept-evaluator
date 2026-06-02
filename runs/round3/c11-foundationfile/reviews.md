# Concept 11 — FoundationFile (foundation grant-compliance network) — Council Reviews

## CFO (avg 7.1, REFINE)
Startup 9, Working-cap 9, Cash-flow 8, **Unit econ 6**, Margin 7, **Path 6**, Market 7, **Concentration 6**, **Scaling 6**, Financeability 7.
Annual-prepay, <$30K to launch (IRS BMF + OFAC public/free). ~160 customers ($9K) mo12 / ~270 mo24 (<1.5% of ~20-40K in-band foundations). Biggest risk: the compounding "shared diligence network" may not convert to real cost savings — if each foundation must legally own/document its OWN ER determination, the network sells TIME not cost-elimination → ARPU compresses, ordinary SaaS not a network.

## CMO (avg 6.7, REFINE)
Positioning 8, **Differentiation 6**, Wedge 7, GTM fit 8, Distribution 7, CAC 7, Brand 7, **Competitive air 6**, **Defensibility 5**, **Customer truth 6**.
Wedge real (Exponent Philanthropy ~2,000 lean foundations, ~30 regional grantmaker assns, 990-PF outbound). Named competitors: Foundant (owns workflow in this segment), Fluxx, Blackbaud, Submittable, **NGOsource (ALREADY runs "vet once reuse" for equivalency — the hardest piece — under TechSoup/Candid)**, Candid/GuideStar Charity Check (thin-wrapper risk). Biggest risk: differentiation sold on a network that doesn't exist at launch (2-sided cold-start) and whose hardest layer is already NGOsource's; real defensible asset is audit-of-record switching cost, not the network.

## COO (avg 7.6, GO)
Delivery clarity 8, Supply chain 8, Logistics 10, Customer-ops 7, Vendor dependency 8, Hiring 7, Throughput 7, QC 7, Geo 8, **Tooling 6**.
No field ops; ~70% automatable (BMF/OFAC); thin judgment band (ER/equivalency ~20%) via fractional practitioner. ~50 foundations mo12 = 2 founders + 1 analyst + 1 fractional practitioner. Biggest risk: practitioner-throughput dependency + unproven reuse rate (if foundations won't reuse others' diligence, judgment load doubles → boutique not scalable).

## Legal (avg 7.6, GO) ← FIRST CLEAN-LIABILITY RESULT
Industry burden 7, **Licensing 9**, **Data privacy 9**, Employment 8, **Consumer protection 9**, IP 7, **Contract 6**, **Liability 6**, Jurisdictional 8, Trajectory 7.
PRIMARY statutory liability stays with the CUSTOMER (IRC 4945 excise tax on foundation/managers; OFAC strict-liability on disbursing foundation; foundation signs own 990-PF). No occupational license. Equivalency has explicit safe harbor (good-faith reliance on "qualified tax practitioner" per Treas Reg 53.4945-5 — NGOsource's lane). Data deliberately low-sensitivity (no beneficiary PII). Residual: aggregated E&O if a SHARED record is wrong (multi-client blast radius) + UPL boundary on ER drafting (engineerable via practitioner-in-loop + Circular 230). REC GO.

## CTO (avg 7.7, GO)
Feasibility 9, Build vs buy 8, Architecture 8, Time-to-MVP 8, **Assumption risk 6**, Third-party dependency 7, Data architecture 8, Infosec 7, Scaling 9, Maintenance 7.
Public/free/non-revocable data (IRS BMF/Pub 78, OFAC); EIN = clean deterministic join key → ~8-12 dev-weeks. Biggest risk: OFAC fuzzy-match false negatives (no EIN join) + silent data staleness = correctness/liability failure; keep Candid off critical path.
