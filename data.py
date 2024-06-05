import pandas as pd
from word_gen import example_contract


print("Ingrese 1 si quiere buscar la informacion de una persona en especifico")
print("Ingrese 2 si quiere buscar la informacion de un grupo de personas")
busqueda = ""
eleccion = input(int())


if eleccion == 1:
    busqueda = "lista"
    a = input("Ingrese el indice de la persona que desea buscar")
else: 
    busqueda = "eleccion"
    a = int(input("Ingrese el primer rango de personas"))
    b = int(input("Ingrese el segundo rango de personas") )   





def singular_data_to_contract(df: pd.DataFrame, Rol:str, lista , eleccion):
    sub_df = df.iloc[Rol]
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

    






