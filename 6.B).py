import matplotlib.pyplot as plt
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("Sql_data/db_personas.db")
cursor = conn.cursor()

# Consulta SQL para obtener la cantidad de personas por profesión
consulta = """
SELECT profesion, COUNT(*) AS cantidad
FROM personas
GROUP BY profesion;
"""

# Ejecutar la consulta
cursor.execute(consulta)

# Obtener los resultados
resultados = cursor.fetchall()

# Cerrar la conexión a la base de datos
conn.close()

# Separar los resultados en profesiones y cantidad de personas
profesiones = [resultado[0] for resultado in resultados]
cantidad_personas = [resultado[1] for resultado in resultados]

# Crear el gráfico de pastel
plt.figure(figsize=(7,7))
plt.pie(cantidad_personas, labels=profesiones, autopct='%1.1f%%', startangle=90)
plt.title("Distribución de profesiones")
plt.axis("equal")  # Hace que el gráfico de pastel sea un círculo en lugar de una elipse
plt.show()
