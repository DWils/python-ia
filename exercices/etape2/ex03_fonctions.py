"""Exercice 3 : fonctions (arguments, fermetures, décorateurs).

    uv run pytest exercices/etape2/test_ex03_fonctions.py
"""

from collections.abc import Callable


def normaliser(valeurs: list[float], *, mini: float = 0.0, maxi: float = 1.0) -> list[float]:
    """Ramène linéairement les valeurs dans l'intervalle [mini, maxi].

    `mini` et `maxi` ne peuvent être passés que par mot-clé (c'est le rôle du `*`).
    Si toutes les valeurs sont égales, chacune devient `mini`.

    >>> normaliser([10, 20, 30])
    [0.0, 0.5, 1.0]
    """
    raise NotImplementedError


def ajouter_element(element, liste: list | None = None) -> list:
    """Ajoute `element` à `liste` et la renvoie. Sans `liste`, part d'une liste vide.

    Piège classique d'entretien : pourquoi ne faut-il pas écrire `liste=[]` ?

    >>> ajouter_element(1)
    [1]
    >>> ajouter_element(2)
    [2]
    """
    raise NotImplementedError


def composer(*fonctions: Callable) -> Callable:
    """Renvoie une fonction qui applique `fonctions` l'une après l'autre, de gauche à droite.

    Sans aucune fonction, le résultat renvoie son argument tel quel.

    >>> composer(str.strip, str.upper)("  ia ")
    'IA'
    """
    raise NotImplementedError


def compteur() -> Callable[[], int]:
    """Renvoie une fonction qui renvoie 1, puis 2, puis 3... à chaque appel.

    Chaque compteur créé est indépendant des autres.
    """
    raise NotImplementedError


def compter_appels(fonction: Callable) -> Callable:
    """Décorateur : la fonction décorée gagne un attribut `appels`, incrémenté à chaque appel.

    La fonction décorée conserve son nom (`__name__`) et sa docstring.

    >>> @compter_appels
    ... def double(x):
    ...     return 2 * x
    >>> double(4)
    8
    >>> double.appels
    1
    """
    raise NotImplementedError
