import os


class DetecteurPalindrome:

    def __init__(self, langue):
        self.__langue = langue

    def détecter(self, mot):
        mot = mot.lower()
        mot = mot.replace(" ", "")
        miroir = mot[::-1]

        début = (self.__langue.bonjour() + os.linesep + miroir + os.linesep)

        return ((début + self.__langue.féliciter()
                 if mot == miroir
                 else début)
                + self.__langue.auRevoir())