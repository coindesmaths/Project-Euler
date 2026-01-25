from utils.entiers import Entiers


def probleme0005():
    D = {}
    for k in range(2, 21):
        diviseurs_premiers = Entiers.facteurs_premiers(k)
        for div in diviseurs_premiers:
            if div in D.keys():
                D[div] = max(D[div], diviseurs_premiers.count(div))
            else:
                D[div] = diviseurs_premiers.count(div)
    result = 1
    for div in D.keys():
        result = result * div ** D[div]
    return result
