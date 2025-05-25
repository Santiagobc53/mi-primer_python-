import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generamos datos de ejemplo
data_box = np.random.randn(100)

# Creamos la figura
plt.figure()

# Violin plot
sns.violinplot(data=data_box)

# Título y mostrar
plt.title('Violin Plot')
plt.show()

