# --- Entrada ---
n = input("Introduce un número entero no negativo: ")

# Intentamos convertir la entrada a entero
try:
    n = int(n)
except ValueError:
    print("⚠️  Debes introducir un número entero.")
    exit(1)

# Comprobamos que no sea negativo
if n < 0:
    print("⚠️  El factorial solo está definido para enteros ≥ 0.")
    exit(1)

# --- Cálculo factorial ---
resultado = 1            # 0! y 1! valen 1
contador = 2             # empezamos en 2 porque multiplicar por 1 no cambia nada

while contador <= n:
    resultado *= contador
    contador += 1