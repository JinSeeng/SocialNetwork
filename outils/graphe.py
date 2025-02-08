def nombre_aretes_matrice(mat):
    """Retourne le nombre d'arêtes dans un graphe représenté par une matrice d'adjacence."""
    n = len(mat)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j]:
                count += 1
    return count

def nombre_aretes_liste(adj):
    """Retourne le nombre d'arêtes dans un graphe représenté par une liste d'adjacence."""
    count = 0
    for voisins in adj.values():
        count += len(voisins)
    return count // 2  # Chaque arête est comptée deux fois

def nombre_arcs_matrice(mat):
    """Retourne le nombre d'arcs dans un graphe orienté représenté par une matrice d'adjacence."""
    n = len(mat)
    count = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j]:
                count += 1
    return count

def nombre_arcs_liste(adj):
    """Retourne le nombre d'arcs dans un graphe orienté représenté par une liste d'adjacence."""
    count = 0
    for voisins in adj.values():
        count += len(voisins)
    return count

def charger_graphe(fichier, representation="matrice"):
    """Charge un graphe à partir d'un fichier texte et le représente en mémoire."""
    with open(fichier, 'r') as f:
        lines = f.readlines()
    
    oriente = lines[0].strip() == "GRAPHE ORIENTE"
    n_sommets = int(lines[1].strip().split()[0])
    sommets = [int(line.strip()) for line in lines[2:2 + n_sommets]]
    n_arcs = int(lines[2 + n_sommets].strip().split()[0])
    arcs = [tuple(map(int, line.strip().split())) for line in lines[3 + n_sommets:3 + n_sommets + n_arcs]]

    if representation == "matrice":
        mat = [[0] * n_sommets for _ in range(n_sommets)]
        for u, v in arcs:
            mat[u][v] = 1
            if not oriente:
                mat[v][u] = 1
        return sommets, mat
    elif representation == "liste":
        adj = {s: [] for s in sommets}
        for u, v in arcs:
            adj[u].append(v)
            if not oriente:
                adj[v].append(u)
        return sommets, adj
    else:
        raise ValueError("Représentation non reconnue")