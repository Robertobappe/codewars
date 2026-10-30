def create_phone_number(n):
    c = '('
    p = n[:3]
    s = n[3:6]
    t = n[6:]
    
    for i in p:
        c += str(i)
    c += ')'
    c += ' '
    
    for j in s:
        c+= str(j)
    c += '-'
    
    for k in t:
        c += str(k)
    return c