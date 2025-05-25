import numpy as np
import matplotlib.pyplot as plt

cats = ['A', 'B', 'C']    # categorías
vals = [5, 7, 3]          # valores

plt.figure()
plt.pie(vals, labels=cats, autopct='%1.1f%%')
plt.title('Pie simple')
plt.show()

explode = [0.1,0,0]
plt.figure()
plt.pie(vals, labels=cats, explode=explode, autopct='%1.1f%%')
plt.title('Pie exploded')
plt.show()

plt.figure()
plt.pie(vals, labels=cats, shadow=True, autopct='%1.1f%%')
plt.title('Pie con sombra')
plt.show()

plt.figure()
plt.pie(vals, labels=cats, wedgeprops={'width':0.4}, autopct='%1.1f%%')
plt.title('Donut chart')
plt.show()

