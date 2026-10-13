"""Exercice 1 : structures de données (str, list, dict, set, tuple).

Remplace chaque `raise NotImplementedError` par ton code, puis lance :

    uv run pytest exercices/etape2/test_ex01_structures.py
"""


def compter_mots(texte: str) -> dict[str, int]:
    """Compte les occurrences de chaque mot, sans tenir compte de la casse.

    Les mots sont séparés par des espaces. La ponctuation `.,;:!?` collée
    à un mot est ignorée.

    >>> compter_mots("Le chat et le chien.")
    {'le': 2, 'chat': 1, 'et': 1, 'chien': 1}
    """
    raise NotImplementedError


def dedoublonner(elements: list) -> list:
    """Retire les doublons en conservant l'ordre de première apparition.

    >>> dedoublonner([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    raise NotImplementedError


def mots_communs(phrase_a: str, phrase_b: str) -> set[str]:
    """Renvoie les mots présents dans les deux phrases, en minuscules.

    >>> sorted(mots_communs("le chat dort", "Le chien dort"))
    ['dort', 'le']
    """
    raise NotImplementedError


def top_n(scores: dict[str, float], n: int) -> list[tuple[str, float]]:
    """Renvoie les `n` meilleurs couples (nom, score), du plus grand au plus petit.

    À score égal, les noms sont classés par ordre alphabétique.

    >>> top_n({"a": 0.9, "b": 0.7, "c": 0.9}, 2)
    [('a', 0.9), ('c', 0.9)]
    """
    raise NotImplementedError


def inverser_dict(d: dict[str, str]) -> dict[str, list[str]]:
    """Regroupe les clés par valeur. Chaque liste de clés est triée.

    >>> inverser_dict({"chien": "animal", "chat": "animal", "rose": "plante"})
    {'animal': ['chat', 'chien'], 'plante': ['rose']}
    """
    raise NotImplementedError
