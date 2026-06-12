# Dashboard Documentation — Retail AI Adoption Evidence
**Tool: Python (matplotlib / seaborn) · Output: 7-chart evidence dashboard**

---

## Dashboard Purpose

This Python-generated dashboard is the evidence layer for Cleo's presentation. It answers one question:
**"Where does market data show AI adoption is worth exploring for mid-market retail?"**

It is a communication layer — not an analysis layer — designed for a non-technical CEO. Every chart is paired with a plain-language insight. All numbers are sourced from published datasets.

---

## Data Sources

1. `data/raw/retail_sales_dataset.csv` — 1,000 transaction-level retail records (Kaggle)
2. `data/raw/global_ai_tool_adoption.csv` — AI adoption rates by industry and company size (Kaggle, filtered: retail + SME segment)

---

## Dashboard Sections & Charts (7 Total)

### Section 1 — Market Signals (Slides 3)

**Chart 1 — AI Adoption Rate by Industry (Bar Chart)**
- X-axis: Average adoption rate
- Y-axis: Industry (Agriculture, Education, Finance, Healthcare, Manufacturing, Retail, Technology, Transportation)
- Highlight: Retail bar in distinct colour — matches sector average (~50%)
- Insight: "Retail adoption matches the sector average — but 56% of retailers still haven't implemented AI. That implementation gap is exactly where Cleo can lead."

**Chart 2 — Adoption vs Full Implementation Gap (KPI callout)**
- 89% retailers using or testing AI
- 33% have fully implemented
- 56% gap = the opportunity
- Insight: "No single AI tool dominates retail SMEs. Cleo can choose on fit, not pressure."

---

### Section 2 — Retail Sales Evidence (Slide 4)

**Chart 3 — Monthly Revenue Trend (Line Chart)**
- X-axis: Month (1–12)
- Y-axis: Revenue (£K)
- Annotated: Peak £51K (Nov), Trough £29K (Feb)
- Insight: "A 76% peak-to-trough revenue swing means buyers are guessing every replenishment cycle. AI forecasting converts this seasonal pattern into a weekly, data-driven reorder plan."

**Chart 4 — Revenue by Product Category (Bar Chart)**
- Categories: Beauty, Clothing, Electronics
- Highlight: Clothing + Electronics = 69% of revenue
- Insight: "69% of revenue is concentrated in two categories — pilot AI forecasting here first."

**Chart 5 — Customer Age Distribution (Bar Chart)**
- Segments: 4 equal age bands
- 84% of customers across 4 segments
- Insight: "Four equal customer segments = a clear Phase 2 personalisation target once forecasting is stable."

---

### Section 3 — Hype vs Evidence (Slide 5)

**Chart 6 — Use Case Hype vs Evidence Scatter (Bubble Chart)**
- X-axis: Hype score (1–10)
- Y-axis: Evidence score (1–10)
- Bubble size: Estimated annual ROI (£)
- Points: Demand Forecasting, Customer Personalisation, AI Customer Service, Dynamic Pricing, Content AI, Autonomous Checkout
- Insight: "Inventory forecasting stands alone — high evidence, low hype, highest ROI. No other use case makes that case."

**Chart 7 — Estimated Annual ROI by Use Case (Horizontal Bar Chart)**
- Inventory Forecasting: £650K (highlighted)
- Customer Personalisation: £300K
- AI Customer Service: £240K
- Dynamic Pricing: £180K
- Content AI: £85K
- Reference line at £300K to show 2× gap
- Insight: "Demand forecasting delivers £650K — more than 2× the next best opportunity."

---

## Dashboard Design Principles

- **Single source of truth:** All numbers from documented public datasets or published benchmarks
- **Stakeholder-focused:** Every chart answers "should Cleo invest in AI, and where?"
- **No jargon:** Labels written for a CEO, not a data scientist
- **Evidence-first:** Hype scores shown alongside evidence scores so the CEO can see the contrast
- **Clear recommendation:** Dashboard ends with a decision — Inventory Forecasting is the start point

---

## Python Setup Notes

- Libraries: `pandas`, `matplotlib`, `seaborn`
- Input files: `data/raw/retail_sales_dataset.csv`, `data/raw/global_ai_tool_adoption.csv`
- Output: 7 charts rendered inline or exported as PNG for slide embedding
- Filtering applied to adoption dataset: `sector == 'Retail'` and `company_size == 'SME'`
- Monthly revenue calculated by aggregating `transaction_date` → month and summing `total_amount`
- All currency values in GBP (£); adoption rates as percentages
