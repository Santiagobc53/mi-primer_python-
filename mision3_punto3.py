import numpy as np
import matplotlib.pyplot as plt

cats = ['A','B','C']
vals = [5,7,3]
plt.figure()
plt.bar(cats, vals)
plt.title('Barras verticales')
plt.show()

plt.figure()
plt.barh(cats, vals)
plt.title('Barras horizontales')
plt.show()

x = np.arange(len(cats))
v2 = [4,6,5]
width = 0.35
plt.figure()
plt.bar(x - width/2, vals, width, label='Serie1')
plt.bar(x + width/2, v2, width, label='Serie2')
plt.xticks(x, cats)
plt.legend()
plt.title('Barras agrupadas')
plt.show()

plt.figure()
plt.bar(x, vals,  width, label='S1')
plt.bar(x, v2,    width, bottom=vals, label='S2')
plt.xticks(x, cats)
plt.legend()
plt.title('Barras apiladas')
plt.show()

colores = ['skyblue','salmon','lime']
hatchs   = ['/', '\\', 'x']
plt.figure()
for i in range(len(cats)):
    plt.bar(cats[i], vals[i],
            color=colores[i],
            edgecolor='black',
            hatch=hatchs[i])
plt.title('Barras personalizadas')
plt.show()


