# Part 2 – NoSQL Implementation (MongoDB)

## Student Information

**Name:** Harshitha Kalluri 
**Course:** BA in Gen AI & Agentic AI
**Project:** FlexiMart Data Architecture  
**Part:** Part 2 – NoSQL (MongoDB)  
**Database:** MongoDB 6.0 Community Server

---

## 1. Overview

This part of the project demonstrates the use of a **NoSQL database (MongoDB)** for managing a flexible product catalog. Unlike relational databases, MongoDB allows schema-less document storage, making it suitable for handling heterogeneous product attributes and embedded data such as customer reviews.

The implementation includes both **theoretical justification** for choosing MongoDB and **practical MongoDB operations** executed using the MongoDB shell (`mongosh`).

---

## 2. Objectives

- Explain why a NoSQL database is suitable for the FlexiMart product catalog
- Design a document-based data model for products
- Store heterogeneous product data using flexible schemas
- Perform CRUD and aggregation operations in MongoDB
- Demonstrate embedded documents and analytics queries

---

## 3. Tools and Technologies Used

- **MongoDB:** 6.0 Community Server
- **MongoDB Shell:** mongosh 2.x
- **Data Format:** JSON
- **Execution Environment:** Local MongoDB instance

---

## 4. File Structure

    --- part2-nosql
        ├── README.md
        ├── nosql_analysis.md
        ├── mongodb_operations.js
        └── products_catalog.json

---

## 5. Data Model Design

### Collection: `products`

Each document represents a single product and contains:

- Basic product attributes (ID, name, category, price, stock)
- Category-specific attributes stored inside a `specs` sub-document
- Embedded `reviews` array containing user feedback

This structure avoids joins and allows flexible schema evolution.

---

## 6. MongoDB Operations Performed

### The file `mongodb_operations.js` contains MongoDB queries and operations executed on a sample product collection. These operations include:

- Loading product data into a MongoDB collection
- Querying products based on category and price
- Calculating average product ratings from embedded reviews
- Updating documents by adding new reviews
- Aggregating product data to analyze pricing by category

The queries are written to be executed using MongoDB Compass or the MongoDB shell.



---

## 7. How to Run the MongoDB Operations

### Step 1: Start MongoDB Server

Ensure MongoDB 6.0 Community Server is running locally.

### Step 2: Navigate to Directory

```bash
cd part2-nosql
```

### Step 3: Execute MongoDB Script

```bash
mongosh < mongodb_operations.js
```

---

## 8. Validation Commands

### To verify data insertion:

    use fleximart_nosql
    db.products.countDocuments()

### Expected Output:

    10

### To verify a sample document:

    db.products.findOne({ product_id: "ELEC001" })

---

## 9. Key Learnings

    MongoDB supports flexible schemas ideal for product catalogs

    Embedded documents reduce the need for joins

    Aggregation pipelines enable powerful analytics

    Schema evolution is simpler compared to relational databases

    MongoDB is better suited for read-heavy, flexible data models

---

## 10. Notes

    MongoDB is used only for product catalog management
   
    MongoDB Compass was used to validate the queries and aggregation pipelines. All operations were tested on a local MongoDB setup.

    Transactional data (orders, payments) remains in MySQL

    MongoDB complements the relational database rather than replacing it

    All operations were executed using MongoDB 6.0 Community Server


## Sample Data

The file `products_catalog.json` contains sample product documents structured with nested fields and arrays. This data demonstrates how MongoDB supports flexible schemas and embedded documents.


## Part 2 Status

NoSQL justification completed \
Product catalog implemented \
MongoDB operations executed successfully \
Output validated

