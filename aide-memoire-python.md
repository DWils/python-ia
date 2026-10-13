# Aide-mémoire : installer un environnement Python (uv)

13 octobre 2026 · David

## L'essentiel

Cinq commandes suffisent pour passer d'une Fedora nue à un projet Python prêt pour pandas et scikit-learn. Règle de base : on n'installe jamais de paquets dans le Python du système, chaque projet a son propre environnement virtuel.

```bash
# 1. Installer uv (une seule fois par machine)
sudo dnf install uv

# 2. Créer le projet
uv init ~/Documents/python-ia

# 3. Se placer dedans
cd ~/Documents/python-ia

# 4. Ajouter les bibliothèques
uv add pandas scikit-learn matplotlib jupyterlab

# 5. Vérifier
uv run python -c "import pandas, sklearn; print(pandas.__version__, sklearn.__version__)"
```

Point de départ vérifié sur cette machine : Fedora 44, Python 3.14.7, git et VS Code présents, ni `pip` ni `uv`.

## Ce que fait chaque commande

`uv` remplace à lui seul `pip` (installer des paquets) et `venv` (isoler un projet), et tient à jour la liste des dépendances.

| Commande | Effet |
| --- | --- |
| `sudo dnf install uv` | Installe l'outil depuis les dépôts Fedora |
| `uv init <dossier>` | Crée le dossier avec `pyproject.toml`, `src/python_ia/__init__.py`, `README.md`, `.python-version` et un dépôt git |
| `uv add <paquets>` | Crée `.venv` si besoin, installe les paquets, les inscrit dans `pyproject.toml` et fige les versions dans `uv.lock` |
| `uv run <commande>` | Lance la commande dans l'environnement du projet, sans avoir à l'activer |

Les fichiers à connaître :

| Fichier | Rôle | Dans git ? |
| --- | --- | --- |
| `pyproject.toml` | Nom du projet, version de Python, dépendances directes | Oui |
| `uv.lock` | Versions exactes de tous les paquets, pour reproduire l'installation à l'identique | Oui |
| `.python-version` | Version de Python utilisée par le projet | Oui |
| `.venv/` | L'environnement virtuel : l'interpréteur et les paquets installés | Non, il se recrée avec `uv sync` |

## Commandes du quotidien

Toutes se lancent depuis le dossier du projet.

| Besoin | Commande |
| --- | --- |
| Lancer un script | `uv run python mon_script.py` |
| Ouvrir un interpréteur | `uv run python` |
| Ouvrir Jupyter | `uv run jupyter lab` |
| Ajouter un paquet | `uv add seaborn` |
| Ajouter un outil de développement | `uv add --dev pytest` |
| Retirer un paquet | `uv remove seaborn` |
| Voir les paquets installés | `uv tree` |
| Mettre à jour les versions | `uv lock --upgrade` puis `uv sync` |
| Lancer les tests | `uv run pytest` |

Reprendre un projet existant (après un `git clone`, ou sur une autre machine) :

```bash
cd le-projet
uv sync
```

`uv sync` recrée `.venv` avec exactement les versions de `uv.lock`.

Dans VS Code : ouvrir le dossier, installer l'extension Python, puis `Ctrl+Maj+P` → « Python: Select Interpreter » → choisir `.venv/bin/python`.

## Équivalent classique : venv + pip

La méthode historique fait la même chose à la main, sans rien installer de plus que Python. C'est celle qu'on peut te demander d'expliquer en entretien.

```bash
mkdir mon-projet && cd mon-projet

# Créer l'environnement virtuel
python3 -m venv .venv

# L'activer (le prompt affiche alors "(.venv)")
source .venv/bin/activate

# Installer les paquets
pip install pandas scikit-learn

# Figer les versions installées
pip freeze > requirements.txt

# Quitter l'environnement
deactivate
```

Pour réinstaller ailleurs : recréer et activer `.venv`, puis `pip install -r requirements.txt`.

|  | venv + pip | uv |
| --- | --- | --- |
| Créer l'environnement | `python3 -m venv .venv` | automatique |
| Activer | `source .venv/bin/activate` | inutile avec `uv run` |
| Installer | `pip install pandas` | `uv add pandas` |
| Liste des dépendances | `requirements.txt`, tenu à la main | `pyproject.toml` + `uv.lock`, tenus automatiquement |
| Réinstaller | `pip install -r requirements.txt` | `uv sync` |

Ce qu'il faut savoir dire : un environnement virtuel est un dossier contenant un interpréteur et ses propres paquets, ce qui évite les conflits de versions entre projets et protège le Python du système.

## Pièges courants

| Symptôme | Cause | Solution |
| --- | --- | --- |
| `ModuleNotFoundError: No module named 'pandas'` | Le script tourne avec le Python du système, pas celui du projet | Lancer avec `uv run python ...`, ou activer `.venv` |
| `error: externally-managed-environment` | `pip install` lancé hors environnement virtuel | Ne pas forcer avec `--break-system-packages` : créer ou activer un environnement |
| VS Code souligne les imports en erreur | Mauvais interpréteur sélectionné | « Python: Select Interpreter » → `.venv/bin/python` |
| Un paquet refuse de s'installer | Pas encore compatible avec la version de Python | `uv python pin 3.13` puis `uv sync` : uv télécharge cette version |
| Import `sklearn` introuvable après `uv add sklearn` | Le paquet s'appelle `scikit-learn`, le module `sklearn` | `uv add scikit-learn` |
| `.venv` cassé ou dossier déplacé | Un environnement virtuel contient des chemins absolus | Supprimer `.venv` puis `uv sync` |

Pour savoir quel Python s'exécute réellement :

```bash
uv run python -c "import sys; print(sys.executable)"
```

Le chemin affiché doit se terminer par `.venv/bin/python`.
