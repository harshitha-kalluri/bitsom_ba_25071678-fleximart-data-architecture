"""
ETL Pipeline for FlexiMart - Part 1
Student: Harshitha Kalluri
"""

# --------------------------
# Import required packages
# --------------------------
import pandas as pd
import numpy as np
import os
import pathlib
import re

# Set current path to the 'data' folder
current_path = pathlib.Path.cwd()
data_path = current_path.parent / 'data'

# --------------------------
# Step 1: Extract - Read CSV Files
# --------------------------
def read_raw_data(filename):
    """Reads a CSV file from the data directory."""
    file_path = data_path / filename
    df = pd.read_csv(file_path)
    return df


# --------------------------
# Step 2: Transform Functions (skeleton only)
# --------------------------
def clean_customer_data(df):
    """Cleans customer data: duplicates, missing values, phone formats, dates."""
    # You will fill this part in next steps
    return df


def clean_product_data(df):
    """Cleans product data: price, categories, missing stock."""
    return df


def clean_sales_data(df):
    """Cleans sales data: dates, missing IDs, duplicates."""
    return df


# --------------------------
# Step 3: Load (MySQL loading functions)
# --------------------------
def load_to_mysql(df, table_name):
    """Loads a pandas DataFrame to MySQL database."""
    # Implementation will be added later
    pass


# --------------------------
# Main ETL Execution Flow
# --------------------------
def run_etl():

    # Extract
    customers = read_raw_data("customers_raw.csv")
    products = read_raw_data("products_raw.csv")
    sales = read_raw_data("sales_raw.csv")

    # Transform
    customers_clean = clean_customer_data(customers)
    products_clean = clean_product_data(products)
    sales_clean = clean_sales_data(sales)

    # Load (MySQL)
    # load_to_mysql(customers_clean, "customers")
    # load_to_mysql(products_clean, "products")
    # load_to_mysql(sales_clean, "orders")   # orders & order_items will need extra join logic

    print("ETL Pipeline executed successfully (skeleton).")

if __name__ == "__main__":
    run_etl()
