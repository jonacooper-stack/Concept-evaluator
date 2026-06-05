# CMMC Compliance Market — Competitive Landscape & White-Space Scan (June 2026)

Research method: 5 parallel web-research agents (one per angle) → source fetch →
adversarial verification of the load-bearing claims. ~250 sources touched; the
most decision-relevant claims were re-verified directly. Confidence/caveats at the
end. Dates are firm; some vendor capability/pricing figures are marketing copy
(many vendor sites blocked direct fetch) and are flagged as claims, not audited.

---

## BOTTOM LINE (blunt)

CMMC compliance is a **genuinely forced, huge, urgent market — and a crowded,
fast-moving, partly-funded, and now partly brand-tainted software field.** The
specific concept evaluated (AI ingests your docs → generates your SSP/POA&M/gap
scorecard → ongoing hub) is **no longer differentiated**: it is already shipping
from a funded horizontal (Secureframe Defense, Mar 2026), a CMMC-native AI tool
(SMPL-C), and adjacent AI-GRC unicorns (Delve, Cynomi). The MSP-channel pivot is
**now funded and operator-backed** (IntelliGRC, Jan 2026, co-led by Huntress's
CEO). And the value/margin is migrating to **assessment capacity + the CUI
enclave**, where an under-funded, software-first team is weakest. For two founders
whose edge is marketing/positioning rather than out-engineering or out-spending,
**a head-on entry is among the harder paths in this space.** The honest verdict
from the council (REFINE) is reinforced, not overturned, by present-day evidence.

---

## 1. THE MARKET IS REAL AND FORCED (the good news)

- Both rules are final and live: **32 CFR Part 170 effective Dec 16, 2024**; the
  **DFARS acquisition rule (48 CFR, 252.204-7021/7025) effective Nov 10, 2025.**
  Phased rollout: Phase 1 began Nov 10, 2025 → **Phase 2 (mandatory third-party
  C3PAO Level 2 certification) Nov 10, 2026** → full enforcement Nov 10, 2028.
  [federalregister.gov 2024-10-15; 2025-09-10; dorsey.com 2025-11; pillsburylaw.com 2025-09]
- **~76,000–80,000 firms need Level 2** (of a ~220,000-org DIB). [DoD RIA via
  a-lign.com, huntress.com, intersecinc.com]
- **Only ~1% of contractors report being fully ready — down from 8% (2023) and 4%
  (2024)**; median SPRS score ~60 vs. 110 required; only ~42% have even submitted a
  score. [CyberSheath/Merrill "State of the DIB" 2025-10-01, businesswire.com]
- **The binding scarcity is assessor capacity:** ~80–103 authorized C3PAOs and
  <600 certified assessors (vs. 2,000–3,000 needed) for tens of thousands of firms;
  only a few hundred L2 certificates issued; backlogs 3–9 months and climbing.
  [Cyber AB town-halls via cmmc.com & secureframe.com; cybersheath.com; coalfirefederal.com]

This is exactly the "regulation-forced, deadline-driven, budgeted, recurring"
demand the objectives doc prizes. The problem is not demand. It is competition and
where the value sits.

---

## 2. THE WALLET: SOFTWARE IS A CHEAP SLICE

