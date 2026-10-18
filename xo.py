def xo(s):
    s = s.lower()
    t = {'o':0, 'x':0}
  
    for i in range(len(s)):
        if s[i] in t:
            t[s[i]] += 1
          
    return t['o'] == t['x']
