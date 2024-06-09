import pandas as pd, funciones as fc
from word_gen import example_contract


a = "--------------------------------------------------------------------------------------------------------------------"

print (a ,"\nIngrese '1' para buscar datos por rut.")
print ("Ingrese '2' para buscar datos por rango.\n",a)

try:
    rqst = int (input ("Ingrese aqui: "))
    if rqst < 1 or rqst > 2:
        print("Ingrese '1' u '2'. \n",a)
    elif rqst == 1:
        print("Usted ha seleccionado 'buscar datos por rut'.\n",a)
        fc.buscar_por_rut()
    elif rqst == 2: 
        print("Usted ha seleccionado buscar por rango \n SelecS el rango que desea buscar:\n",a)
        print("Ingrese 1.- Si desea buscar por indice de filas.")
        print("Ingrese 2.- Si desea buscar por Nacionalidad. \nIngrese 3.- Si desea buscar por numero de rol.")
        print(a)
        choice = int(input("Ingrese aqui: "))
        print(a)
        if choice < 1 or choice > 3:
            print("Ingrese una opcion valida entre '1' a '5'. \n",a)
        if choice == 1 :
            print("Usted ha seleccionado 'Buscar datos por Indice de filas'.\n",a)
            fc.buscar_por_rango_de_filas()
        if choice == 2 :
            print("Usted ha seleccionado 'Buscar datos por Nacionalidad'.\n",a)
            fc.buscar_por_nacionalidad()
        if choice == 3 :
            print("Usted ha seleccionado 'Buscar datos por Numero de rol'.\n",a)
            fc.buscar_por_id_rol()
except :
    print("Ingrese valores validos.")

