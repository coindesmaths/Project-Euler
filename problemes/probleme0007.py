from utils.premiers import NombresPremiers


def probleme0007():
    premiers = NombresPremiers()
    premiers.generer_n_premiers_termes(10000)
    return premiers[-1]
