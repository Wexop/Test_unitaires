from src.detecteurPalindrome import DetecteurPalindrome
from utilities.langueStub import LangueStub


class DétecteurPalindromeBuilder:
    __langue = LangueStub()

    def build(self):
        return DetecteurPalindrome(self.__langue)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self
