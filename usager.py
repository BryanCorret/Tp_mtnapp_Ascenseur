import random

class Usager:
    def __init__(self, etage, destination):
        self.etage = etage
        self.destination = destination

    def appeler_ascenseur(self, ascenseur):
        if ascenseur.appel_existe(self.etage):
            print(f"Un appel a déjà été signalé à l'étage {self.etage}")
        else:
            ascenseur.ajouter_appel(self.etage)
            print(f"Usager appelle l'ascenseur à l'étage {self.etage}")

    def entrer_ascenseur(self, ascenseur):
        if random.choice([True, False]):
            print("L'usager décide d'entrer dans l'ascenseur.")
            ascenseur.ajouter_destination(self.destination)
        else:
            print("L'usager est distrait et ne rentre pas dans l'ascenseur.")
        ascenseur.supprimer_appel(self.etage)

    def attendre_porte_ouverte(self):
        print("Attendre que la porte de l'ascenseur s'ouvre.")