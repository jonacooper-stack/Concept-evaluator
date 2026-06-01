CTO REVIEW — Fractional Data & Analytics Leader for Mid-Market Companies

ONE-PARAGRAPH TECHNICAL READ
This is fundamentally a services business wearing a thin technical jacket, not a technology business — there is no product to build, no IP, and no software asset that compounds. The "tech" is repeatedly re-integrating each client's heterogeneous, often legacy, on-prem-or-cloud systems (ERP, CRM, payroll, POS, spreadsheets) into a per-client warehouse + BI layer using off-the-shelf tooling (Fivetran/Airbyte + Snowflake/BigQuery + dbt + Power BI/Looker). That stack is boring, proven, and well within reach of a competent operator with prototype-grade coding skill, so feasibility is high — but the work does not get cheaper with each client because every account is a fresh, bespoke integration project against systems the founders may have never seen, and the real risk concentrates not in "can we build a dashboard" but in "can we securely hold, isolate, and not lose dozens of clients' most sensitive operational and payroll data with a two-person team and no security function." Treat this as a high-margin consulting practice with a recurring-revenue wrapper.

ARCHITECTURE SKETCH
- Per-client isolated stack (the safest pattern): ingestion via off-the-shelf connectors (Fivetran ~$0.5–2K/mo per client at mid-market volumes [ASSUMED], or Airbyte self-hosted to cut cost) pulling from ERP/CRM/payroll/POS.
- Cloud warehouse per client or per-client schema with strict tenant isolation (Snowflake or BigQuery) — single-tenant-per-account is the security-correct default; shared multi-tenant is cheaper but raises cross-client leakage risk.
- Transformation layer: dbt for modeling/metrics so "the numbers tie out" — where the actual recurring value is encoded.
- BI/serving layer: Power BI (cheapest, ubiquitous in mid-market) or Looker; embedded exec dashboards.
- Orchestration: managed connector schedules + light dbt Cloud or Dagster/Airflow if self-hosting.
- Auth/access: SSO where supported; otherwise per-client BI logins, MFA, least-privilege warehouse roles.
- The real complexity is NOT the stack — it is the long tail of source systems (NetSuite vs Sage vs Epicor vs an AS/400 green-screen ERP with no API; ADP/Paychex/Gusto payroll; Shopify vs a 15-year-old POS). The connector either exists or you are hand-rolling extraction, and that variance is unbounded per client.

BUILD PLAN TO REVENUE-EARNING MVP
There is no product MVP to build before revenue — revenue starts the day the first retainer signs. The "build" is per-client onboarding, which repeats forever. First client onboarding ~3–6 dev-weeks of one person's effort:
1. Source discovery + connector setup (1–2 dev-weeks): inventory systems, confirm off-the-shelf connectors, stand up ingestion. Highest variance — clean NetSuite + Salesforce + Gusto is days; on-prem legacy ERP with no API is weeks and may need a custom extract.
2. Warehouse + isolation + dbt modeling (1–2 dev-weeks): land data, build metric models so figures reconcile across systems. The value-creating chunk; cannot be punted.
3. Dashboard build (0.5–1 dev-week): exec KPIs in Power BI/Looker.
4. Security/access setup (0.5 dev-week): tenant isolation, encryption config, MFA, access roles, backups — must NOT be punted.
5. Cadence enablement (ongoing): the monthly review is labor, not build.
A reusable internal toolkit (standard dbt metric templates, a security/onboarding checklist, an IaC template for spinning up a clean isolated client stack) could be assembled in ~3–4 dev-weeks and would modestly compress chunks 2 and 4 over time — but never eliminates the per-client discovery variance, which is the dominant cost.

