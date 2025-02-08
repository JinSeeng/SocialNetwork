import unittest

# Charger tous les tests
loader = unittest.TestLoader()
suite = loader.discover('tests')

# Exécuter les tests
runner = unittest.TextTestRunner()
runner.run(suite)