import random
import csv

nom = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
      
def sueldos_aleatorios(lista):
    sueldo =[]
    for i in range(10):
        sueldos = round(random.uniform(300000, 2500000),2)
        d = {'nombre': [nom], 'sueldo': sueldo}
        sueldos.append(d)
        return sueldos
        
def menu():
    menu=""" MENU

1- Asignar Sueldos Aleatorios
2- Clasificar Sueldos
3- Ver estadisticas
4- Reporte de sueldos
5- Salir del programa

INGRESA TU OPCION: """
    print(menu, end="")

def validar_op():
    while True:
        try:
            op = int(input())
            if 1 <= op <= 5:
                return op
            else:
                raise ValueError
        except:
            print("Opcion no valida, ingresa una opcion valida: ")       

def clasificar_sueldos(lista):
    menores = []
    entre = []
    mas_de = []

    for trabajador in lista:
        if trabajador["sueldo"] <= 800000:
            menores.append(trabajador)
        elif trabajador["sueldo"] <=2000000:
            entre.append(trabajador)
        else:
            mas_de.append(trabajador)

    print("SUELDO MENOR A $800.000: ")
    print()

    for e in menores:
        print(f'{e["nombre"]} : ${e["sueldo"]:,.0f}')
    print("__________________________")

    print("SUELDO ENTRE $800.000 Y $2.000.000")
    print()

    for e in entre:
        print(f'{e["nombre"]} : ${e["sueldo"]:,.0f}')
    print("__________________________")

    print("SUELDO MAYORES A $2.000.000:")
    print()

    for e in mas_de:
        print(f'{e["nombre"]} : ${e["sueldo"]:,.0f}')

def sueldo_bajo(lista):
    bajo = lista[0]
    for empleado in lista:
        if bajo["sueldo"] > empleado["sueldo"]:
            bajo = empleado
    return bajo
#
def sueldo_alto(lista):
    alto = lista[0]
    for empleado in lista:
        if alto["sueldo"] < empleado["sueldo"]:
            alto = empleado
    return alto
# 
def estadisticas(lista):
    print(f"Sueldo más bajo: {sueldo_bajo(lista)}")
    print(f"Sueldo más alto: {sueldo_alto(lista)}")
    listar_sueldos = [sueldo["sueldo"] for sueldo in lista]
    suma = sum(listar_sueldos)
    promedio = suma / 10
    print(f"Sueldo promedio: {promedio:,.0f}")
# 
def reporte_sueldos(lista):
    reporte = []
    for trabajador in lista:
        sueldo_bruto = trabajador["sueldo"]
        afp = int(sueldo_bruto * 0.12)
        salud = int(sueldo_bruto * 0.07)
        sueldo_liquido = sueldo_bruto - afp - salud
        a = {"nombre": trabajador["nombre"], "sueldo_bruto": sueldo_bruto, "afp": afp, "salud": salud, "sueldo_liquido": sueldo_liquido}
        reporte.append(a)
    
    nombre_campos = ["nombre", "sueldo_bruto", "afp", "salud", "sueldo_liquido"]
    with open('Reporte sueldos empleados.csv', 'w', newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=nombre_campos)
        escritor.writeheader()
        escritor.writerows(reporte)
