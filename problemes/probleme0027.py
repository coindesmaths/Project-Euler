from utils.premiers import NombresPremiers


def probleme0027():
    a_max = 0
    b_max = 0
    n_max = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while True:
                if n**2 + a * n + b < 0 or not NombresPremiers.est_premier(
                    n**2 + a * n + b
                ):
                    break
                n += 1
            if n > n_max:
                n_max = n
                a_max = a
                b_max = b
    return a_max * b_max
