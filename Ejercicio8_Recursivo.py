def cuenta_corregida(n):
    if n == 0:
        return "fin"
    
    else:

        print(n)
        return cuenta_corregida(n - 1)

print(cuenta_corregida(5))