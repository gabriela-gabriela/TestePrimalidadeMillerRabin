import random
from preteste import pre_teste
from decomposicao import decomposicao
from teste_eh_testemunha import eh_testemunha

#ver se acha um jeito de encontrar um melhor k de vezes pra testar
def miller_rabin(n, k):
   preteste = pre_teste(n)
   if preteste == 2:
      return "O número é primo - Nível de certeza: 100%"
   if preteste == 1:
      return "O número é composto - Nível de certeza: 100%"
   
   s, d = decomposicao(n)

   for _ in (range(k)):
      a = random.randint(2, n - 2)
      if eh_testemunha(a, n, s, d):
         return "não é primo"

   prob_acerto = (1 - ((1/4) ** k)) * 100
   return f"o número é provavelmente primo - Nível de certeza: {prob_acerto:.10f}%"
