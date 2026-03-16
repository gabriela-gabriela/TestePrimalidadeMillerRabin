import miller_rabin

def teste_primos_conhecidos():
    primos_conhecidos = [7919, 104729, 1299709, 15485863, 32452843]
    
    print("--- Testando contra Primos Conhecidos (Esperado: 0% de Falsos Negativos) ---")
    print("-" * 55)
    print(f"{'Número Primo':<15} | {'Resultado (com k=1)':<30}")
    print("-" * 55)
    
    erros_primos = 0
    for p in primos_conhecidos:
        resultado = miller_rabin(p, k=1)
        print(f"{p:<15} | {resultado:<30}")
        if resultado == "Composto":
            erros_primos += 1
            
    taxa_erro_primos = (erros_primos / len(primos_conhecidos)) * 100
    print("-" * 55)
    print(f"Taxa de erro para Primos Reais: {taxa_erro_primos:.2f}%\n")


def teste_numeros_carmichael():
    numeros_carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341]
    valores_de_k = [1, 2, 3, 5, 10] 
    rodadas_por_numero = 1000

    print("--- Testando Falsos Positivos com Números de Carmichael ---")
    print("-" * 55)
    print(f"{'Valor de k':<12} | {'Falsos Positivos':<18} | {'Margem de Erro':<18}")
    print("-" * 55)

    for k in valores_de_k:
        falsos_positivos = 0
        total_testes = 0

        for num in numeros_carmichael:
            for _ in range(rodadas_por_numero):
                total_testes += 1
                resultado = miller_rabin(num, k)

                if resultado == "Provavelmente primo":
                    falsos_positivos += 1
        
        taxa_erro = (falsos_positivos / total_testes) * 100
        print(f"{k:<12} | {falsos_positivos:<18} | {taxa_erro:.2f}%")
        
    print("-" * 55)


def main():
    print("Iniciando Análise de Confiabilidade do Miller-Rabin...\n")
    teste_primos_conhecidos()
    teste_numeros_carmichael()


if __name__ == "__main__":
    main()