import time



class Ascenseur:
    def __init__(self):
        self.etage = 0
        self.direction = None
        self.destinations = []
        self.appels = []

    def choisir_direction(self):
        if self.direction == None :
            if self.appels[0] < self.etage :
                self.direction = 'bas'
            elif self.appels[0] > self.etage :
                self.direction = 'haut'
            
    def mise_en_marche_asenceur(self):
        ...
        # a partir de la direction de l'acenseur on descend un par un en vérifier si l'étage et dans les appele si oui on ouvre on prend la destination et o commence a descendre jusqua la destination final pui on prend la prochaine destination

    def monter_descendre(self):
        if self.direction == "haut":
            self.etage += 1
        elif self.direction == "bas":
            self.etage -= 1

        if self.etage in self.appels:
            self.appels.remove(self.etage)
            self.signaler_ouvrir_porte()

        if self.etage in self.destinations:
            self.destinations.remove(self.etage)
            self.signaler_ouvrir_porte()


    def ajouter_appel(self, etage):
        self.appels.append(etage)

    def appel_existe(self, etage):
        return etage in self.appels

    def ajouter_destination(self, destination):
        self.destinations.append(destination)

    def appels_existants(self):
        return len(self.appels) > 0

    def destinations_existants(self):
        return len(self.destinations) > 0

    def appel_ou_destination_existe(self, etage, direction):
        return etage in self.appels or etage in self.destinations

    def signaler_ouvrir_porte(self):
        print(f"Arrivé à l'étage {self.etage}. Signaler à ouvrir la porte.")
        time.sleep(1)  # Temps d'attente simulé pour l'ouverture de la porte
        self.ouvrir_porte()

    def ouvrir_porte(self):
        print(f"La porte s'ouvre à l'étage {self.etage}")

    def fermer_porte(self):
        print(f"La porte se ferme à l'étage {self.etage}")
    
    def supprimer_appel(self,etage):
        self.appels.remove(etage)


