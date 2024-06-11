import pandas as pd
import funciones as fc
import graficos as gf
from word_gen import example_contract

a = "--------------------------------------------------------------------------------------------------------------------"

def menu_principal():
    print(a, "\nIngrese '1' para buscar datos por rut.")
    print("Ingrese '2' para buscar datos por rango.")
    print("Ingrese '3' para ver datos por graficos. \n", a)
    
    while True:
        try:
            rqst = int(input("Ingrese aqui: "))
            if rqst < 1 or rqst > 3:
                print("Ingrese una opción válida entre '1' y '3'. \n", a)
                continue

            if rqst == 1:
                print("Usted ha seleccionado 'buscar datos por rut'.\n")
                fc.buscar_por_rut()
            
            elif rqst == 2:
                print("Usted ha seleccionado buscar por rango.\nSeleccione el rango que desea buscar:\n", a)
                print("Ingrese 1.- Si desea buscar por Indice de Filas.")
                print("Ingrese 2.- Si desea buscar por Nacionalidad.")
                print("Ingrese 3.- Si desea buscar por Numero de Rol.")
                print(a)
                
                while True:
                    try:
                        choice = int(input("Ingrese aqui: "))
                        print(a)
                        
                        if choice < 1 or choice > 3:
                            print("Ingrese una opción válida entre '1' y '3'. \n", a)
                            continue
                        
                        if choice == 1:
                            print("Usted ha seleccionado 'Buscar datos por Indice de filas'.\n", a)
                            fc.buscar_por_rango_de_filas()
                        elif choice == 2:
                            print("Usted ha seleccionado 'Buscar datos por Nacionalidad'.\n", a)
                            fc.buscar_por_nacionalidad()
                        elif choice == 3:
                            print("Usted ha seleccionado 'Buscar datos por Numero de rol'.\n", a)
                            fc.buscar_por_id_rol()
                        break
                    except ValueError:
                        print("Ingrese valores válidos.\n", a)
            
            elif rqst == 3:
                print("Usted ha seleccionado 'ver datos por graficos'.\n", a)
                print("Ingrese '1' si desea ver un grafico para mostrar el promedio de sueldo por profesion.")
                print("Ingrese '2' si desea ver un grafico para ver la distribucion de las profesiones.")
                print("Ingrese '3' si desea ver un grafico para mostrar la distribucion de trabajadores por nacionalidad.")
                
                while True:
                    try:
                        elecc = int(input("Ingrese aqui: "))
                        print(a)
                        
                        if elecc < 1 or elecc > 3:
                            print("Ingrese una opción válida entre '1' y '3'. \n", a)
                            continue
                        
                        if elecc == 1:
                            gf.PromedioSueldos()
                            print("El grafico se ha mostrado correctamente.\n", a)
                        elif elecc == 2:
                            gf.DistribucionProfesiones()
                            print("El grafico se ha mostrado correctamente.\n", a)
                        elif elecc == 3:
                            gf.NacionalidadTrabajadores()
                            print("El grafico se ha mostrado correctamente.\n", a)
                        break
                    except ValueError:
                        print("Ingrese valores válidos.\n", a)
            break
        
        except ValueError:
            print("Ingrese valores válidos.\n", a)


menu_principal()


