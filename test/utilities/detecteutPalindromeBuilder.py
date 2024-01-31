from momentDeLaJournée import MomentDeLaJournée
from src.detecteurPalindrome import DetecteurPalindrome
from utilities.langueStub import LangueStub


class DétecteurPalindromeBuilder:
    __langue = LangueStub()
    __moment = MomentDeLaJournée.INCONNU

    def build(self):
        return DetecteurPalindrome(self.__langue, self.__moment)

    def ayantPourLangue(self, langue):
        self.__langue = langue
        return self

    def ayantPourMomentDeLaJournée(self, moment):
        self.__moment = moment
        return self
