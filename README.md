# AI Adoption Opportunity Project
**AI Consulting and Integration Bootcamp, Module 5**

This project explores an AI adoption opportunity for a mid-market retail company with 51 to 250 employees. The objective is to move from generic AI hype to a practical, evidence-backed recommendation that can be presented to leadership.

## Project Overview

The scenario centers on Cleo, the CEO of a mid-market retail business. She is interested in AI but cautious about inflated vendor promises. This project prepares the research, analysis, dashboard, and implementation proposal needed for a confident decision-making meeting.

**Company profile**
- Sector: Retail
- Size: 100 to 120 employees
- Primary use case: AI-powered demand forecasting and inventory optimization

## Proposed Solution

The `ai_diagnostic_tool.html` file is the working prototype for the proposed solution. It is included in this project because it captures the end-to-end consulting methodology in an interactive form, not just the final recommendation.

It demonstrates:
- An interactive AI readiness diagnostic for a mid-market retail business
- A 5-stage maturity model and readiness layer framework for evaluating data, people, and process readiness
- Evidence-based opportunity recommendations tailored to retail demand forecasting and inventory optimisation
- A way to translate qualitative business constraints into quantitative AI fit scores
- A user-facing deliverable that a CEO like Cleo can use to justify the decision and share with stakeholders

This prototype is therefore part of the project’s value proposition: it is the tangible product that turns research, data, and analysis into a decision-ready recommendation.

## Repository Structure

```text
.
|-- .env
|-- .gitignore
|-- ai_diagnostic_tool.html
|-- cleo_dashboard.py
|-- data_prep.py
|-- data/
|   |-- raw/
|   `-- processed/
|-- dashboard/
|   |-- cleo_ai_dashboard.pdf
|   |-- retail_ai_dashboard.twb
|   `-- dashboard_documentation.md
|-- cost_estimation/
|   |-- cost_analysis.md
|   `-- timeline_estimate.md
|-- implementation/
|   |-- solution_proposal.md
|   `-- implementation_plan.md
|-- research/
|   |-- market_research.md
|   |-- opportunities_risks.md
|   `-- use_case_discovery.md
|-- package.json
|-- package-lock.json
|-- requirements.txt
|-- server.js
`-- README.md
```

## Key Deliverables

- Market research and supporting evidence
- Opportunity and risk analysis
- Use case discovery and recommendation
- Tableau dashboard and supporting documentation
- Implementation proposal and rollout plan
- Cost estimate and timeline
- Working diagnostic prototype

## Datasets

### 1. Retail Sales Dataset
- Source: Kaggle, Retail Sales Dataset by `mohammadtalib786`
- Purpose: Transaction-level retail data used to explore demand patterns, seasonality, and segmentation opportunities
- Application: Sales trends, category performance, customer segmentation, and inventory planning

### 2. Global AI Tool Adoption Across Industries
- Source: Kaggle, Global AI Tool Adoption by `tfisthis`
- Purpose: Industry-level adoption context used to benchmark retail and separate hype from value
- Application: Adoption comparison, trend framing, and opportunity prioritisation

## Getting Started

### Prerequisites
- Node.js
- Python 3.x

### Install Dependencies

```bash
pip install -r requirements.txt
npm install
```

### Run the Diagnostic Tool

```bash
npm start
```

Then open:

```text
http://localhost:3000/ai_diagnostic_tool.html
```

### Tableau Dashboard

Open `dashboard/retail_ai_dashboard.twb` in Tableau and connect to `data/processed/retail_sales_cleaned.csv` if needed.

## Project Checklist

- [x] Sector research and data gathering
- [x] Opportunity and risk mapping
- [x] Use case discovery and recommendation
- [x] Hype vs evidence analysis
- [x] Tableau dashboard
- [x] Dashboard documentation
- [x] Solution proposal
- [x] Implementation plan
- [x] Cost analysis
- [x] Timeline estimate
- [x] Working prototype

## Sources

- McKinsey, State of AI 2024
- Stanford, AI Index 2024
- Ringly.io, AI in Retail Statistics 2026
- Grand View Research, AI in Retail Market Report
- Kaggle, Retail Sales Dataset by `mohammadtalib786`
- Kaggle, Global AI Tool Adoption by `tfisthis`

## Notes

- The project emphasizes practical adoption rather than speculative AI claims.
- The recommendation is designed for a mid-market retail environment with limited resources and a need for measurable impact.
