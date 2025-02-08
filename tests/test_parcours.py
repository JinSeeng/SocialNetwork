import unittest
from outils.graphe import charger_graphe
from outils.parcours import parcours_profondeur, parcours_largeur

class TestParcours(unittest.TestCase):
    def setUp(self):
        self.graphe = charger_graphe('data/go-9-01.txt')

    def test_parcours_profondeur(self):
        resultat = parcours_profondeur(self.graphe, 0)
        self.assertEqual(len(resultat), 9)  # Tous les sommets doivent être visités

    def test_parcours_largeur(self):
        resultat = parcours_largeur(self.graphe, 0)
        self.assertEqual(len(resultat), 9)  # Tous les sommets doivent être visités

if __name__ == '__main__':
    unittest.main()