CRITICAL ASSUMPTIONS
- Most target-client source systems have reliable off-the-shelf connectors. If false, onboarding cost explodes and margins collapse on legacy accounts. Verify: a "source audit" before signing — list exact systems/versions and check Fivetran/Airbyte catalogs and API availability. This audit should be a paid or gating step.
- A two-person team can carry enough $5–12K/mo retainers to hit ~$2M founder income each within 24 months. Math: $2M+ founder income implies ~$4M+ revenue at services margins; at $8K/mo blended ($96K/yr) that is ~40+ concurrent retainers [ASSUMED]. Two founders cannot deliver 40 senior advisory relationships plus 40 living data stacks alone — REQUIRES heavy delegation to contract/offshore analysts well before 24 months, reintroducing the engineering-depth and security-supervision gap. Verify: model realistic per-founder load (likely 6–10 hands-on accounts each before quality degrades).
- "Numbers that tie out" is achievable per client at the proposed effort. Reconciling ERP vs CRM vs paysystem data is frequently a multi-week forensic exercise (duplicate keys, differing fiscal calendars, no canonical customer ID). If it routinely overruns, the setup fee won't cover it. Verify: one real reconciliation on a friendly first client before pricing the offer.
- Clients grant a small outside firm deep access to payroll, financials, and customer data. Many mid-market CFOs balk without security assurances the founders can't yet provide. Verify: ask 5 target buyers what security bar they require before granting warehouse access.
- Connector/warehouse costs stay a small fraction of the retainer. Fivetran pricing scales with data volume and can surprise; verify with a real volume estimate.

INFORMATION SECURITY POSTURE
This is the single most underweighted part of the concept and the area most likely to end the business. The firm will hold, for dozens of clients simultaneously, the crown-jewel datasets of each: full financials, customer-level revenue/margin, and PAYROLL (employee PII, compensation, very possibly SSNs and bank routing data depending on the payroll source). A target-rich aggregation under one small roof. Data lives in cloud warehouses (good — managed encryption at rest and in transit is table-stakes with Snowflake/BigQuery) plus inevitably in connector configs, BI tools, and the founders' laptops and ad-hoc analysis exports (the real leak vector). Required at launch, not later: single-tenant isolation per client (no shared schemas), unique least-privilege warehouse roles, MFA everywhere, a secrets manager (not credentials in spreadsheets or dbt repos), encrypted laptops, audit logging on warehouse access, a written DPA per client, defined backup and retention, and a basic incident-response plan with breach-notification obligations understood. At scale, enterprise-adjacent mid-market buyers and their auditors will ask for SOC 2 Type II; achieving it as a two-person shop with contractors touching client data is a real cost and operational drag ([ASSUMED] $30–80K plus 6–12 months to first Type II). The threat model that should keep them up at night: a contract/offshore analyst with broad access exfiltrating or mishandling one client's payroll data, triggering breach notifications across the portfolio and destroying the referral-based trust the whole GTM depends on. Cyber liability insurance and tight contractor access controls are mandatory.

SCORES (1–10)
1. Technical feasibility: 8 — Entirely boring, proven tooling (Fivetran/Airbyte + Snowflake/BigQuery + dbt + Power BI); no research problems, deliverable in 3–6 dev-weeks per client by a competent operator.
2. Build vs. buy posture: 9 — Essentially 100% off-the-shelf, near-zero custom code; the only "build" is dbt models and per-client config, exactly the right posture for a bootstrap.
3. Architecture cleanliness: 6 — The per-client stack is simple, but operating N independent heterogeneous client stacks multiplies moving parts and source-system variance is unbounded.
4. Time to revenue-earning MVP: 9 — No product to build; revenue begins at first retainer signature, with ~3–6 dev-weeks of onboarding, far under the 8-week bar.
5. Technical-assumption risk: 5 — Hinges on connectors existing for each client's legacy systems and on reconciliation being tractable at the priced effort; both vary wildly per account and are unverified.
6. Third-party dependency risk: 6 — Fivetran/Snowflake/Power BI are stable and replaceable in principle, but per-client volume-based pricing (Fivetran in particular) is a real margin-exposure and a connector gap on a legacy source can block an account.
7. Data architecture quality: 5 — Warehouse data is owned and portable, but the architecture is inherently sprawling (one bespoke stack per client) and leakage-prone via exports, BI access, and contractor accounts rather than centralized and clean.
8. Information security posture: 4 — Aggregating dozens of clients' financials and payroll PII under a two-person team with no security function and contractor access is a serious, under-addressed liability that will fail the first real CFO/auditor security review without dedicated controls (single-tenant isolation, secrets manager, MFA, SOC 2 path).
9. Scaling headroom: 4 — Scaling is linear in human labor and bespoke onboarding, not software; growth means more analysts touching more sensitive data, worsening the security and QC surface rather than amortizing it.
10. Maintenance burden: 5 — Each client stack is a permanent operational commitment (connectors break, source schemas change, dashboards drift) plus a standing monthly advisory cadence; load grows roughly linearly with account count.