Total first-year cost to certify a small (<50-emp) Level 2 contractor: **~$75K–
$150K** (DoD's own 3-year RIA models ~$488K incl. all 800-171 implementation labor).
Breakdown:
- **C3PAO assessment fee: ~$30K–$50K** (small biz). [ibsscorp.com, workstreet.com]
- **Remediation / implementation:** the largest, most variable line.
- **Managed enclave / MSP retainer: ~$2.5K–$50K per *month*** by scope; GCC High
  licensing ~$22–$36/user/mo. [vso-inc.com, secureframe.com]
- **The GRC/doc software itself is the *cheap* part:** FutureFeed ~$1.2K–$4.8K/yr;
  Totem L1 ~$5K–$7K/yr; horizontals ~$7.5K–$20K/yr; ComplianceForge templates
  ~$950/yr. [vendor pricing pages]

Implication: the AI-doc-generation layer the founders targeted is the **lowest-
value, most commoditized slice** of a six-figure spend. The money and the
defensibility live in the **enclave + assessment readiness**, not the document tool.

---

## 3. TIERED COMPETITIVE MAP

### Tier A — Horizontal compliance-automation platforms (moving down into CMMC)
| Vendor | CMMC depth today | Funding (latest) | DIB push |
|---|---|---|---|
| **Secureframe** | **Deepest of the cohort.** "Secureframe Defense" (Mar 2026): AI auto-configures a CMMC enclave in GCC High/Google Workspace <30 min, AI-generates SSP+policies, Audit Module for C3PAO; "assessment-ready in <8 weeks." Prior: Secureframe Federal (SSP Builder/POA&M/SPRS, Jun 2025), CMMC.com + Coalfire C3PAO partnership (May 2025), own CMMC L2 cert via Redspin (Sep 2025). | **Least-funded big-3**: ~$79M total, last round 2022 (~$300M val). | **Highest** — 3 product waves in 12 mo. |
| **Vanta** | Real CMMC + 800-171 products (SSP/POA&M mgmt), routes assessment via RPO/C3PAO partners; Vanta Government Cloud on AWS GovCloud. Critique: still "SOC 2-shaped." | **$504M raised, $4B val (Jul 2025).** | Moderate (webinars, partners). |
| **Drata** | Dedicated CMMC product, SPRS/POA&M workflows; "CMMC Accelerator" w/ BARR Advisory (Feb 2026). Same "SOC 2-shaped" critique. | ~$328M raised, $2B val (2022, flat). | Moderate. |
| **Hyperproof / Thoropass / Sprinto / Scrut** | All "support" CMMC via templates/mapping; no dedicated DIB campaign found; Thoropass skews L1; Sprinto lightest. | $20M–$77M range. | Thin. |

Independent critique (deepfathom.ai): horizontals' SSP generation restates control
language, POA&M logic doesn't model CMMC's rules, and **commercial-cloud hosting is
mismatched to CUI's FedRAMP-Moderate requirement** — a real depth gap, but the gap
Secureframe Defense specifically targets.

### Tier B — CMMC-native specialist software
- **SMPL-C** — AI-first (NIST-tuned LLM), upload docs → one-click SSP/POA&M/SRM, gap
  analysis, **AND a multi-tenant white-label MSP console.** This is the original
  concept *and* Pivot A in one product. Small/early. [smpl-c.com; AWS Marketplace; verified]
- **FutureFeed** — CMMC-native GRC; "Powered-by-FutureFeed" MSP program ($9,995/yr,
  **260+ service providers** claimed). Totem (MSP "Expert" tier), **ScalePad
  ControlMap** ($200–400/mo, MSP-first; note: owned by ScalePad, *not* CyberSaint),
  Ignyte (AI-positioned, USAF CRADA), Cyturus (powers the Cyber AB readiness tool).
- **Managed CUI enclaves** — PreVeil (~$5K–$15K/yr, "only CUI users pay," 2,500+
  contractors, FedRAMP-Moderate-equivalent), Cuick Trac (Beryllium), C3 Integrated
  Solutions (ex-Steel Root + Ingalls). Template-only: ComplianceForge.

### Tier C — Services / MSP / assessor layer (owns the trust)
- **Summit 7** (100+ clients taken to L2, own dual L2 certs, launched "Commander"
  managed-GRC 2025, acquired GRC Academy), **CyberSheath** (Federal Enclave),
  **Coalfire/Redspin/Schellman/Kratos** (C3PAOs). Ecosystem: ~103 C3PAOs, ~759
  CCAs, ~2,000 RPs, ~387 RPOs (Mar 2026); **ISACA takes over CMMC certs Apr 1, 2026.**
- **Cautionary signal:** NeoSystems (a CMMC MSP, ~70 staff, perfect-110 track record)
  **abruptly collapsed May 1, 2026**, stranding hundreds of GovCon clients — provider-
  continuity risk in the managed-enclave model. [oxebridge.com]

---

## 4. THE CONCEPT IS LARGELY PRE-EMPTED (the hard news)

- **"Upload docs → AI writes your SSP/gap analysis" is taken**, by funded players:
  **Secureframe Defense** (Mar 2026), **SMPL-C**, **Delve** ($32M Series A @ $300M
  val, Jul 2025; CMMC + 800-171 policy gen), **Cynomi** (AI vCISO, $37M Apr 2025,
  CMMC L2 via MSPs), plus Workstreet, RegScale, Strike Graph, ConductorAI. The naive
  version is not white space.
- **The MSP-channel pivot (Pivot A) is now funded and operator-backed:**
  **IntelliGRC** ($3.5M seed, closed Jan 31 2026; multi-tenant GRC purpose-built for
  MSPs/MSSPs serving the DIB; **co-led by Huntress CEO Kyle Hanslovan + Blu
  Ventures**). Plus SMPL-C, FutureFeed (260+ providers), Exostar "CMMC Ready Suite
  for MSPs," ControlMap, Blumira. Contested *and* capitalized.
- **The AI-compliance trust gap is real and now public:** the **Delve scandal**
  (Mar–Apr 2026, TechCrunch / MIT *The Tech* / Yahoo Finance / ChannelInsider) —
  the $300M AI-compliance unicorn accused of generating **fabricated audit evidence
  (493/494 SOC 2 reports identical boilerplate, pre-written conclusions, sham audit
  mills)**; pulled from YC's directory; Insight Partners scrubbed its post. This both
  validates demand (AI compliance can mint a unicorn) and **poisons the well** for
  "trust our AI to write your compliance docs" — raising the credibility bar for any
  new AI-first entrant.

---

## 5. WHITE SPACE — honestly assessed for THIS founder profile

The genuinely less-contested positions are at the **seams**, and each has a catch
for an under-funded, software-first, marketing-led team:

1. **Verifiable / "defensible" documentation that survives a C3PAO** (positioned
   *against* Delve-style AI compliance theater; differentiator = provable accuracy
   to the real environment, not speed). *Catch:* this is a hard engineering + human-
   expert problem, and the "AI compliance" brand is now tainted — you'd be selling
   trust into a headwind.
2. **Warranty / outcome-bonded readiness** ("we cover your re-assessment cost if you
   fail despite following the platform"). Genuinely unoccupied — but a true "pass
   guarantee" is **prohibited by Cyber AB rules**, the same firm can't do readiness
   *and* the certifying assessment, and you're not the assessor, so this is an
   insurance/warranty product, narrow and operationally tricky.
3. **CUI-safe / in-boundary (local or FedRAMP-Moderate) AI** — most consumer AI is
   off-limits for CUI (uploading CUI to a non-FedRAMP AI is itself a violation), so
   a provably in-boundary engine is a real moat angle. *Catch:* heavy build; SMPL-C
   already claims a no-network/no-storage posture; this is out-engineering, not
   out-marketing.

Honest meta-point: even the "open" wedges are either **hard to build** (local/FedRAMP
AI), **structurally constrained** (the guarantee), or **brand-tainted** (AI docs) —
none is a clean fit for a marketing-led generalist pair. The one structural opening
that *does* suit the founders' trust/marketing edge is **being the credible,
human-verified, "no-theater" alternative** — but that is a positioning bet into a
crowded, post-scandal category, not an empty field.

---

## 6. IMPLICATIONS FOR THE THREE PIVOTS

- **Pivot A (MSP channel-first):** *Harder than when proposed.* Now funded
  (IntelliGRC + Huntress) and occupied (SMPL-C, FutureFeed, Exostar, ControlMap).
  Still a real lane, but you'd be a late, under-funded entrant against an
  operator-backed incumbent in the exact GTM.
- **Pivot B (assessor-coupled / guaranteed readiness):** *Narrow but genuinely the
  least-occupied.* Must be a warranty/insurance form (guarantees + consult-then-
  assess are barred). Fits the founders' trust/positioning edge better than A, but
  it's a small, operationally complex wedge and drifts toward services.
- **Pivot C (same engine, sleepier mandate):** *Relatively more attractive after
  this research.* The whole point of C was to escape exactly this funded saturation
  — and CMMC is now demonstrably saturated. Pointing the doc-generation engine at a
  fragmented regime with no funded strong-tech incumbent (e.g., FTC Safeguards Rule,
  FDA QMS/21 CFR 820, NERC-CIP, state regimes) is the cleanest fit for the
  founders' "out-position sleepy incumbents" edge — at the cost of CMMC's forced
  deadline certainty (must re-validate demand).

---

## CONFIDENCE & CAVEATS
- **High confidence:** rollout dates; market size order-of-magnitude; "only 1%
  ready"; assessor bottleneck; Secureframe's DIB push; Delve scandal; IntelliGRC
  funding/backers; SMPL-C multi-tenant + AI-first. (All multi-source or directly verified.)
- **Moderate:** exact L2 entity count (76,598 vs. rounded 80,000 vs. industry-floated
  118,000); exact C3PAO count (drifts 83→103 across Jan–Mar 2026); "260 providers"
  (single-source).
- **Soft:** all "total cost to certify" composites and vendor timeline claims
  ("<8 weeks") — marketing/aggregator numbers with an urgency incentive; treat as ranges.
- **Method limit:** many vendor sites returned HTTP 403 to direct fetch, so several
  capability/pricing facts are search-extracted vendor copy, not independently audited.

## KEY SOURCES
- Rules/timing: federalregister.gov (2024-10-15, 2025-09-10); morganlewis.com; pillsburylaw.com; dorsey.com; summit7.us/blog/dfars-7025
- Market/demand: a-lign.com; huntress.com; CyberSheath "State of the DIB" 2025 (businesswire.com 2025-10-01); cmmc.com town-halls; coalfirefederal.com
- Secureframe: secureframe.com/newsroom/announcing-secureframe-defense-for-cmmc; helpnetsecurity.com 2026-03-11; secureframe.com/newsroom/secureframe-federal; /cmmc-level-2-certification
- Horizontals: vanta.com/products/cmmc; drata.com/product/cmmc; cnbc.com 2025-07-23 (Vanta $4B); deepfathom.ai/articles/grc-land-grab-cmmc
- Native/AI: smpl-c.com (+AWS Marketplace); futurefeed.co/pricing; scalepad ControlMap; ignyteplatform.com; cynomi.com; delve.co
- Delve scandal: techcrunch.com 2026-03-22 & 2026-03-23; thetech.com 2026-04-09; finance.yahoo.com; channelinsider.com
- MSP/IntelliGRC: prnewswire.com IntelliGRC 2026-03-03; channele2e.com; intelligrc.com/software-platform
- Ecosystem/services: cmmc.com town-halls; summit7.us; cybersheath.com; oxebridge.com (NeoSystems)
- Pricing: ibsscorp.com; workstreet.com; vso-inc.com; paramify.com; defensescoop.com 2023-12-28 (DoD RIA)
- Assessor independence / no-guarantee: infosecinstitute.com; miraisecurity.com; madsecurity.com
