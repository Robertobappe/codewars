def find_it(seq):
    t = {}
    
    for i in seq:
        if i in t:
            t[i] += 1
        else:
            t[i] = 1
            
    for j, k in t.items():
        if k % 2 != 0:
            return j
        
