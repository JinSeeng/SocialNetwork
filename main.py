from outils.graphe import charger_graphe, nombre_aretes_matrice, nombre_arcs_matrice
from outils.parcours import parcours_profondeur, parcours_largeur
from outils.communaute import est_une_seule_communaute
from outils.influenceur import top_influenceur
from outils.propagation import temps_propagation, chemin_propagation
from outils.generation_graphe import generer_graphe

def main():
    # Charger un graphe à partir du fichier
    print("Chargement du graphe à partir de 'data/go-9-01.txt'...")
    graphe = charger_graphe('data/go-9-01.txt')
    sommets, mat = graphe
    print(f"Sommets du graphe : {sommets}")
    print(f"Matrice d'adjacence : {mat}")

    # Nombre d'arêtes et d'arcs
    print("\nCalcul du nombre d'arêtes et d'arcs...")
    print(f"Nombre d'arêtes (graphe non orienté) : {nombre_aretes_matrice(mat)}")
    print(f"Nombre d'arcs (graphe orienté) : {nombre_arcs_matrice(mat)}")

    # Parcours en profondeur et en largeur
    sommet_depart = 0
    print(f"\nParcours en profondeur à partir du sommet {sommet_depart}...")
    resultat_profondeur = parcours_profondeur(graphe, sommet_depart)
    print(f"Résultat du parcours en profondeur : {resultat_profondeur}")

    print(f"\nParcours en largeur à partir du sommet {sommet_depart}...")
    resultat_largeur = parcours_largeur(graphe, sommet_depart)
    print(f"Résultat du parcours en largeur : {resultat_largeur}")

    # Vérification de la communauté
    print("\nVérification si le graphe est une seule communauté...")
    est_communaute = est_une_seule_communaute(graphe)
    print(f"Le graphe est une seule communauté : {est_communaute}")

    # Top influenceur
    print("\nRecherche du plus grand influenceur...")
    influenceurs = top_influenceur(graphe)
    print(f"Les plus grands influenceurs sont : {influenceurs}")

    # Temps de propagation
    source = 0
    cible = 8
    print(f"\nCalcul du temps de propagation entre {source} et {cible}...")
    temps = temps_propagation(graphe, source, cible)
    print(f"Temps de propagation entre {source} et {cible} : {temps} minutes")

    # Chemin de propagation
    print(f"\nCalcul du chemin de propagation entre {source} et {cible}...")
    chemin = chemin_propagation(graphe, source, cible)
    print(f"Chemin de propagation entre {source} et {cible} : {chemin}")

    # Génération d'un graphe aléatoire
    print("\nGénération d'un graphe aléatoire...")
    sommets_aleatoires, arcs_aleatoires = generer_graphe(n_sommets=5, oriente=True, deg_min=1, deg_max=3)
    print(f"Sommets du graphe généré : {sommets_aleatoires}")
    print(f"Arcs du graphe généré : {arcs_aleatoires}")

if __name__ == "__main__":
    main()