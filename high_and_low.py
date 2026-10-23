def high_and_low(numbers):
    L = numbers.split()
    min_val = float('inf')
    max_val = float('-inf')    
    
    for i in range(len(L)):
        if int(L[i]) < min_val:
            min_val = int(L[i])
        
        if int(L[i]) > max_val:
            max_val = int(L[i])
            
    return str(max_val) + ' ' + str(min_val)
