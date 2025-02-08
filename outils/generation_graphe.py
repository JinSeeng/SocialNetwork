import random

def generer_graphe(n_sommets, oriente=True, deg_min=1, deg_max=5, n_communautes=1):
    """Génère un graphe aléatoire respectant les contraintes."""
    sommets = list(range(n_sommets))
    arcs = []
    for i in range(n_sommets):
        deg = random.randint(deg_min, deg_max)
        voisins = random.sample(sommets, deg)
        for v in voisins:
            if oriente or (i < v):  # Éviter les doublons pour les graphes non orientés
                arcs.append((i, v))
    return sommets, arcs