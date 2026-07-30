def probleme0029():
    n_max = 100
    s = set()
    for a in range(2, n_max + 1):
        for b in range(2, n_max + 1):
            s.add(a**b)
    return len(s)
