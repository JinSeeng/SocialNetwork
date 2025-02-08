import unittest
from outils.graphe import charger_graphe, nombre_aretes_matrice, nombre_arcs_matrice

class TestGraphe(unittest.TestCase):
    def test_charger_graphe(self):
        sommets, mat = charger_graphe('data/go-9-01.txt')
        self.assertEqual(len(sommets), 9)
        self.assertEqual(len(mat), 9)

    def test_nombre_aretes_matrice(self):
        sommets, mat = charger_graphe('data/go-9-01.txt')
        self.assertEqual(nombre_aretes_matrice(mat), 10)  # Exemple de valeur attendue

    def test_nombre_arcs_matrice(self):
        sommets, mat = charger_graphe('data/go-9-01.txt')
        self.assertEqual(nombre_arcs_matrice(mat), 21)  # Exemple de valeur attendue

if __name__ == '__main__':
    unittest.main()