"""Exercice 2 : compréhensions de listes et de dictionnaires.

Contrainte : chaque fonction tient en une seule instruction `return`,
écrite avec une compréhension (ou `zip` pour `transposer`).

    uv run pytest exercices/etape2/test_ex02_comprehensions.py
"""


def carres_pairs(n: int) -> list[int]:
    """Renvoie les carrés des nombres pairs de 0 à n - 1.

    >>> carres_pairs(6)
    [0, 4, 16]
    """
    raise NotImplementedError


def longueurs(mots: list[str]) -> dict[str, int]:
    """Associe chaque mot à sa longueur.

    >>> longueurs(["a", "bcd"])
    {'a': 1, 'bcd': 3}
    """
    raise NotImplementedError


def aplatir(matrice: list[list[int]]) -> list[int]:
    """Met bout à bout les lignes d'une liste de listes.

    >>> aplatir([[1, 2], [3], []])
    [1, 2, 3]
    """
    raise NotImplementedError


def transposer(matrice: list[list[int]]) -> list[list[int]]:
    """Échange lignes et colonnes.

    >>> transposer([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    raise NotImplementedError


def filtrer_enregistrements(lignes: list[dict], cle: str, seuil: float) -> list[dict]:
    """Garde les enregistrements dont `cle` existe, n'est pas None et vaut au moins `seuil`.

    >>> filtrer_enregistrements([{"age": 20}, {"age": 15}, {"nom": "x"}], "age", 18)
    [{'age': 20}]
    """
    raise NotImplementedError
