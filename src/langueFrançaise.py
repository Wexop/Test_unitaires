from momentDeLaJournée import MomentDeLaJournée


class LangueFrançaise:
    def féliciter(self):
        return "Bien dit !"

    def bonjour(self, moment):
        if moment == MomentDeLaJournée.SOIR or moment == MomentDeLaJournée.NUIT:
            return "Bonsoir"
        return "Bonjour"

    def auRevoir(self):
        return "Au revoir"

    def __str__(self):
        return "Langue Française"
