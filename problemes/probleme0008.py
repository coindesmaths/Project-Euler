from utils.data import Data


def probleme0008():
    n = Data.init(8).replace("\n", "")
    maxi = 0
    for k in range(len(n) - 12):
        numbers = list(map(lambda x: int(x), list(n[k : k + 13])))
        produit = 1
        for k in numbers:
            produit *= k
        maxi = max(maxi, produit)
    return maxi
