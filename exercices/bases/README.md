# Les bases, depuis le début

Cinq fichiers à faire dans l'ordre, avant `exercices/etape2`. Chacun commence
par un rappel de cours, suivi des exercices ; le fichier `test_*.py`
correspondant vérifie ton code.

| Fichier | Thème |
| --- | --- |
| `b01_variables.py` | variables, types, opérateurs, chaînes, f-strings |
| `b02_conditions.py` | booléens, `if` / `elif` / `else` |
| `b03_listes_dicts.py` | listes, tranches, tuples, dictionnaires |
| `b04_boucles.py` | `for`, `range`, `while`, accumulation |
| `b05_fonctions.py` | `def`, `return`, valeurs par défaut, FizzBuzz |

## Mise en place (une seule fois)

Depuis la racine du projet :

```bash
uv add --dev pytest
```

## Travailler un exercice

1. Lis le rappel en tête du fichier.
2. Remplace un `raise NotImplementedError` par ton code.
3. Lance les tests du fichier :

```bash
uv run pytest exercices/bases/test_b01_variables.py
```

4. Lis le premier échec, corrige, relance.

## Expérimenter

Pour essayer une ligne de Python sans créer de fichier, ouvre l'interpréteur :

```bash
uv run python
```

Tape une expression, par exemple `7 // 2`, puis Entrée. `exit()` pour quitter.
