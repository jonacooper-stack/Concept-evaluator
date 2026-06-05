COO REVIEW — Multi-State Compliance Dashboard

ONE-PARAGRAPH OPERATIONS READ
A software-first, data-heavy SaaS with a thin but real operational tail, and that distinction is the whole ballgame. The pure dashboard is genuinely operable by two founders plus a lean team because the work is build-once, run-many: a rules engine plus trigger-detecting integrations. Where it gets heavy and starts to look like a field-ops business in disguise is the "ability to file or hand off filing" and done-for-you add-on — per-filing manual labor across 50+ jurisdictions, each with its own forms, portals, cadences, and liability if wrong. The SaaS layer is lean and tractable; the moment done-for-you filing becomes meaningful, this becomes a managed-service ops business whose unit of work is a human completing a government form correctly, on time, with liability.

THE TUESDAY-IN-MARCH WALKTHROUGH
March is peak: Delaware franchise tax due March 1, Q1 annual-report cluster, monthly/quarterly sales-tax. At month 12 assume ~120 customers [ASSUMED 100-150], ~35 on done-for-you [ASSUMED ~30% attach]. Founder A owns product/data + sales; Founder B owns customer ops + filing.
Morning (A): a Gusto/Rippling webhook fires — new employee in Colorado → CO withholding + SUI registration obligation; alert goes out. Friction: the rules engine must be RIGHT. If CO changed its threshold/form in January and it wasn't caught, the alert is wrong on a penalty-bearing item. A spends the morning on a rules-maintenance queue. Hidden recurring labor: 50 states × dozens of obligation types.
Midday (B): batch of done-for-you Delaware franchise + annual reports due in days. For each of 35 customers, log into portal, complete filing, confirm payment, submit, record proof. Delaware franchise via default "authorized shares" can be a six-figure surprise unless recomputed via "assumed par value capital" — B is doing a calculation that, if wrong, costs the customer real money. ~25-40 min/filing; if 35 customers × ~4 obligations cluster in March, ~140 filings in a 3-4 week window on one founder + maybe a contractor.
Afternoon: ticket — a customer crossed the $100K PA nexus threshold three months ago, missed because Stripe wasn't connected (only manual revenue). Angry: "I pay you to see this." B does a churn-save and eats the hit. Core fragility: value is correctness; correctness depends on complete connected data the customer may not provide.
Where it breaks: (1) rules-engine staleness; (2) the March filing crunch; (3) data-completeness gaps producing a confident wrong "green."

CAPACITY MATH
SaaS dashboard (scalable): ~$800K ARR by mo 12 [ASSUMED $200K cost base]; at ~$5K ACV ≈ 160 customers; mo 24 ~$1.3-1.5M ARR at ~$7K ≈ 200 customers. Onboarding/support of 160-200 SaaS accounts is a two-founder + one CS-contractor job. Marginal delivery labor near zero.
The constraint is the rules engine: ~50 states × ~6 obligation categories ≈ 300 rule-sets. Reviewed ~2×/yr at 30 min = 300 hrs/yr ≈ 6 hrs/week of specialized research — a part-time paralegal ($30-50/hr, ~$10-15K/yr). Manageable with discipline. This is the real "supply chain."
Done-for-you filing (un-scalable): a heavy multi-state customer has ~30+ obligations/yr (incl. ~120 sales-tax filings) ≈ 50+ hrs/yr filing labor. A part-time filer (~1,250 productive hrs/yr) handles ~25 such customers → ~1 filing FTE per ~25 customers. At 100 done-for-you customers, ~4 filing staff. Hireable (remote AP clerks ~$45-60K) but converts 85% SaaS margin to 40-55% service and concentrates liability. Strategic call: cap done-for-you as a premium add-on OR route to registered-agent/filing partners (CSC, CT, Harbor, Middesk) for a margin.

