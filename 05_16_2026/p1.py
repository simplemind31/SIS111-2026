a=0
b=0
while 1:
    try:
        a=int(input("Introduzca el primer numero:"))
        b=int(input("Introduzca el segundo numero:"))
        if(a<0):
            print("Debe ser un número positivo")
        elif(a<1000 or b<1000):
            print("Debe ser dos numeros de más de 3 digitos")
        else:
            break  
    except ValueError:
        print("Debe Introducir números")
def caclular(x):
    res=0
    while(x):
        res+=x%10
        x//=10
    return res
sumaa=caclular(a)
sumab=caclular(b)
print(f"La suma de digitos de {a} es {sumaa}")
print(f"La suma de digitos de {b} es {sumab}")
if sumaa==sumab:
    print("Por lo que son amigos")
else:
    print("Por lo que no son amigos")
#12345->5
#1234->4
#123->3
