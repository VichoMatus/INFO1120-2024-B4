import sqlite3
import pandas as pd
import data as dt
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

#CREAR LA CONECCION CON LA BASE DE DATOS
sql = sqlite3.connect("Sql_data/db_personas.db")

#CARGAR LAS TABLAS DE LA BASE DE DATOS EN UN DATAFRAME DE PANDAS
innerJoin= pd.read_sql_query("SELECT * FROM personas INNER JOIN Salarios", sql)

#---------------------------------------------------------------


#holalaaosdalkjd