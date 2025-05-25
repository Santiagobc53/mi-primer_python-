import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X, Y = np.meshgrid(np.linspace(-2,2,30), np.linspace(-2,2,30))
Z    = X**2 + Y**2
fig  = plt.figure()
ax   = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('Superficie 3D')
plt.show()
