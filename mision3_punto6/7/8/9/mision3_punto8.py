import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

matriz = np.random.rand(8,8)
plt.figure(figsize=(6,5))
sns.heatmap(matriz, annot=True, fmt=".2f")
plt.title('Heatmap')
plt.show()
