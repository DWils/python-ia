import pytest

from ex02_comprehensions import (
    aplatir,
    carres_pairs,
    filtrer_enregistrements,
    longueurs,
    transposer,
)


@pytest.mark.parametrize(
    ("n", "attendu"),
    [(0, []), (1, [0]), (6, [0, 4, 16]), (7, [0, 4, 16, 36])],
)
def test_carres_pairs(n, attendu):
    assert carres_pairs(n) == attendu


def test_longueurs():
    assert longueurs(["a", "bcd"]) == {"a": 1, "bcd": 3}
    assert longueurs([]) == {}


def test_aplatir():
    assert aplatir([[1, 2], [3], []]) == [1, 2, 3]
    assert aplatir([]) == []


def test_transposer():
    assert transposer([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transposer([]) == []


def test_transposer_renvoie_des_listes():
    assert all(isinstance(ligne, list) for ligne in transposer([[1, 2], [3, 4]]))


def test_filtrer_enregistrements():
    lignes = [
        {"nom": "Ana", "age": 31},
        {"nom": "Bob", "age": 17},
        {"nom": "Cléo", "age": None},
        {"nom": "Dan"},
        {"nom": "Eve", "age": 18},
    ]
    assert filtrer_enregistrements(lignes, "age", 18) == [
        {"nom": "Ana", "age": 31},
        {"nom": "Eve", "age": 18},
    ]
