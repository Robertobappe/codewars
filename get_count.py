def get_count(sentence):
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    sentence = sentence.lower()
    sentence = ''.join(sentence)
    quant_vowels = 0
    
    for i in range(len(sentence)):
        if sentence[i] in vowels:
            quant_vowels += 1
    
    return quant_vowels 
    
    