# Concept 10 — SupplyAttest (aerospace AS9100 supplier-qualification) — Council Reviews

## CFO (avg 7.5, GO w/ refinement)
Startup 8, Working-cap 8, Cash-flow 8, Unit econ 7, Margin 7, Path 7, Market 7, Concentration 7, Scaling 8, Financeability 8.
~30–45 customers ($20–30K) mo12, ~60–70 mo24; ~2% of ~3,000 in-scope AS9100 Tier-2/3 (IAQG OASIS). Biggest risk: the "qualify once" network is a DEMAND-side assumption about prime behavior founders don't control; without prime acceptance it's a single-sided "keep your binder tidy" service (still clears ladder on subscription, but no compounding/overage/exit premium).

## CMO (avg 6.6, REFINE)
Positioning 7, **Differentiation 6**, Wedge 8, GTM fit 8, Distribution 7, **CAC 6**, Brand 7, **Competitive air 6**, **Defensibility 5**, **Customer truth 6**.
Wedge strong (IAQG OASIS public list of certified sites). Named competitors: OASIS (free cert-status rail), Net-Inspect (FAI, buyer-mandated), Exostar (supplier connectivity across Boeing/RTX/Lockheed — structurally positioned to BE the network), ETQ/MasterControl (enterprise QMS), Apriso. Biggest risk: the magnetic "qualify once" promise is the part founders CANNOT deliver — buyer side is Boeing/RTX/Lockheed who run their own mandated rails and have no incentive to outsource supply-chain trust. Cold-start where the value-conferring side is the one the startup has zero leverage over.

## COO (avg 6.7, REFINE)
Delivery clarity 7, Supply chain 8, Logistics 9, **Customer-ops 6**, Vendor dependency 8, **Hiring 4**, Throughput 6, **QC 5**, Geo 8, **Tooling 6**.
No field ops; ~63 hrs/account/yr. Biggest risk: throughput gated by SCARs+FAI sign-off (~1,200 expert-hrs/yr at 40 accounts) requiring a scarce credentialed aerospace SQE (thin labor pool); asymmetric failure (bad FAI/missed SCAR = frozen POs/ASL removal).

## Legal (avg 5.3, REFINE)
**Industry burden 3**, Licensing 6, **Data privacy 5**, **Employment 5**, Consumer protection 8, IP 7, **Contract 4**, **Liability 4**, Jurisdictional 7, **Trajectory 4**.
Attestation architecture is sound (supplier signs/certifies → FCA stays with supplier). BUT biggest risk: ITAR/EAR (22 CFR 120–130; 15 CFR 730–774) — FAI packages contain export-controlled defense drawings; custodying = deemed-export trap (one non-US-person view = violation), strict-liability, UNINSURABLE fines, personal criminal exposure (22 USC 2778), forces DDTC registration + GovCloud + US-person-only + provider's OWN CMMC/800-171. Refine: architect so provider never custodies plaintext controlled data (22 CFR 120.54 encryption carve-out).

## CTO (avg 7.0, GO w/ scope discipline)
Feasibility 8, Build vs buy 7, Architecture 7, Time-to-MVP 7, **Assumption risk 5**, Third-party dependency 7, Data architecture 7, Infosec 8, Scaling 8, **Maintenance 6**.
Boring core ~14–20 dev-weeks; security posture (GovCloud + US-person enclave + 800-171) IS the moat but adds overhead. Risks: integration creep (ETQ/Net-Inspect/Exostar/Epicor sync demands), export-control mishandling (no controlled data through public LLMs), portability-assumption failure (primes mandate own portals).
