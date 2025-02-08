import unittest
from outils.pile import Pile

class TestPile(unittest.TestCase):
    def test_est_vide(self):
        p = Pile()
        self.assertTrue(p.est_vide())
        p.empiler(1)
        self.assertFalse(p.est_vide())

    def test_empiler_depiler(self):
        p = Pile()
        p.empiler(1)
        p.empiler(2)
        self.assertEqual(p.depiler(), 2)
        self.assertEqual(p.depiler(), 1)
        self.assertTrue(p.est_vide())

    def test_depiler_vide(self):
        p = Pile()
        with self.assertRaises(IndexError):
            p.depiler()

if __name__ == '__main__':
    unittest.main()