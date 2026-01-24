from utils.entiers import Entiers


def probleme0003():
    """
    What is the largest prime factor of the number 600851475143 ?
    """
    return Entiers.facteurs_premiers_uniques(600851475143)[-1]
