"""Exercice 5 : exceptions et lecture de fichiers.

Le fil rouge est le nettoyage de données, ce que tu feras ensuite avec pandas.

    uv run pytest exercices/etape2/test_ex05_exceptions.py

NOTIONS À SAVOIR
----------------
Intercepter une erreur avec `try` / `except` :

    try:
        n = int("abc")
    except ValueError:
        n = 0

Plusieurs types d'erreur dans un même `except`, et récupérer l'erreur :

    try:
        valeur = int(d["age"])
    except (KeyError, ValueError, TypeError) as erreur:
        print("problème :", erreur)

Erreurs courantes :

    int("abc")         # ValueError    valeur au mauvais format
    int(None)          # TypeError     mauvais type
    d["absente"]       # KeyError      clé manquante
    None.replace(...)  # AttributeError  méthode inexistante sur ce type
    open("absent")     # FileNotFoundError

Lever une erreur soi-même : `raise ValueError("âge invalide")`.

Créer sa propre exception : une classe qui hérite d'une exception
existante. Pour lui ajouter un attribut, on surcharge `__init__` et on
appelle `super().__init__(message)` pour garder le message :

    class ConfigInvalideError(ValueError):
        def __init__(self, message, cle):
            super().__init__(message)
            self.cle = cle

    try:
        raise ConfigInvalideError("valeur manquante", "port")
    except ConfigInvalideError as e:
        e.cle          # 'port'
        str(e)         # 'valeur manquante'

Transformer une erreur en une autre, en gardant la cause :

    except KeyError as e:
        raise ConfigInvalideError("clé absente", "port") from e

Copier un dictionnaire avant de le modifier : `nouveau = dict(ancien)`.

Lire un fichier : `with` le referme automatiquement, même en cas d'erreur.

    with open(chemin, encoding="utf-8") as f:
        premiere = f.readline()      # lit une ligne, avec son "\n" final
        reste = f.read()             # lit tout ce qui suit

    "texte\n".rstrip("\n")           # 'texte'
"""

from pathlib import Path


def convertir_en_float(texte, defaut: float | None = None) -> float | None:
    """Convertit `texte` en float, en acceptant la virgule décimale française.

    Renvoie `defaut` si la conversion est impossible (texte invalide ou None).

    >>> convertir_en_float("3,14")
    3.14
    >>> convertir_en_float("abc", defaut=0.0)
    0.0
    """
    raise NotImplementedError


# Définis ici `DonneesInvalidesError`, une exception qui hérite de ValueError.
# Elle se construit avec un message et un numéro de ligne, conservé dans
# l'attribut `ligne` :
#
#     erreur = DonneesInvalidesError("âge manquant", 3)
#     erreur.ligne  ->  3


def valider_ligne(ligne: dict, numero: int) -> dict:
    """Valide et nettoie un enregistrement {"nom": ..., "age": ...}.

    Renvoie un nouveau dict avec `nom` sans espaces autour et `age` converti en int.
    Lève DonneesInvalidesError (avec `numero`) si :
    - une des deux clés manque ;
    - le nom est vide ;
    - l'âge n'est pas un entier compris entre 0 et 150.

    >>> valider_ligne({"nom": " Ana ", "age": "31"}, 1)
    {'nom': 'Ana', 'age': 31}
    """
    raise NotImplementedError


def charger_lignes(lignes: list[dict]) -> tuple[list[dict], list[int]]:
    """Valide toutes les lignes sans s'arrêter à la première erreur.

    Renvoie (lignes valides nettoyées, numéros des lignes rejetées).
    Les lignes sont numérotées à partir de 1.
    """
    raise NotImplementedError


def lire_premiere_ligne(chemin: Path) -> str | None:
    """Renvoie la première ligne du fichier, sans le saut de ligne final.

    Renvoie None si le fichier n'existe pas, et "" s'il est vide.
    Utilise `with open(...)` pour que le fichier soit toujours refermé.
    """
    raise NotImplementedError
