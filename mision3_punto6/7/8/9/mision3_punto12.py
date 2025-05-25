import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.arange(0,10)
y1 = x
y2 = x**1.5
y3 = np.log1p(x)

plt.figure()
plt.plot(x, y1, label='lineal')
plt.bar(x, y2, alpha=0.4, label='bar')
plt.scatter(x, y3, color='k', label='scatter')
plt.xlabel('Eje X compartido')
plt.legend()
plt.title('Tres tipos en mismo eje X')
plt.show()
