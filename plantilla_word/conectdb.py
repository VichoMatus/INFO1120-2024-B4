import sqlite3 , pandas as pd, data as dt

# Conectar con la base de datos
sql = sqlite3.connect("Sql_data/db_personas.db")

# Tablas de la base de datos
TPersonas = pd.read_sql_query("SELECT * FROM personas", sql)
TSalarios = pd.read_sql_query("SELECT * FROM salarios", sql)

# Todos los datos
datos =  pd.read_sql_query("SELECT * FROM personas INNER JOIN salarios",sql)

print (dt.singular_data_to_contract(datos, 2))

