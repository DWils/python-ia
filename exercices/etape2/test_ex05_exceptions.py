import pytest

from ex05_exceptions import (
    DonneesInvalidesError,
    charger_lignes,
    convertir_en_float,
    lire_premiere_ligne,
    valider_ligne,
)


@pytest.mark.parametrize(
    ("texte", "attendu"),
    [("3.14", 3.14), ("3,14", 3.14), (" 42 ", 42.0), ("-1e3", -1000.0)],
)
def test_convertir_en_float_valide(texte, attendu):
    assert convertir_en_float(texte) == pytest.approx(attendu)


@pytest.mark.parametrize("texte", ["abc", "", "1,2,3", None])
def test_convertir_en_float_invalide(texte):
    assert convertir_en_float(texte) is None
    assert convertir_en_float(texte, defaut=0.0) == 0.0


def test_exception_personnalisee():
    erreur = DonneesInvalidesError("âge manquant", 3)
    assert isinstance(erreur, ValueError)
    assert erreur.ligne == 3
    assert "âge manquant" in str(erreur)


def test_valider_ligne_nettoie():
    assert valider_ligne({"nom": " Ana ", "age": "31"}, 1) == {"nom": "Ana", "age": 31}


def test_valider_ligne_ne_modifie_pas_l_entree():
    ligne = {"nom": " Ana ", "age": "31"}
    valider_ligne(ligne, 1)
    assert ligne == {"nom": " Ana ", "age": "31"}


@pytest.mark.parametrize(
    "ligne",
    [
        {"nom": "Ana"},
        {"age": 31},
        {"nom": "   ", "age": 31},
        {"nom": "Ana", "age": "trente"},
        {"nom": "Ana", "age": 200},
        {"nom": "Ana", "age": -1},
        {"nom": "Ana", "age": None},
    ],
)
def test_valider_ligne_rejette(ligne):
    with pytest.raises(DonneesInvalidesError) as info:
        valider_ligne(ligne, 7)
    assert info.value.ligne == 7


def test_charger_lignes_continue_apres_une_erreur():
    lignes = [
        {"nom": "Ana", "age": "31"},
        {"nom": "Bob"},
        {"nom": "", "age": 20},
        {"nom": "Dan ", "age": 45},
    ]
    valides, rejetees = charger_lignes(lignes)
    assert valides == [{"nom": "Ana", "age": 31}, {"nom": "Dan", "age": 45}]
    assert rejetees == [2, 3]


def test_lire_premiere_ligne(tmp_path):
    fichier = tmp_path / "donnees.txt"
    fichier.write_text("bonjour\nmonde\n", encoding="utf-8")
    assert lire_premiere_ligne(fichier) == "bonjour"


def test_lire_premiere_ligne_fichier_vide(tmp_path):
    fichier = tmp_path / "vide.txt"
    fichier.write_text("", encoding="utf-8")
    assert lire_premiere_ligne(fichier) == ""


def test_lire_premiere_ligne_fichier_absent(tmp_path):
    assert lire_premiere_ligne(tmp_path / "absent.txt") is None
