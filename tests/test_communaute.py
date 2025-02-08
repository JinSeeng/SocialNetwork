import unittest
from outils.graphe import charger_graphe
from outils.communaute import est_une_seule_communaute

class TestCommunaute(unittest.TestCase):
    def setUp(self):
        self.graphe = charger_graphe('data/go-9-01.txt')

    def test_est_une_seule_communaute(self):
        self.assertTrue(est_une_seule_communaute(self.graphe))

if __name__ == '__main__':
    unittest.main()