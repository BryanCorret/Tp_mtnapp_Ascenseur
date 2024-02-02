from porte import Porte
from ascenseur import Ascenseur
from usager import Usager

# Simulation
porte = Porte(0)
ascenseur = Ascenseur()
usager = Usager(2, 5)

# Simulation d'appel d'ascenseur
usager.appeler_ascenseur(ascenseur)

ascenseur.choisir_direction()
ascenseur.monter_descendre()
usager.attendre_porte_ouverte()
usager.entrer_ascenseur(ascenseur)

# Simulation de choix de direction et déplacement de l'ascenseur
while ascenseur.appels_existants() or ascenseur.destinations_existants():
    ascenseur.fermer_porte()
    ascenseur.monter_descendre()
    ascenseur.choisir_direction()

