alquileres=[]
codigos=[]
def capturarentero(st):
    while(1):
        try:
            x=int(input(st))
            return x
        except ValueError:
            print("Debe ingresar un número entero")
def capturarfloat(st):
    while(1):
        try:
            x=float(input(st))
            return x
        except ValueError:
            print("Debe ingresar un número entero")
def capturarpositivo(st):
    while(1):
        x=capturarfloat(st)
        if(x<=0):
            print("El número debe ser mayor a 0")
            continue
        return x
def capturarnonegativo(st):
    while(1):
        x=capturarfloat(st)
        if(x<0):
            print("El número no puede ser negativo")
            continue
        return x
def capturarnovacio(st):
    while(1):
        x=input(st)
        if(x==""):
            print("No puede estar vacío")
            continue
        return x
def registrar_alquiler():
    Codigo=capturarnovacio("Introduzca el codigo:")
    if(Codigo in codigos):
        print("El código ya se encuentra registrado")
        return
    codigos.append(Codigo)
    Nombre=capturarnovacio("Introduzca su nombre:")
    CI=capturarnovacio("Introduzca su CI:")
    Telefono=capturarnovacio("Introduzca su telefono:")
    Cliente={
        "Nombre":Nombre,
        "CI":CI,
        "Telefono":Telefono
    }
    Placa=capturarnovacio("Introduzca la placa:")
    Marca=capturarnovacio("Introduzca la marca:")
    Tipo=capturarnovacio("Introduzca el tipo")
    Precio=capturarpositivo("Introduzca el precio por dia:")
    Vehiculo={
        "Placa":Placa,
        "Marca":Marca,
        "Tipo":Tipo,
        "Precio":Precio
    }
    Fecha=capturarnovacio("Introduzca la fecha de inicio de alquiler:")
    Dias=capturarpositivo("Introduzca la cantidad de días")
    Estado=capturarnovacio("Introduzca el estado")
    Datosalquiler={
        "Fecha":Fecha,
        "Dias":Dias,
        "Estado":Estado
    }
    Servicios={
        "Seguro":0,
        "GPS":0,
        "Silla":0
    }
    Pagos={
        "Fecha":"",
        "Monto":0,
        "Método":""
    }
    Alquiler={
        "Codigo":Codigo,
        "Cliente":Cliente,
        "Vehiculo":Vehiculo,
        "Datosalquiler":Datosalquiler,
        "Servicios":Servicios,
        "Pagos":Pagos
    }
    alquileres.append(Alquiler)
    return
def listar_alquileres():
    print(alquileres)
def buscar_pos(st):
    pos=-1
    for i in range(len(codigos)):
        if(codigos[i]==st):
            pos=i
    return pos
def buscar_por_codigo():
    codigo=capturarnovacio("Introduzca el codigo a buscar:")
    pos=buscar_pos(codigo)
    if(pos==-1):
        print("El codigo no se encuentra registrado")
        return
    print(alquileres[pos])
    return
def actualizar_dias_de_alquiler():
    codigo=capturarnovacio("Introduzca el codigo del alquiler que desea extender la cantidad de dias:")
    pos=buscar_pos(codigo)
    if(pos==-1):
        print("El codigo no se encuentra registrado")
        return
    dias=capturarpositivo("Introduzca la cantidad de dias que desea extender:")
    alquileres[pos]["Datosalquiler"]["Dias"]+=dias
def agregar_servicios():
    codigo=capturarnovacio("Introduzca el codigo del alquiler que desea añadir servicios:")
    pos=buscar_pos(codigo)
    if(pos==-1):
        print("El codigo no se encuentra registrado")
        return
    Seguro=capturarnonegativo("Introduzca el monto de seguro que desea agregar:")
    GPS=capturarnonegativo("Introduzca el monto del GPS que desea agregar:")
    Silla=capturarnonegativo("Introduzca el monto de silla infantil que desea agregar:")
    alquileres[pos]["Servicios"]["Seguro"]+=Seguro
    alquileres[pos]["Servicios"]["GPS"]+=GPS
    alquileres[pos]["Servicios"]["Silla"]+=Silla
    return
def calcular_costo():
    codigo=capturarnovacio("Introduzca el codigo del alquiler que desea calcular el monto:")
    pos=buscar_pos(codigo)
    if(pos==-1):
        print("El codigo no se encuentra registrado")
        return
    costo=alquileres[pos]["Datosalquiler"]["Dias"]*alquileres[pos]["Vehiculo"]["Precio"]
    if(alquileres[pos]["Datosalquiler"]["Dias"]>7):
        costo-=costo*10/100
    elif(alquileres[pos]["Datosalquiler"]["Dias"]>3):
        costo-=costo*5/100
    costo+=alquileres[pos]["Servicios"]["Seguro"]+alquileres[pos]["Servicios"]["GPS"]+alquileres[pos]["Servicios"]["Silla"]
    print(f"El costo total es {costo}")
def registrar_pago():
    codigo=capturarnovacio("Introduzca el codigo del alquiler que desea registrar el pago:")
    pos=buscar_pos(codigo)
    if(pos==-1):
        print("El codigo no se encuentra registrado")
        return
def cambiar_estado():
    pass
def mostrar_resumen_general():
    pass
def menu():
    while(1):
        print("=============MENU=============")
        print("1. Registrar alquiler.")
        print("2. Listar alquileres.")
        print("3. Buscar alquiler por código.")
        print("4. Actualizar días de alquiler.")
        print("5. Agregar servicio adicional.")
        print("6. Calcular costo total.")
        print("7. Registrar pago.")
        print("8. Cambiar estado.")
        print("9. Mostrar resumen general.")
        print("10. Salir.")
        opcion=capturarentero("Introduzca la opción que desea realizar:")
        if(opcion==10):
            break
        if(opcion==1):
            registrar_alquiler()
        elif(opcion==2):
            listar_alquileres()
        elif(opcion==3):
            buscar_por_codigo()
        elif(opcion==4):
            actualizar_dias_de_alquiler()
        elif(opcion==5):
            agregar_servicios()
        elif(opcion==7):
            registrar_pago()
        elif(opcion==8):
            cambiar_estado()
        elif(opcion==9):
            mostrar_resumen_general()
        else:
            print("No existe esa opción")
menu()