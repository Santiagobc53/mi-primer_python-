import matplotlib.pyplot as plt
import plotly.express as px

# Datos
labels = ['Manzanas', 'Bananas', 'Cerezas', 'Dátiles']
sizes = [15, 30, 45, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
explode = (0, 0.1, 0, 0)

# Gráfico básico
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('1. Gráfico de Pie Básico')
plt.show()

# Gráfico con explosión
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode)
plt.title('2. Gráfico con Explosión')
plt.show()

# Gráfico con colores personalizados
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
plt.title('3. Gráfico con Colores Personalizados')
plt.show()

# Gráfico de dona
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
centro = plt.Circle((0, 0), 0.70, fc='white')
plt.gca().add_artist(centro)
plt.title('4. Gráfico de Dona')
plt.show()

# Gráfico con rotación
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('5. Gráfico con Rotación')
plt.show()

# Gráfico con sombra simulando 3D
plt.figure(figsize=(6, 4))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
plt.title('6. Gráfico con Sombra (3D Simulado)')
plt.show()

# Gráfico interactivo con Plotly
data = {'Fruta': labels, 'Cantidad': sizes}
fig = px.pie(data, names='Fruta', values='Cantidad', title='7. Gráfico Interactivo con Plotly')
fig.show()