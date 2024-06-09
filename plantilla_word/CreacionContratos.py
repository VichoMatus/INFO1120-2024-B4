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
    return None



# Consulta para los datos
#consu = """ SELECT * FROM personas as p INNER JOIN salarios as s ON p.id_rol = s.id_salarios """
#datos =  pd.read_sql_query(consu,sql)
#print(PDFContratoPorRut(datos, consult))

