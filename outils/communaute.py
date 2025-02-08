from outils.parcours import parcours_profondeur

def est_une_seule_communaute(graphe):
    """Vérifie si le graphe est une seule communauté."""
    sommets, mat = graphe
    visites = parcours_profondeur(graphe, sommets[0])
    return len(visites) == len(sommets)