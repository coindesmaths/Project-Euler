import itertools


def probleme0030():

    def trouver_limite() -> int:
        for k in itertools.count(1):
            n = k * 9**5
            if len(str(n)) <= k:
                return n

    s = 0
    for n in range(2, trouver_limite()):
        digit_sum = sum(int(d) ** 5 for d in str(n))
        if n == digit_sum:
            s += n
    return s
