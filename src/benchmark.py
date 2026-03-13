import time as temporizador
from preteste import pre_teste
import random as randomizador
import matplotlib.pyplot as mpl

def medir_tempo_preteste(numero):
    inicio = temporizador.perf_counter()
    pre_teste(numero)
    fim = temporizador.perf_counter()
    return fim - inicio


def medir_tempo_miller_rabin(numero):
    inicio = temporizador.perf_counter()
    #miller_rabin(numero)
    fim = temporizador.perf_counter()
    return fim - inicio


def gerar_bigint(bits):
    return randomizador.getrandbits(bits)


def executar_teste(numero):
    tempo_preteste = medir_tempo_preteste(numero)
    tempo_miller_rabin = 0
    if pre_teste(numero):
        tempo_miller_rabin = medir_tempo_miller_rabin(numero)
    return tempo_preteste, tempo_miller_rabin


def benchmark(lista_bits, repeticoes=10):
    numeros = []
    medias_preteste = []
    medias_miller_rabin = []
    medias_total = []

    for b in lista_bits:
        soma_pre = 0
        soma_mr = 0
        soma_total = 0

        numero = gerar_bigint(b)
        numeros.append(numero)

        for _ in range(repeticoes):
            tempo1 = medir_tempo_preteste(numero)
            tempo2 = 0
            if pre_teste(numero):
                tempo2 = medir_tempo_miller_rabin(numero)

            soma_pre += tempo1
            soma_mr += tempo2
            soma_total += tempo1 + tempo2

        medias_preteste.append(soma_pre / repeticoes)
        medias_miller_rabin.append(soma_mr / repeticoes)
        medias_total.append(soma_total / repeticoes)

    return numeros, medias_preteste, medias_miller_rabin, medias_total


def mostrar_resultados(numeros, bits, tempos_preteste, tempos_miller_rabin):
    for i in range(len(bits)):
        print("Número: ", numeros[i], "\nBits: ", bits[i], "\nTempo pré-teste: ", tempos_preteste[i], " segundos\nTempo teste de Miller-Rabin: ", tempos_miller_rabin[i], " segundos\n")


def gerar_grafico(bits, tempos_preteste, tempos_miller_rabin, tempos_totalizado, log=False):
    mpl.figure(figsize=(8,5))

    mpl.plot(bits, tempos_preteste, marker="o", label="Pré-teste")
    mpl.plot(bits, tempos_miller_rabin, marker="o", label="Miller-Rabin")
    mpl.plot(bits, tempos_totalizado, marker="o", label="Tempo total")

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


def main():
    bits = [32, 64, 128, 256, 512, 1024, 2048]
    numeros, tempos_preteste, tempos_miller_rabin, tempos_total = benchmark(bits)
    mostrar_resultados(numeros, bits, tempos_preteste, tempos_miller_rabin)
    mostrar_tabela(bits, tempos_preteste, tempos_miller_rabin, tempos_total)
    gerar_grafico(bits, tempos_preteste, tempos_miller_rabin, tempos_total)
    gerar_grafico(bits, tempos_preteste, tempos_miller_rabin, tempos_total, True)


if __name__ == "__main__":
    main()