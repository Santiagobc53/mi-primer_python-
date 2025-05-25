#!/usr/bin/env python3
"""
Cuenta cuántos números primos hay entre 1 y 1 000 000
Método: Criba de Eratóstenes
"""

import math
import time

LIMITE = 1_000_000        # 1 millón

def contar_primos_hasta(n: int) -> int:
    """Devuelve la cantidad de números primos ≤ n."""
    if n < 2:
        return 0

    # Paso 1: suponer que todos los números son primos
    es_primo = bytearray(b"\x01") * (n + 1)
    es_primo[0:2] = b"\x00\x00"           # 0 y 1 no son primos

    # Paso 2: tachar múltiplos
    limite = int(math.isqrt(n)) + 1
    for p in range(2, limite):
        if es_primo[p]:
            es_primo[p*p : n+1 : p] = b"\x00" * ((n - p*p)//p + 1)

    # Paso 3: contar los que quedaron en 1
    return sum(es_primo)

if __name__ == "__main__":
    inicio = time.perf_counter()
    total_primos = contar_primos_hasta(LIMITE)
    duracion = time.perf_counter() - inicio

    print(f"Entre 1 y {LIMITE:,} hay {total_primos:,} números primos.")
    print(f"Tiempo de cálculo: {duracion:.3f} segundos")
