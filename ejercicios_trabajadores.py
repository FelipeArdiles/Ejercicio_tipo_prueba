import os, time


trabajadores=[]

while True:
    print("""MENÚ TRABAJADORES
          1)Registrar trabajador
          2)Listar a todos los trabajadores
          3)Imprimir planilla de sueldos
          4)Salir del programa""")
    opc=int(input("Ingrese opción: "))
    os.system("cls")
    if opc==1:
        print("\tregistrar trabajador")
        nombre_apellido=input("Ingrese su nombre y apellido: ")
        cargo= int(input("ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
        sueldo_bruto= int(input("Ingrese sueldo bruto: "))
        descuento_salud= int(0.07*sueldo_bruto)
        descuento_afp= int(0.12*sueldo_bruto)
        sueldo_liquido= sueldo_bruto-descuento_afp-descuento_salud
        trabajador=[nombre_apellido,cargo,sueldo_bruto,descuento_salud,descuento_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print("Trabajador registrado con éxito")

    elif opc==2:
        if len(trabajadores)==0:
            print("No existen trabajadores registrados, ingrese a la opción 1")
        else:
            print("\tLISTA DE TRABAJADORES")
            print("Trabajador\tcargo\tsueldo bruto\tdesc. salud\tdesc. AFP\tliquido")
            for t in trabajadores:
                print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")

    elif opc==3:
        pass
    else:
        print("Gracias por usar el programa, adios!")
        break
    time.sleep(3)