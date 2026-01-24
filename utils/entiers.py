import math
from .premiers import NombresPremiers


class Entiers:

    def facteurs(n):
        return Entiers.calculer_facteurs(n, False)

    def facteurs_uniques(n):
        return Entiers.calculer_facteurs(n, True)

    def facteurs_premiers(n):
        return Entiers.calculer_facteurs_premiers(n, False)

    def facteurs_premiers_uniques(n):
        return Entiers.calculer_facteurs_premiers(n, True)

    def calculer_facteurs(n, unique):
        facteurs_gauche = [1]
        facteurs_droite = [n]

        limite = math.sqrt(n)
        i = 2
        while i <= limite:
            if n % i == 0:
                facteurs_gauche.append(i)
                if not unique or i != n // i:
                    facteurs_droite.append(n // i)
            i += 1

        factors = facteurs_gauche + facteurs_droite[::-1]
        return factors

    def calculer_facteurs_premiers(n, unique):
        facteurs = []
        diviseur = 2

        while n > 1:
            if n % diviseur == 0:
                facteurs.append(diviseur)
                n //= diviseur
            else:
                diviseur += 1

        if unique:
            return list(dict.fromkeys(facteurs))  # conserve l’ordre
        return facteurs


if __name__ == "__main__":
    print(Entiers.facteurs_premiers(16))
