import matplotlib.pyplot as plt
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect("Sql_data/db_personas.db")
cursor = conn.cursor()

# Consulta SQL para obtener el promedio de sueldo por profesión
consulta = """
SELECT p.profesion, AVG(s.Sueldo) AS sueldo_promedio
FROM personas p
INNER JOIN salarios as s
ON p.id_rol = s.id_salarios
GROUP BY p.profesion;
"""

# Ejecutar la consulta
cursor.execute(consulta)

# Obtener los resultados
resultados = cursor.fetchall()

# Cerrar la conexión a la base de datos
conn.close()

# Separar los resultados en profesiones y sueldos promedio
profesiones = [resultado[0] for resultado in resultados]
sueldos_promedio = [resultado[1] for resultado in resultados]

# Generar el gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(profesiones, sueldos_promedio, color='skyblue')
plt.xlabel('Sueldo promedio')
plt.ylabel('Profesión')
plt.title('Promedio de sueldo por profesión')
plt.gca().invert_yaxis()  # Invertir el eje y para que las profesiones más altas estén arriba

plt.show()
