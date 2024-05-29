import sqlite3
import pandas as pd

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.

#CREAMOS LA CONECCION CON LA BASE DE DATOS
sql = sqlite3.connect("Sql_data/db_personas.db")
#USAMOS PANDAS PARA LEER LA BASE DE DATOS
TPersonas = pd.read_sql_query("SELECT * FROM personas", sql)
TSalarios = pd.read_sql_query("SELECT * FROM Salarios", sql)


"""""
-------------------------------------COSAS QUE PUEDEN SERVIRNOS-----------------------------------------------


SUMA DE SALARIO TOTAL
SalariosTotal = TSalarios["Sueldo"].sum()


SELECT * 
FROM Empleados E
JOIN Departamentos D
ON E.DepartamentoId = D.Id


""" 