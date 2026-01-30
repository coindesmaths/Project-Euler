from utils.combinatoire import Combinatoire


def probleme0020():
    n = Combinatoire.factorielle(100)
    resultat = 0
    while n != 0:
        resultat += n % 10
        n = n // 10
    return resultat
