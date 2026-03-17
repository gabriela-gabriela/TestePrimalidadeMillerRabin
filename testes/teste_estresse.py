import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from teste_primalidade.teste_primalidade_miller_rabin import miller_rabin

import random
import time
import sympy  #vai ter o resultado certo pra comparar

def stress_test_miller_rabin(n_testes=200):
    print(f"{n_testes} testes...\n")
    erros = []

    for i in range(n_testes):
        bits = random.choice([8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) #tamanhos de bits
        n = random.getrandbits(bits) | 1

        esperado = sympy.isprime(n)

        inicio = time.perf_counter()
        resultado = miller_rabin(n, 40)
        tempo = (time.perf_counter() - inicio) * 1000

        if (not esperado and "primo" in resultado) or (esperado and "composto" in resultado):
            erros.append({
                "n": n,
                "bits": bits,
                "esperado": esperado,
                "resultado": resultado
            })
            print(f"FALHA no teste {i+1}")
            print(f"  n        = {n}")
            print(f"  esperado = {esperado}")
            print(f"  resultado   = {resultado}\n")
        else:
            print(f"Teste {i+1:3d} | {bits:5d} bits | {tempo:.3f}ms")

    print(f"\n{'='*40}")
    if not erros:
        print(f"Todos os testes passaram.")
    else:
        print(f"{len(erros)} erro(s) encontrado(s).")


stress_test_miller_rabin()
