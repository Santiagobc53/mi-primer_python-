import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randn(1000)
plt.figure()
plt.hist(data, bins=30)
plt.title('Histograma simple')
plt.show()

plt.figure()
plt.hist(data, bins=30, density=True)
plt.title('Histograma densidad')
plt.show()

plt.figure()
plt.hist(data, bins=30, cumulative=True)
plt.title('Histograma acumulativo')
plt.show()

plt.figure()
sns.histplot(data, bins=30, kde=True)
plt.title('Histograma con KDE')
plt.show()

