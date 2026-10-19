def find_short(s):
    s = s.split()
    min_word = float('inf')
    
    for i in s:
        if len(i) < min_word:
            min_word = len(i)
            
    return min_word