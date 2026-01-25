def probleme0009():
    n = 1000
    result = (0, 0, 0)
    for c in range(n):
        for b in range(c):
            for a in range(b):
                if a + b + c == n:
                    if a**2 + b**2 == c**2:
                        return a * b * c
