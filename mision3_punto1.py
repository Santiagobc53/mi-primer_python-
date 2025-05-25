import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure()
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Líneas múltiples')
plt.legend()
plt.show()

plt.figure()
plt.plot(x, y1, marker='o', markevery=10)
plt.title('Línea con marcadores')
plt.show()

plt.figure()
plt.plot(x, y1, linestyle='-',  label='sólida')
plt.plot(x, y2, linestyle='--', label='discontinua')
plt.title('Estilos de línea')
plt.legend()
plt.show()

plt.figure()
plt.plot(x, y1)
plt.fill_between(x, y1, alpha=0.3)
plt.title('Sombreado bajo la curva')
plt.show()

fig = px.line(x=x, y=y1,
              labels={'x':'x','y':'sin(x)'},
              title='Línea interactiva Plotly')
fig.show()

sns.set_theme()
plt.figure()
sns.lineplot(x=x, y=y1)
plt.title('Línea suavizada Seaborn')
plt.show()

y3 = 0.5*np.sin(x)+1
y4 = 0.3*np.cos(x)+2
plt.figure()
plt.stackplot(x, y1, y3, y4, labels=['sin','serie2','serie3'])
plt.legend(loc='upper right')
plt.title('Líneas apiladas')
plt.show()



