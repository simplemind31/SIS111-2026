def obtener_promedio(lista):
    suma=0
    for elemento in lista:
        suma+=elemento
    return suma/len(lista)
def obtener_por_materia(asignatura,cantidad_examenes,cantidad_practicas,porcentaje_examenes,porcentaje_practicas):
    examenes=[]
    practicas=[]
    for i in range(cantidad_examenes):
        examen=float(input(f"Introduzca su nota del examen {i+1} de la asignatura {asignatura}:"))
        examenes.append(examen)
    for i in range(cantidad_practicas):
        practica=float(input(f"Introduzca su nota de la práctica {i+1} de la asignatura {asignatura}:"))
        practicas.append(practica)
    promedio_examenes=obtener_promedio(examenes)
    promedio_practicas=obtener_promedio(practicas)
    nota_final=promedio_examenes*porcentaje_examenes/100+promedio_practicas*porcentaje_practicas/100
    informacion={
        "cantidad de examenes":cantidad_examenes,
        "cantidad de practicas":cantidad_practicas,
        "porcentaje de examenes":porcentaje_examenes,
        "porcentaje de practicas":porcentaje_practicas,
        "examenes":examenes,
        "practicas":practicas,
        "promedio de examenes":promedio_examenes,
        "promedio de practicas":promedio_practicas,
        "nota final":nota_final
    }
    return informacion
def mostrar(asignaturas,informaciones):
    promedio_total=0
    for asig in asignaturas:
        print(f"Su nota final de la asginatura {asig} es {informaciones[asig]["nota final"]}")
        promedio_total+=informaciones[asig]["nota final"]
    promedio_total/=len(asignaturas)
    print(f"El promedio final de todas las asginaturas es {promedio_total}")
def resolver():
    cantidad_asignaturas=int(input("Introduzca la cantidad de asignaturas:"))
    informaciones={}
    asignaturas=[]
    for i in range(cantidad_asignaturas):
        asignatura=input(f"Introduzca la asginatura {i+1}:")
        asignaturas.append(asignatura)
        cantidad_examenes=int(input("Introduzca la cantidad de examenes:"))
        cantidad_practicas=int(input("Introduzca la cantidad de prácticas:"))
        porcentaje_examenes=float(input("Introduzca el porcentaje que valen los exámenes:"))
        porcentaje_practicas=100-porcentaje_examenes
        informaciones[asignatura]=obtener_por_materia(asignatura,cantidad_examenes,cantidad_practicas,porcentaje_examenes,porcentaje_practicas)
    mostrar(asignaturas,informaciones)
resolver()
