import os, time
from funciones import *


while True:
    print("""MENÚ TRABAJADORES
          1)Registrar trabajador
          2)Listar a todos los trabajadores
          3)Imprimir planilla de sueldos
          4)Salir del programa""")
    
    opc=int(input("Ingrese opción: "))
    os.system("cls")
    if opc==1:
        opcion1()

    elif opc==2:
        opcion2()

    elif opc==3:
        opcion3()
        
    else:
        opcion4()
    time.sleep(3)