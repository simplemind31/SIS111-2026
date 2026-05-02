#escribir un algoritmo que calcule el área de un triángulo
def area(base, altura):
    return base*altura/2
x=int(input("Ingrese la base del triángulo:"))
y=int(input("Ingrese la altura del triángulo:"))
print(area(x,y))