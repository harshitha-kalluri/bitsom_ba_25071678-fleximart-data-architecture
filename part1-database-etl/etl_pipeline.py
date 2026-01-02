"""
ETL Pipeline for FlexiMart - Part 1
Student: Harshitha Kalluri
"""

"""
ETL Pipeline for FlexiMart
--------------------------------
Reads raw CSV files, cleans data, fixes quality issues, 
and loads cleaned data into MySQL.
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime
import mysql.connector

# =============================
# 1. EXTRACT – Read CSV Files
# =============================

def read_csv_file(path):
    """Reads a CSV file and returns a DataFrame."""
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        return pd.DataFrame()
    

# =============================
# 2. TRANSFORM – Clean Data
# =============================

def clean_phone_number(phone):
    """Standardizes phone numbers into +91-XXXXXXXXXX format."""
    if pd.isna(phone):
        return None
    
    # Remove anything that's not numbers
    digits = re.sub(r'\D', '', str(phone))

    # Keep only last 10 digits
    digits = digits[-10:]

    return f"+91-{digits}" if len(digits) == 10 else None


def clean_date(date_value):
    """Converts different date formats into YYYY-MM-DD."""
    try:
        return pd.to_datetime(date_value, errors='coerce').strftime("%Y-%m-%d")
    except:
        return None


def transform_customers(df):
    """Cleans customer data based on the assignment rules."""

    report = {}

    # Remove duplicates
    report["duplicates_removed"] = df.duplicated().sum()
    df = df.drop_duplicates()

    # Handle missing emails → fill with 'unknown@email.com'
    df['email'] = df['email'].fillna("unknown@email.com")

    # Standardize phone
    df['phone'] = df['phone'].apply(clean_phone_number)

    # Fix date formats
    df['registration_date'] = df['registration_date'].apply(clean_date)

    # Standardize city names (capitalize)
    df['city'] = df['city'].str.title()

    report["missing_after_cleaning"] = df.isna().sum().to_dict()
    report["final_record_count"] = len(df)

    return df, report


def transform_products(df):
    """Cleans product data."""

    report = {}

    df = df.drop_duplicates()

    # Fill missing price with median
    df['price'] = df['price'].fillna(df['price'].median())

    # Fill missing stock with zero
    df['stock_quantity'] = df['stock_quantity'].fillna(0)

    # Standardize categories
    df['category'] = df['category'].str.strip().str.capitalize()

    report["final_record_count"] = len(df)
    return df, report


def transform_sales(df):
    """Cleans sales data."""

    report = {}

    df = df.drop_duplicates()

    # Convert all dates
    df['order_date'] = df['order_date'].apply(clean_date)

    # Remove rows where customer/product ID missing
    df = df.dropna(subset=['customer_id', 'product_id'])

    report["final_record_count"] = len(df)
    return df, report


# =============================
# 3. LOAD – Load into MySQL
# =============================

def load_to_mysql(df, table_name):
    """Loads cleaned DataFrame into MySQL database."""

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_PASSWORD",   # ← Update this
            database="fleximart"
        )

        cursor = conn.cursor()

        # Insert each row
        for _, row in df.iterrows():
            cols = ",".join(df.columns)
            vals = tuple(row.values)
            placeholders = ",".join(["%s"] * len(vals))

            query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            cursor.execute(query, vals)

        conn.commit()
        cursor.close()
        conn.close()

        print(f"Inserted {len(df)} rows into {table_name}")

    except mysql.connector.Error as err:
        print("MySQL Error:", err)


# =============================
# MAIN PIPELINE
# =============================

if __name__ == "__main__":
    
    print("\nStarting ETL Pipeline...\n")

    # Extract
    customers = read_csv_file("data/customers_raw.csv")
    products = read_csv_file("data/products_raw.csv")
    sales = read_csv_file("data/sales_raw.csv")

    # Transform
    customers_clean, cust_report = transform_customers(customers)
    products_clean, prod_report = transform_products(products)
    sales_clean, sales_report = transform_sales(sales)

    # Print Data Quality Report
    print("\n=== DATA QUALITY REPORT ===")
    print("Customers:", cust_report)
    print("Products:", prod_report)
    print("Sales:", sales_report)

    # Save report to file
    with open("part1-database-etl/data_quality_report.txt", "w") as f:
        f.write("CUSTOMERS:\n" + str(cust_report) + "\n\n")
        f.write("PRODUCTS:\n" + str(prod_report) + "\n\n")
        f.write("SALES:\n" + str(sales_report) + "\n\n")

    # Load to MySQL
    load_to_mysql(customers_clean, "customers")
    load_to_mysql(products_clean, "products")
    load_to_mysql(sales_clean, "orders")  # if required later

    print("\nETL Pipeline Completed Successfully.")
