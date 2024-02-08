
class Porte:
    def __init__(self, etage):
        self.etage = etage

    def ouvrir(self):
        print(f"La porte s'ouvre à l'étage {self.etage}")

    def fermer(self):
        print(f"La porte se ferme à l'étage {self.etage}")

    def signaler_redemarrage(self):
        print("Signaler à l'ascenseur qu'il peut redémarrer")

    def getEtage(self):
        return self.etage