import sqlite3
import pandas as pd
sql = sqlite3.connect("Sql_data/db_personas.db")
curs = sql.cursor()
df = pd.read_sql_query("SELECT nacionalidad from personas", sql)
print(df)

#prueba



"""
curs.execute("SELECT nacionalidad from personas")
filas = curs.fetchall()
print(filas)
"""