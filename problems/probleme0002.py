from utils.fibonacci import SuiteFibonacci


def probleme0002():
    """
    By considering the terms in the Fibonacci sequence whose values do not exceed 4000000, find the sum of the even-valued terms.
    """
    fibo = SuiteFibonacci()
    fibo.generer_seuil(4000000)
    return sum([f for f in fibo if f % 2 == 0])
