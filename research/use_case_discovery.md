# Use Case Discovery — Mid-Market Retail
**Project 5 · Primary Use Case: AI Demand Forecasting & Inventory Optimisation**

---

## Stakeholder: Cleo, CEO of a Mid-Market Retail Company

**Decision constraints:**
- Worried about AI hype — needs evidence, not promises
- No vendor or internal data available yet — decision based on market research
- Budget cautious — mid-market means any wasted investment is visible on the P&L
- Competitive pressure — larger retailers and pure-play e-commerce are already ahead

**Pain points (assumed from sector research):**
- Seasonal overstock tying up cash (common for 51–250 employee retailers)
- Stockouts during peak periods causing lost sales
- Manual demand planning by buyers using spreadsheets
- Margin erosion from late markdowns and excess clearance stock

---

## Use Case Selected: AI Demand Forecasting & Inventory Optimisation

### Why this use case?
1. **Highest evidence of ROI** for mid-market retail in public research
2. **Directly addresses margin pressure** — the #1 CEO concern in retail
3. **Data-realistic** — works on POS/ERP sales history, no customer data platform needed
4. **Measurable in 3–6 months** — Cleo can see results before full commitment
5. **Vendor-accessible** — SaaS options at £500–£5,000/month, no enterprise contract required

### Why not personalisation first?
- Requires unified customer data platform (typically 6–12 months to build)
- Higher implementation risk for data-immature retailers
- Better as Phase 2 once inventory AI delivers ROI and builds internal AI confidence

### Why not chatbot first?
- Frequently oversold (80% cost reduction claims are unrealistic)
- High staff change management requirement
- Does not address Cleo's core margin and cash flow concerns

---

## Functional Unit (R) for the Diagnostic Tool
> R = one fully-diagnosed retail business — from intake to AI readiness report with retailer-specific recommendations

---

## Data Sources Justification

**Dataset 1: Retail Sales Dataset (Kaggle)**
- URL: https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset
- Contains: 1,000 transactions, date, customer, category, quantity, price, revenue (2023)
- Tableau use: Seasonal demand patterns, category performance, customer segmentation
- Relevance: Demonstrates the type of data that feeds an AI demand forecasting model

**Dataset 2: Global AI Tool Adoption Across Industries (Kaggle)**
- URL: https://www.kaggle.com/datasets/tfisthis/global-ai-tool-adoption-across-industries
- Contains: AI adoption rates, tool types, industries, demographics# Save cleo_dashboard.py to your project5/ folder
# Make sure ai_adoption.csv is at the path it expects, or update line 34:
# ai_raw = pd.read_csv('data/raw/ai_adoption_retail_filtered.csv')

python cleo_dashboard.py
# Output: cleo_ai_dashboard.pdf# Save cleo_dashboard.py to your project5/ folder
# Make sure ai_adoption.csv is at the path it expects, or update line 34:
# ai_raw = pd.read_csv('data/raw/ai_adoption_retail_filtered.csv')

python cleo_dashboard.py
# Output: cleo_ai_dashboard.pdf
# Output: cleo_ai_dashboard.pdf
- Tableau use: Retail vs other sectors adoption benchmarks, hype vs value signal
- Relevance: Shows Cleo where retail stands on the AI adoption curve
