def square_digits(num):
    num = str(num)
    soma = ''
    
    for i in range(len(num)):
        soma += str(int(num[i])**2)
        
    return int(soma)

L = [9119, 765]
for i in L:
    print(square_digits(i))

