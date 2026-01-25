from utils.fibonacci import SuiteFibonacci


def probleme0002():
    fibo = SuiteFibonacci()
    fibo.generer_seuil(4000000)
    return sum([f for f in fibo if f % 2 == 0])
