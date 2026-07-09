def busqueda_binaria_recursiva(lista, objetivo, inicio, fin):
    
    if inicio > fin:
        return -1  
   
    mitad = (inicio + fin) // 2

    if lista[mitad] == objetivo:
        return mitad  

    elif objetivo < lista[mitad]:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, mitad - 1)

    else:
        return busqueda_binaria_recursiva(lista, objetivo, mitad + 1, fin)


lista = [1, 3, 5, 7, 9, 12, 15, 20]
numero = 15
resultado = busqueda_binaria_recursiva(
    lista, numero, 0, len(lista) - 1
)
if resultado != -1:
    print(
        f"  {numero} esta en indice {resultado}."
    )
else:
    print(f"{numero} no esta en la lista")