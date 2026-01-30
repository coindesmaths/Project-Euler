def probleme0014():
    n = 1000000
    maxi = []
    for k in range(1, n + 1):
        flight = [k]
        while k != 1:
            if k % 2 == 0:
                k = k // 2
            else:
                k = 3 * k + 1
            flight += [k]
        if len(flight) > len(maxi):
            maxi = flight
    return maxi[0]
