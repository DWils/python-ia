"""Exercice 4 : classes, dataclasses, méthodes spéciales, héritage.

Ici, c'est à toi d'écrire les classes en entier : seuls les noms et le
comportement attendu sont donnés.

    uv run pytest exercices/etape2/test_ex04_classes.py
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
