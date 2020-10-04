#!/usr/bin/python3

import sqlite3
import pandas

csv_file = "PATH/TO/CSV_FILE"
table_name = "PIZZA"
conn = sqlite3.connect('PATH/TO/TestDB.db')
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - PIZZA
c.execute('''CREATE TABLE PIZZA ([NUMBER] INTEGER,[TYPE] text, [NAME] text, [CONTENT] text, [PRICE] INTEGER)''')
conn.commit()

# Use pandas to import CSV to DB
df = pandas.read_csv(csv_file, sep='\t',header=(0))
df.to_sql(table_name, conn, if_exists='append', index=False)
