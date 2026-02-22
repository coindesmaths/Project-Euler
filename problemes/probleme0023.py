from utils.entiers import Entiers


def probleme0023():
    abundants = [
        i for i in range(1, 28124) if i < sum(Entiers.facteurs_uniques(i)[:-1])
    ]
    sommes = set(a + b for a in abundants for b in abundants if a + b < 28124)
    return 28123 * 28124 // 2 - sum(sommes)
