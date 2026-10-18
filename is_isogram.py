def is_isogram(string):
    string = string.lower()
    t = {}
    
    if len(string) == 0:
        return True
    
    for i in range(len(string)):
        if string[i] in t:
            return False
        t[string[i]] = 1
        
    return True
