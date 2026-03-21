a=int(input())
b=int(input())
c=int(input())
if(a>=c):
    if(a>=b):
        print(f"El numero mayor es {a}")
    else:
        print(f"El numero mayor es {b}")
else:
    if(b>=c):
        print(f"El numero mayor es {b}")
    else:
        print(f"El numero mayor es {c}")
        
        
if(a<=c):
    if(a<=b):
        print(f"El numero menor es {a}")
    else:
        print(f"El numero menor es {b}")
else:
    if(b<=c):
        print(f"El numero menor es {b}")
    else:
        print(f"El numero menor es {c}")