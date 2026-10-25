def solution(number):
    soma = 0
    
    if number < 0:
        return 0
    
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            soma += i
        elif i % 3 == 0:
            soma += i
        elif i % 5 == 0:
            soma += i
    return soma
  