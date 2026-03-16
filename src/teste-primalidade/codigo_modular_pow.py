import random

def modular_pow(base, expoente, mod):
    resultado = 1
    base = base % mod

    while expoente > 0:
        if expoente % 2 == 1:
            resultado = (resultado * base) % mod 

        expoente = expoente // 2

        base = (base * base) % mod 

    return resultado


def base_aleatoria(n):
    return random.randint(2, n - 2)
