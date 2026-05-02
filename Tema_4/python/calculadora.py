def operator(a,b,c):
    if(c==1):
        return a+b
    if(c==2):
        return a-b
    if(c==3):
        return a*b
    if(c==4):
        return a/b
while(1):
    print("Elija una operación")
    print("#1 Suma")
    print("#2 Resta")
    print("#3 Multiplicar")
    print("#4 Dividir")
    print("#5 Salir")
    op=int(input())
    if(op==5):
        break
    if(op!=1 and op!=2 and op!=3 and op!=4):
        print("Error")
        break
    n=int(input())
    a=int(input())
    for i in range(n-1):
        b=int(input())
        a=operator(a,b,op)
    print(a)