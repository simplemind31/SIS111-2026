#registrar 3 estudiantes con su nota final, usando diccionarios
notas={}
for i in range(3):
    nombre=input(f"Introduzca el nombre del estudiante {i+1}:")
    notafianl=int(input(f"Introduzca la nota final del estudiante {nombre}:"))
    notas[nombre]=notafianl
for nomb in notas:
    aprobado=notas[nomb]>=51
    print(f"El estudiante {nomb} tiene {notas[nomb]} en su nota final\nPor lo que",end=' ')
    print(f"aprobó la materia" if aprobado else "reprobó la materia")