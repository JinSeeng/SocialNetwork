def parcours_profondeur(graphe, sommet_depart):
    """Parcours en profondeur d'un graphe représenté par une matrice d'adjacence."""
    sommets, mat = graphe
    visites = []
    pile = [sommet_depart]
    while pile:
        s = pile.pop()
        if s not in visites:
            visites.append(s)
            for voisin in range(len(mat[s])):
                if mat[s][voisin] and voisin not in visites:
                    pile.append(voisin)
    return visites

def parcours_largeur(graphe, sommet_depart):
    """Parcours en largeur d'un graphe représenté par une matrice d'adjacence."""
    sommets, mat = graphe
    visites = []
    file = [sommet_depart]
    while file:
        s = file.pop(0)
        if s not in visites:
            visites.append(s)
            for voisin in range(len(mat[s])):
                if mat[s][voisin] and voisin not in visites:
                    file.append(voisin)
    return visites