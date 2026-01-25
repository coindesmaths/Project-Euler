# -------------------------------------------------------------------------------

import sys
import importlib
from utils.execution import timeit

# -------------------------------------------------------------------------------

if len(sys.argv) == 1:
    c = input("Quel(s) problème(s) voulez-vous résoudre ?")
    c = list(map(lambda x: int(x), c.split(" ")))
    if len(c) == 1:
        debut = c[0]
        fin = c[0]
    elif len(c) == 2:
        debut = c[0]
        fin = c[1]
elif len(sys.argv) == 2:
    debut = int(sys.argv[1])
    fin = debut
elif len(sys.argv) == 3:
    debut = int(sys.argv[1])
    fin = int(sys.argv[2])
else:
    print("Erreur")
    sys.exit(1)


def resoudre_probleme(debut, fin):
    for k in range(debut, fin + 1):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        module = importlib.import_module(f"problemes.probleme{str(k).zfill(4)}")
        fonction = timeit(getattr(module, f"probleme{str(k).zfill(4)}"))
        fonction()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


resoudre_probleme(debut, fin)

# -------------------------------------------------------------------------------
