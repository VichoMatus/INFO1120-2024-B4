import pandas as pd, sqlite3
from word_gen import example_contract
import CreacionContratos as CC

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
        
        pdf= int(input("Desea convertirlo a pdf? \nIngrese '1' para SI y '2' para NO : "))
        if pdf < 0 and pdf>2 : print("Ingrese '1' o '2' porfavor. : ")
        if pdf == 1 :
            CC.PDFContratoPorRut(datos, rut)
        else:
            print("")
            
        
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def buscar_por_nacionalidad():
    # Solicitar al usuario que ingrese la nacionalidad
    nacionalidad = input("Ingrese la nacionalidad (ejemplo: Chilena ): \n")
    
    try:
        # Conectar con la base de datos
        sql = sqlite3.connect("Sql_data/db_personas.db")
    
        consu = """
        SELECT *
        FROM personas as p
        INNER JOIN salarios as s
        ON p.id_rol = s.id_salarios
        WHERE p.nacionalidad = ?
        """
        
        # Ejecutar la consulta con la nacionalidad proporcionado
        datos = pd.read_sql_query(consu, sql, params=(nacionalidad,))
        
        # Verificar si se encontraron datos
        if datos.empty:
            print("No se encontraron datos para la NACIONALIDAD proporcionada, porfavor ingrese valores validos.")
            return 
        
        print(datos)
        
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def buscar_por_rango_de_filas():
    try:
        # Solicitar al usuario que ingrese el rango de filas
        fila_inicio = int(input("Ingrese el número de fila de inicio: \n"))
        fila_fin = int(input("Ingrese el número de fila de fin: \n"))
    except ValueError:
        print("Por favor, ingrese números válidos.")
        return
    
    try:
        # Conectar con la base de datos
        sql = sqlite3.connect("Sql_data/db_personas.db")
        
        # Consulta para extraer todos los datos
        consu = """
        SELECT *
        FROM personas as p
        INNER JOIN salarios as s
        ON p.id_rol = s.id_salarios
        """
        
        # Ejecutar la consulta para extraer todos los datos
        datos = pd.read_sql_query(consu, sql)
        
        # Verificar si se encontraron datos
        if datos.empty:
            print("No se encontraron datos en la base de datos.")
            return 
        
        # Verificar si el rango de filas está dentro del rango
        if fila_inicio < 0 or fila_fin >= len(datos) or fila_inicio > fila_fin:
            print("El rango de filas está fuera del rango. Por favor, ingrese números válidos.")
            return
        
        # Seleccionar el rango de filas deseado
        sub_df = datos.iloc[fila_inicio:fila_fin+1]
        
        # Mostrar los datos de las filas seleccionadas
        print(sub_df)
        

    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def buscar_por_id_rol():
    print ("1.- Asistente \n 2.-Contador \n 3.-Desarrolador \n 4.-Supervisor")
    id_rol = input("Ingrese el id del rol: \n")
    
    try:
        # Conectar con la base de datos
        sql = sqlite3.connect("Sql_data/db_personas.db")
    
        consu = """
        SELECT *
        FROM personas as p
        INNER JOIN salarios as s
        ON p.id_rol = s.id_salarios
        WHERE p.id_rol = ?
        """
        
        # Ejecutar la consulta el id del rol proporcionado
        datos = pd.read_sql_query(consu, sql, params=(id_rol,))
        
        # Verificar si se encontraron datos
        if datos.empty:
            print("No se encontraron datos para el ID proporcionado, porfavor ingrese valores validos.")
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
