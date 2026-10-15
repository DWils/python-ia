"""Exercice 4 : classes, dataclasses, méthodes spéciales, héritage.

Ici, c'est à toi d'écrire les classes en entier : seuls les noms et le
comportement attendu sont donnés.

    uv run pytest exercices/etape2/test_ex04_classes.py

NOTIONS À SAVOIR
----------------
Une classe regroupe des données (attributs) et des fonctions (méthodes).
`__init__` initialise l'objet ; `self` désigne l'objet en cours.

    class Chien:
        def __init__(self, nom, age=0):
            self.nom = nom
            self.age = age

        def aboyer(self):
            return f"{self.nom} aboie"

    rex = Chien("Rex", 3)
    rex.aboyer()       # 'Rex aboie'

Une dataclass écrit `__init__`, `__repr__` et `__eq__` pour toi.
`frozen=True` la rend immuable, et donc utilisable dans un set.

    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Couleur:
        r: int
        g: int
        b: int

    Couleur(255, 0, 0) == Couleur(255, 0, 0)    # True

Propriété en lecture seule : on stocke dans un attribut « privé »
(préfixe `_` par convention) et on l'expose avec `@property`.

    class Thermometre:
        def __init__(self):
            self._temperature = 20.0

        @property
        def temperature(self):
            return self._temperature

    t = Thermometre()
    t.temperature          # 20.0, sans parenthèses
    t.temperature = 30     # AttributeError

Méthodes spéciales : elles branchent ta classe sur la syntaxe de Python.

    __repr__(self)          ->  repr(obj), affichage pour le développeur
    __eq__(self, autre)     ->  obj == autre
    __add__(self, autre)    ->  obj + autre
    __len__(self)           ->  len(obj)
    __getitem__(self, i)    ->  obj[i]

Recevoir un nombre variable de valeurs : `def __init__(self, *valeurs)`.
`!r` dans une f-string utilise repr : f"{'Ana'!r}" donne "'Ana'".

Lever une erreur : `raise ValueError("montant négatif")`.

Héritage et classe abstraite : une classe abstraite ne peut pas être
instanciée, et ses sous-classes doivent définir les méthodes abstraites.

    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def cri(self): ...

    class Chat(Animal):
        def cri(self):
            return "miaou"

    Animal()                       # TypeError
    isinstance(Chat(), Animal)     # True

Calculs utiles : `math.pi`, `math.sqrt(x)`, `math.hypot(dx, dy)`.
"""

# --- Point -------------------------------------------------------------------
# Une dataclass immuable (`frozen=True`) avec deux champs `x` et `y` (float).
# Méthode `distance(autre)` : distance euclidienne jusqu'à un autre Point.
#
#     Point(0, 0).distance(Point(3, 4))  ->  5.0


# --- Compte ------------------------------------------------------------------
# Compte(titulaire, solde=0.0)
# - `solde` est une propriété en lecture seule (`@property`).
# - `deposer(montant)` et `retirer(montant)` lèvent ValueError si le montant
#   est négatif ou nul ; `retirer` aussi si le solde est insuffisant.
# - `repr(Compte("Ana", 50))`  ->  "Compte(titulaire='Ana', solde=50.0)"


# --- Vecteur -----------------------------------------------------------------
# Vecteur(*composantes), par exemple Vecteur(1, 2, 3).
# - `len(v)`, `v[0]`, `v == autre`, `v + autre` fonctionnent.
# - L'addition de deux vecteurs de tailles différentes lève ValueError.
# - `norme()` renvoie la norme euclidienne.


# --- Formes ------------------------------------------------------------------
# - `Forme` : classe abstraite (module `abc`) avec une méthode abstraite `aire()`.
#   On ne peut pas l'instancier directement.
# - `Rectangle(largeur, hauteur)` et `Cercle(rayon)` héritent de `Forme`.
# - `aire_totale(formes)` : fonction qui renvoie la somme des aires.
