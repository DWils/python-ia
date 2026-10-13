import pytest

from ex03_fonctions import (
    ajouter_element,
    composer,
    compter_appels,
    compteur,
    normaliser,
)


def test_normaliser_par_defaut():
    assert normaliser([10, 20, 30]) == pytest.approx([0.0, 0.5, 1.0])


def test_normaliser_intervalle_personnalise():
    assert normaliser([10, 20, 30], mini=-1, maxi=1) == pytest.approx([-1.0, 0.0, 1.0])


def test_normaliser_cas_limites():
    assert normaliser([]) == []
    assert normaliser([5, 5]) == [0.0, 0.0]


def test_normaliser_refuse_mini_maxi_positionnels():
    with pytest.raises(TypeError):
        normaliser([1, 2], 0, 1)


def test_ajouter_element_sans_liste_repart_de_zero():
    assert ajouter_element(1) == [1]
    assert ajouter_element(2) == [2]


def test_ajouter_element_avec_liste():
    liste = ["a"]
    assert ajouter_element("b", liste) == ["a", "b"]
    assert liste == ["a", "b"]


def test_composer():
    assert composer(str.strip, str.upper)("  ia ") == "IA"
    assert composer(lambda x: x + 1, lambda x: x * 10)(1) == 20


def test_composer_sans_fonction():
    assert composer()(42) == 42


def test_compteurs_independants():
    a = compteur()
    b = compteur()
    assert [a(), a(), a()] == [1, 2, 3]
    assert b() == 1


def test_compter_appels():
    @compter_appels
    def addition(x, y=0):
        """Additionne."""
        return x + y

    assert addition.appels == 0
    assert addition(1, y=2) == 3
    addition(1)
    assert addition.appels == 2
    assert addition.__name__ == "addition"
    assert addition.__doc__ == "Additionne."
