#ejercicio 1
#resumen: registrar 5 estudiantes y mostrar la lista completa
nombres=[0]*5
for i in range(5):
    nombres[i]=input(f"Introduzca el nombre del estudiante {i+1}:")
print(nombres)