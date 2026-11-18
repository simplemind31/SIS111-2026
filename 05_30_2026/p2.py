#Ejercicio 2#Resumen registrar 5 notas, mostrarlas t calcular el promedio
notas=[0]*5
for i in range(5):
    notas[i]=int(input(f"Ingrese la nota {i+1}:"))
promedio=sum(notas)/5
print(f"Las notas son {notas} y su promedio es {promedio}")