import pandas as pd, funciones as fc
from word_gen import example_contract


print ("Ingrese '1' para buscar datos por rut.")
print ("Ingrese '2' para buscar datos por rango.")



try:
    rqst = int (input ("Ingrese aqui: "))
    if rqst < 1 or rqst > 2:
        print("Ingrese '1' u '2'. ")
    elif rqst == 1:
        print("Usted ha seleccionado 'buscar datos por rut'.")
        fc.buscar_por_rut()
<<<<<<< Updated upstream
    elif rqst == 2:
        print("Funcion Rango")
=======
    elif rqst == 2: 
        print("Usted ha seleccionado buscar por rango \nSeleccione el rango que desea buscar:\n",a)
        print("Ingrese 1.- Si desea buscar por indice de filas.")
        print("Ingrese 2.- Si desea buscar por Nacionalidad. \nIngrese 3.- Si desea buscar por numero de rol.")
        print(a)
        choice = int(input("Ingrese aqui:"))
        print(a)
        if choice < 1 or choice > 3:
            print("Ingrese una opcion valida entre '1' a '5'. \n",a)
        if choice == 1 :
            print("Usted ha seleccionado 'Buscar datos por Indice de filas'.\n",a)
        if choice == 2 :
            print("Usted ha seleccionado 'Buscar datos por Nacionalidad'.\n",a)
        if choice == 3 :
            print("Usted ha seleccionado 'Buscar datos por Numero de rol'.\n",a)
>>>>>>> Stashed changes
except :
    print("Ingrese solo numeros.")

