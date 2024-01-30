import os
import unittest

from src.langueAnglaise import LangueAnglaise
from src.langueFrançaise import LangueFrançaise
from tests.utilities.detecteutPalindromeBuilder import DétecteurPalindromeBuilder
from tests.utilities.langueSpy import LangueSpy

testNonPalindrome = ["test", "clip"]


class TestMiroir(unittest.TestCase):

    def test_miroir(self):
        for chaîne in testNonPalindrome:
            with (self.subTest(chaîne)):
                détecteur = DétecteurPalindromeBuilder().ayantPourLangue(LangueFrançaise()).build()
                résultat = détecteur.détecter(chaîne)

                attendu = chaîne[::-1]
                self.assertIn(attendu, résultat)

    def test_félicitations(self):
        cas = [[LangueFrançaise(), 'Bien dit !'], [LangueAnglaise(), 'Well said !']]

        for paramètres in cas:
            with (self.subTest(paramètres[0])):
                langue = paramètres[0]
                palindrome = 'radar'

                résultat = (DétecteurPalindromeBuilder()
                            .ayantPourLangue(langue)
                            .build()
                            .détecter(palindrome))

                félicitations = paramètres[1]
                attendu = palindrome + os.linesep + félicitations
                self.assertIn(attendu, résultat)

    def test_absence_bien_dit(self):
        for chaîne in testNonPalindrome:
            with self.subTest(chaîne):
                langue = LangueSpy()
                résultat = DétecteurPalindromeBuilder().ayantPourLangue(LangueFrançaise()).build().détecter(chaîne)

                self.assertFalse(langue.félicitationsConsultées())

    def test_bonjour(self):
        cas = [[LangueFrançaise(), 'Bonjour'], [LangueAnglaise(), 'Hello']]

        for paramètres in cas:
            with (self.subTest(paramètres[0])):
                langue = paramètres[0]
                chaîne = 'test'

                résultat = DétecteurPalindromeBuilder().ayantPourLangue(langue).build().détecter(chaîne)


                bonjour = paramètres[1]
                premiere_ligne = résultat.split(os.linesep)[0]
                self.assertEqual(bonjour, premiere_ligne)

    def test_au_revoir(self):

        cas = [[LangueFrançaise(), 'Au revoir'], [LangueAnglaise(), 'Good-bye']]
        for paramètres in cas:
            with (self.subTest(paramètres[0])):
                langue = paramètres[0]
                chaîne = 'test'

                résultat = DétecteurPalindromeBuilder().ayantPourLangue(langue).build().détecter(chaîne)

                au_revoir = paramètres[1]
                lignes = résultat.split(os.linesep)
                dernière_ligne = lignes[-1]
                self.assertEqual(au_revoir, dernière_ligne)


if __name__ == '__main__':
    unittest.main()
