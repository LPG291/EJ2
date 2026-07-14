# 1. Representación de las carpetas (Estructura de Árbol)
Recorer = {
    "nombre": "Proyecto",
    "hijos": [
        {
            "nombre": "src",
            "hijos": [
                {"nombre": "main", "hijos": []},
            ]
        },
        {
            "nombre": "docs",
            "hijos": [
                {"nombre": "readme", "hijos": []}
            ]
        },
        {"nombre": "EJ2", "hijos": []}
    ]
}

def imprimir_arbol(nodo, nivel=0):
    indentacion = "  " * nivel
    
    print(f"{indentacion}── {nodo['nombre']}")
    
    for hijo in nodo["hijos"]:
        imprimir_arbol(hijo, nivel + 1)

print("Estructura de carpetas generada:")
imprimir_arbol(Recorer)