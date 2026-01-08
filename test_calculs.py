# Fichier: test_calculs.py
from calculs import calculer_moyenne

def test_moyenne_simple():
    assert calculer_moyenne([10, 20]) == 15

def test_moyenne_vide():
    assert calculer_moyenne([]) == 0

def test_moyenne_float():
    assert calculer_moyenne([10.5, 9.5]) == 10.0