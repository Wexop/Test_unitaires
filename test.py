import unittest

from OHCE import miroir, getHello, getGoodBye, printPalindrome


class TestMiroir(unittest.TestCase):

    def test_miroir(self):
        entree = "Bonjour"
        sortie_attendue = "ruojnoB"
        resultat = miroir(entree)
        self.assertEqual(resultat, sortie_attendue)

    def test_bonjour(self):
        result = getHello()
        sortie_attendue = ["Bonjour !", "Hello !", "Good evening !", "Bonsoir !"]
        self.assertIn(result, sortie_attendue)

    def test_aurevoir(self):
        result = getGoodBye()
        sortie_attendue = ["Bonne journée !", "Bonne soirée !", "Have a good evening !", "Have a good day !"]
        self.assertIn(result, sortie_attendue)

    def test_bien_dit(self):
        result = printPalindrome('kayak')
        sortie_attendue = ["Bien dit !", "Well said !"]
        self.assertIn(result, sortie_attendue)


if __name__ == '__main__':
    unittest.main()
