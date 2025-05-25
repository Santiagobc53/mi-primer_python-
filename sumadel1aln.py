# Solicitar al usuario el valor de n
n = int(input("Ingrese un número entero positivo n: "))

# Inicializamos la suma de factoriales
suma_factoriales = 0

# Recorremos cada i desde 1 hasta n
for i in range(1, n + 1):
    # Calculamos el factorial de i usando un bucle
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    # Lo vamos acumulando en la suma total
    suma_factoriales += factorial

# Mostramos el resultado
print(f"La suma de los factoriales de 1 a {n} es: {suma_factoriales}")
