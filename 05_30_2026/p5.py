def capturar(st):
    while 1:
        try:
            nota=int(input(st))
            if(nota>=0 and nota<=100):
                return nota
            print("Debe ingresar un numero entre 0 y 100")
        except:
            print("Debe ingresar un numero entre 0 y 100")
def registrar():
    nombre=input(f"Introduzca el nombre del estudiante a registrar:")
    nota=capturar(f"Introduzca la nota final del estudiante {nombre}:")
    return (nombre,nota)
def listar(lista):
    print(lista)
def buscar(lista,que):
    for el in lista:
        if(el.lower()==que.lower()):
            return True
    return False
def sumar(dic):
    suma=0
    for el in dic:
        suma+=dic[el]
    return suma
def menu():
    dic={}
    while 1:
        print("1=Registrar estudiante")
        print("2=Listar estudiantes")
        print("3=Buscar estudiante")
        print("4=Cacular el promedio general")
        print("0=Salir")
        opcion=int(input("Introduzca la opcion que desea:"))
        if(opcion==0):
            break
        if(opcion==1):
            nom,nota=registrar()
            dic[nom]=nota
        elif(opcion==2):
            listar(dic)
        elif(opcion==3):
            busc=input("Introduzca el nombre a buscar:")
            print(f"El estudiante {busc} se encuentra registrado" if buscar(dic,busc) else f"El estudiante {busc} no se encuentra registrado")
        else:
            print(f"El promedio general es {sumar(dic)/len(dic)}")
menu()