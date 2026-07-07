def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

resultado = fibonacci(4)
print(f"El término 6 de la serie de Fibonacci es: {resultado}")