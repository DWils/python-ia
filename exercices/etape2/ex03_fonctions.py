"""Exercice 3 : fonctions (arguments, fermetures, décorateurs).

    uv run pytest exercices/etape2/test_ex03_fonctions.py

NOTIONS À SAVOIR
----------------
Arguments par mot-clé obligatoires : tout ce qui suit `*` doit être nommé.

    def f(a, *, b=0):
        return a + b

    f(1, b=2)      # 3
    f(1, 2)        # TypeError

Nombre variable d'arguments : `*args` reçoit un tuple.

    def total(*nombres):
        return sum(nombres)

    total(1, 2, 3)     # 6
    total()            # 0

Piège de la valeur par défaut modifiable : `[]` n'est créé qu'UNE fois,
à la définition de la fonction, puis partagé entre tous les appels.

    def mauvais(x, l=[]):          def correct(x, l=None):
        l.append(x)                    if l is None:
        return l                           l = []
                                       l.append(x)
    mauvais(1)   # [1]                 return l
    mauvais(2)   # [1, 2]  !

Une fonction peut renvoyer une fonction. La fonction intérieure se
souvient des variables de celle qui l'a créée (c'est une « fermeture ») :

    def multiplicateur(k):
        def f(x):
            return x * k
        return f

    triple = multiplicateur(3)
    triple(5)          # 15

Pour MODIFIER une variable de la fonction englobante, il faut `nonlocal` :

    def creer():
        total = 0
        def ajouter(x):
            nonlocal total
            total += x
            return total
        return ajouter

Un décorateur est une fonction qui reçoit une fonction et en renvoie une
nouvelle qui l'enveloppe. `@deco` au-dessus d'un `def` équivaut à
`f = deco(f)`. `functools.wraps` recopie le nom et la docstring :

    import functools

    def bavard(fonction):
        @functools.wraps(fonction)
        def enveloppe(*args, **kwargs):
            print("appel de", fonction.__name__)
            return fonction(*args, **kwargs)
        return enveloppe

    @bavard
    def double(x):
        return 2 * x

`*args, **kwargs` transmet tous les arguments, positionnels et nommés.
Une fonction est un objet : on peut lui ajouter un attribut, `f.compte = 0`.
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
