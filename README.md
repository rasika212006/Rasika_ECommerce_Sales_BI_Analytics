# E-Commerce Sales & Business Intelligence Analytics with AI

**AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 Submission Project**  
**Host Organization:** BharatCares  
**Student / Author:** Rasika  
**GitHub Username:** [rasika212006](https://github.com/rasika212006)  
**GitHub Repository:** [https://github.com/rasika212006/Rasika_ECommerce_Sales_BI_Analytics](https://github.com/rasika212006/Rasika_ECommerce_Sales_BI_Analytics)  
**Project Domain:** E-Commerce Business Intelligence & Executive Decision Support  

---

## 1. Project Overview
This project presents an end-to-end, data-driven Business Intelligence (BI) and Executive Decision Support system for an e-commerce retail enterprise. Built strictly according to the analytical concepts taught in the IBM SkillsBuild Data Analytics with AI internship sessions, this repository transforms raw sales transaction logs into verified financial KPIs, diagnostic visual charts, risk evaluations, and executive recommendations.

The project follows the complete 10-stage analytical pipeline:
```
Raw Data -> Data Cleaning -> Exploratory Data Analysis (EDA) -> Business KPIs -> Trends -> Drivers -> Risks -> Opportunities -> Recommended Actions -> Executive Decision Support
```

---

## 2. Business Problem
Modern e-commerce enterprises face key operational hurdles that erode profitability:
1. **Uncontrolled Promotional Discounting:** Sales representatives frequently grant deep discounts (>20%) without knowing the threshold where gross profit turns into direct net loss.
2. **Hidden Product Loss Leaders:** High top-line sales figures mask severe net financial losses in specific sub-categories like Tables and Bookcases.
3. **Geographic Margin Disparities:** Uniform promotional policies perform poorly across states with high operational or freight overheads (e.g., Texas, Ohio, Pennsylvania).
4. **Executive Data Overload:** Leadership receives raw data dumps rather than structured, actionable executive intelligence.

---

## 3. Objectives
- **Process & Clean:** Standardize transaction schemas, convert datetime fields, handle missing values, and engineer financial features (`Profit Margin %`, `Shipping Days`, `Discount Bracket`).
- **Quantify Core KPIs:** Compute verified business metrics including Total Sales ($2.30M), Total Profit ($286.40k), Total Orders (5,009), Total Customers (793), Average Order Value ($458.61), and Profit Margin (12.47%).
- **Diagnose Performance:** Analyze sales and profit distribution across Categories, Sub-Categories, Customer Segments, and Regions.
- **Isolate Risk Drivers:** Quantify the exact financial impact of discount levels and identify severe loss-making states.
- **Formulate Management Guardrails:** Apply the **FACT -> INSIGHT -> RISK/OPPORTUNITY -> ACTION** framework.
- **AI Decision Support:** Demonstrate how AI tools (IBM AI / Gemini) can be integrated as executive assistants using verified metric payloads.

---

## 4. Dataset Information
- **Dataset Name:** Sample Superstore Sales Dataset
- **Primary Source URL:** [https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv](https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv)
- **Local File Path:** `data/Sample_Superstore.csv` (and `data/Sample - Superstore.csv`)
- **Dataset Size:** 9,994 transactional records across 21 columns
- **Features Included:** `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`.

---

## 5. Technologies Used
- **Programming Language:** Python 3.10
- **Data Manipulation & Analysis:** `pandas`, `numpy`
- **Data Visualization & Dashboards:** `matplotlib`, `seaborn`
- **Notebook & Environment:** Jupyter Notebook (`nbformat`, `ipykernel`)
- **Document Generation:** `python-docx` (Word report automation)
- **Spreadsheet / Utility:** `openpyxl`

---

## 6. Project Structure
```text
Rasika_ECommerce_Sales_BI_Analytics/
│
├── data/
│   ├── Sample_Superstore.csv                  # Verified CSV dataset
│   └── Sample - Superstore.csv                 # Dataset mirror copy
│
├── outputs/
│   └── charts/                                # Generated dashboard PNG visualizations
│       ├── kpi_summary_cards.png
│       ├── monthly_sales_trend.png
│       ├── category_performance.png
│       ├── sub_category_profitability.png
│       ├── discount_vs_profit.png
│       ├── top_bottom_states.png
│       └── executive_dashboard.png
│
├── Rasika_ECommerce_Sales_BI_Analytics.ipynb   # Complete executable Jupyter Notebook
├── requirements.txt                            # Required Python dependencies
├── README.md                                   # Project documentation and summary
└── Rasika_ECommerce_Sales_BI_Analytics_ProjectReport.docx # Official Word Project Report
```

---

## 7. Key Business KPIs (Verified Data)

| Metric | Verified Value | Analytical Definition |
| :--- | :--- | :--- |
| **Total Revenue / Sales** | **$2,297,200.86** | Cumulative transaction revenue across all orders |
| **Total Net Profit** | **$286,397.02** | Net corporate earnings after costs and discounts |
| **Total Orders** | **5,009** | Unique transactional orders processed |
| **Total Unique Customers** | **793** | Total distinct B2B and consumer accounts |
| **Total Units Sold** | **37,873** | Total physical quantity of products shipped |
| **Average Order Value (AOV)** | **$458.61** | Revenue per unique order (`Total Sales / Total Orders`) |
| **Overall Profit Margin** | **12.47%** | Net profit percentage (`Total Profit / Total Sales`) |
| **Average Discount Rate** | **15.62%** | Mean promotional discount applied across line items |

---

## 8. Key Findings (FACT -> INSIGHT -> RISK/OPPORTUNITY -> ACTION)

### Finding 1: Uncontrolled Discounting Destroys Net Profitability
- **FACT:** Transactions with 0% discount yield a **+29.51% profit margin** ($320.99k profit). Discounts of 21–50% yield **-19.70% margin** (-$58.82k loss), and discounts >50% produce **-119.20% margin** (-$76.56k loss).
- **INSIGHT:** Discounts exceeding 20% severely erode unit economics, turning revenue into net financial losses.
- **RISK:** Sales reps use deep discounting to hit top-line quotas at the expense of company net profit.
- **ACTION:** Implement automated system guardrails capping rep discounts at 15%, requiring VP sign-off for 15–20%, and prohibiting discounts >20%.

### Finding 2: Tables Sub-Category is a Major Financial Loss Leader
- **FACT:** The **Tables** sub-category generated $206,965.53 in sales but suffered a **net loss of -$17,725.48** (-8.56% margin) with an average discount of 26.13%.
- **INSIGHT:** Heavy discounting combined with high freight costs makes Tables unviable under current list prices.
- **RISK:** Scaling sales of Tables under current terms increases corporate losses.
- **ACTION:** Increase base retail prices for Tables by 10% and cap Table discounts at 10%.

### Finding 3: Severe Loss-Making States (Texas, Ohio, Pennsylvania, Illinois)
- **FACT:** Texas (-$25,729.36 profit, 37.02% avg discount) and Ohio (-$16,971.38 profit, 32.49% avg discount) represent the worst loss-making states.
- **INSIGHT:** Central/East region sales teams rely excessively on promotional discounts to compete.
- **RISK:** Uncontrolled state discounting causes over $75,000 in annual profit leakage.
- **ACTION:** Conduct state-level pricing audits in Texas and Ohio, remove universal promo codes, and enforce margin-aligned regional pricing.

### Finding 4: Technology & Office Supplies are High Profit Engines
- **FACT:** Technology generated **$145,454.95 profit (17.40% margin)** and Office Supplies generated **$122,490.80 profit (17.04% margin)**. Copiers achieved a **37.20% profit margin**.
- **INSIGHT:** Hardware and consumable supplies represent stable, high-margin revenue drivers.
- **OPPORTUNITY:** Cross-selling high-margin consumables alongside hardware purchases boosts basket profitability.
- **ACTION:** Reallocate 60% of digital marketing budget to Copiers, Phones, Paper, and Accessories.

---

## 9. AI-Assisted Executive Analysis
Generative AI tools (such as IBM AI / Gemini) can assist executives by synthesizing verified metrics into concise briefings.

### Prompt Template Used:
```text
PROMPT:
Using the following verified e-commerce business metrics, generate an executive summary detailing financial performance, top 3 risks, top 3 opportunities, and 4 actionable management recommendations:
{
  "total_revenue": "$2,297,200.86",
  "total_profit": "$286,397.02",
  "profit_margin": "12.47%",
  "loss_subcategories": ["Tables (-$17.7k)", "Bookcases (-$3.47k)"],
  "loss_states": ["Texas (-$25.7k)", "Ohio (-$16.9k)"],
  "discount_impact": {"0%": "+29.5%", "21-50%": "-19.7%", ">50%": "-119.2%"}
}
```

> **Human-in-the-Loop Rule:** All AI-generated insights must be cross-checked against verified dashboard metrics before executive policy implementation.

---

## 10. Setup and Run Instructions

### Prerequisites
- Python 3.10 or higher installed.
- Jupyter Notebook environment.

### Installation & Execution
1. **Clone Repository:**
   ```bash
   git clone https://github.com/rasika212006/Rasika_ECommerce_Sales_BI_Analytics.git
   cd Rasika_ECommerce_Sales_BI_Analytics
   ```
2. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Jupyter Notebook:**
   ```bash
   jupyter notebook Rasika_ECommerce_Sales_BI_Analytics.ipynb
   ```
4. **Execute Cells in Order:** Run all cells sequentially from top to bottom.

---

## 11. Conclusion
This project demonstrates how structured Business Intelligence analytics converts raw sales data into high-value decision support. By implementing discount caps (<=20%), repricing loss-leader categories (Tables), and targeting high-margin categories (Technology), management can recover over **$100,000 in lost profit** and lift net corporate margins from **12.47% to 18%+**.

---
*Created for AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 Submission by Rasika (GitHub: rasika212006).*