SCORES (1–10)
1. Delivery clarity & repeatability: 8 — Build-once-deliver-many; ~300 codified rule-sets is a finite documentable spine; onboarding is a connect-your-systems flow.
2. Supply chain resilience: 6 — Real "supply" is regulatory content + data integrations; buildable in-house but perpetual maintenance load.
3. Logistics tractability: 9 — Zero physical logistics, no trucks/installs, fully remote; only "delivery" is bytes and optionally a human submitting a form.
4. Customer-ops scalability: 6 — Pure SaaS scales at 160-200 accounts, but correctness-on-penalty-bearing-items drives anxious tickets; done-for-you is high-touch and headcount-linear.
5. Vendor/partner dependency risk: 6 — Dependent on payroll/billing/accounting APIs + optional filing partners; each replaceable but a degrade hits the whole product.
6. Hiring feasibility: 7 — First hires (research contractor ~$10-15K; remote filing clerks ~$45-60K) from a broad pool; no scarce credential gates the core.
7. Throughput capacity at target: 8 — ~160-200 accounts within two founders + 1-2 contractors PROVIDED done-for-you is capped/partner-routed so the March crunch doesn't swamp a founder.
8. Quality control simplicity: 4 — Weak point: asserting compliance where wrong = client penalties; a stale rule or unconnected source yields a confident false green; failure mode is reputation/liability, not refund.
9. Geographic / seasonality risk: 6 — National year-round, but Q1/March peak + monthly sales-tax create a real workload spike the filing service must staff for.
10. Tooling maturity available: 7 — Operating stack off-the-shelf; core IP (rules engine, trigger detection) is custom but exactly what these founders build.

AVERAGE SCORE: 6.7 / 10

TOP 3 STRENGTHS
- Zero physical logistics, near-zero marginal delivery cost on SaaS; ~160-200 accounts hits the ladder inside two founders' reach.
- Finite codify-once core (~300 rule-sets) that gets cheaper per customer with scale.
- Recurring by construction; strong structural retention.

TOP 3 RISKS
- QC on penalty-bearing data: a stale rule or unconnected revenue source yields a confident false "green" and the customer eats a penalty.
- Done-for-you filing is a headcount-linear managed service in SaaS clothing (~1 filer per ~25 customers; ~140 filings in March).
- Regulatory-content maintenance treadmill across 50 jurisdictions, with silent failure.

BIGGEST SINGLE RISK
Correctness liability colliding with the regulatory-maintenance treadmill. The product's value is asserting "you are compliant," but maintaining true correctness across ~300 living rule-sets while depending on customer-supplied data completeness is a perpetual, unforgiving, silent-failure operation. A wrong green means a real penalty, lost good standing, or surprise back taxes — a reputation-and-litigation event, not a churn event. Two people can build/run the dashboard; what's unclear is whether two people can indefinitely guarantee fifty states' worth of constantly-changing rules at a bar where being wrong is catastrophic. Smart posture: position as "visibility and reminders, verify with your accountant," lean on authoritative data partners, and resist letting done-for-you turn the company into a liability-bearing filing factory.

QUESTIONS THE FOUNDERS MUST ANSWER
- Source-of-truth and update cadence for the rules engine — in-house, licensed, or hybrid — and the SLA on catching a mid-year change before a wrong status?
- Is done-for-you in-house, partner-routed, or capped premium? Show headcount/margin at 50 and 100 filing customers.
- How do you handle data completeness — what stops an unconnected-Stripe customer getting a confident wrong "green," and how is that disclaimed?
- March-peak staffing plan — how many filings in the 3-4 week window at target, and who clears them?
- Do you carry it as "informational visibility" or "compliance guarantee," and does pricing/positioning/insurance match?

RECOMMENDATION: REFINE — (1) resolve rules-content/correctness structurally (license authoritative data + change-monitoring SLA; position as visibility not guarantee); (2) cap or partner-route done-for-you. Make those moves and it's a GO-shaped lean recurring software business; leave them unresolved and the QC (4) and filing throughput trap turn it into an anxious managed-service grind.
