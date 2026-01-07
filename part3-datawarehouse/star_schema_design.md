# Star Schema Design – FlexiMart Data Warehouse

## Section 1: Schema Overview

FlexiMart’s data warehouse is designed using a **star schema** to support analytical reporting on historical sales data. The design separates transactional facts from descriptive dimensions to improve query performance and simplify analysis.

---

### FACT TABLE: fact_sales

**Grain**  
One row per product per order line item.

**Business Process**  
Sales transactions.

**Measures (Numeric Facts)**  
- quantity_sold: Number of units sold  
- unit_price: Price per unit at the time of sale  
- discount_amount: Discount applied on the transaction  
- total_amount: Final transaction amount  

**Foreign Keys**  
- date_key → dim_date  
- product_key → dim_product  
- customer_key → dim_customer  

---

### DIMENSION TABLE: dim_date

**Purpose**  
Supports time-based analysis such as daily, monthly, quarterly, and yearly trends.

**Type**  
Conformed dimension.

**Attributes**  
- date_key (PK): Surrogate key in YYYYMMDD format  
- full_date: Actual calendar date  
- day_of_week: Day name (Monday, Tuesday, etc.)  
- month: Month number (1–12)  
- month_name: Month name  
- quarter: Q1, Q2, Q3, Q4  
- year: Calendar year  
- is_weekend: Indicates weekend days  

---

### DIMENSION TABLE: dim_product

**Purpose**  
Stores descriptive product information for product-level analysis.

**Attributes**  
- product_key (PK): Surrogate key  
- product_id: Source system identifier  
- product_name: Name of the product  
- category: Product category  
- subcategory: Detailed classification  
- unit_price: Standard price  

---

### DIMENSION TABLE: dim_customer

**Purpose**  
Enables customer segmentation and behavioral analysis.

**Attributes**  
- customer_key (PK): Surrogate key  
- customer_id: Source system identifier  
- customer_name: Customer name  
- city: Customer location  
- customer_segment: Business-defined segment  

---

## Section 2: Design Decisions

The data warehouse uses a **transaction line-item level granularity**, meaning each row in the fact table represents a single product sold within an order. This provides maximum analytical flexibility, enabling detailed drill-down analysis and accurate aggregations.

**Surrogate keys** are used instead of natural keys to ensure stability and consistency. Natural keys from source systems can change or be reused, while surrogate keys remain immutable and improve join performance.

The **star schema** design simplifies query logic by separating measurable facts from descriptive attributes. This structure supports **roll-up operations** (e.g., yearly or category-level sales) and **drill-down analysis** (e.g., from year → quarter → month → day), making it ideal for analytical workloads.

---

## Section 3: Sample Data Flow

**Source Transaction**  
Order #101  
Customer: John Doe  
Product: Laptop  
Quantity: 2  
Unit Price: ₹50,000  
Order Date: 2024-01-15  

**Data Warehouse Representation**

**fact_sales**  
- date_key: 20240115  
- product_key: 5  
- customer_key: 12  
- quantity_sold: 2  
- unit_price: 50000  
- total_amount: 100000  

**dim_date**  
- date_key: 20240115  
- full_date: 2024-01-15  
- month: 1  
- quarter: Q1  
- year: 2024  

**dim_product**  
- product_key: 5  
- product_name: Laptop  
- category: Electronics  

**dim_customer**  
- customer_key: 12  
- customer_name: John Doe  
- city: Mumbai  