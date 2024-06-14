trabajadores=[]
cargos=("CEO","DESARROLLO","ANALISTA")




def opcion1():
    print("\tregistrar trabajador")
    nombre_apellido=input("Ingrese su nombre y apellido: ")
    cargo= int(input("ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
    sueldo_bruto= int(input("Ingrese sueldo bruto: "))
    descuento_salud= int(0.07*sueldo_bruto)
    descuento_afp= int(0.12*sueldo_bruto)
    sueldo_liquido= sueldo_bruto-descuento_afp-descuento_salud
    trabajador=[nombre_apellido,cargos[cargo-1],sueldo_bruto,descuento_salud,descuento_afp,sueldo_liquido]
    trabajadores.append(trabajador)
    print("Trabajador registrado con éxito")


def opcion2():
    if len(trabajadores)==0:
            print("No existen trabajadores registrados, ingrese a la opción 1")
    else:
        print("\tLISTA DE TRABAJADORES")
        print("Trabajador\tcargo\tsueldo bruto\tdesc. salud\tdesc. AFP\tliquido")
        for t in trabajadores:
            print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t{t[4]}\t\t{t[5]}")


def opcion3():
    if len(trabajadores)==0:
            print("No existen trabajadores, elija la opción 1")
    else:
        opc2=int(input("¿Qué cargo desea imprimir? (1.CEO, 2.DESARROLLADOR 3.ANALISTA 4.TODOS)"))
        if opc2==4:
            with open("todos_trabajadores.txt","w", newline="\n") as archivo:
                for t in trabajadores:
                    texto= f"Nombre: {t[0]} \nCargo: {t[1]} \nBruto: {t[2]} \ndesc. Salud: {t[3]} \nDesc. AFP: {t[4]} \nLiquido: {t[5]}"
                    archivo.write(texto)
            print("ARCHIVO CREADO CON ÉXITO!")
        else:
            with open ("trabajadores_por_cargo.txt","w") as archivo:
                for t in trabajadores:
                    if cargos[opc2-1]==t[1]:
                        texto= f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}"
                        archivo.write(texto)

def opcion4():
    print("Gracias por usar el programa, adios!")
    exit()