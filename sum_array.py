def sum_array(a):
    soma = 0
    if a is None:
        return 0
    
    for i in a:
        soma += i
    return soma