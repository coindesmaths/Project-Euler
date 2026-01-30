class SuiteFibonacci(list):

    def __init__(self, n=None, seuil=None):
        super().__init__()
        self += [0, 1]
        if n is not None:
            self.generer_n_premiers_termes(n)
        else:
            if seuil is not None:
                self.generer_seuil(seuil)

    def calculer_suivant(self):
        self.append(self[-2] + self[-1])
        return self[-1]

    def generer_n_premiers_termes(self, n):
        for k in range(n + 1 - len(self)):
            self.calculer_suivant()

    def generer_seuil(self, seuil):
        while self[-1] < seuil:
            self.calculer_suivant()


if __name__ == "__main__":
    fibo = SuiteFibonacci()
    fibo.generer_seuil(100)
    print(fibo)
