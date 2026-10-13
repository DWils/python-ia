import pytest

from b01_variables import (
    additionner_textes,
    aire_rectangle,
    celsius_en_fahrenheit,
    heures_minutes,
    initiales,
    presenter,
)


def test_aire_rectangle():
    assert aire_rectangle(3, 4) == 12
    assert aire_rectangle(2.5, 2) == pytest.approx(5.0)


def test_celsius_en_fahrenheit():
    assert celsius_en_fahrenheit(0) == pytest.approx(32)
    assert celsius_en_fahrenheit(100) == pytest.approx(212)
    assert celsius_en_fahrenheit(-40) == pytest.approx(-40)


def test_heures_minutes():
    assert heures_minutes(125) == "2h05"
    assert heures_minutes(59) == "0h59"
    assert heures_minutes(600) == "10h00"


def test_presenter():
    assert presenter("Ana", 31) == "Je m'appelle Ana et j'ai 31 ans."


def test_initiales():
    assert initiales("ana", "diaz") == "A.D."
    assert initiales("Bob", "Martin") == "B.M."


def test_additionner_textes():
    assert additionner_textes("12", "30") == 42
    assert additionner_textes("-5", "5") == 0
