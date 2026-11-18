def capturar(st):
    while 1:
        try:
            valor=int(input(st))
            if(valor>=0 and valor<=100):
                return valor
            print("Debe ingresar un numero entero entre 0 y 100")
        except ValueError:
            print("Debe ingresar un numero entero entre 0 y 100")
def capturarporcentaje():
    while 1:
        try:
            valor=float(input("Introduzca el porcentaje que valen los parciales:"))
            if(valor>0 and valor<100):
                return valor
            print("Debe ingresar un numero mayor a 0 y menor a 100")
        except ValueError:
            print("Debe ingresar un numero mayor a 0 y menor a 100")
def capturasino(st):
    while 1:
        try:
            valor=int(input(st))
            if(valor==0 or valor==1):
                return valor
            print("Debe ingresar 0 o 1")
        except ValueError:
            print("Debe ingresar 0 o 1")
def suma(lis):
    sum=0
    for el in lis:
        sum+=el
    return sum
def prome(lis):
    return suma(lis)/len(lis)
def obtenerdatos(parcial):
    nombre=input("Ingrese el nombre del estudiante:")
    notas=[0]*parcial
    for i in range(parcial):
        notas[i]=capturar(f"Ingrese la nota del parcial {i+1} del estudiante:")
    final1=capturar("Ingrese la nota del primer final:")
    final2=-1
    if(final1==0):
        final2=capturar("Ingrese la nota del segundo final:")
    elif(final1<100):
        if(capturasino("Desea dar el segundo final(0=no;1=si)?")):
            final2=capturar("Ingrese la nota del segundo final:")
    promedio=prome(notas)
    return nombre,notas,final1,final2,promedio
def mostrar(nombre,notas,final1,final2,promedio,notafinal):
    print(f"Este es el reporte del alumno {nombre}")
    print(f"Notas de sus parciales: {notas}")
    print(f"Nota de su primer final: {final1}")
    if(final2==-1):
        print("No dió su segundo final")
    else:
        print(f"Nota de su segundo final: {final2}")
    print(f"Su nota final final es {notafinal}")
def solve():
    cantidad_parcial=int(input("Introduzca la cantidad de parciales que hay:"))
    porcentaje_parcial=capturarporcentaje()
    porcentaje_examen=100-porcentaje_parcial
    nombre,notas,final1,final2,promedio=obtenerdatos(cantidad_parcial)
    notafinal=promedio*porcentaje_parcial/100
    if(final2==-1):
        notafinal+=final1*porcentaje_examen/100
    else:
        notafinal+=final2*porcentaje_examen/100
    mostrar(nombre,notas,final1,final2,promedio,notafinal)
solve()
        