import unittest
from outils.file import File

class TestFile(unittest.TestCase):
    def test_est_vide(self):
        f = File()
        self.assertTrue(f.est_vide())
        f.enfiler(1)
        self.assertFalse(f.est_vide())

    def test_enfiler_defiler(self):
        f = File()
        f.enfiler(1)
        f.enfiler(2)
        self.assertEqual(f.defiler(), 1)
        self.assertEqual(f.defiler(), 2)
        self.assertTrue(f.est_vide())

    def test_defiler_vide(self):
        f = File()
        with self.assertRaises(IndexError):
            f.defiler()

if __name__ == '__main__':
    unittest.main()