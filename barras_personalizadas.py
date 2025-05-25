import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
categorias = ['A', 'B', 'C', 'D']
valores1 = [10, 15, 7, 12]
valores2 = [5, 9, 4, 6]

def barras_verticales():
    plt.bar(categorias, valores1, color='skyblue')
    plt.title('Barras Verticales')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.show()

def barras_horizontales():
    plt.barh(categorias, valores1, color='orange')
    plt.title('Barras Horizontales')
    plt.xlabel('Valores')
    plt.ylabel('Categorías')
    plt.show()

def barras_agrupadas():
    x = np.arange(len(categorias))
    width = 0.35
    plt.bar(x - width/2, valores1, width, label='Serie 1', color='green')
    plt.bar(x + width/2, valores2, width, label='Serie 2', color='purple')
    plt.title('Barras Agrupadas')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.xticks(x, categorias)
    plt.legend()
    plt.show()

def barras_apiladas():
    plt.bar(categorias, valores1, label='Serie 1', color='blue')
    plt.bar(categorias, valores2, bottom=valores1, label='Serie 2', color='red')
    plt.title('Barras Apiladas')
    plt.xlabel('Categorías')
    plt.ylabel('Valores Totales')
    plt.legend()
    plt.show()

def barras_personalizadas():
    colores = ['#FF5733', '#33FF57', '#3357FF', '#F1C40F']
    estilos_borde = ['-', '--', '-.', ':']
    for i in range(len(categorias)):
        plt.bar(categorias[i], valores1[i], color=colores[i], edgecolor='black', hatch=estilos_borde[i % len(estilos_borde)])
    plt.title('Barras Personalizadas')
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.show()

# Menú para elegir el tipo de gráfica
def menu():
    while True:
        print("\nTIPOS DE GRÁFICAS DE BARRAS:")
        print("1. Barras Verticales")
        print("2. Barras Horizontales")
        print("3. Barras Agrupadas")
        print("4. Barras Apiladas")
        print("5. Barras Personalizadas")
        print("0. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            barras_verticales()
        elif opcion == '2':
            barras_horizontales()
        elif opcion == '3':
            barras_agrupadas()
        elif opcion == '4':
            barras_apiladas()
        elif opcion == '5':
            barras_personalizadas()
        elif opcion == '0':
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar menú
menu()