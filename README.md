# Marketing Analytics Pipeline (Bank Telemarketing Data)

This project builds a complete end-to-end **marketing analytics data pipeline** using the Portuguese Bank Telemarketing Dataset.  
It transforms raw marketing call records into clean **dimensional warehouse tables**, performs **business analytics using SQL**, validates data quality with **pytest**, and orchestrates everything using an **Airflow DAG**.

---

## 📌 Project Goals

- Ingest raw bank marketing campaign data (train/test CSVs)
- Clean and standardize customer and campaign fields
- Build a **star schema** with fact and dimension tables
- Compute key marketing KPIs:
  - conversion rate
  - conversion by job/age/month
  - call-duration effectiveness
  - previous campaign outcome impact
- Add **data quality tests** for warehouse tables
- Add **Airflow DAG** to orchestrate Bronze → Silver/Gold pipeline

---

## 🧱 Architecture (Bronze → Silver → Gold)

```text
Raw (CSV)
↓
Bronze Layer (Standardized CSV)
↓
Silver Layer (Dimensional Modeling)
├── dim_customer
├── dim_campaign
└── fact_marketing_interactions
↓
Gold Layer (KPIs / SQL Analytics)

```

---

## 📦 Dataset

Source: Portuguese Bank Telemarketing Dataset  
(Train: 45,211 rows • Test: 4,521 rows)

Placed in:

data/raw/train.csv
data/raw/test.csv

### Key Columns
- age, job, marital, education  
- balance, housing, loan, default  
- contact, day, month, duration  
- campaign, previous, poutcome, pdays  
- y → target (subscribed: yes/no)

---

## ⭐ Star Schema (Warehouse Layer)

### **dim_customer**
- customer_id (synthetic hash)
- age
- job
- marital
- education
- balance
- housing
- loan
- default

### **dim_campaign**
- campaign_id
- contact
- month
- campaign (current call count)
- previous
- poutcome
- pdays

### **fact_marketing_interactions**
- customer_id
- campaign_id
- day
- month
- duration
- contact
- campaign
- previous
- poutcome
- pdays
- balance
- housing
- loan
- target (0/1)

---

## 📂 Project Structure

```text
marketing-analytics-pipeline/
├── data/
│ ├── raw/
│ │ ├── train.csv
│ │ └── test.csv
│ ├── clean/
│ └── warehouse/
│ ├── dim_customer.csv
│ ├── dim_campaign.csv
│ └── fact_marketing_interactions.csv
├── src/
│ ├── ingest/
│ │ └── ingest_marketing_data.py
│ └── transform/
│ └── transform_marketing_data.py
├── sql/
│ └── marketing_kpis.sql
├── tests/
│ └── test_marketing_quality.py
├── dags/
│ └── marketing_pipeline_dag.py
└── README.md

```

---

## ▶️ How to Run Locally

### **1. Clone the Repository**
```bash
git clone https://github.com/DeepthiPalle381/marketing-analytics-pipeline.git
cd marketing-analytics-pipeline

```

### 2. Create & Activate Virtual Environment (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate

```

### 3. Install Dependencies
```bash
pip install -r requirements.txt

```

### 4. Run Bronze Ingestion (Raw → Clean)
```bash
python src/ingest/ingest_marketing_data.py

```

### 5. Run Warehouse Builder (Clean → Dim/Fact Tables)
```bash
python src/transform/transform_marketing_data.py

```

### 6. Run Data Quality Tests
```bash
pytest

```

# 📊 SQL Marketing Analytics (Gold Layer)

Located in: sql/marketing_kpis.sql

Includes:

Overall conversion rate

Conversion by job

Conversion by month

Effect of previous campaign outcome

Call-duration effectiveness

Customer age group conversion rates

These queries simulate real business analytics for marketing teams.

---

# 🪄 Airflow DAG

File: dags/marketing_pipeline_dag.py

Tasks:

ingest_raw_to_clean (Bronze)

build_warehouse_tables (Silver/Gold)

Scheduled daily (@daily).

---

# ✔ Data Quality Checks

Implemented in:

tests/test_marketing_quality.py

Includes:

Target values must be 0 or 1

All customer_id and campaign_id must exist in dims

No negative balances or durations

Unique keys for dimension tables

---

# 🏁 Summary

This project demonstrates:

ETL/ELT data engineering

Dimensional modeling (star schema)

Fact & dimension table creation

Marketing KPI analytics using SQL

Automated data quality testing

Workflow scheduling (Airflow)

Clean, professional GitHub structure

It closely mirrors real-world data engineering work in banking, marketing, and analytics teams.