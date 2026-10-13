import dataclasses
import math

import pytest

from ex04_classes import (
    Cercle,
    Compte,
    Forme,
    Point,
    Rectangle,
    Vecteur,
    aire_totale,
)


def test_point_distance():
    assert Point(0, 0).distance(Point(3, 4)) == pytest.approx(5.0)


def test_point_egalite_et_hachage():
    assert Point(1, 2) == Point(1, 2)
    assert len({Point(1, 2), Point(1, 2)}) == 1


def test_point_immuable():
    p = Point(1, 2)
    with pytest.raises(dataclasses.FrozenInstanceError):
        p.x = 10


def test_compte_depot_et_retrait():
    compte = Compte("Ana")
    assert compte.solde == 0
    compte.deposer(50)
    compte.retirer(20)
    assert compte.solde == 30


@pytest.mark.parametrize("montant", [0, -5])
def test_compte_refuse_les_montants_non_positifs(montant):
    compte = Compte("Ana", 100)
    with pytest.raises(ValueError):
        compte.deposer(montant)
    with pytest.raises(ValueError):
        compte.retirer(montant)


def test_compte_solde_insuffisant():
    compte = Compte("Ana", 10)
    with pytest.raises(ValueError):
        compte.retirer(100)
    assert compte.solde == 10


def test_compte_solde_en_lecture_seule():
    compte = Compte("Ana", 10)
    with pytest.raises(AttributeError):
        compte.solde = 1_000_000


def test_compte_repr():
    assert repr(Compte("Ana", 50)) == "Compte(titulaire='Ana', solde=50.0)"


def test_vecteur_acces():
    v = Vecteur(1, 2, 3)
    assert len(v) == 3
    assert v[0] == 1
    assert v[2] == 3


def test_vecteur_egalite():
    assert Vecteur(1, 2) == Vecteur(1, 2)
    assert Vecteur(1, 2) != Vecteur(1, 3)


def test_vecteur_addition():
    assert Vecteur(1, 2) + Vecteur(3, 4) == Vecteur(4, 6)


def test_vecteur_addition_tailles_differentes():
    with pytest.raises(ValueError):
        Vecteur(1, 2) + Vecteur(1, 2, 3)


def test_vecteur_norme():
    assert Vecteur(3, 4).norme() == pytest.approx(5.0)


def test_forme_est_abstraite():
    with pytest.raises(TypeError):
        Forme()


def test_aires():
    assert Rectangle(2, 3).aire() == pytest.approx(6)
    assert Cercle(1).aire() == pytest.approx(math.pi)


def test_heritage():
    assert isinstance(Rectangle(1, 1), Forme)
    assert isinstance(Cercle(1), Forme)


def test_aire_totale():
    assert aire_totale([Rectangle(2, 3), Cercle(1)]) == pytest.approx(6 + math.pi)
    assert aire_totale([]) == 0
