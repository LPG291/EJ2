def suma(lista):
    if not lista: 
        return 0
    else:
        
        return lista[0] + suma(lista[1:])
mi_lista = [2, 4, 6, 8]
resultado = suma(mi_lista)
print(f"La suma es igual a {resultado}")