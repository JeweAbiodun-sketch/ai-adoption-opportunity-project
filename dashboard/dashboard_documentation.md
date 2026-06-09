# Dashboard Documentation — Retail AI Adoption Evidence
**Tool: Tableau · File: retail_ai_dashboard.twbx**

---

## Dashboard Purpose
This dashboard is the evidence layer for Cleo's meeting. It answers one question:
**"Where does market data show AI adoption is worth exploring for mid-market retail?"**

It is a communication layer (not an analysis layer) — designed for a non-technical CEO.

---

## Data Sources
1. `data/processed/retail_sales_cleaned.csv` — transaction-level retail data
2. `data/processed/ai_adoption_retail_filtered.csv` — AI adoption by industry

---

## Dashboard Views (Recommended 3-sheet structure in Tableau)

### Sheet 1 — "The Retail AI Opportunity" (KPI overview)
**Metrics to display:**
- 89% retailers using/testing AI (big number callout)
- 33% fully implemented (contrast callout — the gap IS the opportunity)
- $18.4B global retail AI market size
- $3.50 return per $1 in AI customer service
- 10–20% average inventory cost reduction

**Chart types:** Big number KPI tiles, simple bar showing adoption vs implementation gap

### Sheet 2 — "Your Sales Data: Why AI Would Help" (from Kaggle dataset)
**Metrics to display:**
- Monthly revenue trend (line chart — show seasonality)
- Revenue by product category (bar chart — shows where demand concentration is)
- Quantity sold vs revenue by category (scatter — shows margin variability)
- Customer age distribution (bar — shows segmentation opportunity)

**Insight to communicate:** "This is the pattern of data your business generates. AI demand forecasting reads exactly this pattern to predict what to stock and when."

### Sheet 3 — "Hype vs Evidence" (adoption context)
**Metrics to display:**
- AI adoption rate by industry (bar — show retail vs other sectors)
- AI use case by evidence tier (colour-coded table: green/amber/red)
- Recommended use case timeline (Gantt or milestone chart)

**Insight to communicate:** "Not all AI is equal. This shows where the evidence is strong and where Cleo should be cautious."

---

## Dashboard Design Principles Applied
- **Single source of truth:** All numbers from documented public sources
- **Stakeholder-focused:** Every metric answers "should Cleo invest?"
- **No jargon:** Labels written for a CEO, not a data scientist
- **Clear recommendation:** Dashboard ends with a decision — invest, wait, or pilot

---

## Tableau Setup Instructions
1. Open Tableau Desktop
2. Connect to `data/processed/retail_sales_cleaned.csv`
3. Create calculated fields: Month (from Date), Revenue per Customer
4. Build Sheet 1 → Sheet 2 → Sheet 3 as described above
5. Create a Dashboard combining all three sheets
6. Add a title: "AI Adoption Evidence — Mid-Market Retail"
7. Export as `.twbx` packaged workbook
