

def cuenta(n):
    if n == 0:
        return
    
    else:
        print(n)
        cuenta(n - 1)

print("Resultado: ")
cuenta(5)