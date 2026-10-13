import pytest

from b05_fonctions import appliquer, carre, fizzbuzz, min_max, moyenne, saluer


def test_carre():
    assert carre(5) == 25
    assert carre(-3) == 9


def test_saluer():
    assert saluer("Ana") == "Bonjour Ana !"
    assert saluer("Ana", "Bonsoir") == "Bonsoir Ana !"
    assert saluer(politesse="Salut", nom="Bob") == "Salut Bob !"


def test_moyenne():
    assert moyenne([10, 20]) == pytest.approx(15.0)
    assert moyenne([1, 2, 4]) == pytest.approx(7 / 3)
    assert moyenne([]) == 0.0


def test_min_max():
    assert min_max([3, 9, 5]) == (3, 9)
    assert min_max([7]) == (7, 7)


def test_appliquer():
    assert appliquer(carre, [1, 2, 3]) == [1, 4, 9]
    assert appliquer(str.upper, ["a", "b"]) == ["A", "B"]
    assert appliquer(carre, []) == []


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    resultat = fizzbuzz(15)
    assert resultat[5] == "Fizz"
    assert resultat[9] == "Buzz"
    assert resultat[14] == "FizzBuzz"
    assert fizzbuzz(0) == []
