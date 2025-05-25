# Leer 5 números y determinar el mayor y el menor SIN usar for

n1 = int(input("Ingrese el número 1: "))
n2 = int(input("Ingrese el número 2: "))
n3 = int(input("Ingrese el número 3: "))
n4 = int(input("Ingrese el número 4: "))
n5 = int(input("Ingrese el número 5: "))

mayor = n1
menor = n1

# Comparaciones para encontrar el mayor
if n2 > mayor:
    mayor = n2
if n3 > mayor:
    mayor = n3
if n4 > mayor:
    mayor = n4
if n5 > mayor:
    mayor = n5

# Comparaciones para encontrar el menor
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4
if n5 < menor:
    menor = n5

print("El número mayor es:", mayor)
print("El número menor es:", menor)