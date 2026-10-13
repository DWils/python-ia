from ex01_structures import (
    compter_mots,
    dedoublonner,
    inverser_dict,
    mots_communs,
    top_n,
)


def test_compter_mots_ignore_casse_et_ponctuation():
    assert compter_mots("Le chat et le chien.") == {
        "le": 2,
        "chat": 1,
        "et": 1,
        "chien": 1,
    }


def test_compter_mots_texte_vide():
    assert compter_mots("") == {}


def test_compter_mots_espaces_multiples():
    assert compter_mots("oui,  oui !") == {"oui": 2}


def test_dedoublonner_conserve_l_ordre():
    assert dedoublonner([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert dedoublonner(["b", "a", "b"]) == ["b", "a"]


def test_dedoublonner_ne_modifie_pas_l_entree():
    entree = [1, 1, 2]
    dedoublonner(entree)
    assert entree == [1, 1, 2]


def test_mots_communs():
    assert mots_communs("le chat dort", "Le chien dort") == {"le", "dort"}
    assert mots_communs("un deux", "trois quatre") == set()


def test_top_n_trie_par_score_puis_par_nom():
    scores = {"a": 0.9, "b": 0.7, "c": 0.9, "d": 0.1}
    assert top_n(scores, 2) == [("a", 0.9), ("c", 0.9)]
    assert top_n(scores, 3) == [("a", 0.9), ("c", 0.9), ("b", 0.7)]


def test_top_n_plus_grand_que_le_dictionnaire():
    assert top_n({"x": 1.0}, 5) == [("x", 1.0)]


def test_inverser_dict():
    d = {"chien": "animal", "chat": "animal", "rose": "plante"}
    assert inverser_dict(d) == {"animal": ["chat", "chien"], "plante": ["rose"]}
    assert inverser_dict({}) == {}
