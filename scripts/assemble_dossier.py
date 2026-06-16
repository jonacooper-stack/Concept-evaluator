#!/usr/bin/env python3
"""Assemble the full SecureControls Concept Dossier: plain-English body (sections
1-8) + Section 9 appendix (PM synthesis + the six verbatim council packets)."""
import os

RUN = "runs/2026-06-16-securecontrols"
DELIV = "deliverables/2026-06-16"

body = open(f"{DELIV}/SecureControls-Concept-Dossier-body.md", encoding="utf-8").read()

appendix_parts = [
    ("PM SYNTHESIS & TWO-DIRECTIONAL RED-TEAM", f"{RUN}/07-pm-synthesis.md"),
    ("COUNCIL PACKET — CFO", f"{RUN}/01-cfo-review.md"),
    ("COUNCIL PACKET — CMO", f"{RUN}/02-cmo-review.md"),
    ("COUNCIL PACKET — COO", f"{RUN}/03-coo-review.md"),
    ("COUNCIL PACKET — LEGAL / REGULATORY", f"{RUN}/04-legal-review.md"),
    ("COUNCIL PACKET — CTO", f"{RUN}/05-cto-review.md"),
    ("COUNCIL PACKET — COMPETITIVE & INDUSTRY ANALYST", f"{RUN}/06-competitive-analyst-review.md"),
]

out = [body.rstrip(), "\n## 9. Appendix — full council packet\n",
       "*The complete, uncompressed expert reviews and the PM synthesis with the "
       "documented two-directional red-team, verbatim, for anyone who wants the "
       "rigor behind the plain-English summary above. These were produced "
       "independently by six expert subagents, each blind to the others and to any "
       "target score, working only from a neutral clean-room one-pager.*\n"]

for title, path in appendix_parts:
    text = open(path, encoding="utf-8").read()
    out.append(f"\n---\n\n### APPENDIX — {title}\n")
    out.append(text.rstrip())

combined = "\n".join(out) + "\n"
dest = f"{DELIV}/SecureControls-Concept-Dossier.md"
open(dest, "w", encoding="utf-8").write(combined)
print(f"[ok] wrote {dest} ({len(combined):,} chars)")
