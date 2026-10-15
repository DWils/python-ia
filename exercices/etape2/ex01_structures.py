"""Exercice 1 : structures de données (str, list, dict, set, tuple).

Remplace chaque `raise NotImplementedError` par ton code, puis lance :

    uv run pytest exercices/etape2/test_ex01_structures.py

NOTIONS À SAVOIR
----------------
Découper et nettoyer du texte :

    "le  chat dort".split()        # ['le', 'chat', 'dort']  sans argument : ignore les espaces en trop
    "le  chat".split(" ")          # ['le', '', 'chat']      avec " " : crée des morceaux vides
    "Chien.".lower()               # 'chien.'
    "chien.".strip(".,!")          # 'chien'   retire ces caractères aux deux bouts

Dictionnaires :

    d = {"a": 1}
    d["a"]                 # 1     lecture par CLÉ, jamais par position (d[0] -> KeyError)
    d.get("z", 0)          # 0     valeur par défaut si la clé manque
    d["b"] = 2             # ajoute ou remplace
    for cle in d: ...                  # parcourt les CLÉS
    for cle, valeur in d.items(): ...  # parcourt les couples (clé, valeur)

Compter avec un dictionnaire (schéma à connaître par cœur) :

    compteur = {}
    for x in ["a", "b", "a"]:
        compteur[x] = compteur.get(x, 0) + 1     # {'a': 2, 'b': 1}

Regrouper dans des listes :

    groupes = {}
    if cle not in groupes:
        groupes[cle] = []
    groupes[cle].append(element)

Ensembles (set) : pas de doublons, pas d'ordre garanti.

    {1, 2, 3} & {2, 3, 4}      # {2, 3}         intersection : dans les deux
    {1, 2} | {2, 3}            # {1, 2, 3}      union
    {1, 2, 3} - {2}            # {1, 3}         différence
    set(["a", "b", "a"])       # {'a', 'b'}
    set({"a": 1, "b": 2})      # {'a', 'b'}     les clés d'un dictionnaire

Garder l'ordre en retirant les doublons : `list(dict.fromkeys(liste))`.

Trier :

    sorted([3, 1, 2])                      # [1, 2, 3]   NOUVELLE liste, l'original ne change pas
    liste.sort()                           # trie la liste elle-même, renvoie None
    sorted(mots, key=len)                  # trie selon le résultat de len(mot)
    sorted(couples, key=lambda c: c[1])    # trie des couples par leur 2e élément
    sorted(couples, key=lambda c: (-c[1], c[0]))  # 2e élément décroissant, puis 1er croissant

`lambda c: c[1]` est une petite fonction sans nom, équivalente à
`def f(c): return c[1]`. Les tuples se comparent élément par élément.

`in` ne fait pas la même chose selon le type :

    "chat" in "chateau"            # True   morceau de texte
    "chat" in ["chateau"]          # False  élément entier d'une liste
"""


def compter_mots(texte: str) -> dict[str, int]:
    """Compte les occurrences de chaque mot, sans tenir compte de la casse.

    Les mots sont séparés par des espaces. La ponctuation `.,;:!?` collée
    à un mot est ignorée.

    >>> compter_mots("Le chat et le chien.")
    {'le': 2, 'chat': 1, 'et': 1, 'chien': 1}
    """
    compteur = {}
    for word in texte.split(" ") :
        mot = word.lower().strip(".,;:!?") 
        if mot == "":
            continue
        if mot in compteur :
            compteur[mot] = compteur[mot] + 1
        else :
            compteur[mot] = 1
    return compteur
    


def dedoublonner(elements: list) -> list:
    """Retire les doublons en conservant l'ordre de première apparition.

    >>> dedoublonner([3, 1, 3, 2, 1])
    [3, 1, 2]
    """
    el = []
    for n in elements:
        if n in el :
            continue
        else :
            el.append(n)
    return el


def mots_communs(phrase_a: str, phrase_b: str) -> set[str]:
    """Renvoie les mots présents dans les deux phrases, en minuscules.

    >>> sorted(mots_communs("le chat dort", "Le chien dort"))
    ['dort', 'le']
    """
    mc = set()
    for w in phrase_a.split(" "):
        m = w.lower()
        for w2 in phrase_b.split(" "):
            m2 = w2.lower()
            if m == m2 :
                mc.add(m)
    return mc



def top_n(scores: dict[str, float], n: int) -> list[tuple[str, float]]:
    """Renvoie les `n` meilleurs couples (nom, score), du plus grand au plus petit.

    À score égal, les noms sont classés par ordre alphabétique.

    >>> top_n({"a": 0.9, "b": 0.7, "c": 0.9}, 2)
    [('a', 0.9), ('c', 0.9)]
    """
    couples = list(scores.items())
    couples_tries = sorted(couples, key=lambda c: (-c[1], c[0]))
    return couples_tries[:n]





def inverser_dict(d: dict[str, str]) -> dict[str, list[str]]:
    """Regroupe les clés par valeur. Chaque liste de clés est triée.

    >>> inverser_dict({"chien": "animal", "chat": "animal", "rose": "plante"})
    {'animal': ['chat', 'chien'], 'plante': ['rose']}
    """
    id = {}
    
    for x in d :
        if d[x] not in id:
            id[d[x]] = []
        id[d[x]].append(x)   
        id[d[x]].sort()
    return id

