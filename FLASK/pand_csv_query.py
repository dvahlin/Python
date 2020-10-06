#!/usr/bin/python3
import sqlite3
import pandas as pd

conn = sqlite3.connect('/PATH/TO/TestDB.db')
c = conn.cursor()

# Read sqlite query
df = pd.read_sql_query("SELECT * from PIZZA", conn)

# Verify that result of SQL query is stored in the dataframe
print(df.head(1))

conn.close()
