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
**un-modernized** small businesses. Buying day-one cash flow at a fair multiple — and
running the same business better with modern marketing, systems, and AI — is a faster
path to founder free cash flow than building. See `01-objectives.md`.

## The doc set (mirrors the build council, re-pointed to buy-side)
| File | Lens | What changed from the build council |
|---|---|---|
| `01-objectives.md` | Source of truth | Deal box, DSCR ≥1.25–1.5x, transferability, owner-replaceability, modernization upside, SBA eligibility |
| `02-council-cfo.md` | CFO | Earnings quality / add-backs, valuation & multiple, sources & uses, DSCR, working capital, resale arbitrage |
| `03-council-cmo.md` | CMO | Customer concentration, brand-vs-owner, retention through transition, **modernizing sleepy marketing** |
| `04-council-coo.md` | COO | Owner-dependency, key-staff retention, transition, **streamlining/modernizing ops** |
| `05-council-legal-regulatory.md` | Legal | SBA eligibility, license/contract transfer, deal structure, seller liability tail, PG exposure |
| `06-council-cto.md` | CTO | Inherited systems condition, tech debt, **modernizing with off-the-shelf tech + AI** |
| `07-product-manager-synthesizer.md` | Deal lead | Produces a **Deal Memo** → LOI/thesis → 100-day plan → SBA package; verdict GO / NO-GO / RE-TRADE |
| `08-founder-profile.md` | Founders | Same founders as **full-time owner-operators** who manage (not perform) a field crew |
| `09-discovery-loop.md` | Orchestration | Cheap-to-expensive funnel over **target profiles** |
| `CLAUDE.md` | Operating rules | Honesty-first discovery for acquisitions |

The COO, CMO, and CTO lenses all explicitly credit the founders' edge of **taking a
sleepy old business and modernizing it** (modern marketing, modern systems, modern
tech/AI) — that upside is a scored dimension in each.

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
