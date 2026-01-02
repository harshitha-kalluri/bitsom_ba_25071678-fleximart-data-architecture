"""
ETL Pipeline for FlexiMart - Part 1
Student: Harshitha Kalluri
# Test commit by Harshitha
"""

import pandas as pd
import numpy as np
import re
from datetime import datetime
import mysql.connector


# =============================
# 1. EXTRACT
# =============================

def read_csv_file(path):
    """Reads CSV and returns DataFrame."""
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return pd.DataFrame()


# =============================
# 2. TRANSFORM HELPERS
# =============================

def clean_phone_number(phone):
    """Standardize to +91-XXXXXXXXXX."""
    if pd.isna(phone):
        return None

    digits = re.sub(r'\D', '', str(phone))
    digits = digits[-10:]   # keep last 10 digits

    return f"+91-{digits}" if len(digits) == 10 else None


def clean_date(date_value):
    """Convert mixed date formats into YYYY-MM-DD."""
    try:
        dt = pd.to_datetime(date_value, errors="coerce")
        if pd.isna(dt):
            return None
        return dt.strftime("%Y-%m-%d")
    except:
        return None


# =============================
# 2A. TRANSFORM CUSTOMERS
# =============================

def transform_customers(df):

    report = {}

    # Remove duplicates
    report["duplicates_removed"] = df.duplicated().sum()
    df = df.drop_duplicates()

    # Remove original text ID (C001...) because DB has AUTO_INCREMENT
    if "customer_id" in df.columns:
        df = df.drop(columns=["customer_id"])

    # Handle missing email
    #df['email'] = df['email'].fillna("unknown@email.com")
    df['email'] = df.apply(
    lambda row: row['email'] if pd.notna(row['email']) 
                else f"unknown_{row.name}@email.com",
    axis=1)

    #df['email'] = df.apply(
    #lambda row: row['email'] if pd.notna(row['email']) else f"{row['customer_id'].lower()}@unknown.com",
    #axis=1)


    #df['email'] = df.apply(
    #lambda row: row['email'] if pd.notna(row['email']) 
    #else f"unknown_{row['customer_id']}@email.com",
    #axis=1)

    # Standardize phone
    df["phone"] = df["phone"].apply(clean_phone_number)

    # Fix date
    df["registration_date"] = df["registration_date"].apply(clean_date)

    # Clean city format
    df["city"] = df["city"].str.title()

    report["final_records"] = len(df)
    return df, report


# =============================
# 2B. TRANSFORM PRODUCTS
# =============================

def transform_products(df):

    report = {}

    df = df.drop_duplicates()

    if "product_id" in df.columns:
        df = df.drop(columns=["product_id"])

    df["price"] = df["price"].fillna(df["price"].median())
    df["stock_quantity"] = df["stock_quantity"].fillna(0)
    df["category"] = df["category"].str.strip().str.capitalize()

    report["final_records"] = len(df)
    return df, report


# =============================
# 3. LOAD TO MYSQL
# =============================

def load_to_mysql(df, table_name):
    """Insert DataFrame into MySQL."""

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Harshitha@123",     # ←password given here
            database="fleximart"
        )
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cols = ",".join(df.columns)
            placeholders = ",".join(["%s"] * len(row))
            query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})"
            cursor.execute(query, tuple(row.values))

        conn.commit()

        print(f"Inserted {len(df)} rows into {table_name}")

    except mysql.connector.Error as err:
        print("MySQL Error:", err)

    finally:
        cursor.close()
        conn.close()


# =============================
# MAIN
# =============================

if __name__ == "__main__":

    print("\nStarting ETL Pipeline...\n")
    

    # Extract
    customers = read_csv_file("data/customers_raw.csv")
    products = read_csv_file("data/products_raw.csv")

    # Transform
    customers_clean, cust_report = transform_customers(customers)
    products_clean, prod_report = transform_products(products)

    print("Customer Columns:", customers.columns.tolist())

    # Data Quality Report
    with open("part1-database-etl/data_quality_report.txt", "w") as f:
        f.write("CUSTOMERS REPORT:\n" + str(cust_report) + "\n\n")
        f.write("PRODUCTS REPORT:\n" + str(prod_report) + "\n\n")

    # Load
    load_to_mysql(customers_clean, "customers")
    load_to_mysql(products_clean, "products")

    print("\nETL Pipeline Complete.")
