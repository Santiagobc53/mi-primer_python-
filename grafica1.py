import matplotlib.pyplot as plt

# Datos de ejemplo: días promedio hasta notar mejoría
medicamentos = ['Lurasidona', 'Risperidona']
tiempos = [5, 3]  # Valores hipotéticos

# Crear gráfica de barras
plt.figure()
plt.bar(medicamentos, tiempos)
plt.xlabel('Medicamento')
plt.ylabel('Días para notar mejoría')
plt.title('Comparación de rapidez de resultados')
plt.grid(True)
plt.show()
