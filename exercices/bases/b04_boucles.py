"""Bases 4 : boucles `for` et `while`.

    uv run pytest exercices/bases/test_b04_boucles.py

RAPPEL
------
`for` parcourt les éléments d'une suite, un par un :

    for note in [12, 15, 9]:
        print(note)

    for lettre in "ana":          # une chaîne se parcourt caractère par caractère
        print(lettre)

`range` produit des entiers, borne de fin exclue :

    range(5)          # 0, 1, 2, 3, 4
    range(1, 6)       # 1, 2, 3, 4, 5
    range(10, 0, -2)  # 10, 8, 6, 4, 2

Le schéma le plus courant, l'accumulation :

    total = 0
    for note in notes:
        total = total + note      # ou : total += note

    pairs = []
    for n in range(10):
        if n % 2 == 0:
            pairs.append(n)

Parcourir un dictionnaire, ou une liste de tuples :

    for nom, age in ages.items():
        print(nom, age)

    for produit, prix in [("pomme", 1.2), ("poire", 2.0)]:
        print(produit, prix)

`while` répète tant qu'une condition est vraie :

    n = 3
    while n > 0:
        print(n)
        n -= 1

`break` sort de la boucle ; dans une fonction, `return` en sort aussi,
ce qui permet de s'arrêter dès que l'on a trouvé ce que l'on cherche.
"""


def somme_jusqua(n: int) -> int:
    """Renvoie 1 + 2 + ... + n (0 si n vaut 0).

    >>> somme_jusqua(4)
    10
    """
    somme = 0
    if n > 0 :
        for i in range(n) :
            somme += i + 1
    return somme


def compter_voyelles(texte: str) -> int:
    """Compte les voyelles (a, e, i, o, u, y), majuscules comprises.

    >>> compter_voyelles("Python")
    2
    """
    voyelles = 0
    voy_liste = ("a","e", "i", "o", "u", "y")
    for lettre in texte :
        if lettre.lower() in voy_liste :
            voyelles += 1
    return voyelles



def table_multiplication(n: int) -> list[str]:
    """Renvoie la table de `n`, de 1 à 10, sous forme de lignes de texte.

    >>> table_multiplication(7)[:2]
    ['7 x 1 = 7', '7 x 2 = 14']
    """
    mult_table = []
    for i in range(10):
        mult_table.append(f"{n} x {i + 1} = {(i + 1) * n}")
    return mult_table

    


def plus_grand(nombres: list[float]) -> float | None:
    """Renvoie le plus grand nombre de la liste, sans utiliser `max()`.

    Renvoie None si la liste est vide.

    >>> plus_grand([3, 9, 5])
    9
    """
    if len(nombres) == 0 :
        return None
    else :
        max = nombres[0]
        for n in nombres :
            if max < n :
                max = n
        return max



def premier_multiple(nombres: list[int], diviseur: int) -> int | None:
    """Renvoie le premier nombre de la liste divisible par `diviseur`, ou None.

    >>> premier_multiple([5, 8, 9, 12], 3)
    9
    """
    if len(nombres) == 0 :
        return None
    else :
        for n in nombres :
            if n%diviseur == 0 :
                return n


def compte_a_rebours(n: int) -> list[int]:
    """Renvoie la liste [n, n - 1, ..., 1, 0], avec une boucle `while`.

    >>> compte_a_rebours(3)
    [3, 2, 1, 0]
    """
    numbers = []
    for i in range(n,-1,-1):
        numbers.append(i)
    return numbers



def total_par_categorie(achats: list[tuple[str, float]]) -> dict[str, float]:
    """Additionne les montants par catégorie.

    >>> total_par_categorie([("fruits", 2.0), ("pain", 1.0), ("fruits", 3.0)])
    {'fruits': 5.0, 'pain': 1.0}
    """
    stock = {}
    for ach in achats :
        produit, quantite = ach
        if produit in stock :
            stock[produit] = stock[produit] + quantite
        else :
            stock[produit] = quantite
    return stock

