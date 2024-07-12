import funciones as ff

op=0

empleados=[]


while op !=5:
    ff.menu()
    op= ff.validar_op()
    if op ==1:
        ff.sueldos_aleatorios(empleados)
    elif op ==2:
        ff.clasificar_sueldos(empleados)
    elif op ==3:
        ff.estadisticas(empleados)
    elif op ==4:
        ff.reporte_sueldos(empleados)
    if op != 5:
        input("Presione enter para continuar ...")

print ("Finalizando programa...")
print ("Desarrollado por Bryckson Gutierrez")
print ("RUT 16.719.003-0")
