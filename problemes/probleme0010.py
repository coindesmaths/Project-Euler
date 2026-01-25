from utils.premiers import NombresPremiers


def probleme0010():
    premiers = NombresPremiers()
    premiers.generer_seuil(2000000)
    return sum(premiers)
