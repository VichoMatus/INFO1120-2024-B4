













"""""
-------------------------------------COSAS QUE PUEDEN SERVIRNOS-----------------------------------------------


SUMA DE SALARIO TOTAL
SalariosTotal = TSalarios["Sueldo"].sum()




CARGAR TABLAS DE PERSONAS Y SALARIOS EN UN DATAFRAME DE PANDAS
TPersonas = pd.read_sql_query("SELECT * FROM personas", sql)
TSalarios = pd.read_sql_query("SELECT * FROM Salarios", sql)




SELECT * 
FROM Empleados E
JOIN Departamentos D
ON E.DepartamentoId = D.Id


""" 