def DNA_strand(dna):
    c = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    s = ''
    for i in range(len(dna)):
        s += c[dna[i]]
        
    return s