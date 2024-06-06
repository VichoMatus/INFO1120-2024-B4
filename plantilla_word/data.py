import pandas as pd
from word_gen import example_contract


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
    

def singular_data_to_contract(df: pd.DataFrame, index_row:int):
    sub_df = df.iloc[index_row]
    date = sub_df['Fecha']
    rol = sub_df['Rol']
    address = sub_df['Residencia']
    rut = sub_df['RUT']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['Nacionalidad']
    birth_date = sub_df['Fecha de nacimiento']
    profession = sub_df['Profesion']
    salary = sub_df['Sueldo']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))

    






