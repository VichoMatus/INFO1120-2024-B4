import matplotlib.pyplot as plt
import sqlite3

# Conectarse a la base de datos
conn = sqlite3.connect("Sql_data/db_personas.db")
cursor = conn.cursor()

# Consulta SQL para obtener el conteo de profesionales por nacionalidad
consulta = """
SELECT nacionalidad, COUNT(*) AS cantidad
FROM personas
GROUP BY nacionalidad;
"""

# Ejecutar la consulta
cursor.execute(consulta)

# Obtener los resultados
resultados = cursor.fetchall()

# Cerrar la conexión a la base de datos
conn.close()

# Separar los resultados en nacionalidades y cantidades
nacionalidades = [resultado[0] for resultado in resultados]
cantidades = [resultado[1] for resultado in resultados]

# Crear el gráfico de barras

plt.bar(nacionalidades, cantidades, color='skyblue')
plt.xlabel('Nacionalidad')
plt.ylabel('Cantidad de Profesionales')
plt.title('Conteo de Profesionales por Nacionalidad')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()  # Ajustar el diseño para evitar cortes
plt.show()
