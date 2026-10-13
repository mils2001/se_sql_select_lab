
# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName
    FROM employees
""", conn)

# STEP 3
# Reverse the column order
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber
    FROM employees
""", conn)

# STEP 4
# Alias employeeNumber as ID
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID
    FROM employees
""", conn)

# STEP 5
# Classify employees by role
df_executive = pd.read_sql("""
    SELECT jobTitle,
           CASE
               WHEN jobTitle IN (
                   'President',
                   'VP Sales',
                   'VP Marketing'
               ) THEN 'Executive'
               ELSE 'Not Executive'
           END AS role
    FROM employees
""", conn)

# STEP 6
# Get the length of each last name
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# Get the first two letters of each job title
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# STEP 8
# Calculate the sum of rounded order prices
sum_total_price = pd.read_sql("""
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails
""", conn).sum()


# STEP 9
# Extract day, month, and year from the order date
df_day_month_year = pd.read_sql("""
    SELECT o.orderDate,
           STRFTIME('%d', o.orderDate) AS day,
           STRFTIME('%m', o.orderDate) AS month,
           STRFTIME('%Y', o.orderDate) AS year
    FROM orderDetails AS od
    JOIN orders AS o ON od.orderNumber = o.orderNumber
""", conn)

# Close the connection
conn.close()

