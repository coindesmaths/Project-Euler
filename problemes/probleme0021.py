from utils.entiers import Entiers


def probleme0021():
    n = 10000
    d = lambda k: sum(Entiers.facteurs(k)) - k
    result = 0
    amicable = []
    for k in range(1, n):
        if k not in amicable:
            t = d(k)
            if d(t) == k and k != t:
                amicable += [k, t]
    for num in amicable:
        result += num
    return result
