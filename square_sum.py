def square_sum(numbers):
    soma = 0
    for i in numbers:
        soma += i**2
    
    return soma

L = [[1,2], [-1,0,1]]

for i in L:
    print(f'resultado {square_sum(i)}')