# AI Adoption Opportunity Project

AI Consulting and Integration Bootcamp — Module 5

---

## Project Overview

This project builds a complete, evidence-backed AI adoption recommendation for a mid-market retail company. The objective is to move from generic AI hype to a practical proposal that a CEO can take into a board or investor meeting.

The output is not just a report — it is a working consulting toolkit: a diagnostic prototype, a Tableau dashboard, a phased implementation plan, a cost estimate with ROI scenarios, and a gap analysis benchmarked against an external AI readiness report.

**The primary recommendation:** AI-powered demand forecasting and inventory optimisation, deployed first as a SaaS pilot, with a conditional path to a hybrid architecture as the programme scales.

---

## Use Case Discovery

### Sector and Company Size

- **Sector:** Retail (omnichannel, physical stores + online)
- **Company size:** 51–250 employees (mid-market)
- **Stores:** 10+ locations
- **Revenue proxy:** ~£15M annual

### Stakeholder Profile — Cleo, CEO

Cleo is a commercially minded CEO, not a technologist. Her constraints shape every recommendation in this project:

| Constraint | Implication for the recommendation |
| --- | --- |
| Worried about AI hype — wants evidence, not promises | Every recommendation is backed by published data with source citations |
| Budget cautious — wasted investment shows on the P&L | SaaS pilot model before any infrastructure commitment |
| No internal AI team | SaaS tools with vendor support, not custom builds |
| Competitive pressure from larger retailers | Urgency to act, but not urgency to over-invest |

**Pain points identified from sector research:**

- Seasonal overstock tying up working capital
- Stockouts during peak periods causing lost sales
- Manual demand planning by buyers using spreadsheets
- Margin erosion from late markdowns and excess clearance stock

### Why AI Demand Forecasting Was Selected

| Criterion | Demand Forecasting | Customer Personalisation | AI Chatbot |
| --- | --- | --- | --- |
| Evidence of ROI at mid-market scale | High | Moderate | Low–Moderate |
| Works on data Cleo already has | Yes — POS/ERP history | No — needs unified customer data | Partially |
| Time to measurable result | 6–12 months | 12–18 months | 3–6 months |
| Change management burden | Medium | High | High |
| Hype risk | Low | Medium | High |

**Why not personalisation first?** Requires a unified customer data platform, typically 6–12 months to build. Better as Phase 2 once inventory AI has delivered ROI and built internal AI confidence.

**Why not chatbot first?** The "80% cost reduction" claim is industry hype; 30–50% is realistic. Does not address Cleo's core margin and cash flow concerns.

See full discovery reasoning in [research/use_case_discovery.md](research/use_case_discovery.md).

---

## Market Research Summary

### Retail AI — Key Market Signals

| Metric | Figure | Source |
| --- | --- | --- |
| Global AI in retail market size (2026) | $18.4 billion | Grand View Research |
| Retailers using or testing AI | 89% | McKinsey 2024 |
| Retailers with full AI implementation | 33% | Triple Whale 2024 |
| Retailers allocating >5% tech budget to AI | 23% | Triple Whale 2024 |
| AI adoption growth YoY (2023–2024) | +23 percentage points | Stanford AI Index 2024 |

**The gap between "using AI" (89%) and "fully implemented" (33%) is the opportunity.** Most mid-market retailers are experimenting but not yet capturing value.

### Where AI Delivers Proven ROI in Retail

**Tier 1 — High evidence, production at scale:**

- Demand forecasting & inventory optimisation: 10–20% inventory cost reduction
- Customer personalisation & recommendations: 15–25% revenue uplift
- Dynamic pricing & markdown optimisation: 3–8% margin improvement

**Tier 2 — Moderate evidence, growing adoption:**

- AI customer service & returns automation: £3.50 return per £1 spent
- Supply chain optimisation: 15% logistics cost reduction

**Tier 3 — Early stage, watch carefully:**

- Visual merchandising AI, AI store layout, autonomous checkout — insufficient mid-market evidence

### Mid-Market Specific Signals

- Average retail margin 2–5% — operational inefficiency is material at this scale
- 42% of retail AI projects fail due to data quality — fragmented POS/ERP/CRM is the primary risk
- Affordable SaaS AI vendors now serve mid-market at £500–£5,000/month (Inventory Planner, Relex Lite)

### Sources

