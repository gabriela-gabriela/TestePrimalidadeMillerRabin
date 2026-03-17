def decomposicao(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d = d // 2
        s += 1
    return s, d
