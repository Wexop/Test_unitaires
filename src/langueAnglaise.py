from momentDeLaJournée import MomentDeLaJournée


class LangueAnglaise:
    def féliciter(self):
        return "Well said !"

    def bonjour(self, moment):
        if moment == MomentDeLaJournée.MATIN:
            return "Good Morning"
        if moment == MomentDeLaJournée.APRES_MIDI:
            return "Good Afternoon"
        if moment == MomentDeLaJournée.SOIR:
            return "Good Evening"
        if moment == MomentDeLaJournée.NUIT:
            return "Good Night"

        return "Hello"

    def auRevoir(self):
        return "Good-bye"

    def __str__(self):
        return "Langue Anglaise"
