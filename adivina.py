# Juego para adivinar un número aleatorio del 1 al 10

import random  # Importa la librería de números aleatorios

numero_secreto = random.randint(1, 10)  # Número aleatorio entre 1 y 10
intento = int(input("Adivina un número del 1 al 10: "))

if intento == numero_secreto:
    print("¡Correcto! 🎉 Adivinaste el número.")
else:
    print("¡Incorrecto! 😅 El número era", numero_secreto)
