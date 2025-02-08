def temps_propagation(graphe, source, cible):
    """Retourne le temps de propagation d'une information entre deux personnes."""
    sommets, mat = graphe
    distances = {s: float('inf') for s in sommets}
    distances[source] = 0
    file = [source]
    while file:
        s = file.pop(0)
        for voisin in range(len(mat[s])):
            if mat[s][voisin] and distances[voisin] == float('inf'):
                distances[voisin] = distances[s] + 5
                file.append(voisin)
    return distances[cible]

def chemin_propagation(graphe, source, cible):
    """Retourne le chemin minimum suivi par une information entre deux personnes."""
    sommets, mat = graphe
    parents = {s: None for s in sommets}
    file = [source]
    while file:
        s = file.pop(0)
        if s == cible:
            break
        for voisin in range(len(mat[s])):
            if mat[s][voisin] and parents[voisin] is None:
                parents[voisin] = s
                file.append(voisin)
    chemin = []
    s = cible
    while s is not None:
        chemin.append(s)
        s = parents[s]
    return chemin[::-1]