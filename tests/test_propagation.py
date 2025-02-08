import unittest
from outils.graphe import charger_graphe
from outils.propagation import temps_propagation, chemin_propagation

class TestPropagation(unittest.TestCase):
    def setUp(self):
        self.graphe = charger_graphe('data/go-9-01.txt')

    def test_temps_propagation(self):
        temps = temps_propagation(self.graphe, 0, 8)
        self.assertEqual(temps, 15)  # Exemple de valeur attendue

    def test_chemin_propagation(self):
        chemin = chemin_propagation(self.graphe, 0, 8)
        self.assertEqual(chemin, [0, 1, 8])  # Exemple de valeur attendue

if __name__ == '__main__':
    unittest.main()