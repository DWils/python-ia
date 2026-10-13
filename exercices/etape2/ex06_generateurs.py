"""Exercice 6 : générateurs et gestionnaires de contexte.

Les quatre premières fonctions sont des générateurs : elles utilisent `yield`
et ne construisent jamais la liste complète en mémoire.

    uv run pytest exercices/etape2/test_ex06_generateurs.py
"""

from collections.abc import Iterable, Iterator


def fibonacci() -> Iterator[int]:
    """Produit sans fin la suite de Fibonacci : 0, 1, 1, 2, 3, 5, 8..."""
    raise NotImplementedError


def par_lots(elements: Iterable, taille: int) -> Iterator[list]:
    """Découpe `elements` en listes de `taille` éléments (la dernière peut être plus courte).

    C'est le principe des « batchs » en entraînement de modèles. `elements` peut
    être n'importe quel itérable, y compris un générateur : pas de `len()` ni de tranches.
    Lève ValueError si `taille` est inférieure à 1.

    >>> list(par_lots(range(7), 3))
    [[0, 1, 2], [3, 4, 5], [6]]
    """
    raise NotImplementedError


def lire_nombres(lignes: Iterable[str]) -> Iterator[float]:
    """Produit un float par ligne, en ignorant les lignes vides et celles qui commencent par `#`.

    >>> list(lire_nombres(["1", "", "# commentaire", " 2.5 "]))
    [1.0, 2.5]
    """
    raise NotImplementedError


def fenetre_glissante(valeurs: list, taille: int) -> Iterator[tuple]:
    """Produit tous les tuples de `taille` valeurs consécutives.

    >>> list(fenetre_glissante([1, 2, 3, 4], 2))
    [(1, 2), (2, 3), (3, 4)]
    """
    raise NotImplementedError


# Définis ici la classe `Minuteur`, un gestionnaire de contexte (`__enter__` et
# `__exit__`) qui mesure la durée du bloc `with` avec `time.perf_counter()` :
#
#     with Minuteur() as m:
#         ...
#     m.duree  ->  durée du bloc en secondes
#
# `duree` doit être renseignée même si le bloc lève une exception, et
# l'exception ne doit pas être étouffée.
