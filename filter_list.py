def filter_list(l):
    L = []
    for i in range(len(l)):
        if type(l[i]) == int:
            L.append(l[i])
    return L