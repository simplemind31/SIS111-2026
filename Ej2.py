import random
def aleatorios(n):
    pares=""
    impares=""
    for i in range(n):
        numero=random.randint(1,100)
        if(numero%2==0):
            pares=f"{pares} {numero},"
        else:
            impares=f"{impares} {numero},"
    return f"Pares: {pares}\nImpares: {impares}"
n=int(input())
print(aleatorios(n))