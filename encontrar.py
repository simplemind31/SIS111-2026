#Elaborar un algoritmo dada un numero limite=n de aleatorios entre 1 y 100, encontrar las coincidencias de x
import random
def generar(n):
    numeroran=[]
    for i in range(n):
        numeroran.append(random.randint(1,100))
    return numeroran
def buscar(x,n):
    a=generar(n)
    con=0
    for i in a: con+=(i==x)
    return f"el numero de coincidencias para {x} en el conjunto {a} es {con}"
n=int(input())
x=int(input())
print(buscar(x,n))
