# retornos 1, 2 e 3 corresponde respectivamente a "composto", "primo", "incerto"
def pre_teste(numero):
    if numero < 2:
        return 1
    
    primos_pequenos = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    
    if numero in primos_pequenos:
        return 2

    for primo in primos_pequenos:
        if numero % primo == 0:
            return 1
  
    return 3
