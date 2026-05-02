"""
escribir un algoritmo que dado un valor en bolivianos x 
realizar la conversion a dolares y a euros ademas debe introducir
el tipo de cambio de las divisa
"""
def tipo_cambio():
    d=float(input("Ingrese el tipo de cambio de $us:"))
    e=float(input("Ingrese el tipo de cambio de Euro:"))
    return (d,e)
def conversion():
    (d,e)=tipo_cambio()
    b=float(input("Ingrese los Bolivianos:"))
    dolares=b/d
    euro=b/e
    return (dolares,euro)
def mostrar():
    (d,e)=conversion()
    print(f"Tienes actualmente {d} dolares o {e} euros")
mostrar()