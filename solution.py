def solution(text, ending):
    s = ''
    for i in range(len(text)):
        if text[i] == ending[0]:
            s = text[i:]
            if s == ending:
                return True
    return False