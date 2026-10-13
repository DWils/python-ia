import inspect
import time
from itertools import islice

import pytest

from ex06_generateurs import (
    Minuteur,
    fenetre_glissante,
    fibonacci,
    lire_nombres,
    par_lots,
)


def test_fibonacci():
    assert list(islice(fibonacci(), 8)) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_ce_sont_des_generateurs():
    assert inspect.isgenerator(fibonacci())
    assert inspect.isgenerator(par_lots([1], 1))
    assert inspect.isgenerator(lire_nombres([]))
    assert inspect.isgenerator(fenetre_glissante([1], 1))


def test_par_lots():
    assert list(par_lots(range(7), 3)) == [[0, 1, 2], [3, 4, 5], [6]]
    assert list(par_lots([], 3)) == []
    assert list(par_lots([1, 2], 2)) == [[1, 2]]


def test_par_lots_accepte_un_generateur():
    source = (x * x for x in range(5))
    assert list(par_lots(source, 2)) == [[0, 1], [4, 9], [16]]


def test_par_lots_taille_invalide():
    with pytest.raises(ValueError):
        list(par_lots([1, 2, 3], 0))


def test_lire_nombres():
    lignes = ["1", "", "# commentaire", " 2.5 ", "   ", "-3"]
    assert list(lire_nombres(lignes)) == [1.0, 2.5, -3.0]


def test_fenetre_glissante():
    assert list(fenetre_glissante([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
    assert list(fenetre_glissante([1, 2, 3], 3)) == [(1, 2, 3)]
    assert list(fenetre_glissante([1, 2], 3)) == []


def test_minuteur_mesure_la_duree():
    with Minuteur() as m:
        time.sleep(0.02)
    assert 0.02 <= m.duree < 1


def test_minuteur_laisse_passer_les_exceptions():
    m = Minuteur()
    with pytest.raises(ZeroDivisionError):
        with m:
            1 / 0
    assert m.duree >= 0