- McKinsey, State of AI 2024 — [mckinsey.com](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- Stanford AI Index 2024 — [aiindex.stanford.edu](https://aiindex.stanford.edu/)
- Ringly.io, AI in Retail Statistics 2026 — [ringly.io](https://www.ringly.io/blog/ai-in-retail-statistics-2026)
- Grand View Research, AI in Retail Market Report
- Triple Whale, Ecommerce Benchmarks 2024

See full research and hype analysis in [research/market_research.md](research/market_research.md) and [research/opportunities_risks.md](research/opportunities_risks.md).

---

## Datasets

### Dataset 1 — Retail Sales Dataset (Primary)

- **Source:** [Kaggle — mohammadtalib786/retail-sales-dataset](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset)
- **Author:** mohammadtalib786
- **Contents:** 1,000 transactions (2023) — Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, Total Amount
- **Save to:** `data/raw/retail_sales_dataset.csv`
- **Used for:** Seasonal demand patterns, category performance, customer segmentation in the Tableau dashboard; demonstrates the type of data that feeds an AI demand forecasting model

### Dataset 2 — Global AI Tool Adoption Across Industries

- **Source:** [Kaggle — tfisthis/global-ai-tool-adoption-across-industries](https://www.kaggle.com/datasets/tfisthis/global-ai-tool-adoption-across-industries)
- **Author:** tfisthis
- **Contents:** AI adoption rates by industry, tool types, demographics
- **Save to:** `data/raw/global_ai_tool_adoption.csv`
- **Used for:** Retail vs other sectors adoption benchmarks; hype vs evidence signal in the Tableau dashboard

**Download steps for both datasets:**

1. Open the Kaggle URL (free account required)
2. Click Download
3. Save the CSV to the path shown above

See `data/raw/README_datasets.md` for full download instructions and column descriptions.

---

## How to View the Dashboard

The dashboard is the evidence layer for Cleo's meeting. It answers: *"Where does market data show AI adoption is worth exploring for mid-market retail?"*

### Option A — Pre-built PDF (no software required)

Open `dashboard/cleo_ai_dashboard.pdf` directly in any PDF viewer.

### Option B — Tableau Workbook (interactive)

1. Install [Tableau Desktop](https://www.tableau.com/products/desktop) or use Tableau Public
2. Open `dashboard/retail_ai_dashboard.twb`
3. If prompted, reconnect to `data/processed/retail_sales_cleaned.csv`

### Option C — Python-generated dashboard

```bash
pip install -r requirements.txt
python cleo_dashboard.py
# Output: cleo_ai_dashboard.pdf
```

### Dashboard Contents

| Sheet | Title | What it shows |
| --- | --- | --- |
| Sheet 1 | The Retail AI Opportunity | KPI tiles: market size, adoption gap, ROI benchmarks |
| Sheet 2 | Your Sales Data: Why AI Would Help | Seasonality, category demand, margin variability |
| Sheet 3 | Hype vs Evidence | Retail position on the adoption curve; evidence tiers by use case |

See full design documentation in [dashboard/dashboard_documentation.md](dashboard/dashboard_documentation.md).

---

## Implementation Plan

The phased rollout plan is in [implementation/implementation_plan.md](implementation/implementation_plan.md).

Summary of phases:

| Phase | Timing | Objective |
| --- | --- | --- |
| Phase 0 — Data Audit | Weeks 1–2 | Validate data quality; go/no-go gate before any spend |
| Phase 1 — Vendor Selection | Weeks 3–6 | Evaluate Inventory Planner, Relex Lite, Brightpearl AI on free trials |
| Phase 2 — Pilot Deployment | Weeks 7–16 | Run AI forecast in shadow mode alongside buyer; track MAPE and adoption |
| Phase 3 — Evaluation | Weeks 17–20 | Operational review: is the tool in use? Is data flowing? (not final ROI gate) |
| Phase 4 — Full Rollout | Months 6–12 | Expand to all SKUs and stores; integrate with buying calendar |
| ROI Decision | Months 12–18 | Compare actual inventory cost, stockout rate, and markdown rate vs baseline |

**Data readiness gate:** If the Phase 0 audit finds less than 12 months of clean daily sales data, a 3–6 month data remediation phase (£30k–£60k) must be inserted before vendor selection.

The full solution rationale, cost scenarios, and success metrics are in [implementation/solution_proposal.md](implementation/solution_proposal.md).

---

## Project Structure

```text
.
├── README.md                          ← This file
├── ai_diagnostic_tool.html            ← Interactive AI readiness diagnostic prototype
├── cleo_dashboard.py                  ← Python script to generate the PDF dashboard
├── data_prep.py                       ← Data cleaning and preparation script
├── server.js                          ← Local server for serving the diagnostic tool
├── package.json
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── README_datasets.md         ← Dataset download instructions and column descriptions
│   └── processed/
│       ├── retail_sales_cleaned.csv   ← Cleaned transaction data (Tableau input)
│       └── ai_adoption_retail_filtered.csv  ← Filtered AI adoption data (Tableau input)
│
├── dashboard/
│   ├── cleo_ai_dashboard.pdf          ← Pre-built PDF dashboard (no Tableau required)
│   ├── retail_ai_dashboard.twb        ← Tableau workbook
│   └── dashboard_documentation.md    ← Dashboard design and setup instructions
│
├── research/
│   ├── use_case_discovery.md          ← Stakeholder profile and use case selection rationale
│   ├── market_research.md             ← Market data, ROI evidence, hype signals
│   └── opportunities_risks.md        ← Ranked opportunities and risk map
│
├── implementation/
│   ├── solution_proposal.md           ← Recommended solution with cost, ROI, and success metrics
│   └── implementation_plan.md         ← Phased rollout plan with owners and budgets
│
├── cost_estimation/
│   ├── cost_analysis.md               ← SaaS pilot cost and hybrid TCO scenarios
│   └── timeline_estimate.md           ← Effort and timeline breakdown
│
└── research/diagnostic-gap-analysis.md  ← Gap analysis: project vs external AI readiness benchmark
```

### Key files for a first read

| Start here | Then read |
| --- | --- |
| `research/use_case_discovery.md` — why this use case | `implementation/solution_proposal.md` — the recommendation |
| `research/market_research.md` — the evidence base | `implementation/implementation_plan.md` — how to execute it |
| `ai_diagnostic_tool.html` — the prototype | `research/diagnostic-gap-analysis.md` — external benchmark comparison |

---

## Running the Diagnostic Tool

```bash
npm install
npm start
```

Then open `http://localhost:3001/ai_diagnostic_tool.html` in a browser.

The tool places a retail business on a 5-stage AI maturity model, scores data, workforce, and leadership readiness, and produces a CFO-legible recommendation report downloadable as PDF.
