"""
Tests unitaires pour la calculatrice
"""

import unittest
from calculatrice import additionner, soustraire, multiplier, diviser


class TestCalculatrice(unittest.TestCase):
    """Tests pour les fonctions de la calculatrice"""

    def test_additionner(self):
        """Test de l'addition"""
        self.assertEqual(additionner(2, 3), 5)
        self.assertEqual(additionner(-1, 1), 0)
        self.assertEqual(additionner(0, 0), 0)
        self.assertEqual(additionner(10.5, 2.5), 13.0)

    def test_soustraire(self):
        """Test de la soustraction"""
        self.assertEqual(soustraire(5, 3), 2)
        self.assertEqual(soustraire(0, 5), -5)
        self.assertEqual(soustraire(10, 10), 0)
        self.assertEqual(soustraire(7.5, 2.5), 5.0)

    def test_multiplier(self):
        """Test de la multiplication"""
        self.assertEqual(multiplier(2, 3), 6)
        self.assertEqual(multiplier(5, 0), 0)
        self.assertEqual(multiplier(-2, 3), -6)
        self.assertEqual(multiplier(2.5, 4), 10.0)

    def test_diviser(self):
        """Test de la division"""
        self.assertEqual(diviser(6, 2), 3)
        self.assertEqual(diviser(10, 4), 2.5)
        self.assertEqual(diviser(-10, 2), -5)

    def test_diviser_par_zero(self):
        """Test de la division par zéro"""
        with self.assertRaises(ValueError):
            diviser(5, 0)


if __name__ == "__main__":
    unittest.main()
