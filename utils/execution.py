import time


def timeit(f):

    def timed(*args, **kw):

        # Résolution du problème et chronométrage
        debut = time.perf_counter()
        resultat = f()
        duree = time.perf_counter() - debut

        # Affichage du résultat
        print(f"🧮 Problème {int(f.__name__[-4:])}")
        print(f"✅ Résultat : {resultat}")
        print(f"⏱️  Durée    : {duree:.6f} secondes")

        return resultat

    return timed
