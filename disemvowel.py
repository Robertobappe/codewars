def disemvowel(string_):
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    newString = ''
    
    for i in range(len(string_)):
        if string_[i].lower() not in vowels:
            newString += string_[i]
    
    return newString

