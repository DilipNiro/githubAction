# Fichier: calculs.py
def calculer_moyenne(liste_nombres):
    if not liste_nombres:
        return 0
    return sum(liste_nombres) / len(liste_nombres)
