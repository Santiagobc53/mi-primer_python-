import matplotlib.pyplot as plt   # corregido de 'pylot' a 'pyplot'

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]              # uso de lista en lugar de set

plt.plot(x, y)
plt.title("Gráfico de línea Simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.show()
