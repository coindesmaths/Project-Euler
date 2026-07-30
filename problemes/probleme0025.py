from utils.fibonacci import generateur_fibonacci


def probleme0025():
    for i, f in enumerate(generateur_fibonacci(), 2):
        if len(str(f)) >= 1000:
            return i
