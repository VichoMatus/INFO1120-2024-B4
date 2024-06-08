import sqlite3
import pandas as pd

def buscar_y_mostrar_por_rut():
    # Solicitar al usuario que ingrese el RUT
    rut = input("Ingrese el RUT (ejemplo: 12345678-9): ")
    
    try:
        # Conectar con la base de datos
        sql = sqlite3.connect("Sql_data/db_personas.db")
        
        # Consulta para unir los datos de las tablas `personas` y `salarios` usando el RUT
        query = """
        SELECT *
        FROM personas as p
        INNER JOIN salarios as s
        ON p.id_rol = s.id_salarios
        WHERE p.rut = ?
        """
        
        # Ejecutar la consulta con el RUT proporcionado
        datos = pd.read_sql_query(query, sql, params=(rut,))
        
        # Verificar si se encontraron datos
        if datos.empty:
            print("No se encontraron datos para el RUT proporcionado.")
            return
        
        # Configurar pandas para mostrar todas las columnas
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)  # Ajustar el ancho según tus necesidades
        
        print(datos)
        
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    print("Ingrese valores válidos.")

# Llamar a la función
buscar_y_mostrar_por_rut()

  