def top_influenceur(graphe):
    """Retourne le ou les plus grands influenceurs du graphe."""
    sommets, mat = graphe
    influence = {s: 0 for s in sommets}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]:
                influence[j] += 1
    max_influence = max(influence.values())
    return [s for s, val in influence.items() if val == max_influence]