"""Bases 3 : listes, tuples et dictionnaires.

    uv run pytest exercices/bases/test_b03_listes_dicts.py

RAPPEL
------
Une liste est une suite ordonnée et modifiable de valeurs :

    notes = [12, 15, 9, 18]
    notes[0]          # 12   premier élément (indice 0)
    notes[-1]         # 18   dernier élément
    len(notes)        # 4
    15 in notes       # True

Les tranches (slices) extraient un morceau, borne de fin exclue :

    notes[1:3]        # [15, 9]
    notes[:2]         # [12, 15]   les deux premiers
    notes[2:]         # [9, 18]    à partir de l'indice 2

Modifier une liste :

    notes.append(11)        # ajoute à la fin, modifie la liste elle-même
    notes[0] = 13           # remplace un élément
    autre = notes + [20]    # crée une NOUVELLE liste, `notes` ne change pas

Un tuple est une suite non modifiable, pratique pour renvoyer deux valeurs :

    couple = (3, 4)
    x, y = couple           # décomposition : x vaut 3, y vaut 4

Un dictionnaire associe des clés à des valeurs :

    ages = {"Ana": 31, "Bob": 25}
    ages["Ana"]             # 31
    ages["Zoé"]             # KeyError : la clé n'existe pas
    ages.get("Zoé")         # None, sans erreur
    ages.get("Zoé", 0)      # 0, valeur par défaut au choix
    ages["Cléo"] = 40       # ajoute ou remplace
    "Bob" in ages           # True (teste les clés)
"""


def premier_et_dernier(elements: list) -> tuple:
    """Renvoie le premier et le dernier élément dans un tuple.

    >>> premier_et_dernier([4, 8, 15])
    (4, 15)
    """
    raise NotImplementedError


def trois_premiers(elements: list) -> list:
    """Renvoie les trois premiers éléments (ou moins si la liste est plus courte).

    >>> trois_premiers([1, 2, 3, 4, 5])
    [1, 2, 3]
    """
    raise NotImplementedError


def ajouter_a_la_fin(elements: list, element) -> list:
    """Renvoie une nouvelle liste avec `element` en plus, sans modifier `elements`.

    >>> ajouter_a_la_fin([1, 2], 3)
    [1, 2, 3]
    """
    raise NotImplementedError


def contient(elements: list, element) -> bool:
    """Indique si `element` se trouve dans la liste.

    >>> contient(["a", "b"], "b")
    True
    """
    raise NotImplementedError


def age_de(annuaire: dict[str, int], nom: str) -> int | None:
    """Renvoie l'âge de `nom`, ou None si la personne est absente de l'annuaire.

    >>> age_de({"Ana": 31}, "Ana")
    31
    """
    raise NotImplementedError


def ajouter_stock(stock: dict[str, int], produit: str, quantite: int) -> dict[str, int]:
    """Ajoute `quantite` au stock de `produit` et renvoie le dictionnaire modifié.

    Si le produit n'existe pas encore, il est créé.

    >>> ajouter_stock({"pomme": 3}, "pomme", 2)
    {'pomme': 5}
    """
    raise NotImplementedError
