from teste_primalidade_miller_rabin import miller_rabin

def main():
   print(f"{'\033[1m'}═"*46)
   print(f"     TESTE DE PRIMALIDADE DE MILLER-RABIN")
   print(f"═"*46 + f"{'\033[0m'}\n")
   while True:
      try:
         n = int(input("Digite um inteiro para descobrir se é primo: "))
         break
      except ValueError:
         print("Entrada inválida, digite um inteiro.")
   
   while True:
      resposta = input("Deseja escolher um valor para k? (digite sim ou não) ")
      if resposta not in ("sim", "não"):
         print("Resposta inválida.")
         pass
      else:
         break
   
   if resposta == "sim":
      while True:
         try:
            k = int(input("Digite o valor k: "))
            break
         except ValueError:
            print("Entrada inválida, digite um inteiro.")

      resultado = miller_rabin(n, k)
	
   else:
      resultado = miller_rabin(n)
   
   print('\n' + resultado)


if __name__ == "__main__":
   main()