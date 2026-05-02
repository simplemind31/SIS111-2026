#escribir un algoritmo que calcule el area y area y volumen de un cilindro 
import math
def ingresarDatos():
    r=float(input("Ingrese el radio:"))
    h=float(input("Ingrese la altura:"))
    return (r,h)
def area(r,h):
    return 2*pow(r,2)*math.pi+2*r*math.pi*h
def volumen(r,h):
    return pow(r,2)*math.pi*h
def mostrar():
    (a,b)=ingresarDatos()
    print(f"El area del cilindro de radio {a} y altura {b} es {area(a,b)}")
    print(f"El volumen del cilindro de radio {a} y altura {b} es {volumen(a,b)}")
mostrar()