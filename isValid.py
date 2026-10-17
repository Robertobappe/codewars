def isValid(s):
    open_char = {'(', '{', '[',}
    chars = {')':'(', '}':'{', ']':'['}
    pilha = []

    for i in s:
        if i in open_char:
            pilha.append(i)
        else:
            if chars[i] != pilha[-1]:
                return False
            else:
                chars[i] == pilha[-1]
                pilha.pop() 
    print(pilha)   
    return True if len(pilha) == 0 else False


L = ['(]']
print(isValid(L[0]))