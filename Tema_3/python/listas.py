def bubble_sort(lista, ascendente=True):
    n=len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if((ascendente and lista[j]>lista[j+1]) or (((not ascendente) and lista[j]<lista[j+1]))):
                lista[j],lista[j+1]=lista[j+1],lista[j]
    return lista
lista=[9,1,3,6,1,40,5,10]
print(bubble_sort(lista,True))
print(bubble_sort(lista,False))
print(lista)