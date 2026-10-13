import pytest

from b02_conditions import (
    est_bissextile,
    est_pair,
    maximum_de_trois,
    mention,
    prix_billet,
)


def test_est_pair():
    assert est_pair(4) is True
    assert est_pair(7) is False
    assert est_pair(0) is True


@pytest.mark.parametrize(
    ("a", "b", "c", "attendu"),
    [(3, 9, 5, 9), (9, 3, 5, 9), (3, 5, 9, 9), (2, 2, 2, 2), (-1, -5, -3, -1)],
)
def test_maximum_de_trois(a, b, c, attendu):
    assert maximum_de_trois(a, b, c) == attendu


@pytest.mark.parametrize(
    ("note", "attendu"),
    [
        (0, "insuffisant"),
        (9.99, "insuffisant"),
        (10, "passable"),
        (12, "assez bien"),
        (13, "assez bien"),
        (14, "bien"),
        (16, "très bien"),
        (20, "très bien"),
    ],
)
def test_mention(note, attendu):
    assert mention(note) == attendu


@pytest.mark.parametrize(
    ("annee", "attendu"),
    [(2024, True), (2023, False), (1900, False), (2000, True)],
)
def test_est_bissextile(annee, attendu):
    assert est_bissextile(annee) is attendu


@pytest.mark.parametrize(
    ("age", "etudiant", "attendu"),
    [
        (30, False, 10.0),
        (20, True, 8.0),
        (8, False, 5.0),
        (11, True, 5.0),
        (12, False, 10.0),
        (65, False, 7.0),
        (70, True, 7.0),
    ],
)
def test_prix_billet(age, etudiant, attendu):
    assert prix_billet(age, etudiant) == attendu
