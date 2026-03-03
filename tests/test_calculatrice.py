import unittest

from src.calculatrice import division, puissance, moyenne


class TestCalculatrice(unittest.TestCase):

    # --- division ---
    def test_division_entiers(self):
        self.assertEqual(division(10, 2), 4.0)

    def test_division_decimales(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(12, 0)

    # --- puissance ---
    def test_puissance_cas_normal(self):
        self.assertEqual(puissance(2, 3), 8.0)

    def test_puissance_exposant_zero(self):
        self.assertEqual(puissance(7, 0), 1.0)

    def test_puissance_exposant_negatif(self):
        with self.assertRaises(ValueError):
            puissance(3, -1)

    # --- moyenne ---
    def test_moyenne_plusieurs_valeurs(self):
        self.assertEqual(moyenne([11, 20, 14]), 15.0)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])


if __name__ == "__main__":
    unittest.main()
