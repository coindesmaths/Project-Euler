def probleme0019():

    def dimanche_suivant(date):
        durees_mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if date[2] % 4 == 0 and (date[2] % 100 != 0 or date[2] % 400 == 0):
            durees_mois[1] = 29
        date[0] += 7

        if date[0] > durees_mois[date[1] - 1]:
            date[0] = date[0] - durees_mois[date[1] - 1]
            date[1] += 1
            if date[1] > 12:
                date[1] = date[1] % 12
                date[2] += 1
        return date

    resultat = 0
    date = [7, 1, 1900]
    while date[2] != 1901:
        date = dimanche_suivant(date)

    while date[2] != 2001:
        if date[0] == 1:
            resultat += 1
        date = dimanche_suivant(date)

    return resultat
