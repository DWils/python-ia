# Étape 2 : les bases de Python

Six exercices, à faire dans l'ordre. Chaque fichier `exNN_*.py` contient les
énoncés ; le fichier `test_exNN_*.py` correspondant vérifie ton code.

| Exercice | Thème |
| --- | --- |
| `ex01_structures.py` | str, list, dict, set, tuple, tri |
| `ex02_comprehensions.py` | compréhensions de listes et de dicts, `zip` |
| `ex03_fonctions.py` | arguments par mot-clé, valeurs par défaut, fermetures, décorateurs |
| `ex04_classes.py` | dataclasses, propriétés, méthodes spéciales, classes abstraites |
| `ex05_exceptions.py` | `try`/`except`, exceptions personnalisées, fichiers |
| `ex06_generateurs.py` | `yield`, gestionnaires de contexte |

## Mise en place (une seule fois)

Depuis la racine du projet :

```bash
uv add --dev pytest
```

## Travailler un exercice

1. Ouvre le fichier d'énoncé et remplace les `raise NotImplementedError`.
2. Lance ses tests :

```bash
uv run pytest exercices/etape2/test_ex01_structures.py
```

3. Lis le premier test en échec, corrige, relance.

Options utiles :

| Commande | Effet |
| --- | --- |
| `uv run pytest exercices/etape2` | Lance tous les exercices |
| `uv run pytest exercices/etape2 -x` | S'arrête au premier échec |
| `uv run pytest exercices/etape2 -k top_n` | Ne lance que les tests dont le nom contient `top_n` |
| `uv run pytest exercices/etape2 -q` | Affichage court |

Les fichiers de tests sont aussi à lire : `pytest.raises`, `pytest.approx`,
`pytest.mark.parametrize` et `tmp_path` sont des outils à connaître.
