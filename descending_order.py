def descending_order(num):
    # Frequência para cada dígito de 0 a 9
    counts = [0] * 10
    
    # 1. Conta quantas vezes cada dígito aparece
    for char in str(num):
        counts[int(char)] += 1
    
    # 2. Constrói a string do maior dígito (9) para o menor (0)
    resultado = []
    for digit in range(9, -1, -1):
        if counts[digit] > 0:
            resultado.append(str(digit) * counts[digit])
            
    return ''.join(resultado)


Lista = [42145, 145263, 123456789]
Validacao = [54421, 654321, 987654321]

for m in range(len(Lista)):
    resultado = descending_order(Lista[m])
    print('R', resultado)
    print('V', Validacao[m])


'''
num = str(num)
    L = []
    n = ''

    for k in range(len(num)):
        L.append(int(num[k]))
        
    for i in range(len(L) - 1):
        for j in range(i+1, len(L)):                        
            while L[i] < L[j]:
                L[i], L[j] = L[j], L[i]

    for a in L:
        n += str(a)          
            
    return n

'''