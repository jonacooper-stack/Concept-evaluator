COO REVIEW — AccessGuard

ONE-PARAGRAPH OPERATIONS READ
This is a software-leveraged recurring managed service with a genuinely attractive operational shape: remote-first, no trucks, no field installs, no inventory, year-round demand, and a delivery spine (crawl + audit + remediate + document) that is mostly digital. The hard operational truth, though, is that the "remediation" leg is skilled human accessibility-engineering labor — manual audits of checkout/booking flows and code-level fixes against WCAG 2.2 AA — and that is the part that does not scale linearly with software. Two founders can absolutely run the monitoring/reporting/sales engine themselves, but the moment volume rises the bottleneck lands squarely on credentialed accessibility-remediation hands, and that labor pool is thin and not cheap. The business is operable by two founders plus a small specialist team, but its margins and throughput live or die on how much of remediation can be templatized versus done bespoke per client.

THE TUESDAY-IN-MARCH WALKTHROUGH
Picture month 12, roughly 35 clients at a blended ~$2,500/mo ($30K/yr → ~$1.05M ARR). It is a Tuesday in March. Founder A starts in the sales/intake seat: two new inbound leads came overnight from the "ADA website lawsuit" SEO page and the scraped-filings outbound, one an "active litigation" hot lead — a Florida e-commerce company served Friday whose defense attorney told them to "get documentation in place yesterday." That account needs same-week onboarding: a baseline crawl, a manual audit of checkout, and a dated remediation-plan artifact the lawyer can wave at opposing counsel. Founder A scopes and closes it on a 60-minute call; the onboarding clock is now running and it is the day's emergency.

Meanwhile the crawler ran overnight across all 35 client sites. It flags ~9 sites with new violations — a WordPress client pushed a marketing landing page with unlabeled form fields, a Shopify client installed a third-party reviews widget that broke keyboard navigation, two clients had theme updates that regressed color contrast. These are the "drift" events that justify the recurring fee. The accessibility engineer (first hire) triages: the form-field and contrast issues are templatized fixes pushed as PRs or implemented directly on the CMS in ~30-60 min each; the third-party widget is the ugly one — not the client's code, so the fix is config, a documented exception, or a back-and-forth with the client's dev team. That one eats two hours and an email thread.

Founder B splits the day between (a) the new-litigation client's rapid-response evidence package — crawl history, VPAT-style attestation, dated audit trail — the premium deliverable, and (b) a quarterly manual expert audit for a hotel-booking client (checkout + reservation flow tested with screen reader and keyboard, ~4-6 hours of skilled work). Support tickets trickle in: "are we covered now?" (15 min), another forwards a fresh demand letter (rapid-response playbook, escalated). Where it breaks: if two active-litigation clients land in the same week, the manual-audit + evidence-package labor collides with the founders' sales and the engineer's drift queue, and something slips — which here is not cosmetic, because a late or sloppy attestation is the exact artifact a client relies on in a lawsuit.

CAPACITY MATH
Target: ~$300K/founder by month 12 = ~$600K combined. At [ASSUMED] ~50-60% owner margin with one or two specialist hires, that implies ~$1.0M-$1.2M ARR → at $30K ARPU, ~35-40 clients. The $500K/founder by month 24 rung implies ~$3M+ ARR → ~100 clients.

Per-client monthly delivery load [ASSUMED, verifiable by 10 pilot accounts]:
- Automated crawl + triage: human triage ~1-2 hrs/client/month.
- Drift remediation: ~2-4 hrs/client/month averaged.
- Periodic manual expert audit (quarterly, ~4-6 hrs) → amortized ~1.5-2 hrs/client/month.
- Documentation/attestation upkeep: ~0.5-1 hr/client/month.
- Support/reassurance: ~0.5 hr/client/month.
Blended ~5-9 skilled hours/client/month; midpoint ~7.

At 35 clients × 7 hrs = ~245 hrs/month. A productive accessibility engineer delivers ~120-140 delivery hours/month. So 35 clients needs ~2 FTEs of delivery capacity → ~1 specialist hire plus ~1 founder-equivalent of delivery time by month 12. Tight but doable.
At 100 clients: ~700 hrs/month → ~5-6 delivery FTEs, plus spiky active-litigation rapid-response on top. That is a real services org. The bottleneck is unambiguously credentialed accessibility-remediation labor; the key lever is whether tooling pulls ~7 hrs/client toward ~3-4.

Cloud/crawler supply chain: trivial — commodity cloud + headless browser farm, cost a rounding error against $30K/yr ARPU.

