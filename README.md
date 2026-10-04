# Task 2: Data Visualization and Storytelling

## Overview
This project analyzes a two-year retail sales dataset and turns it into a business story using charts, KPIs, and recommendations. It follows the internship brief: choose appropriate charts, avoid clutter, highlight takeaways, add context, focus on business insights, and provide a summary.

**Data note:** `data.csv` is a reproducible synthetic practice dataset (1,200 orders from 2024–2025), not actual company data.

## Key findings
- Sales: $1,055,264.89
- Profit: $138,192.11
- Profit margin: 13.1%
- Leading category by sales: Technology
- Leading region by sales: West
- Largest segment by sales: Consumer
- Most profitable sub-category: Machines
- Lowest-profit sub-category: Paper

## Contents
- `data.csv`: dataset
- `report.pdf`: visual report, charts, insights, and recommendations
- `charts/`: chart images
- `src/analyze_sales.py`: reproducible analysis script
- `interview_questions.md`: answers to all seven interview questions

## Run
Install Python 3.10+, then run `pip install pandas matplotlib` and `python src/analyze_sales.py` from the project root.

## Method
Inspect data quality; aggregate sales/profit by month, category, region, segment, and sub-category; select line, bar, and pie charts based on analytical purpose; interpret results and recommend business actions.

## Limitation
Because the data is simulated, findings are for learning only and must not be presented as real retailer performance.
