def solution(string):
    return string[::-1]
    


L = ['world', 'word']
for i in range(len(L)):
    print(f'word: {L[i]} <-> reverse: {solution(L[i])}') 
