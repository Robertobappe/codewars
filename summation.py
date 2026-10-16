def summation(num):
    soma = 0    
    for i in range(1, num+1):
        soma += i
        
    return soma
        
    
L = [1, 8, 22]

for i in L:
    print(f'Number: {i} resultado: {summation(i)}')