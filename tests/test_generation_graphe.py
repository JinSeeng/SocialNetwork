import unittest
from outils.generation_graphe import generer_graphe

class TestGenerationGraphe(unittest.TestCase):
    def test_generer_graphe(self):
        sommets, arcs = generer_graphe(10, oriente=True, deg_min=1, deg_max=3)
        self.assertEqual(len(sommets), 10)
        self.assertTrue(len(arcs) >= 10)  # Au moins un arc par sommet

if __name__ == '__main__':
    unittest.main()