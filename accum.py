def accum(st):
    s = ''
    
    for i in range(len(st)):
        s += st[i].upper() + (st[i]*i).lower() + '-'
    return s[:-1]