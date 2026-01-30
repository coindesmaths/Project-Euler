def nombre_en_lettres(n):
    if n == 0:
        return "zero"

    unites = [
        "",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    nombres_speciaux = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]

    dizaines = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    def convertir_centaines(nombre):
        resultat = ""

        if nombre >= 100:
            resultat += unites[nombre // 100] + " hundred"
            nombre %= 100
            if nombre != 0:
                resultat += " and "

        if 10 <= nombre < 20:
            resultat += nombres_speciaux[nombre - 10]
        else:
            if nombre >= 20:
                resultat += dizaines[nombre // 10]
                if nombre % 10 != 0:
                    resultat += "-" + unites[nombre % 10]
            else:
                resultat += unites[nombre]

        return resultat

    resultat_final = ""

    if n >= 1000:
        resultat_final += convertir_centaines(n // 1000) + " thousand"
        n %= 1000
        if n != 0:
            resultat_final += " "

    resultat_final += convertir_centaines(n)

    return resultat_final.strip()


def probleme0017():
    n = 1000
    resultat = 0
    for k in range(1, n + 1):
        lettres = nombre_en_lettres(k)
        for lettre in lettres:
            if 96 < ord(lettre) < 123:
                resultat += 1
    return resultat
