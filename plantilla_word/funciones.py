import pandas as pd, sqlite3
from word_gen import example_contract

def buscar_por_rut():
    # Solicitar al usuario que ingrese el RUT
    rut = input("Ingrese el RUT (ejemplo: 12345678-9): \n")
    
    try:
        # Conectar con la base de datos
        sql = sqlite3.connect("Sql_data/db_personas.db")
        
        # Consulta para unir los datos de las tablas `personas` y `salarios` usando el RUT
        consu = """
        SELECT *
        FROM personas as p
        INNER JOIN salarios as s
        ON p.id_rol = s.id_salarios
        WHERE p.rut = ?
        """
        
        # Ejecutar la consulta con el RUT proporcionado
        datos = pd.read_sql_query(consu, sql, params=(rut,))
        
        # Verificar si se encontraron datos
        if datos.empty:
            print("No se encontraron datos para el RUT proporcionado, porfavor ingrese valores validos.")
            return 
        
        print(datos)
        
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")





def singular_data_to_contract(df: pd.DataFrame, index_row:int):
    sub_df = df.iloc[index_row]
    date = sub_df['fecha_ingreso']
    rol = sub_df['Rol']
    address = sub_df['residencia']
    rut = sub_df['rut']
    full_name = sub_df['nombre_completo']
    nationality = sub_df['nacionalidad']
    birth_date = sub_df['fecha_de_nacimiento']
    profession = sub_df['profesion']
    salary = sub_df['Sueldo']
    example_contract(date, rol, address, rut, full_name, nationality, birth_date, profession, str(salary))

