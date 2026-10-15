"""Exercice 2 : compréhensions de listes et de dictionnaires.

Contrainte : chaque fonction tient en une seule instruction `return`,
écrite avec une compréhension (ou `zip` pour `transposer`).

    uv run pytest exercices/etape2/test_ex02_comprehensions.py

NOTIONS À SAVOIR
----------------
Une compréhension est une boucle écrite à l'intérieur des crochets.
Le début est la VALEUR à mettre dans le résultat, jamais un `append`.

    resultat = []
    for x in nombres:                  ->     [x * 2 for x in nombres]
        resultat.append(x * 2)

Avec un filtre, le `if` se place à la fin :

    [x for x in nombres if x > 0]

Les trois formes ne diffèrent que par la ponctuation :

    [x for x in mots]              # liste
    {x for x in mots}              # ensemble
    {x: len(x) for x in mots}      # dictionnaire : deux-points entre clé et valeur

Boucles imbriquées : les `for` s'écrivent dans le même ordre qu'en boucles.

    for ligne in lignes:
        for x in ligne:            ->     [x for ligne in lignes for x in ligne]
            ...

`zip` associe les éléments de même position, sous forme de tuples :

    list(zip([1, 2, 3], ["a", "b", "c"]))      # [(1, 'a'), (2, 'b'), (3, 'c')]

L'étoile `*` déballe une liste en plusieurs arguments :

    lignes = [[1, 2], [3, 4]]
    zip(*lignes)               # identique à zip([1, 2], [3, 4])

Un tuple n'est pas égal à une liste : convertis avec `list(...)`.

    (1, 2) == [1, 2]           # False
    list((1, 2))               # [1, 2]

Lire une clé qui peut manquer sans planter : `d.get("cle")` renvoie None.
Pour tester « existe et n'est pas None » : `d.get("cle") is not None`.
"""


def carres_pairs(n: int) -> list[int]:
    """Renvoie les carrés des nombres pairs de 0 à n - 1.

    >>> carres_pairs(6)
    [0, 4, 16]
    """
    return [x ** 2 for x in range(n) if x%2 == 0]


def longueurs(mots: list[str]) -> dict[str, int]:
    """Associe chaque mot à sa longueur.

    >>> longueurs(["a", "bcd"])
    {'a': 1, 'bcd': 3}
    """
    return {x: len(x) for x in mots}


def aplatir(matrice: list[list[int]]) -> list[int]:
    """Met bout à bout les lignes d'une liste de listes.

    >>> aplatir([[1, 2], [3], []])
    [1, 2, 3]
    """
    return [x for ligne in matrice for x in ligne]


def transposer(matrice: list[list[int]]) -> list[list[int]]:
    """Échange lignes et colonnes.

    >>> transposer([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(colonne) for colonne in zip(*matrice)]


def filtrer_enregistrements(lignes: list[dict], cle: str, seuil: float) -> list[dict]:
    """Garde les enregistrements dont `cle` existe, n'est pas None et vaut au moins `seuil`.

    >>> filtrer_enregistrements([{"age": 20}, {"age": 15}, {"nom": "x"}], "age", 18)
    [{'age': 20}]
    """
    return [ligne for ligne in lignes if ligne.get(cle) is not None and ligne[cle] >= seuil]
