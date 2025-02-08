import unittest
from outils.graphe import charger_graphe
from outils.influenceur import top_influenceur

class TestInfluenceur(unittest.TestCase):
    def setUp(self):
        self.graphe = charger_graphe('data/go-9-01.txt')

    def test_top_influenceur(self):
        influenceurs = top_influenceur(self.graphe)
        self.assertIn(1, influenceurs)  # Exemple de valeur attendue

if __name__ == '__main__':
    unittest.main()