from b03_listes_dicts import (
    age_de,
    ajouter_a_la_fin,
    ajouter_stock,
    contient,
    premier_et_dernier,
    trois_premiers,
)


def test_premier_et_dernier():
    assert premier_et_dernier([4, 8, 15]) == (4, 15)
    assert premier_et_dernier(["seul"]) == ("seul", "seul")


def test_trois_premiers():
    assert trois_premiers([1, 2, 3, 4, 5]) == [1, 2, 3]
    assert trois_premiers([1, 2]) == [1, 2]
    assert trois_premiers([]) == []


def test_ajouter_a_la_fin():
    assert ajouter_a_la_fin([1, 2], 3) == [1, 2, 3]


def test_ajouter_a_la_fin_ne_modifie_pas_l_original():
    original = [1, 2]
    ajouter_a_la_fin(original, 3)
    assert original == [1, 2]


def test_contient():
    assert contient(["a", "b"], "b") is True
    assert contient(["a", "b"], "z") is False
    assert contient([], 1) is False


def test_age_de():
    annuaire = {"Ana": 31, "Bob": 25}
    assert age_de(annuaire, "Ana") == 31
    assert age_de(annuaire, "Zoé") is None


def test_ajouter_stock_produit_existant():
    assert ajouter_stock({"pomme": 3}, "pomme", 2) == {"pomme": 5}


def test_ajouter_stock_nouveau_produit():
    assert ajouter_stock({"pomme": 3}, "poire", 4) == {"pomme": 3, "poire": 4}


def test_ajouter_stock_modifie_le_dictionnaire_recu():
    stock = {}
    ajouter_stock(stock, "kiwi", 1)
    assert stock == {"kiwi": 1}
