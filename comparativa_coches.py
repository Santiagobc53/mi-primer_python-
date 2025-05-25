import matplotlib.pyplot as plt
import numpy as np

# Modelos a comparar
carros = ['Toyota GR Yaris', 'Subaru WRX']

# Precios en USD (ajusta con datos reales si los tienes)
precios = [36000, 30000]

# Potencia en caballos de fuerza (hp)
potencia = [261, 271]

# Consumo en litros por cada 100 km
consumo_l_per_100km = [7.4, 9.8]
# Caballos de fuerza por cada $1000
hp_por_1000usd = [
    p / (c / 1000)
    for p, c in zip(potencia, precios)
]

# Km por litro
km_por_litro = [100 / c for c in consumo_l_per_100km]

# Km/L por cada $1000
kmpl_por_1000usd = [
    k / (c / 1000)
    for k, c in zip(km_por_litro, precios)
]
# Ejes X
x = np.arange(len(carros))
ancho = 0.35

plt.figure()

# Barras de potencia
plt.bar(x - ancho/2, hp_por_1000usd, ancho, label='Hp por $1000')

# Barras de consumo
plt.bar(x + ancho/2, kmpl_por_1000usd, ancho, label='Km/L por $1000')

# Etiquetas y estilo
plt.xticks(x, carros, rotation=15, ha='right')
plt.xlabel('Modelo')
plt.ylabel('Ratio costo-beneficio')
plt.title('Comparación: potencia vs consumo')
plt.legend()
plt.grid(True)

# Muestra la gráfica
plt.tight_layout()
plt.show()

