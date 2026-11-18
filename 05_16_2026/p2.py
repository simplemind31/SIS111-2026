def introducir():
    while 1:
        try:
            x=int(input("Introduzca un numero:"))
            if(x<=0):
                print("Debe ser un número positivo")
            else:
                return x
        except ValueError:
            print("Debe introducir números")
def esprimo(x):
    j=2
    while(j*j<=x):
        if(x%j==0):
            return False
        j+=1
    return True
def primosmenorn(x):
    primos=[]
    for i in range(2,x+1):
        if(esprimo(i)):
            primos.append(i)
    return primos
def sumalista(x):
    suma=0
    for el in x:
        suma+=el
    return suma
n=introducir()
primos=primosmenorn(n)
suma=sumalista(primos)
print(f"Numero primos: {primos}")
print(f"Suma: {suma}")
