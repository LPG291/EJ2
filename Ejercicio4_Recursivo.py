def invertir(texto):
    if len(texto) <= 1:
        return texto
    
    else:
        return invertir(texto[1:]) + texto[0]

cadena_original = 'docker'
resultado = invertir(cadena_original)
print(f"Cadena original: {cadena_original}")
print(f"Cadena invertida: {resultado}")