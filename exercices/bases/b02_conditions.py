"""Bases 2 : booléens et conditions.

    uv run pytest exercices/bases/test_b02_conditions.py

RAPPEL
------
Les comparaisons donnent un booléen (True ou False) :

    3 == 3     # True   égal (un seul = sert à affecter)
    3 != 4     # True   différent
    3 < 4      # True   aussi : <=  >  >=
    0 <= x < 10         # les comparaisons s'enchaînent

Elles se combinent avec `and`, `or`, `not` :

    age >= 18 and age < 65
    not majeur

Une condition s'écrit avec `if`, `elif` (sinon si) et `else`. Le bloc est
délimité par l'indentation (4 espaces), pas par des accolades :

    if note >= 16:
        mention = "très bien"
    elif note >= 10:
        mention = "admis"
    else:
        mention = "refusé"

Les conditions sont testées dans l'ordre : la première vraie l'emporte.

Une fonction peut renvoyer directement le résultat d'une comparaison :

    def est_majeur(age):
        return age >= 18
"""


def est_pair(n: int) -> bool:
    """Indique si `n` est pair.

    >>> est_pair(4)
    True
    """
    if n % 2 == 0:
        return True
    else:
        return False


def maximum_de_trois(a: float, b: float, c: float) -> float:
    """Renvoie le plus grand des trois nombres, sans utiliser `max()`.

    >>> maximum_de_trois(3, 9, 5)
    9
    """
    max = a
    if a < b < c :
        return c
    elif a < b :
        return b
    else :
        return a



def mention(note: float) -> str:
    """Renvoie la mention correspondant à une note sur 20.

    - moins de 10 : "insuffisant"
    - de 10 à moins de 12 : "passable"
    - de 12 à moins de 14 : "assez bien"
    - de 14 à moins de 16 : "bien"
    - 16 et plus : "très bien"

    >>> mention(13)
    'assez bien'
    """
    if note >= 16 :
        return "très bien"
    elif note >= 14 :
        return "bien"
    elif note >= 12 :
        return "assez bien"
    elif note >= 10 :
        return "passable"
    else :
        return "insuffisant"



def est_bissextile(annee: int) -> bool:
    """Indique si une année est bissextile.

    Elle l'est si elle est divisible par 4, sauf les années divisibles par 100
    qui ne le sont que si elles sont aussi divisibles par 400.

    >>> est_bissextile(2024)
    True
    >>> est_bissextile(1900)
    False
    """
    if annee%100 == 0 and annee%400 != 0 :
        return False
    if annee%4 == 0 :
        return True
    else :
        return False


def prix_billet(age: int, etudiant: bool) -> float:
    """Renvoie le prix d'un billet de cinéma.

    - moins de 12 ans : 5.0
    - 65 ans et plus : 7.0
    - étudiant : 8.0
    - sinon : 10.0

    Les règles d'âge passent avant le tarif étudiant.

    >>> prix_billet(30, False)
    10.0
    """
    if age >= 65 :
        return 7.0
    elif age < 12 :
        return 5.0
    elif etudiant == True :
        return 8.0
    else :
        return 10.0