SCORES (1–10)
1. Delivery clarity & repeatability: 6 — Monitoring/reporting/attestation are highly standardizable, but manual audits and code-level remediation across Shopify, WooCommerce, custom stacks, and third-party widgets are partly bespoke; "productized" claims capped until the remediation playbook is shown templatized.
2. Supply chain resilience: 9 — Inputs are commodity cloud + headless-browser crawling, multiple substitutable providers, zero MOQs/deposits/FX, per-client infra cost in the low single-dollar range against $2,500/mo revenue.
3. Logistics tractability: 10 — Fully remote, zero physical goods, zero on-site work, no routing/scheduling/travel; delivery is code PRs and PDFs over the internet.
4. Customer-ops scalability: 5 — The recurring fee is justified by ongoing human triage + drift remediation + periodic manual audits at ~5-9 hrs/client/month [ASSUMED], mid-touch and growing roughly linearly with client count, not self-serve.
5. Vendor/partner dependency risk: 7 — Crawler infra is replaceable, but operational reliance on third-party CMS/widget ecosystems means fixes sometimes sit outside the team's direct reach; defense-attorney referral is a partner to cultivate, not a single point of failure.
6. Hiring feasibility: 5 — The core hire is a WCAG-literate accessibility engineer; the pool is real but thin and competitively priced [ASSUMED ~$90K-$140K loaded] with high quality variance — this labor market gates growth.
7. Throughput capacity at target: 6 — Two founders + ~1 specialist clear the ~35-40-client / month-12 rung (shown above), but the month-24 rung (~100 clients, ~700 hrs/month, ~5-6 engineers) is a genuine services-org build.
8. Quality control simplicity: 4 — Output variance is high and stakes are unforgiving: the deliverable is legal-grade evidence used in litigation, so a missed violation or sloppy attestation is a potential liability/reputation event; consistency across engineers and changing sites is hard.
9. Geographic / seasonality risk: 9 — Demand is national, year-round, weather-neutral, arguably counter-cyclical; no peak/trough or regional install-density problem.
10. Tooling maturity available: 6 — Crawl/scan engines (axe-core), ticketing, CRM, billing are off-the-shelf, but the differentiated attestation/audit-trail/VPAT workflow + prioritized-remediation pipeline must be built.

AVERAGE SCORE: 6.7 / 10

TOP 3 OPERATIONAL STRENGTHS
- Pristine logistics and supply chain: fully remote, no field ops, no inventory, commodity cloud at trivial per-client cost — exactly the non-field-ops shape the founders want.
- National, year-round, non-seasonal demand with no geographic constraint; the "just sued" trigger is enumerable via public court filings, making top-of-funnel scrapeable.
- A large slice of the work (monitoring, drift detection, attestation generation) is genuinely software-automatable — the founders' build edge keeps part of delivery off human hands.

TOP 3 OPERATIONAL RISKS
- Remediation labor is the hard ceiling: skilled WCAG-literate engineers are a thin, competitively-priced pool, and headcount scales roughly linearly (~7 hrs/client/month) unless templatization brings it down.
- Quality control on a legal-grade deliverable: variance across engineers and constantly-changing sites is high, and a missed violation lands in a courtroom, not a bug tracker.
- Third-party/widget dependency on code the team doesn't own creates remediation work that can't always be closed cleanly, forcing documented exceptions and client-dev coordination that slows the clock.

BIGGEST SINGLE RISK
The single operational issue most likely to break this is the remediation-labor bottleneck colliding with the non-deferrable, spiky active-litigation rapid-response load. The recurring monitoring fee is software-leverageable, but the thing customers pay a premium for — the dated, defensible evidence package and the manual expert audit of their real checkout/booking flows — is skilled human work that cannot be deferred when a demand letter arrives, because the client is under a legal clock. If two or three "active litigation" onboardings land in the same week (plausible, since the founders target just-sued companies as the entry segment), the manual-audit and attestation labor spikes precisely when the founders are also selling and the lone engineer is buried in the drift queue. At ~7 hrs/client/month and a thin hiring pool, the team cannot simply surge; the realistic failure mode is a late or under-tested attestation handed to a client mid-lawsuit — the worst possible quality miss in this category. Whether two people can actually do this hinges entirely on how much of remediation can be templatized down from ~7 to ~3-4 hrs/client — unproven until they run real accounts.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the real measured hours-per-client-per-month after running 10 live pilot accounts for 90 days? (Instrument time tracking; this number sets your entire headcount-to-ARR curve.)
- How much of remediation is genuinely templatizable versus bespoke — can you drive ~7 hrs toward ~3-4? (Catalog the violation distribution across the first 20 audits, tag each "template" vs "bespoke.")
- Where do you source and how do you retain WCAG-literate engineers, at what loaded cost, and what is your QC process to prevent a missed violation in a legal-grade deliverable? (Post one req, measure applicant quality; draft a two-reviewer QC checklist before client #1.)
- When the violation is in third-party code the client doesn't control, what is the standard play — config, documented exception, or client-dev escalation — and does your attestation hold up with documented exceptions? (Verify with a defense-side ADA attorney advisor.)

RECOMMENDATION: REFINE
The operational chassis is excellent — remote, non-field, year-round, supply-chain-trivial, with a software-automatable monitoring layer that fits the founders' build edge. What keeps this from a clean GO is that the premium-justifying work (manual audits + legal-grade attestation + rapid response) is skilled human labor that scales near-linearly and carries high-stakes quality variance, with a thin hiring pool as the growth ceiling. I need to see: (1) a measured hours-per-client figure from a real pilot; (2) a templatized remediation playbook that demonstrably pulls per-client hours down; (3) a two-reviewer QC process and a standard play for third-party code; and (4) a surge plan for simultaneous active-litigation onboardings. Nail those four and this moves to GO — the month-12 rung is operationally reachable with two founders plus one strong specialist; the month-24 rung is a real but buildable services org.
