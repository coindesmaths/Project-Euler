import itertools


def probleme0024():
    n = 9
    p = 1000000
    num = tuple(k for k in range(10))
    string = "".join(list(map(lambda x: str(x), range(10))))
    permut = list(itertools.permutations(string))[p - 1]
    result = "".join(permut)
    return result
