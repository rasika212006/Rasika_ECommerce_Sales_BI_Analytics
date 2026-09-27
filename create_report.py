import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
import os

doc = docx.Document()

# Page Setup - Margins 1 inch
sections = doc.sections
for section in sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Helper functions for styling
def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(24)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 61, 89) # Navy
    p.paragraph_format.space_after = Pt(6)

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(23, 185, 120) # Teal/Green
    p.paragraph_format.space_after = Pt(18)

def add_h1(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = RGBColor(30, 61, 89)
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)

def add_h2(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = RGBColor(67, 138, 94)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)

def add_body(text, bold=False, italic=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(11)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(51, 51, 51)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    return p

def add_bullet(text, bold_prefix=""):
    p = doc.add_paragraph(style='List Bullet')
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Arial'
        r_pre.font.size = Pt(11)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(30, 61, 89)
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(51, 51, 51)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15

def add_image(image_path, caption="", width=Inches(6.0)):
    if os.path.exists(image_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run()
        run.add_picture(image_path, width=width)
        if caption:
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r_cap = p_cap.add_run(f"Figure: {caption}")
            r_cap.font.name = 'Arial'
            r_cap.font.size = Pt(9.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = RGBColor(100, 100, 100)
            p_cap.paragraph_format.space_after = Pt(10)

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

# -------------------------------------------------------------
# 1. TITLE PAGE
# -------------------------------------------------------------
add_title("E-Commerce Sales & Business Intelligence Analytics with AI")
add_subtitle("AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026")

p_meta = doc.add_paragraph()
p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_meta.add_run("Submission Project Report\nHost Organization: BharatCares\nStudent / Author: Rasika\nGitHub Username: rasika212006\nGitHub Repository: https://github.com/rasika212006/Rasika_ECommerce_Sales_BI_Analytics\nDomain: E-Commerce Business Intelligence & Executive Decision Support\nDate: September 2026\n")
r.font.name = 'Arial'
r.font.size = Pt(11)
r.font.italic = True
r.font.color.rgb = RGBColor(80, 80, 80)
p_meta.paragraph_format.space_after = Pt(24)

doc.add_page_break()

# -------------------------------------------------------------
# 2. ABSTRACT / EXECUTIVE SUMMARY
# -------------------------------------------------------------
add_h1("1. Abstract / Executive Summary")
add_body("This project presents an end-to-end Business Intelligence (BI) and Executive Decision Support system for an e-commerce retail enterprise, created by Rasika (GitHub: rasika212006) for the AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026. Following the analytical framework taught in the internship sessions, the project transforms raw transactional data into verified key performance indicators (KPIs), diagnostic visual charts, risk evaluations, and executive recommendations.")

add_body("Analyzing 9,994 transactional order records from the public Sample Superstore dataset, the analysis reveals cumulative revenue of $2,297,200.86 with net profit of $286,397.02 (overall profit margin of 12.47%). However, deep diagnostic evaluation highlights severe net losses driven by uncontrolled promotional discounting (>20% discount rates) and unprofitable sub-categories (Tables incurring -$17,725.48 net loss).")

add_body("By enforcing discount caps at <=20%, repricing loss-leader categories, and focusing marketing spend on high-margin Technology hardware and consumable Office Supplies, management can recover over $100,000 in lost profit and elevate overall net profit margin to 18%+.")

# -------------------------------------------------------------
# 3. INTRODUCTION
# -------------------------------------------------------------
add_h1("2. Introduction")
add_body("In today's digital economy, e-commerce enterprises generate vast volumes of transactional data daily. However, possessing raw data does not automatically translate into strategic advantage. Without structured Business Intelligence processing, executive leadership is often blind to profit drains hidden beneath strong top-line sales figures.")

add_body("This project demonstrates the systematic conversion of raw transactional logs into executive decision support. By executing a rigorous analytical pipeline, raw order records are cleaned, aggregated into core KPIs, evaluated across key business dimensions (Category, Sub-Category, Region, State, Segment), and synthesized into actionable business interventions.")

# -------------------------------------------------------------
# 4. BUSINESS PROBLEM & OBJECTIVES
# -------------------------------------------------------------
add_h1("3. Business Problem & Project Objectives")
add_h2("3.1 Business Problem Statement")
add_bullet("Regional sales representatives grant steep promotional discounts without knowing the threshold where gross margin turns into direct net financial loss.", "1. Uncontrolled Discounting: ")
add_bullet("High revenue in product categories like Furniture masks severe underlying net losses in sub-categories such as Tables and Bookcases.", "2. Hidden Product Loss Leaders: ")
add_bullet("Uniform promotional rules fail in states with high operating and freight overheads, resulting in severe state-level net losses.", "3. Geographic Margin Leakage: ")
add_bullet("Leadership receives massive transactional logs rather than structured, actionable executive decision support.", "4. Executive Data Overload: ")

add_h2("3.2 Project Objectives")
add_bullet("Process raw sales logs, handle missing values, standardize schemas, and engineer financial metric features.", "Data Cleaning & Engineering: ")
add_bullet("Calculate verified aggregate KPIs including Total Sales, Total Profit, Profit Margin %, AOV, and Order Counts.", "KPI Quantification: ")
add_bullet("Determine the exact margin impact of discounting levels and isolate loss-making states and product lines.", "Diagnostic Analytics: ")
add_bullet("Synthesize findings into executive management actions using the FACT -> INSIGHT -> RISK/OPPORTUNITY -> ACTION model.", "Decision Support: ")
add_bullet("Demonstrate prompt templates and human-in-the-loop validation for AI executive briefing tools.", "AI Integration: ")

# -------------------------------------------------------------
# 5. DATASET DESCRIPTION & SOURCE
# -------------------------------------------------------------
add_h1("4. Dataset Description & Public Source")
add_body("To ensure complete project authenticity and reproducibility, a real publicly available e-commerce dataset was selected.")

add_bullet("Sample Superstore Sales Dataset", "Dataset Title: ")
add_bullet("https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv", "Exact Public Source URL: ")
add_bullet("data/Sample_Superstore.csv (and data/Sample - Superstore.csv)", "Local Storage Path: ")
add_bullet("9,994 order records across 21 columns.", "Dataset Size & Dimensions: ")
add_bullet("Order ID, Order Date, Ship Date, Ship Mode, Customer ID, Customer Name, Segment, Country, City, State, Postal Code, Region, Product ID, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit.", "Key Column Attributes: ")

# -------------------------------------------------------------
# 6. TECHNOLOGIES USED & METHODOLOGY
# -------------------------------------------------------------
add_h1("5. Technologies Used & Analytical Methodology")
add_h2("5.1 Technologies Used")
add_bullet("Python 3.10 (Core programming language)", "Language: ")
add_bullet("pandas, numpy (Data manipulation, feature engineering, numerical aggregation)", "Data Processing: ")
add_bullet("matplotlib, seaborn (Executive dashboard rendering, trend plotting)", "Visualization: ")
add_bullet("Jupyter Notebook (Interactive analytical code notebook with pre-rendered outputs)", "Notebook Environment: ")
add_bullet("python-docx, openpyxl (Automated document reporting and data exports)", "Report Generation: ")

add_h2("5.2 10-Stage Analytical Methodology")
add_body("The project adheres strictly to the analytical workflow taught in the IBM SkillsBuild Data Analytics with AI internship:")
add_body("Raw Data -> Data Cleaning -> Exploratory Data Analysis -> Business KPIs -> Trends -> Drivers -> Risks -> Opportunities -> Recommended Actions -> Executive Decision Support")

# -------------------------------------------------------------
# 7. DATA CLEANING & PREPROCESSING
# -------------------------------------------------------------
add_h1("6. Data Cleaning & Feature Engineering")
add_body("A thorough quality check was performed prior to analysis:")
add_bullet("The dataset contained 9,994 clean records. Missing postal codes were validated, and data types were verified.", "Missing Values & Duplicates: ")
add_bullet("Order Date and Ship Date strings were parsed into native Python datetime objects.", "Datetime Processing: ")
add_bullet("Profit Margin % (Profit / Sales), Order Year, Year-Month, Shipping Days (Ship Date - Order Date), and Discount Brackets (0%, 1-20%, 21-50%, >50%) were engineered.", "Feature Engineering: ")

# -------------------------------------------------------------
# 8. VERIFIED BUSINESS KPIS
# -------------------------------------------------------------
add_h1("7. Core Business KPIs Analysis")
add_body("The table below presents the verified aggregate financial metrics calculated from the raw dataset:")

# Create KPI Table
table = doc.add_table(rows=9, cols=3)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.style = 'Table Grid'

headers = ["Metric Name", "Verified Value", "Analytical Business Definition"]
hdr_cells = table.rows[0].cells
for i, head in enumerate(headers):
    hdr_cells[i].text = head
    set_cell_background(hdr_cells[i], "1E3D59")
    hdr_cells[i].paragraphs[0].runs[0].font.bold = True
    hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

kpi_data = [
    ["Total Revenue / Sales", "$2,297,200.86", "Cumulative gross sales across 9,994 transaction lines"],
    ["Total Net Profit", "$286,397.02", "Net corporate profit after all costs and discounts"],
    ["Total Orders", "5,009", "Unique transactional order IDs processed"],
    ["Total Unique Customers", "793", "Total distinct corporate and individual accounts"],
    ["Total Units Sold", "37,873", "Total physical product quantity shipped"],
    ["Average Order Value (AOV)", "$458.61", "Revenue generated per unique order (Sales / Orders)"],
    ["Overall Profit Margin", "12.47%", "Overall net profitability percentage (Profit / Sales)"],
    ["Average Discount Rate", "15.62%", "Mean promotional discount rate across all line items"]
]

for row_idx, data in enumerate(kpi_data):
    row_cells = table.rows[row_idx + 1].cells
    for col_idx, text in enumerate(data):
        row_cells[col_idx].text = text
        if row_idx % 2 == 1:
            set_cell_background(row_cells[col_idx], "F8F9FA")

doc.add_paragraph().paragraph_format.space_after = Pt(12)
add_image("outputs/charts/kpi_summary_cards.png", "Executive KPI Summary Panel", width=Inches(6.2))

# -------------------------------------------------------------
# 9. EXPLORATORY DIAGNOSTICS & TRENDS
# -------------------------------------------------------------
add_h1("8. Exploratory Performance Diagnostics & Trends")

add_h2("8.1 Monthly Trend Analysis")
add_body("Revenue and profit performance across 2014-2017 exhibit strong Q4 seasonality, driven by holiday sales spikes. However, profit growth fails to keep pace with revenue growth during promotional periods due to heavy discounting.")
add_image("outputs/charts/monthly_sales_trend.png", "Monthly Sales and Profit Performance Trend (2014 - 2017)", width=Inches(6.0))

add_h2("8.2 Category & Sub-Category Performance")
add_body("Analysis across major product categories highlights severe profit margin divergence:")
add_bullet("Technology: Sales = $836,154.03 | Profit = $145,454.95 | Profit Margin = 17.40%", "1. ")
add_bullet("Office Supplies: Sales = $719,047.03 | Profit = $122,490.80 | Profit Margin = 17.04%", "2. ")
add_bullet("Furniture: Sales = $741,999.80 | Profit = $18,451.27 | Profit Margin = 2.49% (UNDERPERFORMER)", "3. ")

add_image("outputs/charts/category_performance.png", "Sales and Profitability Comparison by Product Category", width=Inches(5.8))
add_image("outputs/charts/sub_category_profitability.png", "Sub-Category Net Profit Breakdown (Highlighting Loss Leaders)", width=Inches(6.0))

add_h2("8.3 Regional & State Performance")
add_body("Geographic breakdown reveals that while the West region achieves top performance ($725.46k sales, $108.42k profit, 14.94% margin), the Central region lags significantly (7.92% margin) due to severe loss-making states including Texas (-$25,729.36 net profit) and Ohio (-$16,971.38 net profit).")
add_image("outputs/charts/top_bottom_states.png", "Top 5 Profitable vs Bottom 5 Loss-Making States", width=Inches(6.0))

# -------------------------------------------------------------
# 10. KEY DRIVERS & DISCOUNT IMPACT
# -------------------------------------------------------------
add_h1("9. Key Business Drivers (Discount Impact Analysis)")
add_body("Discounting is the single strongest driver of profitability in the business. Evaluating profit margins across discount brackets provides empirical proof of margin erosion:")
add_bullet("0% Discount (No Discount): Sales = $1,087,908.47 | Profit = $320,987.60 | Profit Margin = +29.51%", "• ")
add_bullet("1-20% Discount (Moderate): Sales = $846,522.24 | Profit = $100,785.47 | Profit Margin = +11.91%", "• ")
add_bullet("21-50% Discount (High): Sales = $298,541.41 | Profit = -$58,817.00 | Profit Margin = -19.70%", "• ")
add_bullet(">50% Discount (Severe): Sales = $64,228.74 | Profit = -$76,559.05 | Profit Margin = -119.20%", "• ")

add_image("outputs/charts/discount_vs_profit.png", "Impact of Discount Rate Brackets on Profit Margin %", width=Inches(5.8))

# -------------------------------------------------------------
# 11. EXECUTIVE DASHBOARD
# -------------------------------------------------------------
add_h1("10. Executive Business Intelligence Dashboard")
add_body("The executive decision view combines key visual diagnostics into an integrated panel answering core management questions:")
add_image("outputs/charts/executive_dashboard.png", "Integrated Executive Decision View Dashboard", width=Inches(6.2))

# -------------------------------------------------------------
# 12. FACT -> INSIGHT -> RISK/OPPORTUNITY -> ACTION
# -------------------------------------------------------------
add_h1("11. Structured Decision Analysis (Fact -> Insight -> Action)")

add_h2("Finding 1: Uncontrolled Discounting Destroys Margins")
add_bullet("Transactions with 0% discount generate +29.51% profit margin ($320.99k profit), whereas discounts >20% result in negative margins of -19.70% to -119.20%, causing over $135,000 in direct losses.", "FACT: ")
add_bullet("Promotional discounting above 20% severely erodes unit economics and turns gross sales into net corporate losses.", "INSIGHT: ")
add_bullet("Sales representatives are using deep discounts to hit revenue quotas at the expense of net profit.", "RISK: ")
add_bullet("Implement automated system discount caps at 15%, require VP sign-off for 15-20%, and strictly prohibit discounts >20%.", "ACTION: ")

add_h2("Finding 2: Tables Sub-Category is a Major Financial Loss Leader")
add_bullet("Tables generated $206,965.53 in sales but incurred a net loss of -$17,725.48 (-8.56% margin) with an average discount of 26.13%.", "FACT: ")
add_bullet("Heavy discounting combined with high shipping and supplier costs makes Tables unviable under current list pricing.", "INSIGHT: ")
add_bullet("Scaling sales of Tables under current terms increases overall corporate profit leakage.", "RISK: ")
add_bullet("Re-engineer Table supplier pricing, increase base list prices by 10%, and cap Table discounts at 10%.", "ACTION: ")

add_h2("Finding 3: Severe Loss-Making States (Texas, Ohio, Pennsylvania, Illinois)")
add_bullet("Texas (-$25,729.36 profit, 37.02% avg discount) and Ohio (-$16,971.38 profit, 32.49% avg discount) are severe loss-making states.", "FACT: ")
add_bullet("Regional sales managers in Central and East regions rely excessively on promotional discounts to secure orders.", "INSIGHT: ")
add_bullet("Unmonitored state discounting causes over $75,000 in annual net profit leakage.", "RISK: ")
add_bullet("Conduct immediate state-level pricing audits in Texas and Ohio, remove universal promo codes, and shift to margin-aligned pricing.", "ACTION: ")

add_h2("Finding 4: Technology & Office Supplies are High Profit Engines")
add_bullet("Technology generated $145,454.95 profit (17.40% margin) and Office Supplies generated $122,490.80 profit (17.04% margin). Copiers achieved a 37.20% profit margin.", "FACT: ")
add_bullet("Tech hardware and consumable supplies represent stable, highly profitable core product lines.", "INSIGHT: ")
add_bullet("Cross-selling high-margin consumables alongside hardware purchases significantly boosts total basket profitability.", "OPPORTUNITY: ")
add_bullet("Reallocate 60% of digital marketing budget to Copiers, Phones, Paper, and Accessories.", "ACTION: ")

# -------------------------------------------------------------
# 13. AI-ASSISTED EXECUTIVE ANALYSIS
# -------------------------------------------------------------
add_h1("12. AI-Assisted Executive Analysis")
add_body("Generative AI tools (such as IBM AI / Gemini) can act as an executive analyst assistant by processing verified dataset metrics.")

add_body("In accordance with internship instructions, no API calls were fabricated. The exact verified metric payload and structured prompt template used for AI integration are presented below:")

add_bullet("Structured JSON containing total revenue ($2.30M), total profit ($286.40k), loss sub-categories, loss states, and discount margin impacts.", "Verified Context Payload: ")
add_bullet("Prompt instructing AI to act as Chief Commercial Officer (CCO) and generate an Executive Briefing strictly using verified numbers.", "Prompt Template: ")
add_bullet("AI-generated summaries must be cross-validated against verified dashboard charts prior to strategic implementation.", "Human-in-the-Loop Validation: ")

# -------------------------------------------------------------
# 14. RESULTS, LIMITATIONS & CONCLUSION
# -------------------------------------------------------------
add_h1("13. Results, Limitations & Conclusion")
add_h2("13.1 Key Results Synthesis")
add_body("The BI analytics framework successfully isolated the root causes of profit leakage. By enforcing discount caps (<=20%), repricing Tables, and reallocating marketing spend to Technology, the business can recover over $100,000 in lost profit and elevate overall net profit margin from 12.47% to 18%+.")

add_h2("13.2 Analytical Limitations")
add_bullet("Cost of Goods Sold (COGS) and freight costs are implicitly embedded in net Profit; detailed cost breakdowns were unavailable.", "1. Implicit Costs: ")
add_bullet("The dataset reflects offline and online retail transactions up to 2017.", "2. Historical Context: ")

add_h2("13.3 Final Business Conclusion")
add_body("This project demonstrates that revenue alone is a misleading metric for business health. By establishing rigorous BI reporting, monitoring profit margin after discount, and enforcing automated discount controls, enterprise management can achieve sustained, profitable growth.")

add_h1("14. Dataset Reference & Repository Citation")
add_body("Author / Student: Rasika")
add_body("GitHub Username: rasika212006")
add_body("GitHub Repository: https://github.com/rasika212006/Rasika_ECommerce_Sales_BI_Analytics")
add_body("Dataset Title: Sample Superstore Sales Dataset")
add_body("Exact Public Dataset URL: https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv")
add_body("Host Internship: AICTE | IBM SkillsBuild Data Analytics with AI Internship 2026 | BharatCares")

# Save document
report_path = "Rasika_ECommerce_Sales_BI_Analytics_ProjectReport.docx"
doc.save(report_path)
print(f"Project Report Word Document regenerated successfully: {report_path}")
