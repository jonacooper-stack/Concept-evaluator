# Concept Evaluation — Final Report
**Run date:** 2026-06-09 · **Branch:** claude/stoic-thompson-48nvvx

## 1. What was asked, and the bar
Run the council evaluator until at least **two** concepts each score, on honest
red-teamed numbers:
- **Objectives weighted total (doc-01) > 75 / 100**, AND
- **every one of the five expert averages ≥ 7.5 / 10.**

Additional operator constraints honored this run:
- **Reference the prior corpus** so no concept is re-evaluated. A ledger of ~45
  concepts across 10 prior `claude/*` branches was built first
  (`00-prior-concept-ledger.md`); all 14 new candidates were checked clear of it.
- **Cap of 5 total council passes** (cost control).
- **Surface the top concepts even if none clear the bar.**

## 2. Headline outcome
**5 council passes run. ZERO concepts cleared the bar.** Every concept was scored on
absolute merit, the mean computed only after all sub-scores were fixed, and the
mandatory PM red-team only ever LOWERED scores. Per CLAUDE.md, *"a run that explores
the field, produces full rigorous packets, and finds ZERO qualifiers is a SUCCESS; a
run that manufactures qualifiers at 8.1 is a FAILURE."* This is the former.

The result also matches the prior corpus: across ~45 earlier concepts in 10 branches,
**none ever cleared even the (stricter) native bar** — honest means clustered 6.3–7.4.
This run's five honest means clustered 6.58–7.14. The field is consistent.

## 3. Top 10 concepts evaluated this run (ranked)
Council-validated concepts first (red-teamed), then the strongest triage-only
candidates. Headline rank is by Objectives total; mean and lowest-expert-avg shown
so distribution quality is visible (e.g., FranAudit's obj is high but its Legal 4.8
is a fatal-class flaw).

| Rank | Concept | Obj /100 | Mean /10 | Lowest expert | Stage | Verdict |
|---|---|---|---|---|---|---|
| 1 | **ChemSDS** | 75.0 | 7.10 | Legal 6.5 | Full council | FAIL (near-miss; liability tail) |
| 2 | **AccessGuard** | 72.0 | 7.14 | COO 6.7 | Full council | FAIL (near-miss; labor-scaling) |
| 3 | **FranAudit** | 71.5 | 6.60 | Legal 4.8 | Full council | FAIL (UPL fatal-class flaw) |
| 4 | **GovRenew** | 70.5 | 7.02 | Legal 6.0 | Full council | FAIL (FCA/UPL + free-DIY WTP) |
| 5 | **ProxyDocket** | 69.5 | 6.58 | CTO 6.1 | Full council | FAIL (latent demand; ingestion) |
| 6 | TariffLedger | ~74* | — | — | Triage only | not councilled (pass cap) |
| 7 | EmissionsLedger | ~72* | — | — | Triage only | not councilled (pass cap) |
| 8 | FundFiler | ~71* | — | — | Triage only | not councilled (pass cap) |
| 9 | RenewRail | ~70* | — | — | Triage only | not councilled (pass cap) |
| 10 | AdReg | ~68* | — | — | Triage only | not councilled (pass cap) |

\* Triage gut-check estimate only, NOT council-validated. This run's triage→council
gap averaged ~8 points of optimism (e.g., AccessGuard triaged 82, councilled 72), so
the true council numbers for #6–#10 would very likely land in the high-60s/low-70s.

