import sqlite3, pandas as pd

sql = sqlite3.connect("Sql_data/db_personas.db")

TPersonas = pd.read_sql_query("SELECT * FROM personas", sql)
TSalarios = pd.read_sql_query("SELECT * FROM salarios", sql)

