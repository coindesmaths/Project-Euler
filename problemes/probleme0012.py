from utils.entiers import Entiers


def probleme0012():
    n = 500
    triangle_number, k, div_number = 1, 2, 0
    while len(Entiers.facteurs(triangle_number)) < n:
        triangle_number += k
        k += 1
    return triangle_number