**Best two by overall strength** (objectives + healthiest score distribution, setting
aside FranAudit's fatal Legal flaw): **ChemSDS** and **AccessGuard**. Both are honest
near-misses with the clearest path to a future GO via cheap validation, NOT structural
redesign.

## 4. How the top two differ (customer · market · revenue mechanism)
- **ChemSDS** — *customer:* small chemical formulators/blenders/manufacturers;
  *market:* OSHA HazCom 2024 / GHS chemical-safety document compliance;
  *revenue:* SDS-authoring + label + hosted-portal subscription (~$1,800/mo).
- **AccessGuard** — *customer:* mid-market companies with high-traffic transactional
  websites (entry: just-sued); *market:* ADA Title III web-accessibility litigation
  defense; *revenue:* monitoring + remediation + legal-grade attestation retainer
  (~$2,500/mo).
They are materially distinct on all three axes.

## 5. Evidence spot-check on the top two (per the goal's CHECK clause)
Restating ≥8 sub-scores with the inline evidence that earned them (a number, a named
competitor, or shown math):

**ChemSDS**
- CFO Startup-capital-efficiency **9** — launchable for low five figures, no inventory/
  equipment, "vs enterprise EHS platforms (VelocityEHS, Sovos) built over years/millions." (named competitor)
- COO Logistics-tractability **9** — zero physical logistics; 100% remote document/data
  work deliverable to any US state. (structural fact)
- CMO Competitive-air **8** — VelocityEHS/Verisk 3E/Sphera can't profitably serve a
  $500–$5K/mo customer with their enterprise cost/sales structure; per-hour
  consultancies won't productize. (named competitors + economics)
- CMO Customer/demand-evidence **8** — HazCom perennially among OSHA's most-cited
  standards; May 2024 final rule with Jan-2026/Jul-2027 staggered compliance deadlines. (named regulation + dates)

**AccessGuard**
- CFO Working-capital **9** — annual contract billed upfront; customer pays a full year
  before most COGS is incurred (negative working-capital cycle). (shown mechanism)
- CMO Wedge **9** — buyer list is literal public record: PACER Title III dockets,
  ~4,000+ federal filings/yr (Seyfarth/UsableNet), enumerable named defendants. (named source + number)
- CMO Customer/demand-evidence **9** — accessiBe paid a $1M FTC settlement (2025);
  $5K–$25K settlement ranges; multiple-thousand annual filings concentrated in NY/FL/CA. (named competitor + numbers)
- Legal Licensing **9** — no occupational license exists for web-accessibility services
  in any US state; WCAG is a W3C standard, not a licensed practice. (specific legal fact)

All restated ≥8 scores carry real evidence; none is a vague adjective. (FranAudit and
GovRenew, by contrast, are dragged down precisely where their evidence is weakest —
the Legal liability dimension — which is why they FAIL rather than pass.)

## 6. The five structural walls (consistent across this run AND the prior 45)
1. **Software-vs-BPO margin hinge** — the defensible work is human and scales linearly
   (AccessGuard manual audits, ChemSDS chemist sign-off, ProxyDocket ingestion).
2. **Liability coupling** — the value prop and the largest liability are the same thing
   (ChemSDS bodily-injury, GovRenew FCA, AccessGuard FTC overclaim).
3. **Latent vs forced demand** — "should-comply" deferred until enforcement is acute
   (ProxyDocket's cold base; GovRenew's free-DIY anchor).
4. **Funded/strong-tech incumbent in the lane** — constraint #5 (AccessGuard/AudioEye).
5. **UPL / "this is legal work"** — when the deliverable is a legal document or opinion
   (FranAudit FDD, GovRenew eligibility attestation).

## 7. Honest recommendation to the operator
This was a successful, rigorous, zero-qualifier run. Two legitimate next moves (the
choice is the operator's):
- **Take the top two near-misses (ChemSDS, AccessGuard) into cheap pre-build
  validation.** Each has a clearly defined, days-to-weeks experiment set in its PM
  synthesis (ChemSDS: chemist-hours-per-SDS, insurability, hazard-data coverage,
  ARPU/distributor channel; AccessGuard: retention cohort, automation-vs-cited-
  violation coverage, defang positioning, out-position AudioEye). If those land, re-score
  from real numbers — either could legitimately cross the bar on validated data.
- **OR keep generating** in genuinely new territory (e.g., the held triage candidates
  TariffLedger / EmissionsLedger were never councilled due to the 5-pass cap), but only
  as an explicit operator decision — never by inflating a packet.

## 8. Artifacts (all committed to this branch under runs/2026-06-09-stoic/)
- `00-prior-concept-ledger.md` — the ~45-concept de-dup ledger from 10 prior branches.
- `01-brainstorm-and-triage.md` — 14 fresh candidates + triage screen.
- `SCOREBOARD.md` — the compact scoreboard.
- `AccessGuard/`, `ChemSDS/`, `FranAudit/`, `ProxyDocket/`, `GovRenew/` — each with its
  clean-room one-pager, all five full uncompressed expert reviews, and the PM synthesis
  with the documented red-team.