AVERAGE SCORE: 6.1 / 10

TOP 3 TECHNICAL STRENGTHS
- Maximally boring, proven, off-the-shelf stack with effectively zero custom engineering — perfectly suited to founders whose engineering is prototype-grade (Fivetran/Airbyte + Snowflake/BigQuery + dbt + Power BI).
- No pre-revenue build: the first dollar arrives with the first retainer, and onboarding is ~3–6 dev-weeks, not quarters — excellent cash-to-effort profile.
- A reusable internal toolkit (dbt metric templates, IaC client-stack template, onboarding/security checklist) can be built in ~3–4 dev-weeks and modestly compounds delivery efficiency over time.

TOP 3 TECHNICAL RISKS
- Per-client integration heterogeneity means delivery cost never amortizes — each account is a fresh bespoke project against unpredictable source systems, including legacy ERPs with no API.
- Concentrated data-security liability: holding many clients' financials and payroll PII under a two-person team with contractor access and no SOC 2, where a single mishandling triggers cross-portfolio breach notifications.
- Scaling is purely linear in human labor; the path to ~$2M/founder requires ~40+ retainers, forcing reliance on offshore/contract analysts and degrading both quality control and the security surface.

BIGGEST SINGLE RISK
The business will eventually be holding the complete financials and payroll-level employee PII of dozens of mid-market clients inside a small, security-immature operation that grows by handing broad data access to contract and offshore analysts. That is a textbook high-value aggregation target with a weak control environment, and the entire go-to-market — referrals from CFOs, accountants, fractional-CFOs, and CEO peer groups — runs on trust. A single incident (a contractor exfiltrating or accidentally exposing one client's payroll file, a misconfigured shared schema leaking Client A's margins to Client B, or a laptop with cached exports getting lost) does not stay contained: it triggers breach-notification obligations across multiple clients, invites legal exposure, and vaporizes the referral engine the whole model depends on. The founders, per their own profile, have no information-security depth and a known detail-attention weakness, yet the security posture here must be designed in from day one — single-tenant isolation, secrets management, MFA, least-privilege roles, audit logging, DPAs, cyber insurance, and a credible SOC 2 path before they can serve security-conscious mid-market CFOs at all.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is your per-client source-system audit process, and what happens when a target client runs a legacy ERP with no off-the-shelf connector — decline, hand-roll extraction, or eat the margin? Show the realistic onboarding-cost distribution across 5 representative clients, not the happy path.
- What is the concrete security architecture on day one — single-tenant vs shared, where secrets live, MFA, audit logging, backup/retention, DPA template, cyber insurance — and your timeline/budget to SOC 2 Type II ([ASSUMED] $30–80K, 6–12 months) when a CFO's auditor demands it?
- Do the math on portfolio scale: how many hands-on accounts can each founder personally own before quality drops, how many contract/offshore analysts does ~40+ retainers require, and how do you supervise those analysts' access to payroll PII without a security function?
- When you add offshore/contract analysts, what access controls, exfiltration prevention, and contractual/insurance protections govern their handling of client financials and PII?
- What are the real monthly Fivetran/Snowflake/BI costs per client at mid-market data volumes, and what gross margin survives after tooling on a $5K/mo (low end) retainer?

RECOMMENDATION: REFINE
