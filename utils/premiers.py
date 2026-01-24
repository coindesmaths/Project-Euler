import math


class NombresPremiers(list):

    def __init__(self):
        super().__init__()
        self += NombresPremiers.premiers_premiers()

    def premiers_premiers():
        return [2, 3, 5, 7, 11, 13]

    def calculer_suivant(self):
        dernierPremier = self[-1]

        modSix = dernierPremier % 6
        prochainMultipleSix = dernierPremier + 6 - modSix

        prochainPremier = -1
        i = prochainMultipleSix
        while prochainPremier == -1:
            if i - 1 != dernierPremier and NombresPremiers.est_premier(i - 1):
                prochainPremier = i - 1
            elif NombresPremiers.est_premier(i + 1):
                prochainPremier = i + 1
            else:
                i += 6

        self.append(prochainPremier)
        return prochainPremier

    def generer_n_premiers_termes(self, n):
        for k in range(n + 1 - len(self)):
            self.calculer_suivant()

    def generer_seuil(self, seuil):
        while self[-1] < seuil:
            self.calculer_suivant()

    def est_premier(n):
        if n == 1:
            return False
        if n <= 3:
            return True
        if n % 6 not in [1, 5]:
            return False
        return NombresPremiers.determine_est_premier(n)

    def determine_est_premier(n):
        limite = math.isqrt(n)
        if n % 2 == 0:
            return False
        for i in range(3, limite + 1, 2):
            if n % i == 0:
                return False
        return True


if __name__ == "__main__":
    premiers = NombresPremiers()
    premiers.generer_seuil(100)
    print(premiers)
