from utils.data import Data


def probleme0013():
    numbers = Data.init(13)
    somme = 0
    for num in numbers.split("\n"):
        somme += int(num)
    return somme
