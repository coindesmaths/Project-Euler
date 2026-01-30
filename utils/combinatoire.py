class Combinatoire:
    """
    Classe utilitaire pour les permutations et combinaisons
    """

    def combinaison(n, k):
        n_moins_k = n - k
        petit = n_moins_k if n_moins_k < n else n
        grand = n_moins_k if k == petit else k
        return Combinatoire.factorielle(n, grand) // Combinatoire.factorielle(petit)

    def factorielle(n, diviseur=1):
        produit = 1
        for m in range(diviseur + 1, n + 1):
            produit *= m
        return produit

    def pour_chaque_n_permutations(n, choix, callback):
        Combinatoire._pour_chaque_n_possibilites(n, choix, True, callback)

    def pour_chaque_n_possibilites(n, choix, callback):
        Combinatoire._pour_chaque_n_possibilites(n, choix, False, callback)

    def obtenir_n_permutations(n, choix):
        resultat = []
        Combinatoire._pour_chaque_n_possibilites(
            n, choix, True, lambda perm: resultat.append(perm)
        )
        return resultat

    def obtenir_n_possibilites(n, choix):
        resultat = []
        Combinatoire._pour_chaque_n_possibilites(
            n, choix, False, lambda perm: resultat.append(perm)
        )
        return resultat

    def _pour_chaque_n_possibilites(n, choix, unique, callback):
        if n == 0:
            return

        if n == 1:
            for element in choix:
                if callback(str(element)) is False:
                    return

        continuer = True

        for i in range(len(choix)):
            if not continuer:
                break

            element = choix[i]
            choix_restants = (
                [c for j, c in enumerate(choix) if j != i] if unique else choix
            )

            def sous_callback(sous_chaine):
                nonlocal continuer
                continuer = callback(str(element) + sous_chaine) is not False
                return continuer

            Combinatoire._pour_chaque_n_possibilites(
                n - 1, choix_restants, unique, sous_callback
            )

    def sont_chiffres_permutations(a, b):
        compteur = [0] * 10

        while a > 10:
            compteur[a % 10] += 1
            a //= 10
        compteur[a % 10] += 1

        while b > 10:
            compteur[b % 10] -= 1
            b //= 10
        compteur[b % 10] -= 1

        for valeur in compteur:
            if valeur != 0:
                return False

        return True
