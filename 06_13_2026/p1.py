reservas=[]
codigos_de_reservas=[]
def capturar18(st):
    while 1:
        try:
            res=int(input(st))
            if(res>=1 and res<=8):
                return res
            print("Debe ingresar un numero entero entre 1 y 8")
        except ValueError:
            print("Debe ingresar un numero entero entre 1 y 8")
def caputrarnonegativo(st):
    while 1:
        try:
            res=float(input(st))
            if(res>=0):
                return res
            print("Debe ingresar un numero no negativo")
        except ValueError:
            print("Debe ingresar un numero no negativo")
def caputrarpositivo(st):
    while 1:
        try:
            res=int(input(st))
            if(res>0):
                return res
            print("Debe ingresar un numero positivo")
        except ValueError:
            print("Debe ingresar un numero positivo")
def calcular_costo_habitacion(precio_noches,noches):
    return precio_noches*noches
def calcular_total_servicios(servicios):
    suma=0
    for el in servicios:
        suma+=servicios[el]
    return suma
def calcular_subtotal(precio_noche,noches,servicios):
    return calcular_costo_habitacion(precio_noche,noches)+calcular_total_servicios(servicios)
def calcular_descuento(subtotal):
    if(subtotal>=1000):
        return subtotal*10/100
    if(subtotal>=500):
        return subtotal*5/100
    return 0
def calcular_total(precio_noche,noches,servicios):
    sub=calcular_subtotal(precio_noche,noches,servicios)
    des=calcular_descuento(sub)
    return sub-des
def registrar_reserva():
    codigo=input("Ingrese el codigo de reserva:")
    if codigo in codigos_de_reservas:
        print("Ya existe reserva con ese codigo")
        return None
    nombre=input("Ingrese el nombre del huesped:")
    ci=input("Ingrese el carnet del huesped:")
    huesped={
        "nombre":nombre,
        "ci":ci
    }
    tipo=input("Ingrese el tipo de la habitación:")
    precio=caputrarpositivo("Ingrese el precio por la noche de la habitación:")
    habitacion={
        "tipo":tipo,
        "precio_noche":precio
    }
    noches=caputrarpositivo("Ingrese la cantidad de noches que desea quedar:")
    servicios={
        "desayuno":0,
        "lavanderia":0,
        "garaje":0
    }
    subtotal=calcular_subtotal(precio,noches,servicios)
    descuento=calcular_descuento(subtotal)
    total=calcular_total(precio,noches,servicios)
    estado=input("Ingrese el estado de la reserva").lower()
    reserva={
        "codigo":codigo,
        "huesped":huesped,
        "habitacion":habitacion,
        "noches":noches,
        "servicios":servicios,
        "subtotal":subtotal,
        "descuento":descuento,
        "total":total,
        "estado":estado
    }
    reservas.append(reserva)
def listar_reservas():
    print(reservas)
def buscar_reserva(codigo):
    for i in range(len(reservas)):
        if(reservas[i]["codigo"]==codigo):
            return i
    return -1
def agregar_servicio(codigo):
    posicion=buscar_reserva(codigo)
    if(posicion==-1):
        print("No existe reserva con ese codigo")
        return
    desayuno=caputrarnonegativo("Ingrese el costo del desayuno:")
    lavanderia=caputrarnonegativo("Ingrese el costo de la lavanderia:")
    garaje=caputrarnonegativo("Ingrese el costo del garaje:")
    reservas[posicion]["servicios"]={
        "desayuno":desayuno,
        "lavanderia":lavanderia,
        "garaje":garaje
    }
    reservas[posicion]["subtotal"]=calcular_subtotal(reservas[posicion]["habitacion"]["precio_noche"],reservas[posicion]["noches"],reservas[posicion]["servicios"])
    reservas[posicion]["total"]=calcular_total(reservas[posicion]["habitacion"]["precio_noche"],reservas[posicion]["noches"],reservas[posicion]["servicios"])
    reservas[posicion]["descuento"]=calcular_descuento(reservas[posicion]["subtotal"])
def mostrar_reservas_activas():
    for el in reservas:
        if el["estado"]=="activo":
            print(el)
def mostrar_resumen():
    cantidad_reservas=len(reservas)
    cantidad_activas=0
    monto_total=0
    mayor=-1
    codi=""
    for el in reservas:
        monto_total+=el["total"]
        if el["estado"]=="activo":
            cantidad_activas+=1
        if el["total"]>mayor:
            mayor=el["total"]
            codi=el["codigo"]
    promedio=monto_total/cantidad_reservas
    print(f"Cantidad total de reservas: {cantidad_reservas}")
    print(f"Cantidad total de reservas activas: {cantidad_activas}")
    print(f"Monto total acumulado {monto_total}")
    print(f"Promedio por reserva {promedio}")
    print(f"Reserva con mayor total: {codi} - {mayor} Bs")
def menu():
    while 1:
        print("================")
        print("Menú del sistema")
        print("1. Registrar reserva")
        print("2. Listar reserva")
        print("3. Buscar reserva por código")
        print("4. Agregar servicio adicional")
        print("5. Calcular total de una reserva")
        print("6. Mostrar reserva activas")
        print("7. Mostrar resumen general")
        print("8. Salir")
        ope=capturar18("Introduzca la operacion que desea realizar:")
        if(ope==8):
            break
        elif(ope==1):
            registrar_reserva()
        elif(ope==2):
            listar_reservas()
        elif(ope==3):
            codigo=input("Ingrese el codigo:")
            posicion=buscar_reserva(codigo)
            if(posicion==-1):
                print("No existe reserva con ese codigo")
            else:
                print(reservas[posicion])
        elif(ope==4):
            codigo=input("Ingrese el codigo:")
            agregar_servicio(codigo)
        elif(ope==5):
            codigo=input("Ingrese el codigo:")
            posicion=buscar_reserva(codigo)
            if(posicion==-1):
                print("No existe reserva con ese codigo")
            else:
                print(f"El total de esa reserva es {reservas[posicion]["total"]}")
        elif(ope==6):
            mostrar_reservas_activas()
        elif(ope==7):
            mostrar_resumen()
menu()