import time



class Ascenseur:
    def __init__(self):
        self.etage = 0
        self.etageMax = 5
        self.etageMin = 0
        self.direction = None
        self.destinations = []
        self.appels = []
        self.listeUsager = []
        self.maxPersonnes = 5
        self.nbPersonnesActu = 0

    def choisir_direction(self):
        if self.direction == None :
            if len(self.appels) > 0:
                if self.appels[0] < self.etage :
                    self.direction = 'bas'
                elif self.appels[0] > self.etage :
                    self.direction = 'haut'
            elif len(self.destinations) > 0:
                if self.destinations[0]<self.etage :
                    self.direction = 'bas'
                elif self.destinations[0]>self.etage :
                    self.direction = 'haut'

    def getMaxPersonnes(self):
        return self.maxPersonnes
        
    def getPersonneActu(self):
        return self.nbPersonnesActu

    def getEtage(self):
        return self.etage

    def addPersonne(self):
        self.nbPersonnesActu +=1
        
    def removePersonne(self,personne):
        self.nbPersonnesActu -=1
        self.listeUsager.remove(personne)

    def addListUsager(self,listeUsager):
        self.listeUsager.append(listeUsager)

    def monter_descendre(self):
        if self.etageMax == self.etage:
            self.direction = "bas"
            self.etage -= 1
            
        else :
            if self.direction == "haut":
                self.etage += 1
            elif self.direction == "bas" and self.etage>self.etageMin:
                self.etage -= 1
            else :
                self.direction = "haut"
                self.etage += 1


        if self.etage in self.appels:
            self.appels.remove(self.etage)
            self.signaler_ouvrir_porte()
            self.getPersonneActuEtage(self.etage)
            self.fermer_porte()

        if self.etage in self.destinations:
            self.destinations.remove(self.etage)
            self.signaler_ouvrir_porte()
            self.getPersonneActuEtage(self.etage)
            self.fermer_porte()


        if len(self.appels) == 0 and len(self.destinations)==0:
            self.direction = None

    def getPersonneActuEtage(self,etage):
        usagerSortit = []
        for usager in self.listeUsager:
            if usager.getEtage() == etage:
                usager.attendre_porte_ouverte()
                usager.entrerAscenseur(self,testMax=True)
            if usager.getDestination() == etage:
                usager.sortirAscenseur(self)
                usagerSortit.append(usager)


        for usager in usagerSortit:
            self.removePersonne(usager)





    def ajouter_appel(self, etage):
        self.appels.append(etage)

    def appel_existe(self, etage):
        return etage in self.appels

    def ajouter_destination(self, destination):
        if destination in self.destinations:
            print('Destination deja selectionné')
        else :
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
        if etage in self.appels :
            self.appels.remove(etage)
    
    def getDestination(self):
        return self.destinations

    def getAppel(self):
        return self.appels


