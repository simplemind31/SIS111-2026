"""
Una persona que va de compras a la multitienda "CyberSTORE" decide llevar 
un control sobre lo que va comprando, para saber la cantidad de dinero 
que tendrá que pagar al llegar a la caja
La tienda solamente vende 3 tipos de productos, estos pueden ser 
Televisores (codigo 1), Refrigeradores (codigo 2), Lavadoras (codigo 3)
No se puede ingresar el codigo de otro articulo, por lo que solo esos 3
valores pueden ser ingresados (validacion)
La persona comprará exactamente 3 productos...

Ud. debe realizar un Algoritmo que permita, en cada uno de los 3 articulos:
    > Indicar el codigo
    > Ingresar la cantidad
    > Ingresar el valor unitario

Finalmente, el algoritmo debe dar como respuesta lo siguiente:

Se compraron X televisores, a un total de XXXXX
Se compraron Y refrigeradores, a un total de XXXXX
Se compraron Z lavadoras, a un total de XXXXX

"""
def validar(x):
    return x==1 or x==2 or x==3
def ingresardatos():
    print("Seleccione su producto")
    print("Televisores (codigo 1), Refrigeradores (codigo 2), Lavadoras (codigo 3)")
    lista=[]
    for i in range(3):
        while(1):
            codigo=int(input("Ingresar codigo: "))
            if(not validar(codigo)):
                continue
            cantidad=int(input("Ingresar la cantidad: "))
            precio=float(input("Ingrese el precio de cada uno: "))
            temp={"codigo":codigo,"cantidad":cantidad,"precio":precio}
            lista.append(temp)
            break
    return lista
def calculo():
    cantidad=[0]*3
    valor=[0]*3
    productos=ingresardatos()
    for prod in productos:
        cantidad[prod["codigo"]-1]+=prod["cantidad"]
        valor[prod["codigo"]-1]+=prod["cantidad"]*prod["precio"]
    print(f"Se compró un total de {cantidad[0]} televisores, a un total de {valor[0]}")
    print(f"Se compró un total de {cantidad[1]} refrigeradores, a un total de {valor[1]}")
    print(f"Se compró un total de {cantidad[2]} lavadores, a un total de {valor[2]}")
calculo()