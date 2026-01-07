# bitsom_ba_25071678-fleximart-data-architecture
FlexiMart Data Architecture Project

Student Name: Harshitha Kalluri
Student ID: BITSoM_BA_25071678
Email: harshithakalluri4011@gmail.com
Course: Data Architecture Design & Implementation
Submission Date: 08 Jan 2026

# Project Overview

This project implements an end-to-end data architecture solution for FlexiMart, covering transactional ETL processing, NoSQL modeling, and analytical data warehousing. The goal is to design scalable systems that support historical sales analysis, customer insights, and business decision-making using relational, NoSQL, and dimensional modeling techniques.

The project is structured into three parts:

-Relational ETL and data quality handling

-NoSQL modeling and MongoDB analytics

-Data warehouse design using a star schema with OLAP queries

# Repository Structure

bitsom_ba_25071678-fleximart-data-architecture/
├── part1-database-etl/
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ ├── data_quality_report.txt
│ └── requirements.txt
│
├── part2-nosql/
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
│
├── part3-datawarehouse/
│ ├── star_schema_design.md
│ ├── warehouse_schema.sql
│ ├── warehouse_data.sql
│ └── analytics_queries.sql
│
├── screenshots/
│ └── README.md
│
├── .gitignore
└── README.md

# Technologies Used

Python 3.x (pandas, mysql-connector-python)

MySQL 8.0

MongoDB 6.0

MongoDB Compass

Git & GitHub

# Part 1: Database ETL Pipeline
# Description

-Built an ETL pipeline to load customer, product, and sales data into MySQL

-Performed data cleaning, deduplication, null handling, and standardization

-Generated a data quality report capturing duplicates, null counts, and final records

# Key Deliverables

-etl_pipeline.py

-schema_documentation.md

-business_queries.sql

-data_quality_report.txt

# Part 2: NoSQL Implementation (MongoDB)
# Description

1.Designed a document-based product catalog using MongoDB

2.Executed CRUD operations and aggregation queries

3.Analyzed NoSQL advantages for flexible schema and nested data (reviews)

4.Key Deliverables

5.products_catalog.json

6.mongodb_operations.js

7.nosql_analysis.md

# Part 3: Data Warehouse & Analytics
# Description

-Designed a star schema with fact and dimension tables

-Implemented the schema in MySQL

-Loaded realistic warehouse data

-Executed OLAP queries for business analytics

-Star Schema Components

-fact_sales

-dim_date

-dim_product

-dim_customer

-Analytical Queries

-Monthly sales drill-down (Year → Quarter → Month)

-Top 10 products by revenue with contribution percentage

-Customer segmentation (High / Medium / Low value)

# Key Deliverables

-star_schema_design.md

-warehouse_schema.sql

-warehouse_data.sql

-analytics_queries.sql

# Setup Instructions
> Note: SQL scripts were executed using MySQL Workbench and MongoDB Compass.
> The CLI commands below are provided as an alternative execution method.

# Database Setup

# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run ETL pipeline
python part1-database-etl/etl_pipeline.py

# Run business queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run data warehouse scripts
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

# MongoDB Setup
mongosh < part2-nosql/mongodb_operations.js

# Key Learnings

1.Practical implementation of ETL pipelines and data quality checks

2.Differences between relational and NoSQL data modeling

3.Designing star schemas for analytical workloads

4.Writing OLAP queries to support business decision-making

5.Importance of schema design, grain definition, and surrogate keys

# Challenges Faced

1.Handling duplicate(especially with email generation and cleaning) and missing values during ETL and ensuring database constraints were respected 

2.Aligning operational data with dimensional modeling concepts during warehouse implementation

3.Both were resolved through iterative debugging and schema validation.

# Submission Notes

1.All required files are present and structured as per assignment guidelines.

2.SQL scripts run without schema or foreign key errors.

3.Analytical queries demonstrate correct OLAP concepts even with limited test data.