import matplotlib.pyplot as plt
categorias = ['Enero', 'Febrero', 'Marzo', 'Abril']
valores = [10, 15, 7, 12]
colores = ['red', 'yellow','green','purple']

plt.bar(categorias, valores)
plt.bar(categorias,valores, color=colores)
plt.grid(True, axis='y', alpha=0.7, zorder=1)
plt.title('Ventas por Mes')
plt.xlabel('Meses')
plt.ylabel('Cantidad de ventas')

plt.show()