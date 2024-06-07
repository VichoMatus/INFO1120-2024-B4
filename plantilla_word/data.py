import pandas as pd
from word_gen import example_contract
import sqlite3


"""
busqueda = ""
eleccion = input(int())
print ("Ingrese '1' para seleccionar datos por rut.")
print ("Ingrese '2' para seleccionar datos por rango.")

rqst = input ("Ingrese aqui: ")

try:
    if rqst < 1 or rqst > 2:
        print("Ingrese '1' u '2'. ")
    elif rqst == 1:
        print("Funcion Rut")
    elif rqst == 2:
        print("Funcion Rango")
except:
    print("Ingrese solo numeros.")

"""


def singular_data_to_contract(df: pd.DataFrame, index_row:int):
    sub_df = df.iloc[index_row]
    date = sub_df['fecha_ingreso']
    address = sub_df['residencia']
    rut = sub_df['rut']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['nacionalidad']
    birth_date = sub_df['fecha_de_nacimiento']
    profession = sub_df['profesion']
    salary = sub_df['Sueldo']
    rol = sub_df['Rol']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))



sql = sqlite3.connect("Sql_data/db_personas.db") 
datos =  pd.read_sql_query("SELECT * FROM personas INNER JOIN salarios",sql)
#print(datos)
print (singular_data_to_contract(datos, 2))





