"""Bases 1 : variables, types, opérateurs, chaînes de caractères.

    uv run pytest exercices/bases/test_b01_variables.py

RAPPEL
------
Une variable est un nom qui désigne une valeur. Pas de déclaration de type :

    age = 31              # int   (entier)
    taille = 1.75         # float (nombre à virgule)
    nom = "Ana"           # str   (texte)
    majeur = True         # bool  (True ou False)
    type(age)             # <class 'int'>

Opérateurs sur les nombres :

    7 + 2    # 9        7 / 2    # 3.5   division, donne toujours un float
    7 - 2    # 5        7 // 2   # 3     division entière
    7 * 2    # 14       7 % 2    # 1     reste de la division (modulo)
                        7 ** 2   # 49    puissance

Chaînes de caractères :

    "Ana" + " " + "Diaz"      # "Ana Diaz"   concaténation
    len("Ana")                # 3
    "Ana"[0]                  # "A"          premier caractère (on compte à partir de 0)
    "ana".upper()             # "ANA"
    "  ana ".strip()          # "ana"

Les f-strings insèrent des valeurs dans un texte :

    f"{nom} a {age} ans"      # "Ana a 31 ans"
    f"{3.14159:.2f}"          # "3.14"  deux décimales
    f"{5:02d}"                # "05"    entier sur deux chiffres

Conversions entre types :

    int("42")      # 42         str(42)      # "42"
    float("3.5")   # 3.5        int(3.9)     # 3   (tronque, n'arrondit pas)

Chaque exercice est une fonction : remplace `raise NotImplementedError`
par ton code et renvoie le résultat avec `return`.
"""


def aire_rectangle(largeur: float, hauteur: float) -> float:
    """Renvoie l'aire d'un rectangle.

    >>> aire_rectangle(3, 4)
    12
    """
    return largeur * hauteur


def celsius_en_fahrenheit(celsius: float) -> float:
    """Convertit des degrés Celsius en Fahrenheit : F = C × 9 / 5 + 32.

    >>> celsius_en_fahrenheit(100)
    212.0
    """
    return celsius * 9 / 5 + 32


def heures_minutes(minutes: int) -> str:
    """Convertit une durée en minutes au format « 2h05 ».

    Les minutes s'écrivent toujours sur deux chiffres.

    >>> heures_minutes(125)
    '2h05'
    """
    hours = minutes//60
    newMinutes = minutes%60
    if (newMinutes < 10):
        return f"{hours}h0{newMinutes}"
    else :
        return f"{hours}h{newMinutes}"


def presenter(nom: str, age: int) -> str:
    """Renvoie une phrase de présentation.

    >>> presenter("Ana", 31)
    "Je m'appelle Ana et j'ai 31 ans."
    """
    return f"Je m'appelle {nom} et j'ai {age} ans."


def initiales(prenom: str, nom: str) -> str:
    """Renvoie les initiales en majuscules, chacune suivie d'un point.

    >>> initiales("ana", "diaz")
    'A.D.'
    """
    return f"{prenom[0].upper()}.{nom[0].upper()}."


def additionner_textes(a: str, b: str) -> int:
    """Additionne deux nombres entiers reçus sous forme de texte.

    >>> additionner_textes("12", "30")
    42
    """
    result = int(a) + int(b)
    return result
