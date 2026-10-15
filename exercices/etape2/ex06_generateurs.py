"""Exercice 6 : générateurs et gestionnaires de contexte.

Les quatre premières fonctions sont des générateurs : elles utilisent `yield`
et ne construisent jamais la liste complète en mémoire.

    uv run pytest exercices/etape2/test_ex06_generateurs.py

NOTIONS À SAVOIR
----------------
Une fonction qui contient `yield` devient un générateur : elle produit
ses valeurs une par une, à la demande, au lieu de renvoyer une liste.

    def compter_jusqua(n):
        i = 1
        while i <= n:
            yield i            # met la fonction en pause et donne i
            i += 1

    gen = compter_jusqua(3)
    next(gen)                  # 1
    next(gen)                  # 2
    list(compter_jusqua(3))    # [1, 2, 3]

Rien ne s'exécute avant la première demande : une erreur levée au début
du générateur n'apparaît qu'au premier `next()` ou `list()`.

Un générateur peut être infini (`while True:`) : on en prend un morceau
avec `itertools.islice`.

    from itertools import islice
    list(islice(generateur_infini(), 5))     # les 5 premières valeurs

Un générateur ne se parcourt qu'une fois, et ne supporte ni `len()` ni
les tranches `[a:b]`. Pour traiter n'importe quel itérable, il faut donc
le parcourir avec `for`.

`yield` dans une boucle `for`, avec un filtre :

    def positifs(nombres):
        for x in nombres:
            if x > 0:
                yield x

Tranches et tuples : `tuple(liste[i:i + 3])` donne 3 éléments à partir de i.

Gestionnaire de contexte : un objet utilisable avec `with`. Il définit
`__enter__` (appelé à l'entrée, sa valeur de retour va dans `as`) et
`__exit__` (appelé à la sortie, TOUJOURS, même en cas d'exception).

    class Annonce:
        def __enter__(self):
            print("début")
            return self

        def __exit__(self, type_exc, valeur_exc, trace):
            print("fin")
            return False       # False : l'exception éventuelle continue sa route

    with Annonce() as a:
        print("dans le bloc")

Mesurer une durée : `time.perf_counter()` renvoie un instant en secondes ;
la différence entre deux appels donne le temps écoulé.
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
