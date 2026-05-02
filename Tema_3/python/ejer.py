#crea un programa que en un rango de numeros del 1 al 100 aleatorios 
#cantidad n numeros aleatorios para generar dos listas una de numeros pares y otro de impares
import random
def generar(n):
    numeroran=[]
    for i in range(n): numeroran.append(random.randint(1,100))
    return numeroran
limite=int(input())
lista=generar(limite)
pares=list(filter(lambda x: x%2==0,lista))
impares=list(filter(lambda x: x%2==1,lista))
sumapar=sumaimpar=0
for numero in pares: sumapar+=numero
for numero in impares: sumaimpar+=numero
print(f"La lista es: {lista}\nLa lista de impares es: {impares} y su suma es {sumaimpar}\nLa lista de pares es: {pares}, y su suma es {sumapar}")