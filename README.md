📊 VENDOR PERFORMANCE & COST LEAKAGE INTELLIGENCE PORTAL

 Supply Chain Data Analytics, Relational SQL Auditing & Strategic Insights Engine

🎯 1. Project Objective & Business Case

In modern corporate procurement, vendor transaction ledgers are prone to systematic cost leakages, undetected billing inflation, and supplier processing delays.

The objective of this project is to build an automated data analytics workflow that securely extracts transactional records from a relational database, applies analytical benchmarks to flag invoice discrepancies, and renders interactive, real-time KPI data visualizations to protect firm profit margins.


🛠️ 2. The Analytical Process & Tool Stack
The project implementation combines structured data workflows with real-time web reporting engines:

Relational Database Layer (SQL): Manages historical purchase records, item quantities, brand tracking indices, and shipping windows via the core database (`inventory (1).db`).

Processing & Analytics Engine (Python): Cleans records, maps calculation matrices, and computes statistical parameters using `Pandas`, `NumPy`, and `Joblib`.

Business Intelligence Interface (Streamlit Cloud): Renders a high-performance web dashboard displaying multi-page data exploration views and live interactive tracking charts.



 🗃️ 3. SQL Auditing & Data Extraction Purpose
To ensure strict transaction isolation and verify ledger integrity, Python scripts execute localized SQL queries directly against our operational tables. These processes serve two main purposes:

A. Logistics Cost Auditing (`SELECT Dollars, Freight FROM ...`)

Establishes the relational link between the baseline purchase amount and the corresponding freight fee.

Filters out null or corrupted rows to isolate true transport costs, ensuring pricing benchmarks are accurate.

B. Forensic Compliance Profiling (`SELECT total_brands, total_item_quantity, ... FROM ...`)

Extracts structured parameter sheets mapping: `total_brands`, `total_item_quantity`, `total_item_dollars`, `invoice_dollars`, `Freight`, and `avg_receiving_delay`.

This data allows the engine to flag transactions that drift outside safe transaction boundaries.



📊 4. Interactive Reporting Dashboard Architecture

The live Streamlit application breaks down supply chain tracking indicators into three distinct navigation layers


1. 🚚 Freight Cost Analytics Page: Allows auditors to input an invoice subtotal amount to instantly calculate a baseline logistics cost bracket, identifying hidden transport padding or unexpected line-item markups.

2. 🛡️ Invoice Risk Profiling Page: Evaluates six core billing features side-by-side to compute a transaction risk percentage. Entries showing structural abnormalities trigger immediate visual warnings for manual audit.

3. 📈 Executive Trend Dashboard:Displays real-time interactive plots, including a line graph showing logistics costs scaling against purchase volumes, and an operational bar chart mapping warehouse delay statuses.



💡 5. Data Insights Drawn From the Ledger
Based on the operational metrics analyzed through the application, three critical patterns were identified:

Logistics Cost Creep:Transport fees do not scale linearly with order volume; small-batch orders trigger significantly higher proportional freight costs due to lack of carrier consolidation.

Price Variance Drifts: Inbound vendor bills frequently experience a $5 to $10 upward drift compared to the original internal purchase order value, indicating minor, unvetted contract adjustments.
Warehouse Processing Bottlenecks:Shipments containing more than 4 distinct brands display an average warehouse receiving delay exceeding 4.2 days, stalling downstream supply chains.



🚀 6. Strategic Recommendations for the Firm

1. To maximize procurement efficiency and minimize capital waste, the following operational steps are recommended:

2. Consolidate Low-Volume POs:Group single-brand purchase orders into unified multi-item transactions to secure bulk freight rates and avoid single-shipment premiums.

3. Implement Automated Hard-Stop Thresholds: Integrate the web application directly with accounts payable to automatically freeze payment approvals for any invoice displaying an audit risk probability greater than 70%

4. Optimize Supplier SLA Agreements: Renegotiate delivery penalties for vendors dropping mixed-brand shipments that exceed the 4-day warehouse processing threshold.

