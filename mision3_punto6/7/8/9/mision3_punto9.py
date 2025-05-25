import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x_a = np.arange(0,5)
a   = [1,3,2,5,4]
b   = [2,2,3,3,5]
plt.figure()
plt.fill_between(x_a, a, alpha=0.5, label='A')
plt.fill_between(x_a, b, alpha=0.5, label='B')
plt.legend()
plt.title('Gráfica de áreas')
plt.show()
