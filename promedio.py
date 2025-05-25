# Programa que pide 10 números enteros y calcula su promedio

suma = 0

for i in range(1, 11):
    numero = int(input(f"Ingrese el número {i}: "))
    suma += numero  # Es lo mismo que: suma = suma + numero

promedio = suma / 10

print("La suma total es:", suma)
print("El promedio es:", promedio)
