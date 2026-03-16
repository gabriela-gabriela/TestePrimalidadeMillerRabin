from teste_primalidade_miller_rabin import miller_rabin

def main():
   while True:
      try:
         n = int(input("Digite um inteiro para descobrir se é primo: "))
         break
      except ValueError:
         print("Entrada inválida, digite um inteiro.")
   
   while True:
      resposta = input("Deseja escolher um valor para k? (digite sim ou não)")
      if resposta not in ("sim", "não"):
         print("Resposta inválida.")
         pass
      else:
         break
   
   if resposta == "sim":
      while True:
         try:
            k = int(input("Digite um inteiro para descobrir se é primo: "))
            break
         except ValueError:
            print("Entrada inválida, digite um inteiro.")

      resultado = miller_rabin(n, k)
	
   else:
      # ainda tenho q fazer esse
      resultado = miller_rabin_sem_k(n)
   
   print(resultado)


if __name__ == "__main__":
   main()
