import matplotlib.pyplot as plt
import sqlite3

def PromedioSueldos():
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
    plt.xlabel("Sueldo promedio")
    plt.ylabel("Profesión")
    plt.title("Promedio de sueldo por profesión")
    plt.gca().invert_yaxis()  # Invertir el eje y para que las profesiones más altas estén arriba
    plt.tight_layout()  # Ajustar el diseño para evitar cortes
    plt.show()

def DistribucionProfesiones():
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

def NacionalidadTrabajadores():
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