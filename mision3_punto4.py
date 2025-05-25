import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

x_sc = np.random.rand(50)
y_sc = np.random.rand(50)
plt.figure()
plt.scatter(x_sc, y_sc)
plt.title('Scatter básico')
plt.show()

plt.figure()
plt.scatter(x_sc, y_sc, c=y_sc, cmap='viridis')
plt.title('Scatter con gradiente')
plt.colorbar(label='valor y')
plt.show()

sizes = 100 * np.random.rand(50)
plt.figure()
plt.scatter(x_sc, y_sc, s=sizes)
plt.title('Scatter con tamaños')
plt.show()

fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')
z_sc = np.random.rand(50)
ax.scatter(x_sc, y_sc, z_sc)
ax.set_title('Scatter 3D')
plt.show()

df = px.data.iris()  # ejemplo de dataset
fig = px.scatter(df, x='sepal_width', y='sepal_length',
                 color='species', size='petal_length')
fig.show()
