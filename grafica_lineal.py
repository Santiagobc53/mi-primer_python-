import matplotlib.pyplot as plt
import numpy as np 

def grafica_linea():
    x = [1, 2, 3, 4, 5] 
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.title("Gráfico de Línea Simple")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.show()

grafica_linea()

def grafica_barras():
    categorias = ['Ene', 'Feb', 'Mar', 'Abr', 'May']
    valores = [10, 15, 7, 12, 9]
    plt.bar(categorias, valores)
    plt.title("Ventas por mes")
    plt.xlabel("Mes")
    plt.ylabel("Ventas")
    plt.show()

grafica_barras()

def grafica_pastel():
    categorias = ['Cardio', 'Fuerza', 'Yoga', 'Ciclismo']
    valores = [30, 40, 15, 15]
    plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=90)
    plt.title("Distribución de Rutinas de Entrenamiento")
    plt.axis('equal') 
    plt.show()
    
grafica_pastel()


