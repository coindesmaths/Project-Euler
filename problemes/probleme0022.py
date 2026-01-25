from utils.data import Data


def probleme0022():
    data = Data.init(22)
    noms = sorted(list(map(lambda x: x[1:-1], data.split(","))))

    S = 0
    for k in range(len(noms)):
        score = sum(map(lambda x: ord(x) - 64, noms[k]))
        S += (k + 1) * score
    return S
