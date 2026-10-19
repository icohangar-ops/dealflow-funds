# dealflow-funds

**Deal Flow: NYC's First VC Hackathon** — Sat Oct 24, 2026, 9:00 AM–6:00 PM ET, Betaworks NYC.
**Track 4: Funds. Make LPs as informed as their GPs**

> **Status: pre-event scaffold only.** The organisers say *"On Saturday you only build. Everything a founder does before writing code happens this week."* This repo therefore holds only the plan, founder-brief template, interview notes template, a synthetic dataset (the track brief explicitly says to generate synthetic data before the event), and an empty package with a data-loading smoke test. **No product features have been built yet** — they get written on build day.

## Problem statement (verbatim from organisers)
LPs commit capital for ten years and get PDFs in return. Yearly K-1s and quarterly reports arrive in different formats, valuation marks move with little explanation, and judging a GP's real track record means rebuilding it by hand. Secondary buyers face the same fog when they price an LP stake. Build tools that read fund documents, diligence GP teams and price what LPs own.

**Who has this problem:** family offices, endowments, fund-of-funds, emerging LPs, secondary buyers, fund admins, and emerging managers raising Fund I or II.

**Data to start with:** adviser filings (Form ADV) on the SEC's adviser search, the reporting templates published by ILPA, and synthetic K-1s and quarterly reports you generate before the event. Never upload real LP documents without the owner's permission.

## Working idea (to validate in interviews)
LP report reader: extract NAV, calls, distributions, mark changes from quarterly reports; compute TVPI/DPI/IRR; explain what moved QoQ; rough secondary price from NAV x discount.

## Interview questions (from organisers)
- How many hours does one quarter of fund reports take your team?
- How do you judge a GP's track record today, and what can't you verify?
- How do you decide what an LP stake is worth on the secondary market?

## Prior work to reference
- [proof-of-assay](https://github.com/icohangar-ops/proof-of-assay) — deterministic reconciliation + hash-chained extraction receipts (reference only; code to be written on build day)
- [Strata](https://github.com/icohangar-ops/Strata) — CFO-function scoring (reference only; code to be written on build day)
- [Live-Diligence](https://github.com/icohangar-ops/Live-Diligence) — SEC filing retrieval (Form ADV) (reference only; code to be written on build day)

## Planned architecture (to build Saturday)
ingest (public APIs / synthetic files) → deterministic checks/scoring → LLM explanation with citations → Streamlit one-workflow demo. Every output links to its source row/document.

## Saturday finalize checklist
- [ ] Founder brief filled in (`docs/FOUNDER_BRIEF.md`) with real interview evidence
- [ ] Market map filled in (`docs/MARKET_MAP.md`)
- [ ] Build the one demo workflow (core logic + tests)
- [ ] Streamlit UI for the demo
- [ ] Record 2-min demo / prep pitch (business + code are judged equally)
- [ ] Submit via the organisers' Saturday process (not yet announced)

## Demo plan
Upload 3 synthetic quarterly reports for one fund, see extracted NAV table, QoQ explanation, TVPI/DPI, and a secondary bid range.

## Run
```bash
pip install -e .[dev]
python -m dealflow_funds            # prints synthetic dataset summary
pytest -q
```

## Data
`data/synthetic/` is **synthetic, fabricated data**. Never commit real confidential company, fund or LP documents.

MIT License.
