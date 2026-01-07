# FlexiMart Database Schema Documentation (Part 1)

This document describes the relational database schema used in Part 1 of the FlexiMart Data Architecture project.  
The schema is designed following normalization principles to support transactional operations and reporting.

---

## 1. customers

Stores customer-related information.

### Columns
- customer_id (INT, PK, AUTO_INCREMENT)
- first_name (VARCHAR)
- last_name (VARCHAR)
- email (VARCHAR, UNIQUE)
- phone (VARCHAR)
- city (VARCHAR)
- registration_date (DATE)

### Description
Each record represents a unique customer.  
Email is enforced as UNIQUE, and missing or duplicate emails are handled during ETL.

---

## 2. products

Stores product catalog information.

### Columns
- product_id (INT, PK, AUTO_INCREMENT)
- product_name (VARCHAR)
- category (VARCHAR)
- price (DECIMAL)
- stock_quantity (INT)

### Description
Each record represents a product available for sale.  
Stock quantity and missing prices are cleaned during ETL.

---

## 3. sales

Stores transaction-level sales data.

### Columns
- sale_id (INT, PK, AUTO_INCREMENT)
- customer_id (INT, FK → customers.customer_id)
- product_id (INT, FK → products.product_id)
- quantity (INT)
- order_date (DATE)
- total_amount (DECIMAL)

### Description
Each row represents a single sales transaction involving one product and one customer.

---

## Relationships
- One customer → many sales
- One product → many sales

---

## Normalization (3NF Explanation)

The schema follows **Third Normal Form (3NF)**:

### First Normal Form (1NF)
- All attributes contain atomic values.
- No repeating groups exist.

### Second Normal Form (2NF)
- All non-key attributes depend fully on the primary key.
- Example: In `customers`, all attributes depend on `customer_id`.

### Third Normal Form (3NF)
- No transitive dependencies exist.
- Customer contact details are not duplicated in sales.
- Product details are not stored in sales.

This design prevents update, insert, and delete anomalies and ensures data integrity.

---

## Sample Data Representation

### Customers Table
| customer_id | first_name | last_name | email            | city   | registration_date |
|------------|-----------|----------|------------------|--------|-------------------|
| 1 | Rahul | Sharma | rahul@gmail.com | Delhi | 2024-01-10 |

### Products Table
| product_id | product_name | category | price | stock_quantity |
|-----------|--------------|----------|-------|----------------|
| 1 | Laptop | Electronics | 50000 | 10 |

### Sales Table
| sale_id | customer_id | product_id | quantity | order_date | total_amount |
|--------|-------------|------------|----------|------------|--------------|
| 1 | 1 | 1 | 2 | 2024-01-15 | 100000 |