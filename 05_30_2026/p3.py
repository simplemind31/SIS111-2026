#ejercicio 3
#resumen: registrar 5 estudiantes y buscar uno por nombre
nombres=[""]*5
for i in range(5):
    nombres[i]=input(f"Introduzca el nombre del estudiante {i+1}:")
buscar=input("Introduzca el nombre a buscar:")
xd=False
for i in range(5):
    if(buscar.lower()==nombres[i].lower()):
        xd=True
print(f"El estudiante {buscar} se encuentra registrado" if xd else f"El estudiante {buscar} no se encuentra registrado")