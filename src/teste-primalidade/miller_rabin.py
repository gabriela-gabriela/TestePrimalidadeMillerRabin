def eh_testemunha(a, n, s, d):
    x = pow(a, d, n)

    if x == 1 or x == n-1:
        return False
    
    for _ in range(s-1):
        x = pow(x, 2, n)
        
        if x == n-1:
            return False
    
    return True