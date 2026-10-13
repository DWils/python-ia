import pytest

from b04_boucles import (
    compte_a_rebours,
    compter_voyelles,
    plus_grand,
    premier_multiple,
    somme_jusqua,
    table_multiplication,
    total_par_categorie,
)


def test_somme_jusqua():
    assert somme_jusqua(4) == 10
    assert somme_jusqua(100) == 5050
    assert somme_jusqua(0) == 0


def test_compter_voyelles():
    assert compter_voyelles("Python") == 2
    assert compter_voyelles("OISEAU") == 5
    assert compter_voyelles("brrr") == 0
    assert compter_voyelles("") == 0


def test_table_multiplication():
    table = table_multiplication(7)
    assert len(table) == 10
    assert table[0] == "7 x 1 = 7"
    assert table[9] == "7 x 10 = 70"


def test_plus_grand():
    assert plus_grand([3, 9, 5]) == 9
    assert plus_grand([-4, -2, -7]) == -2
    assert plus_grand([]) is None


def test_premier_multiple():
    assert premier_multiple([5, 8, 9, 12], 3) == 9
    assert premier_multiple([5, 8], 3) is None
    assert premier_multiple([], 3) is None


def test_compte_a_rebours():
    assert compte_a_rebours(3) == [3, 2, 1, 0]
    assert compte_a_rebours(0) == [0]


def test_total_par_categorie():
    achats = [("fruits", 2.0), ("pain", 1.0), ("fruits", 3.0)]
    assert total_par_categorie(achats) == pytest.approx({"fruits": 5.0, "pain": 1.0})
    assert total_par_categorie([]) == {}
