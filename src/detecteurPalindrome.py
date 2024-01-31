import os


class DetecteurPalindrome:

    def __init__(self, langue, moment):
        self.__langue = langue
        self.__moment = moment

    def détecter(self, mot):
        mot = mot.lower()
        mot = mot.replace(" ", "")
        miroir = mot[::-1]

        début = (self.__langue.bonjour(self.__moment) + os.linesep + miroir + os.linesep)
        print("DEBUT " + str(self.__moment))

        return ((début + self.__langue.féliciter()
                 if mot == miroir
                 else début)
                + self.__langue.auRevoir())
