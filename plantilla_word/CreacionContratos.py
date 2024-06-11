from word_gen import example_contract
import sqlite3
import pandas as pd
from docx import Document


sql = sqlite3.connect("Sql_data/db_personas.db")

def PDFContratoPorRut(df: pd.DataFrame, rut):
    # Filtrar el DataFrame para obtener la fila que corresponde al rut proporcionado
    sub_df = df.loc[df['rut'] == rut]
    sub_df = sub_df.iloc[0]
    date = sub_df['fecha_ingreso']
    rol = sub_df['Rol']
    address = sub_df['residencia']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['nacionalidad']
    birth_date = sub_df['fecha_de_nacimiento']
    profession = sub_df['profesion']
    salary = sub_df['Sueldo']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))
    print("Contrato para", full_name,"generado exitosamente.")
    return None

def PDFContratoPorNacionalidad(df: pd.DataFrame, nacionalidad:str):
# Filtrar el DataFrame para obtener las filas que corresponden a la nacionalidad proporcionada
    sub_df = df[df['nacionalidad'] == nacionalidad]
    try:
        rango = len(sub_df)
    
        for i in range(rango):
            fila = sub_df.iloc[i]
            date = fila['fecha_ingreso']
            rol = fila['Rol']
            address = fila['residencia']
            rut = fila['rut']
            full_name = fila['nombre_completo']
            nationality = fila['nacionalidad']
            birth_date = fila['fecha_de_nacimiento']
            profession = fila['profesion']
            salary = fila['Sueldo']
        
            # Llamar a la función para generar el contrato
            example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))
            print("Contrato para", full_name,"generado exitosamente.")

    except ValueError:
        print("Ha ocurrido un error, ingrese valores validos")

def PDFContratoPorFilas(df: pd.DataFrame, start: int, end: int):
    try:
        for i in range(start, end):
            fila = df.iloc[i]
            date = fila['fecha_ingreso']
            rol = fila['Rol']
            address = fila['residencia']
            rut = fila['rut']
            full_name = fila['nombre_completo']
            nationality = fila['nacionalidad']
            birth_date = fila['fecha_de_nacimiento']
            profession = fila['profesion']
            salary = fila['Sueldo']
            
            # Llamar a la función para generar el contrato
            example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))
            print("Contrato para", full_name, "generado exitosamente.")
    except ValueError:
        print("Ha ocurrido un error, ingrese valores válidos.")
    except IndexError:
        print("Ha ocurrido un error: índice fuera de rango. Por favor, verifique los índices.")


def PDFContratoPorID_Rol(df: pd.DataFrame, id_rol:int):
# Filtrar el DataFrame para obtener las filas que corresponden a la nacionalidad proporcionada
    filas = df[df['id_rol'] == id_rol]
    try:
       
    
        for i in range(len(filas)):
            fila = filas.iloc[i]
            date = fila['fecha_ingreso']
            rol = fila['Rol']
            address = fila['residencia']
            rut = fila['rut']
            full_name = fila['nombre_completo']
            nationality = fila['nacionalidad']
            birth_date = fila['fecha_de_nacimiento']
            profession = fila['profesion']
            salary = fila['Sueldo']
        
            # Llamar a la función para generar el contrato
            example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))
            print("Contrato para", full_name,"generado exitosamente.")

    except ValueError:
        print("Ha ocurrido un error, ingrese valores validos")
# Consulta para los datos
#consu = """ SELECT * FROM personas as p INNER JOIN salarios as s ON p.id_rol = s.id_salarios """
#datos =  pd.read_sql_query(consu,sql)
#print(PDFContratoPorRut(datos, consult))

