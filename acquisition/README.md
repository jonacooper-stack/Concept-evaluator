# Acquisition Council (SBA buy-and-modernize fork)

This folder is a **fork** of the repo-root council. The root council
(`/01-objectives.md` … `/13-*.md` + root `CLAUDE.md`) evaluates businesses to **BUILD**
from scratch. This `acquisition/` folder evaluates businesses to **BUY** — specifically,
acquiring an existing, cash-flowing small business using an **SBA 7(a) loan** and then
modernizing its marketing, operations, and technology.

Both councils live in the same repo and can be run side-by-side. They share nothing at
runtime: different objective docs, different rubrics, different agents.

## The thesis
Retiring Baby Boomer owners are selling large numbers of profitable, durable, but
**un-modernized** small businesses. Buying proven cash flow at a fair price — and running
the same business better with modern marketing, systems, and AI — is a faster path to
founder free cash flow than building. See `01-objectives.md`.

## Two stages (the key design choice)
- **STAGE 1 — Industry Screen** (`01`–`07`): decide **which TYPES of business (industries)
  to hunt in**. Score only industry-level traits knowable from the outside. Verdict per
  industry: **PURSUE / MAYBE / PASS**. Output: ~3 industries to source real deals in.
- **STAGE 2 — Target Due Diligence** (`10-due-diligence.md`): on a **real listing**, check
  the company-specific tells (earnings quality, owner-dependency, systems, key staff,
  customer concentration). Verdict per deal: **GO / PASS / OFFER A LOWER PRICE**.

**Why split them?** Every sleepy, retiring-owner business has owner-dependency, un-verified
earnings, and old systems. Those are *universal* — they don't help you choose an industry,
they just drag every score down — so Stage 1 leaves them out and Stage 2 checks them on the
actual company.

## The doc set
| File | Lens | What it scores |
|---|---|---|
| `01-objectives.md` | Source of truth | Two-stage model; industry-level rubric (durability, financeability, deal supply, modernization upside, competition, operator fit) |
| `02-council-cfo.md` | CFO | The industry's economics — typical margins, normal multiples, SBA financeability, typical-deal DSCR, capital intensity |
| `03-council-cmo.md` | CMO | The industry's customer/demand shape + how sleepy its **marketing** is (founders' edge) |
| `04-council-coo.md` | COO | The industry's operating model + how systematizable its **operations** are (founders' edge) |
| `05-council-legal-regulatory.md` | Legal | The industry's SBA eligibility, license-transfer norms, typical liability/environmental profile |
| `06-council-cto.md` | CTO | The industry's typical systems + how modernizable with **off-the-shelf tech + AI** (founders' edge) |
| `07-product-manager-synthesizer.md` | Deal lead | Produces an **Industry Memo**; verdict **PURSUE / MAYBE / PASS** + red-team |
| `08-founder-profile.md` | Founders | Same founders as **full-time owner-operators** who manage (not perform) a field crew |
| `09-discovery-loop.md` | Orchestration | Cheap-to-expensive funnel over **candidate industries** → ~3 PURSUE |
| `10-due-diligence.md` | **Stage 2** | Company-specific checklist on a real listing; verdict **GO / PASS / OFFER A LOWER PRICE** |
| `CLAUDE.md` | Operating rules | Honesty-first, two-stage discovery |

The CMO, COO, and CTO lenses each credit the founders' edge of **taking a sleepy old industry
and modernizing it** (marketing, systems, tech/AI) — a scored dimension in each. The
"obvious tells" (owner-dependency, earnings verification, this company's systems) are
deliberately moved OUT of Stage 1 and INTO `10-due-diligence.md`.

## Agents (in `.claude/agents/`)
The acquisition council uses dedicated agents prefixed `acq-`:
`acq-idea-generator`, `acq-idea-triage`, `acq-cfo-reviewer`, `acq-cmo-reviewer`,
`acq-coo-reviewer`, `acq-legal-reviewer`, `acq-cto-reviewer`, `acq-deal-synthesizer`.
The build council's agents (no prefix) are untouched.

> NOTE: newly-created agents only become dispatchable as their own type after Claude Code
> reloads (a fresh session). Within the session that created them, run the council by
> dispatching `general-purpose` subagents pointed at the specific `acquisition/0X-*.md`
> docs — the isolation and output rules are identical.

## How to run
1. Open this repo in Claude Code (fresh session so the `acq-*` agents load).
2. Read `acquisition/CLAUDE.md`, then `01`–`08`.
3. Use `09-discovery-loop.md`: generate target profiles → triage → full council deep-dive.
4. Outputs (scoreboard, deal memos, red-teams) save under `acquisition/runs/<date>/`.

## Important caveats
This is a decision-support tool, not advice. Real acquisitions require a quality-of-
earnings review, an M&A attorney, a CPA, and an SBA lender. Discovery-stage financials
are representative `[ASSUMED]` ranges; re-run the council on a real listing's actual
numbers before signing an LOI.
