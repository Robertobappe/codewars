def get_sum(a,b):
    s = 0
    max_val = float('-inf')
    min_val = float('inf')
    
    if a == b:
        return a
    elif a > b:
        max_val = a
        min_val = b
    else:
        max_val = b
        min_val = a        
    
    for i in range(min_val,max_val+1):
        s += i
    return s

    
        