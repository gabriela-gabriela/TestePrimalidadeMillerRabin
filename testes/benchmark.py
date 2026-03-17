import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "src"))

from teste_primalidade.teste_primalidade_miller_rabin import miller_rabin
import time as temporizador
from teste_primalidade.preteste import pre_teste
import random as randomizador
import matplotlib.pyplot as mpl

def medir_tempo_preteste(numero):
    inicio = temporizador.perf_counter()
    resultado = pre_teste(numero)
    fim = temporizador.perf_counter()
    return resultado, fim - inicio


def medir_tempo_miller_rabin(numero, k):
    inicio = temporizador.perf_counter()
    resultado = miller_rabin(numero, k)
    fim = temporizador.perf_counter()
    return resultado, fim - inicio


def gerar_bigint(bits):
    return randomizador.getrandbits(bits)


def gerar_int_que_roda_miller_rabin(bits):
    primos_pequenos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    while True:
        n = randomizador.getrandbits(bits) | 1
        if n > 97 and all(n % p != 0 for p in primos_pequenos):
            return n

def benchmark(lista_bits, repeticoes=10, k=40):
    print(f"Iniciando testes para {repeticoes} caso(s) por quantidade de bits (é normal que o processo demore para muitos bits).")
    medias_preteste = []
    medias_miller_rabin = []
    medias_total = []

    for b in lista_bits:
        print(f"testando para {b} bits...")
        soma_pre = 0
        soma_mr = 0
        soma_total = 0
        entrou_mr = 0

        for _ in range(repeticoes):
            numero = gerar_int_que_roda_miller_rabin(b)

            # Pré-teste
            resultado_pre, tempo_pre = medir_tempo_preteste(numero)

            # Miller-Rabin
            resultado_mr, tempo_mr = medir_tempo_miller_rabin(numero, k) if resultado_pre == 3 else (None, 0)
 
            if resultado_pre == 3:
                entrou_mr += 1
            
            soma_mr += tempo_mr
            soma_pre += tempo_pre
            soma_total += tempo_mr + tempo_pre

        medias_preteste.append(soma_pre / repeticoes)
        medias_miller_rabin.append(soma_mr / entrou_mr if entrou_mr > 0 else 0)
        medias_total.append(soma_total / repeticoes)

    return medias_preteste, medias_miller_rabin, medias_total


def mostrar_resultados(bits, tempos_preteste, tempos_miller_rabin):
    for i in range(len(bits)):
        print("\nBits: ", bits[i], "\nTempo médio pré-teste: ", tempos_preteste[i], " segundos\nTempo medio teste de Miller-Rabin: ", tempos_miller_rabin[i], " segundos\n")


def gerar_grafico(bits, tempos_preteste, tempos_miller_rabin, tempos_totalizado, log=False):
    mpl.figure(figsize=(8,5))

    mpl.plot(bits, tempos_preteste, marker="o", label="Pré-teste")
    mpl.plot(bits, tempos_totalizado, marker="^", label="Tempo total")
    mpl.plot(bits, tempos_miller_rabin, marker="o", label="Miller-Rabin")

    mpl.xlabel("Tamanho do número (bits)")
    mpl.ylabel("Tempo de execução (s)")

    if log:
        mpl.title("Performance do Teste de Primalidade (Escala Log)")
        mpl.yscale("log")
    else:
        mpl.title("Performance do Teste de Primalidade")

    mpl.legend()
    mpl.tight_layout()
    mpl.grid(True, linestyle="--", alpha=0.6)
    mpl.show()


def mostrar_tabela(bits, tempos_preteste, tempos_miller_rabin, tempos_total):
    print("\nResultados do Benchmark\n")
    print(f"{'Bits':<10}{'Pré-teste (s)':<20}{'Miller-Rabin (s)':<20}{'Total (s)':<15}")
    print("-" * 65)

    for i in range(len(bits)):
        print(f"{bits[i]:<10}{tempos_preteste[i]:<20.8f}{tempos_miller_rabin[i]:<20.8f}{tempos_total[i]:<15.8f}")


def main(repeticoes=3, k=40):
    bits = [32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    tempos_preteste, tempos_miller_rabin, tempos_total = benchmark(bits, repeticoes, k)

    mostrar_resultados(bits, tempos_preteste, tempos_miller_rabin)
    mostrar_tabela(bits, tempos_preteste, tempos_miller_rabin, tempos_total)

    gerar_grafico(bits, tempos_preteste, tempos_miller_rabin, tempos_total)
    gerar_grafico(bits, tempos_preteste, tempos_miller_rabin, tempos_total, True)


if __name__ == "__main__":
    repeticoes = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    main(repeticoes, k=40)


