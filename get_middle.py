def get_middle(s):
    tam = len(s)
    d = tam%2
    
    if d == 0:
        m = tam//2
        return s[m-1:m+1]
    
    m = round((tam-1)/2)
    return s[m]
