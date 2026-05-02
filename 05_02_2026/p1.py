"""
uan eempresa deasea saber cuanto gasta en bonos pro hijos 
de sus trabajadores. Esta empresa tiene n trabajadoras, los que pueden
ser solteras(codigo 1), casadas(codigo 2), en pareja(codigo 3).
soolo pueden ser esos 3 codigos pro lo que debe validar el ingreso.
El algoritmo debe preguntar a cada una de los trabajadoras los siguiente
codigo de su estado civil
cantidad de hijos

se sabe que el bono actualmente es de 2000bs por cada hijo
finalmente el algoritmo debe dar como respuesta lo siguiente:

hay xxx trabajadoras solteras, con xxx hijos
hay xxx trabajadoras casados, con xxx hijos
hay xxx trabajadoras en pareja, con xxx hijos
el total del bono entregado por la empresa es de: xxxxxx
"""
def validar(x):
    return x==1 or x==2 or x==3
def capturar():
    print("Los estados civiles corresponden a los siguientes codigos:")
    print("soltera(codigo 1), casada(codigo 2), en pareja(codigo 3)")
    n=int(input("Introduzca la cantidad de trabajadores:"))
    trabajadores=[]
    for i in range(n):
        while(1):
            codigo=int(input(f"Introduzca el estado civil del trabajador {i+1}:"))
            if(not validar(codigo)):
                print("Código inválido, vuelva a indtroducir")
                continue
            canti_hijos=int(input(f"Introduzca la cantidad de hijos del trabajador {i+1}:"))
            trabaja={"codigo":codigo,"hijos":canti_hijos}
            trabajadores.append(trabaja)
            break
    return trabajadores
def calcular():
    trabajadores=capturar()
    cantidad=[0]*3
    hijos=[0]*3
    for trabaja in trabajadores:
        cantidad[trabaja["codigo"]-1]+=1
        hijos[trabaja["codigo"]-1]+=trabaja["hijos"]
    print(f"Hay {cantidad[0]} trabajadoras solteras, con {hijos[0]} hijos")
    print(f"Hay {cantidad[1]} trabajadoras casadas, con {hijos[1]} hijos")
    print(f"Hay {cantidad[2]} trabajadoras en pareja, con {hijos[2]} hijos")
    totalhijos=hijos[0]+hijos[1]+hijos[2]
    bonototal=2000*totalhijos
    print(f"El total del bono entregado por la empresa es de {bonototal}bs")
        
calcular()