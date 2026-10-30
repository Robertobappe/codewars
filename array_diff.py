def array_diff(a, b):
    c = []
    
    for i in range(len(a)):
        if not b:
            return a
        
        elif a[i] not in b:
            c.append(a[i])    
    return c