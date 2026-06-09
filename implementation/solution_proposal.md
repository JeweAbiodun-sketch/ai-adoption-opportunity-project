# Solution Proposal — AI Demand Forecasting for Mid-Market Retail
**Recommended for: Cleo, CEO · Mid-Market Retail (51–250 employees)**

---

## The Recommended Solution
**AI-powered demand forecasting and inventory optimisation**

A cloud-based SaaS AI tool (entry recommendation: Inventory Planner or similar) that connects to your existing ERP or POS system, learns your sales patterns, and generates weekly replenishment recommendations — replacing or augmenting your buyer's spreadsheet-based forecasting.

> **Architecture note:** The SaaS tools named here are the correct entry point for a **pilot phase**, not the end-state infrastructure. A company at this scale that scales the programme beyond one use case will move toward a hybrid operating model (SaaS layer + data integration middleware + internal tooling). The pilot cost is £700–£5,800/month. Full hybrid infrastructure runs closer to £70,560 setup + £120,485/year. Plan the pilot to test value; plan the budget to scale it.

---

## What It Does
- Analyses 12–24 months of historical sales data by SKU, category, location, and season
- Predicts demand for the next 4–12 weeks with confidence intervals
- Flags overstock risk (items likely to need early markdown)
- Flags stockout risk (items to reorder now)
- Generates automated purchase order drafts for buyer review

---

## Prerequisite: Data Readiness Gate

Before any tool is procured, a data audit (Weeks 1–2) must confirm that clean, daily-level sales data exists for at least 12 months. The outcome of this audit determines the path forward:

| Audit finding | Next step |
|---|---|
| 12+ months of clean daily sales data available | Proceed to Phase 1 tool selection |
| Significant gaps or < 12 months of usable data | Insert a **3–6 month data remediation phase** (budget: £30k–£60k) before any AI tool procurement |
| 9+ month data gaps or no SKU-level history | Pause AI investment; prioritise data infrastructure first |

This gate is not optional. Demand forecasting models trained on patchy data produce inaccurate recommendations and erode buyer trust faster than the status quo.

---

## Why This Solution for Cleo
- Directly addresses margin pressure through reduced overstock and fewer lost sales
- Works on data Cleo's business already has (POS/ERP transaction history) — **provided the data audit passes**
- SaaS model: no large upfront investment, cancel if it doesn't deliver
- No customer data platform required — lower implementation risk than personalisation or pricing use cases
- Natural second use case: Customer Personalisation Engine (requires unified customer view; best sequenced after demand forecasting is stable)

---

## Change Management Requirements

Workforce readiness is the weakest dimension at this company profile (3/10). A well-designed AI tool with poor adoption delivers nothing. The following are not optional:

- **Named roles required before launch:** executive sponsor, merchandising champion, store pilot lead
- **Training budget:** £500–£1,000 per affected buyer or merchandiser
- **Protected time:** 20–30 hours per person during Phases 1–2 for onboarding and supervised use
- **Adoption target:** >70% active tool usage by Week 16 of the pilot — this is a success criterion, not a nice-to-have

Without this budget and these named owners, expect 30–50% tool underutilisation in the first 6 months regardless of technical quality.

---

## The Diagnostic Tool Connection
The `ai_diagnostic_tool.html` prototype in this repo demonstrates the consulting methodology used to arrive at this recommendation. When Cleo runs the diagnostic on her own business, the tool will:
1. Place her company on the 5-stage AI maturity model
2. Score her retail data, workforce, and leadership readiness
3. Recommend inventory AI as the highest-priority opportunity (based on her answers)
4. Generate a CFO-legible value estimate specific to her revenue and tech budget
5. Flag the risks that are most likely to derail implementation

The report is downloadable as a PDF — a deliverable Cleo can share with her board.

---

## Success Metrics and Evaluation Timeline

Demand forecasting accuracy improves as the model learns seasonal patterns. Do not draw ROI conclusions before Month 12. The evaluation schedule below prevents a premature stop decision based on incomplete data.

| Checkpoint | Timing | What to measure |
|---|---|---|
| Operational review | Week 17–20 | Is the tool being used? Is data flowing correctly? Adoption rate vs 70% target |
| First accuracy checkpoint | Month 6 | MAPE below 15%? Adoption rate above 70%? Stockout rate trending down? |
| ROI and scale decision | Month 12–18 | Inventory days-on-hand, stockout rate, markdown rate vs baseline; proceed to hybrid architecture? |

### Value estimate (with attribution discount)

| Scenario | Attribution assumption | Estimated annual benefit |
|---|---|---|
| Pessimistic | 30% of gains attributable to AI | ~£200k |
| Base case | 60% attribution | ~£405k |
| Optimistic | 80% attribution | ~£540k |

A 30:1 ROI headline is a red flag for a CFO. The base case of ~£405k on a £15M revenue business is still a compelling, boardroom-defensible number — use that.

---

## Baseline Metrics (measure before go-live)

| Metric | Baseline | Accuracy checkpoint (Month 6) | ROI gate (Month 12–18) |
| --- | --- | --- | --- |
| Inventory days-on-hand | Measure at start | Directional improvement | Reduce by 15% vs baseline |
| Stockout rate (% of SKUs) | Measure at start | Trending down | Reduce by 30% vs baseline |
| Markdown rate (% of revenue) | Measure at start | Stable or improving | Reduce by 20% vs baseline |
| Forecast accuracy (MAPE) | Buyer estimate | <15% MAPE | <12% MAPE |
| Gross margin | Measure at start | Directional improvement | +2–4 percentage points |
| Tool adoption rate | 0% (pre-launch) | >70% active users | >85% active users |

> Baselines must be locked before go-live. Without a documented baseline, attribution is impossible and leadership will have no grounds to approve the scale investment.
