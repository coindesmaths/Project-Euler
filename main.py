# -------------------------------------------------------------------------------

import sys
import importlib
from utils.execution import timeit

# -------------------------------------------------------------------------------

if len(sys.argv) == 1:
    n = input("Quel problème voulez-vous résoudre ?")
elif len(sys.argv) == 2:
    n = int(sys.argv[1])
else:
    print("Usage: python main.py <nombre>")
    sys.exit(1)

module = importlib.import_module(f"problems.probleme000{n}")
fonction = timeit(getattr(module, f"probleme000{n}"))

fonction()

# -------------------------------------------------------------------------------
