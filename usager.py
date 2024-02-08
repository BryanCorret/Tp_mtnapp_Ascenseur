import random

class Usager:
    def __init__(self,nom, etage, destination):
        self.nom = nom
        self.etage = etage
        self.destination = destination

    def appelerAscenseur(self, ascenseur):
        if ascenseur.appel_existe(self.etage):
            print(f"Un appel a déjà été signalé à l'étage {self.etage}")
        else:
            ascenseur.ajouter_appel(self.etage)
            print(f"Usager appelle l'ascenseur à l'étage {self.etage}")

    def getEtage(self):
        return self.etage

    def entrerAscenseur(self, ascenseur,testMax=None):
        if testMax or ((random.choice([True, False])) and not testMax):
            if ascenseur.getMaxPersonnes()>ascenseur.getPersonneActu():
                print(f"{self.nom} décide d'entrer dans l'ascenseur.")
                ascenseur.ajouter_destination(self.destination)
                ascenseur.addPersonne()
            else :
                print(f"Ascenseur plein,{self.nom} doit attendre quelque minutes")


        else:
            print("L'usager est distrait et ne rentre pas dans l'ascenseur.")

    def attendre_porte_ouverte(self):
        print("Attendre que la porte de l'ascenseur s'ouvre.")
    
    def sortirAscenseur(self,ascenseur):
        print(f"{self.nom} sort de l'ascenseur")
        ascenseur.removePersonne()

    def getDestination(self):
        return self.destination
