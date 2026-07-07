def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

resultado = fibonacci(6)
print(f"el sexto numero en la serie de Fibonacci es: {resultado}")