"""Bases 5 : écrire ses propres fonctions.

    uv run pytest exercices/bases/test_b05_fonctions.py

RAPPEL
------
Une fonction se définit avec `def`, reçoit des paramètres et renvoie une
valeur avec `return` :

    def aire(largeur, hauteur):
        return largeur * hauteur

    aire(3, 4)                    # 12
    aire(hauteur=4, largeur=3)    # arguments nommés, l'ordre devient libre

Sans `return`, une fonction renvoie None. Attention à ne pas confondre
`print` (affiche à l'écran) et `return` (transmet la valeur à l'appelant).

Un paramètre peut avoir une valeur par défaut :

    def puissance(x, exposant=2):
        return x ** exposant

    puissance(3)       # 9
    puissance(3, 3)    # 27

Une fonction peut renvoyer plusieurs valeurs, sous forme de tuple :

    def division(a, b):
        return a // b, a % b

    quotient, reste = division(17, 5)

Une fonction est une valeur comme une autre : on peut la passer en argument.

    def appliquer_deux_fois(f, x):
        return f(f(x))

    appliquer_deux_fois(puissance, 3)    # 81

Les annotations de type (`x: int`, `-> str`) sont facultatives : elles
documentent le code mais Python ne les vérifie pas à l'exécution.

Dans ce fichier, il n'y a plus de squelette : écris chaque fonction en
entier, avec sa ligne `def`.
"""

# carre(x)
#     Renvoie x au carré.
#     carre(5)  ->  25
def carre(x: int) -> int :
    return x * x

# saluer(nom, politesse="Bonjour")
#     saluer("Ana")             ->  "Bonjour Ana !"
#     saluer("Ana", "Bonsoir")  ->  "Bonsoir Ana !"
def saluer(nom : str, politesse: str ="Bonjour" ) -> str :
    return f"{politesse} {nom} !"

# moyenne(nombres)
#     Renvoie la moyenne d'une liste de nombres, et 0.0 si la liste est vide.
#     moyenne([10, 20])  ->  15.0
def moyenne(nombres: list) -> float :
    moyenne = 0.0
    for n in nombres :
        moyenne += n
    if len(nombres) > 0 :
        moyenne /= len(nombres)
    return moyenne
    


# min_max(nombres)
#     Renvoie le plus petit et le plus grand nombre de la liste, dans un tuple.
#     Ici `min()` et `max()` sont autorisés.
#     min_max([3, 9, 5])  ->  (3, 9)
def min_max(nombres: list):
    return min(nombres), max(nombres)

# appliquer(fonction, valeurs)
#     Renvoie la liste des résultats de `fonction` appliquée à chaque valeur.
#     appliquer(carre, [1, 2, 3])  ->  [1, 4, 9]
def appliquer(fonction, valeurs):
    resultats = []
    for valeur in valeurs:
        resultats.append(fonction(valeur))
    return resultats


# fizzbuzz(n)
#     Grand classique d'entretien. Renvoie la liste des textes de 1 à n où :
#     - les multiples de 3 sont remplacés par "Fizz" ;
#     - les multiples de 5 par "Buzz" ;
#     - les multiples de 3 et de 5 par "FizzBuzz" ;
#     - les autres nombres sont convertis en texte.
#     fizzbuzz(5)  ->  ["1", "2", "Fizz", "4", "Buzz"]
def fizzbuzz(n : int) -> list:
    fb = []
    for i in range(1, n+1):
        if i%15 == 0 :
            fb.append("FizzBuzz")
        elif i%5 == 0 :
            fb.append("Buzz")
        elif i%3 == 0 :
            fb.append("Fizz")
        else :
            fb.append(str(i))
    return fb
