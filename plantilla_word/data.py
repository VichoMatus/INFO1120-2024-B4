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
    elif rqst == 2:
        print("Funcion Rango")
except :
    print("Ingrese solo numeros.")

