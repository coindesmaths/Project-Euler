def probleme0028():
    dim = 1001
    resultat = n = 1
    for k in range(2, dim, 2):
        for j in range(4):
            n += k
            resultat += n
    return resultat
