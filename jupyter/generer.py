import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell
import inspect
import pandas as pd
from urllib.request import urlopen
import os


def code_importation():
    return inspect.cleandoc(
        """
        import sys
        sys.path.append("..")
        from utils.entiers import Entiers
        from utils.fibonacci import SuiteFibonacci
        from utils.premiers import NombresPremiers
        """
    )


def code_entete(debut, fin):
    return inspect.cleandoc(
        f"""
        <div style="padding:10px ;border:solid 4px #006699; border-radius: 10px; background-color:#CCEEFF;">
        <table width="100%">
            <tr>
                <td width="10%" style="text-align: left; font-size: large; font-weight: regular; background-color:#CCEEFF;"> 
                    <!-- -->
                </td>
                <td width="80%" style="text-align: center; background-color:#CCEEFF; font-weight: bold;">
                    <span style="font-weight: regular; font-size: x-large; ">
                        Project Euler
                    </span>
                    <br/> <br/> 
                    <span style="font-weight: bold; font-size: xx-large; ">
                        Problèmes {debut} à {fin}
                    </span>
                    <br/>
                </td>
                <td style="background-color:#CCEEFF;" > 
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Leonhard_Euler.jpg/250px-Leonhard_Euler.jpg" width="100%" height="100%" > 
                </td>
        </table>
        </div>
    """
    )


def obtenir_problemes():
    url = "https://projecteuler.net/minimal=problems"
    df = pd.read_csv(url, sep="##", engine="python")
    data = df.to_dict(orient="records")
    return data


def code_titre(n, problemes):
    titre = problemes[n]["Title"]
    return inspect.cleandoc(
        f"""
        <h1 style="color: #006699;">
            <span style="margin-right: 20px;">███</span>
            <span>Problème {n}</span>
            <span style="margin-left: 20px; margin-right: -15px;">▏</span>
            {titre}
        </h1>
        """
    )


def obtenir_description(n):
    url = f"https://projecteuler.net/minimal={n}"
    with urlopen(url) as f:
        texte = f.read()[:-1].decode("utf-8")
    return "\n".join("> " + line for line in texte.splitlines())


def obtenir_programme(n):
    path = f"problemes/probleme{str(n).zfill(4)}.py"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read() + f"\n\nprobleme{str(n).zfill(4)}()"
    return ""


def generer_notebook(debut, fin):
    importation = new_code_cell(code_importation())
    entete = new_markdown_cell(code_entete(debut, fin))

    problemes = obtenir_problemes()
    titres = [
        new_markdown_cell(code_titre(n, problemes)) for n in range(debut, fin + 1)
    ]
    descriptions = [
        new_markdown_cell(obtenir_description(n)) for n in range(debut, fin + 1)
    ]
    programmes = [new_code_cell(obtenir_programme(n)) for n in range(debut, fin + 1)]

    problems = [elem for pair in zip(titres, descriptions, programmes) for elem in pair]

    cells = [entete, importation, *problems]
    nb = new_notebook(cells=cells)

    with open(
        f"jupyter/Project Euler - Problèmes {debut} à {fin}.ipynb",
        "w",
        encoding="utf-8",
    ) as f:
        nbformat.write(nb, f)


def generer_notebooks(debut, fin, pas):
    for k in range(debut, fin + 1, pas):
        generer_notebook(k, k + pas - 1)


if __name__ == "__main__":
    generer_notebooks(1, 50, 10)
