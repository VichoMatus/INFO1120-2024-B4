import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk

def buscar_por_rut(rut):
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
        
        if datos.empty:
            print("No se encontraron datos para el RUT proporcionado.")
            return None
        else:
            return datos
        
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    return None

def mostrar_resultados(datos):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Resultados de Búsqueda")
    
    # Crear un Treeview para mostrar los datos
    tree = ttk.Treeview(root)
    tree["columns"] = list(datos.columns)
    tree["show"] = "headings"
    
    # Añadir encabezados de columnas
    for col in datos.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Ajusta el ancho según tus necesidades
    
    # Añadir datos a la tabla
    for index, row in datos.iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack(expand=True, fill='both')
    
    # Iniciar la aplicación
    root.mainloop()

# Solicitar al usuario que ingrese el RUT
rut = input("Ingrese el RUT (ejemplo: 12345678-9): ")
resultados = buscar_por_rut(rut)

if resultados is not None:
    mostrar_resultados(resultados)
else:
    print("Ingrese valores válidos.")
